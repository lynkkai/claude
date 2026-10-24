---
platform: Hashnode
title: "How Meeting Bots Actually Join a Zoom, Google Meet or Teams Call"
subtitle: "Headless browsers, official SDKs and post-meeting APIs: the three architectures behind every AI notetaker, and what each one costs you."
slug: how-meeting-bots-join-zoom-meet-teams
tags: [meeting-bot, webrtc, architecture, zoom, microsoft-teams]
target_queries: ["meeting bot", "how to make a meeting bot", "meeting bot api", "join zoom call bot", "meeting bot as a service"]
evidence: "GSC: 'meeting bot' 117 impr at 20.3, 'join zoom call bot' 93 at 27.6, 'zoom connector bot' 56, 'how to make a meeting bot' 21, 'meeting bot as a service' 12; prior GSC analysis found this cluster is developer intent (399 impr) that marketing pages cannot serve, which makes it a fit for Hashnode. Ubersuggest: 'meeting bot' 70/mo, 'meeting bot api' 40/mo"
main_site_links:
  - https://lynkk.ai/features/meeting-bot
  - https://lynkk.ai/blog/zoom-bot-join-meeting
  - https://lynkk.ai/blog/zoom-ai-companion-alternatives
canonical: "none (original article, do not set a canonical)"
cover_image: "Architecture diagram: calendar -> scheduler -> bot worker -> meeting platform -> transcription -> notes"
status: draft
---

# How Meeting Bots Actually Join a Zoom, Google Meet or Teams Call

If you've ever had "Someone's Notetaker" appear in your participant list, you've seen a meeting bot. From the outside it looks simple: a fake participant that listens. From the inside, getting a reliable bot into three different platforms is one of the messier problems in applied engineering.

This post walks through the three architectures teams use, the trade-offs of each, and the parts nobody warns you about (waiting rooms, scheduling and consent). It's written from the perspective of building a notetaker, but it applies to anything that needs live meeting audio.

## The three architectures

There are basically three ways to get audio out of a meeting:

1. **Join as a participant through the web client** (a headless browser).
2. **Join through the platform's official bot or media SDK.**
3. **Don't join at all**: pull recordings or transcripts from the platform's API after the meeting.

Most production notetakers use a mix.

## Architecture 1: Headless browser in the web client

Zoom, Google Meet and Teams all have browser clients. A bot can be a real Chromium instance (driven by Playwright or Puppeteer) that navigates to the meeting URL, types a display name, clicks "Join" and then captures the audio that the browser plays.

A minimal join flow looks like this:

```ts
import { chromium } from "playwright";

const browser = await chromium.launch({
  args: [
    "--use-fake-ui-for-media-stream",      // auto-accept mic/camera prompts
    "--use-fake-device-for-media-stream",  // bot has no real devices
    "--autoplay-policy=no-user-gesture-required",
  ],
});
const page = await browser.newPage();
await page.goto(meetingUrl);
await page.getByPlaceholder(/your name/i).fill("Maya's Notetaker");
await page.getByRole("button", { name: /ask to join|join now/i }).click();
```

The selectors above are illustrative. In practice they change whenever the platform ships a UI update, and that's the main cost of this approach.

**Capturing audio.** You have two options:

- **At the OS level**: run the browser on Linux inside a container with a PulseAudio (or PipeWire) null sink as the default output, then record that sink with ffmpeg. Robust and language-agnostic.
- **Inside the page**: inject a script that hooks the `RTCPeerConnection` remote tracks or the `<audio>` elements and pipes them into a `MediaRecorder` or a WebSocket. This gives you per-track audio on some platforms, which helps speaker attribution, but it's fragile.

**Pros:** one codebase pattern for all three platforms; works with any meeting a human could join from a browser.
**Cons:** breaks on UI changes; each bot is a full browser (roughly a CPU core and a few hundred MB of RAM per concurrent meeting); some platforms detect or restrict automated clients.

## Architecture 2: Official SDKs and bot frameworks

Each platform offers a sanctioned path, with very different ergonomics.

**Zoom: Meeting SDK.** The Zoom Meeting SDK (including a Linux build) lets an app join meetings as a participant and, with the right permissions, access raw audio data. Joining meetings outside your own account requires your app to go through Zoom's review. Zoom has also introduced Realtime Media Streams (RTMS), which streams meeting media to an app without a visible participant; check its availability for your account type.

**Microsoft Teams: Graph Communications (calling and meeting bots).** Teams supports bots that join calls and meetings through the Microsoft Graph communications APIs. For raw audio you need *application-hosted media*, which historically means a .NET bot running on Windows Server in Azure, with the Real-time Media Platform. It's powerful and heavy.

**Google Meet: no general-purpose bot SDK.** Meet's official options are the Meet REST API (conference records, recordings and transcripts after the fact) and add-ons that run inside Meet's UI. For live audio, most third-party Meet bots use the browser approach.

**Pros:** supported, more stable than UI automation, sometimes better audio (per-participant streams).
**Cons:** three entirely different stacks; review processes; some require the meeting host's org to approve your app.

## Architecture 3: Skip the bot, use the platform's data

If you don't need live audio, the cheapest bot is no bot. All three platforms can expose recordings or transcripts after the meeting:

- **Zoom** cloud recordings include an audio transcript file (VTT) when that setting is on.
- **Google Meet** transcripts are available through the Meet REST API's `conferenceRecords.transcripts` resources.
- **Teams** transcripts are available through Microsoft Graph's `onlineMeetings/{id}/transcripts`.

This only works when the meeting was recorded or transcribed on a plan that supports it, and only for meetings in tenants that grant you access. It's great for internal tools and useless for meetings hosted by someone else's company.

## The parts nobody warns you about

**Scheduling.** A notetaker that "joins automatically" is really a scheduler reading calendars. You need calendar sync (Google Calendar or Microsoft Graph), a parser that extracts meeting links from event descriptions and conference data, deduplication (three attendees may all have the bot enabled for the same meeting), and a job queue that spins up a worker a minute or so before start time.

**Waiting rooms and lobbies.** Zoom waiting rooms, Meet's "ask to join" and Teams lobbies mean the bot often sits outside until a human admits it. Your bot needs a timeout, a clear display name so the host knows what they're admitting, and a way to tell the user "the bot couldn't get in." We wrote a user-facing guide on [what to do when a Zoom or Meet bot can't join](https://lynkk.ai/blog/zoom-bot-join-meeting) that mirrors these failure modes.

**Leaving.** Bots should leave when the meeting ends, which in practice means "when the bot is the only participant left" or when the platform signals the end. Otherwise you'll record hours of silence.

**Naming and consent.** A bot named after the person who sent it ("Maya's Notetaker") is honest and helps hosts decide whether to admit it. Recording laws vary by jurisdiction, so the product should make it easy for users to tell participants they're recording. Don't build bots designed to go unnoticed.

**Concurrency and cost.** Meetings cluster on the hour. Your infrastructure needs to handle a spike at 9:00, 10:00 and 11:00 local time across every time zone you serve. Autoscale workers ahead of the hour, not reactively.

## How a production notetaker combines these

A typical setup looks like this:

```
Calendar sync ──► Scheduler ──► Bot worker (browser or SDK) ──► Audio chunks
                                                              │
                                     Speech-to-text ◄─────────┘
                                          │
                                 Summary, action items, decisions
                                          │
                              Notes app, email recap, Jira, Slack
```

Lynkk's [meeting bot](https://lynkk.ai/features/meeting-bot), for example, follows Google Calendar and joins Zoom, Meet and Teams calls when they begin, appears under the user's name, and leaves once it's the last one in the call. It doesn't speak or post a consent message, so the product tells users to announce the recording themselves. For users who don't want a bot at all, the same product records from a Mac app or Chrome extension instead, which is a different capture path with its own trade-offs.

## Build or buy?

If you're building a product where meeting audio is an input but not the core, consider a third-party meeting-bot API rather than maintaining three integrations yourself. If live meeting capture *is* your core product, you'll likely end up owning the stack, and you should budget for ongoing maintenance every time a platform ships a UI change.

If your goal is simply notes from your own meetings, you don't need to build anything: built-in tools like Zoom AI Companion, or a third-party notetaker, will do. There's a comparison of [Zoom AI Companion alternatives](https://lynkk.ai/blog/zoom-ai-companion-alternatives) on the Lynkk blog if you want to see how existing products handle bot vs bot-free capture.

## Summary

| Approach | Live audio | Platforms | Main cost |
|---|---|---|---|
| Headless browser | Yes | All three | Breaks on UI changes, heavy per meeting |
| Official SDKs | Yes | One stack each | Three codebases, app reviews |
| Post-meeting APIs | No | All three, with limits | Needs recording/transcripts on, tenant access |

Pick based on whether you need audio *during* the meeting. If you don't, start with the APIs. If you do, expect to maintain it.

---

*Written by the Lynkk team. Lynkk turns Zoom, Meet, Teams and in-person meetings into searchable notes. Drafted with AI assistance and edited by the Lynkk team.*
