---
platform: Hashnode
title: "Downloading Zoom Cloud Recording Transcripts With the Zoom API (and Parsing the VTT)"
subtitle: "Server-to-Server OAuth, the recordings endpoint, the TRANSCRIPT file type, and a webhook so new transcripts arrive on their own."
slug: zoom-cloud-recording-transcripts-api
tags: [zoom, api, python, webhooks, transcription]
target_queries: ["how to transcribe zoom meetings", "zoom transcription", "zoom note taker", "zoom ai notetaker"]
evidence: "GSC: 'zoom note taker' 42 impr at 17.7, 'zoom ai notetaker' 35, 'zoom notes taker' 22 at 19.3, 'zoom transcription' 13; /blog/zoom-note-taker 419 impr at avg 31; /blog/how-to-transcribe-zoom-meetings 153 impr at avg 47.6; /blog/zoom-meeting-recorders live"
main_site_links:
  - https://lynkk.ai/blog/how-to-transcribe-zoom-meetings
  - https://lynkk.ai/blog/zoom-note-taker
  - https://lynkk.ai/integrations/zoom
canonical: "none (original article, do not set a canonical)"
cover_image: "A webhook arrow from a cloud icon to a terminal printing a VTT transcript"
status: draft
---

# Downloading Zoom Cloud Recording Transcripts With the Zoom API (and Parsing the VTT)

Zoom can generate an audio transcript for cloud recordings. Most people find it in the web portal and download it by hand. If you want those transcripts in your own system (a searchable archive, an internal summary bot, a data warehouse), the Zoom API gives you the same file programmatically.

This post covers authentication, finding the transcript file, parsing Zoom's VTT format and a webhook that delivers new transcripts as they're ready.

> **Prerequisites.** You need a Zoom plan with cloud recording, and the **audio transcript** option enabled in the account's recording settings. Local recordings don't produce cloud transcripts. If you're not sure which options your plan has, the non-technical guide to [transcribing Zoom meetings](https://lynkk.ai/blog/how-to-transcribe-zoom-meetings) covers the three ways, including on a free plan.

## Step 1: Create a Server-to-Server OAuth app

For an internal tool that reads your own account's recordings, a **Server-to-Server OAuth** app in the Zoom App Marketplace is the simplest option. Give it the cloud recording read scopes (Zoom's granular scopes for listing and reading recording files) and note the account ID, client ID and client secret.

```python
import base64, os, requests

def zoom_token() -> str:
    auth = base64.b64encode(
        f"{os.environ['ZOOM_CLIENT_ID']}:{os.environ['ZOOM_CLIENT_SECRET']}".encode()
    ).decode()
    r = requests.post(
        "https://zoom.us/oauth/token",
        params={"grant_type": "account_credentials",
                "account_id": os.environ["ZOOM_ACCOUNT_ID"]},
        headers={"Authorization": f"Basic {auth}"},
        timeout=20,
    )
    r.raise_for_status()
    return r.json()["access_token"]   # valid for about an hour; cache it
```

## Step 2: Find the transcript file

Each meeting's cloud recording has several files: video, audio, chat and, if enabled, a transcript. List them and pick the one with `file_type == "TRANSCRIPT"`:

```python
API = "https://api.zoom.us/v2"

def transcript_download_url(token: str, meeting_id: str) -> str | None:
    r = requests.get(f"{API}/meetings/{meeting_id}/recordings",
                     headers={"Authorization": f"Bearer {token}"}, timeout=20)
    r.raise_for_status()
    for f in r.json().get("recording_files", []):
        if f.get("file_type") == "TRANSCRIPT" and f.get("status") == "completed":
            return f["download_url"]
    return None
```

For recurring meetings, the meeting ID refers to the series. Use the specific occurrence's UUID to get one instance; UUIDs that start with `/` or contain `//` must be **double URL-encoded** in the path, a classic Zoom API gotcha.

To list everything recorded in a date range, use `GET /users/me/recordings?from=YYYY-MM-DD&to=YYYY-MM-DD` and page through `next_page_token`.

## Step 3: Download and parse

```python
def download(url: str, token: str) -> str:
    r = requests.get(url, headers={"Authorization": f"Bearer {token}"},
                     timeout=60, allow_redirects=True)
    r.raise_for_status()
    return r.content.decode("utf-8")
```

Zoom's transcript VTT puts the speaker name at the start of the cue text:

```
WEBVTT

1
00:00:02.120 --> 00:00:05.480
Priya Shah: Can we move the rollout to the 28th?

2
00:00:06.010 --> 00:00:08.300
Dev Patel: Yes, if QA signs off by Friday.
```

That's different from Teams, which uses `<v Speaker>` tags. A parser for Zoom's format:

```python
import re

CUE = re.compile(
    r"(?:^\d+\s*\n)?(\d{2}:\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}:\d{2}\.\d{3})\s*\n(.+?)(?=\n\s*\n|\Z)",
    re.S | re.M,
)

def parse_zoom_vtt(vtt: str):
    turns = []
    for start, end, body in CUE.findall(vtt):
        body = " ".join(body.split())
        speaker, sep, text = body.partition(": ")
        if not sep:                      # no speaker prefix on this cue
            speaker, text = "Unknown", body
        if turns and turns[-1]["speaker"] == speaker:
            turns[-1]["text"] += " " + text
            turns[-1]["end"] = end
        else:
            turns.append({"speaker": speaker, "start": start, "end": end, "text": text})
    return turns
```

Speaker names come from participants' Zoom display names, so "iPhone" or "Conference Room 3" will show up exactly like that. Plan for a rename step.

## Step 4: Get transcripts automatically with a webhook

Polling works, but Zoom can tell you when a transcript is ready. Subscribe your app to the **`recording.transcript_completed`** event. Zoom first sends a URL validation challenge, then signs each event so you can verify it:

```python
import hashlib, hmac, json, time
from flask import Flask, request, jsonify

app = Flask(__name__)
SECRET = os.environ["ZOOM_WEBHOOK_SECRET"].encode()

@app.post("/zoom/webhook")
def webhook():
    body = request.get_data(as_text=True)
    event = json.loads(body)

    if event.get("event") == "endpoint.url_validation":
        plain = event["payload"]["plainToken"]
        enc = hmac.new(SECRET, plain.encode(), hashlib.sha256).hexdigest()
        return jsonify(plainToken=plain, encryptedToken=enc)

    ts = request.headers.get("x-zm-request-timestamp", "")
    sig = request.headers.get("x-zm-signature", "")
    expected = "v0=" + hmac.new(SECRET, f"v0:{ts}:{body}".encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(sig, expected) or abs(time.time() - int(ts or 0)) > 300:
        return "", 401

    if event["event"] == "recording.transcript_completed":
        enqueue_transcript_job(event["payload"]["object"])   # fetch + parse async
    return "", 200
```

Do the download in a background job. Webhook handlers should return quickly.

## What you get, and what you don't

This pipeline gets you Zoom's transcript, reliably and automatically, for meetings recorded to your own account's cloud. It doesn't cover:

- meetings hosted by **other organizations** (you don't own their recordings);
- meetings that weren't **cloud recorded**;
- Google Meet, Teams or **in-person** conversations;
- summaries, action items and cross-meeting search.

That's the space notetakers occupy, with a bot in the call, a desktop app or the platform's own AI Companion. If you're comparing those rather than building, here's a rundown of [Zoom note takers](https://lynkk.ai/blog/zoom-note-taker), from AI Companion to bot-free apps. Lynkk's [Zoom integration](https://lynkk.ai/integrations/zoom) is one example: it records Zoom with a bot, the Mac app or the Chrome extension, without needing cloud recording turned on.

---

*Written by the Lynkk team with AI assistance. Zoom API v2 as of October 2026; check Zoom's developer documentation for current scopes and event names.*
