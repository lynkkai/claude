---
platform: Hashnode
title: "Getting Microsoft Teams Meeting Transcripts With the Graph API"
subtitle: "From a join URL to a parsed, speaker-labelled transcript: permissions, the VTT format Teams uses, and how to get notified when a new transcript is ready."
slug: microsoft-teams-transcripts-graph-api
tags: [microsoft-teams, microsoft-graph, api, python, transcription]
target_queries: ["microsoft teams ai note taker", "teams ai note taker", "meeting notes in teams", "how to get meeting notes in teams"]
evidence: "GSC: /blog/ai-note-taker-microsoft-teams 875 impr at avg 23.6 (second-largest blog page off page one); 'microsoft teams ai note taker' 36 impr, 'teams ai note taker' 26, 'ai notetaker teams' 13; Ubersuggest: 'meeting notes in teams' 260/mo, 'microsoft team meeting notes' 480/mo, 'how to get meeting notes in teams' 40/mo"
main_site_links:
  - https://lynkk.ai/blog/ai-note-taker-microsoft-teams
  - https://lynkk.ai/integrations/microsoft-teams
  - https://lynkk.ai/blog/meeting-summary-template
canonical: "none (original article, do not set a canonical)"
cover_image: "A WebVTT file with <v Priya Shah> voice tags beside a Teams-style meeting tile"
status: draft
---

# Getting Microsoft Teams Meeting Transcripts With the Graph API

When transcription is turned on in a Teams meeting, Microsoft stores the transcript and exposes it through **Microsoft Graph**. If you're building internal tooling (a summary bot, a searchable archive, a CRM sync), you can fetch those transcripts programmatically instead of asking people to download files.

This post covers the permissions, the endpoints, the WebVTT format Teams uses, and change notifications so you don't have to poll.

> Transcripts only exist if someone turned on transcription (or recording with transcription) in the meeting, and your tenant's policies allow it. Graph can't transcribe audio after the fact.

## Permissions

Transcript access uses the `OnlineMeetingTranscript.Read.All` permission.

- **Delegated** (acting as a signed-in user): the user can read transcripts of meetings they organized or attended, subject to policy.
- **Application** (a daemon with no user): needs admin consent **and** an **application access policy** that a Teams admin assigns, allowing your app to read meetings on behalf of specific users. Without the policy, calls fail even with the permission granted.

You'll typically also need `OnlineMeetings.Read` (or `.All`) to look meetings up.

## Step 1: Resolve the meeting from its join URL

Graph identifies meetings by an `onlineMeeting` ID, not the URL people paste. Look it up by `JoinWebUrl`:

```python
import requests

GRAPH = "https://graph.microsoft.com/v1.0"

def meeting_id_from_join_url(token: str, user_id: str, join_url: str) -> str:
    r = requests.get(
        f"{GRAPH}/users/{user_id}/onlineMeetings",
        headers={"Authorization": f"Bearer {token}"},
        params={"$filter": f"JoinWebUrl eq '{join_url}'"},
        timeout=30,
    )
    r.raise_for_status()
    return r.json()["value"][0]["id"]
```

With delegated auth you can use `/me/onlineMeetings` instead of `/users/{id}/onlineMeetings`. Get the token with MSAL (`msal` package) using whichever flow matches your app.

## Step 2: List and download transcripts

A meeting can have several transcripts (for example if transcription was stopped and restarted).

```python
def list_transcripts(token, user_id, meeting_id):
    r = requests.get(
        f"{GRAPH}/users/{user_id}/onlineMeetings/{meeting_id}/transcripts",
        headers={"Authorization": f"Bearer {token}"}, timeout=30)
    r.raise_for_status()
    return r.json()["value"]

def transcript_vtt(token, user_id, meeting_id, transcript_id) -> str:
    r = requests.get(
        f"{GRAPH}/users/{user_id}/onlineMeetings/{meeting_id}"
        f"/transcripts/{transcript_id}/content",
        headers={"Authorization": f"Bearer {token}"},
        params={"$format": "text/vtt"}, timeout=60)
    r.raise_for_status()
    return r.text
```

## Step 3: Parse Teams' WebVTT

Teams transcripts use WebVTT with **voice tags** for speakers:

```
WEBVTT

00:00:02.120 --> 00:00:05.480
<v Priya Shah>Can we move the rollout to the 28th?</v>

00:00:06.010 --> 00:00:08.300
<v Dev Patel>Yes, if QA signs off by Friday.</v>
```

A small parser that also merges consecutive cues from the same speaker:

```python
import re

CUE = re.compile(
    r"(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})\s*\n(.+?)(?:\n\n|\Z)",
    re.S,
)
VOICE = re.compile(r"<v ([^>]+)>(.*?)</v>", re.S)

def parse_teams_vtt(vtt: str):
    turns = []
    for start, end, body in CUE.findall(vtt):
        m = VOICE.search(body)
        speaker, text = (m.group(1), m.group(2)) if m else ("Unknown", body)
        text = " ".join(text.split())
        if turns and turns[-1]["speaker"] == speaker:
            turns[-1]["text"] += " " + text
            turns[-1]["end"] = end
        else:
            turns.append({"speaker": speaker, "start": start, "end": end, "text": text})
    return turns
```

Some cues may carry an identifier line before the timestamp; the regex above skips it because it only matches from the timestamp onwards.

## Step 4: Get notified instead of polling

Graph supports change notifications for transcripts. Subscribe to new transcripts for a specific meeting:

```
POST https://graph.microsoft.com/v1.0/subscriptions
{
  "changeType": "created",
  "notificationUrl": "https://your-app.example.com/graph/notify",
  "resource": "communications/onlineMeetings/{meetingId}/transcripts",
  "expirationDateTime": "2026-10-25T12:00:00Z",
  "clientState": "a-secret-you-verify"
}
```

There are also tenant-wide resources for transcripts (for example `communications/onlineMeetings/getAllTranscripts`), which need the application permission and are subject to Microsoft's licensing and metering rules for these APIs. Check current requirements before you design around them. Subscriptions expire, so renew them on a schedule, and always validate `clientState`.

## Step 5: Turn transcripts into something people read

Nobody reads raw transcripts. The usual next step is a short summary: decisions, action items with owners and dates, and open questions. If you're generating that with an LLM, feed it the parsed speaker turns (not the raw VTT) and give it a fixed output structure. A plain [meeting summary template](https://lynkk.ai/blog/meeting-summary-template) is a good target format, because humans already know how to read it.

## Limits of the native route

The Graph route is ideal for internal tools inside one Microsoft 365 tenant. It's a weaker fit when:

- you meet with external organizations whose meetings you don't own;
- you also meet on Zoom, Google Meet or in person;
- transcription isn't consistently turned on;
- you want features beyond the transcript, like search across months of meetings.

If you're weighing Copilot, Teams Premium recaps and third-party notetakers rather than building, the Lynkk team wrote a comparison of [AI note takers for Microsoft Teams](https://lynkk.ai/blog/ai-note-taker-microsoft-teams), with costs for a 10-person team. And Lynkk's own [Teams integration](https://lynkk.ai/integrations/microsoft-teams) records Teams calls with a bot, the Chrome extension or the Mac app, without depending on Teams transcription being on.

---

*Written by the Lynkk team with AI assistance. Microsoft Graph v1.0 as of October 2026; check Microsoft's documentation for current permissions and licensing.*
