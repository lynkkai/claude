---
platform: Medium
status: draft v1, needs human edit before publishing
primary_keyword: "ai note taker that doesn't join meetings" (90/mo, SD 30, CPC $21.61)
secondary_keywords: ["bot free ai note taker" (110, CPC $8.54), "bot free ai meeting assistant" (40, CPC $16.20), "ai note taker no subscription" (40)]
intent: Transactional. Low volume, very high CPC: small audience, high purchase readiness.
internal_links: [https://lynkk.ai/features/chrome-extension, https://lynkk.ai/features/meeting-bot]
word_count: ~1,500
collision_check: |
  /blog/zoom-bot-join-meeting covers "can you record a meeting without a bot?" as part of a Zoom
  how-to and troubleshooting page. This post is deliberately framed as a decision between two
  capture models, not a how-to, so the two do not compete.
---

# AI Note Takers That Do Not Join Your Meeting

**Subtitle:** Why "a bot has joined the meeting" is a product decision, not a law of physics, and
when you want the other option.

---

*Disclosure: I work on Lynkk, an AI meeting assistant that offers both capture models described
here. Lynkk appears by name once, in a marked section at the end.*

There is a particular silence that happens on a sales call when a notetaker bot joins. The
customer stops, looks at the participant list, and says "what's that?"

You explain. They say "sure, that's fine". The call resumes. Nothing bad happened, except that the
first ninety seconds of a conversation you had prepared for went on administering your own tooling,
and the person on the other side now knows there is a recording and has not quite been asked.

Most AI note takers work this way, and for good reasons. But it is a choice, not a requirement, and
a growing number of tools offer the alternative. If you have searched for a note taker that does
not join your meeting, here is what you are actually choosing between.

## What the bot is, and why it exists

A notetaker bot is a participant. It dials into the Zoom, Meet or Teams call like a person, using
the meeting link, and appears in the participant list with a name like "Priya's Notetaker".

It exists because being a participant is the easiest way to get clean audio. The platform hands the
bot a proper media stream, usually with separate audio per speaker, which makes it far easier to
label who said what. It also means capture does not depend on your laptop: the bot can sit in a
call you joined from your phone, or a call you are five minutes late to, or a call you are not in
at all.

That last property is the real reason bots dominate. A bot can record a meeting you are not
attending. Nothing that runs on your device can.

## What bot-free capture actually is

The alternative is to record the call on the machine you are already using. In practice that means
one of two things: a browser extension that captures the audio of the tab the call is running in,
or a desktop app that captures system audio and your microphone together.

No extra participant appears. The platform does not know anything unusual is happening, because
nothing is: your computer is recording its own audio output and its own microphone, the same way a
screen recorder does.

## Four reasons people want this

**External and client-facing calls.** Internal standups do not care. A first call with a prospect
is different. A bot in the participant list is a visible piece of your infrastructure sitting in a
conversation where you are trying to establish that you are competent and easy to work with.

**Consent that happens properly.** This is the one I would weigh most heavily, and it cuts against
the intuition. A bot looks like disclosure, and it is thin disclosure: a name in a list that
nobody reads, which does not announce itself. Without a bot, there is nothing to hide behind, so
you have to say it out loud: "I'm recording this so I don't miss anything, is that all right?"
That is better consent, and it takes four seconds.

**Platforms and policies that block bots.** Plenty of enterprises disable third-party apps in
Zoom or Teams, or block unknown participants from joining. Some customers' IT will not admit a bot
from the waiting room. If you sell into regulated industries, you will hit this.

**Meetings with no link at all.** In-person conversations, a phone call on speaker, a conference
corridor. There is no meeting for a bot to join, so this question answers itself.

## What you give up

Be clear about the trade-offs, because vendors selling bot-free capture tend to be quiet about them.

- **Your device has to be there, on, and awake.** No laptop, no recording. Close the lid and you
  may lose the session. If you join calls from your phone, this model does not cover you.
- **You cannot capture a meeting you are not in.** Delegating recording to a bot is a genuine
  feature for managers and for calls you skip.
- **Speaker separation is harder.** With a bot, the platform often supplies per-speaker streams.
  Recording system audio gives you a mixed stream where everyone on the far side arrives on the
  same channel, so the tool has to separate voices acoustically. Good tools do this well. Ask the
  question directly.
- **Usually no video.** Bots commonly record the gallery view. Local audio capture typically does
  not.
- **Battery and thermals.** An hour of recording and transcription on a laptop is real work.

## So which one, when

The honest answer is that the question is wrong. You want both, available per call, and you choose
at the moment the call starts:

- **Internal meeting, or one you are not attending:** bot.
- **First call with a prospect, or any call where the room's impression of you matters:** no bot.
- **Customer with strict IT:** no bot, because the bot will not get in.
- **In person:** device capture, necessarily.
- **You are joining from your phone, or you are late:** bot, because nothing else will be there.

Treating this as a vendor-level religious position is the mistake. It is a per-meeting decision.

## Questions to ask before you buy

1. Do you offer both bot and bot-free capture, or only one?
2. For bot-free capture, do you label speakers, given the audio arrives mixed?
3. Does it capture system audio and the microphone, or only the browser tab?
4. What happens if I close the laptop lid, or the machine sleeps?
5. Does the bot announce itself, or only appear in the participant list?
6. Can I use bot-free capture for in-person conversations too?
7. What do you do with the audio, and do you train models on it?

## How Lynkk does it

As disclosed, I work on Lynkk, so this is the vendor's own account.

Lynkk offers both, and the reason is everything above: neither model covers every meeting. There is
a [meeting bot](https://lynkk.ai/features/meeting-bot) you send with a call link or via calendar
auto-join, which is on the free plan, and a
[Chrome extension](https://lynkk.ai/features/chrome-extension) that records with no bot in the call
at all. The Mac app also notices calls and records both sides locally, and records in-person
conversations. Whichever route you use, the notes land in the same searchable place, with speakers
labelled and timestamps you can click to hear the moment.

Worth stating plainly: Lynkk's bot appears in the participant list as "<Name>'s Notetaker" and does
**not** announce itself out loud. Lynkk's own documentation tells you to disclose the recording
yourself, which is the right instruction and the one most vendors leave out. Do that regardless of
which capture model you pick.

The limits: offline and in-person recording are Mac-only, the web app needs a connection, one
recording caps at two hours, and the free plan includes unlimited recordings and transcripts but
caps AI notes at your first 5 hours over the life of the account, with Pro at $15 a month after
that.

## The short version

"A bot has joined the meeting" is a capture strategy, not a feature, and it is the wrong one for
the calls where you care most about the impression you make. Pick a tool that lets you choose per
meeting, and either way, say out loud that you are recording.

---

## Publishing notes

**Medium tags:** AI, Sales, Productivity, Privacy, Meetings
**Platform compliance:** disclosure in the first screen; two product links in the marked section;
expect Network Distribution.
**Required before publishing:** human edit, plus one real story of a bot being blocked by a
customer's IT or creating an awkward moment on a call. That detail is the hook and I cannot
invent it.
