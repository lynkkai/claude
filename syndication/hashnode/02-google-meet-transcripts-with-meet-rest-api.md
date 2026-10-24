---
platform: Hashnode
title: "Pulling Google Meet Transcripts With the Meet REST API (Python)"
subtitle: "Find a meeting's conference record, list its transcripts, and turn transcript entries into a clean, speaker-labelled text file."
slug: google-meet-transcripts-meet-rest-api-python
tags: [google-meet, python, api, google-workspace, transcription]
target_queries: ["google meet api get transcript", "google meet transcript", "how to download transcript from google meet recording"]
evidence: "GSC: 'google meet api get transcript' 12 impr at 21.7 (developer intent the main blog does not answer); 'google meet transcript' 101 impr at 11.5; 'how to download transcript from google meet recording' 10 at 13.4; /blog/google-meet-transcript 3,450 impr at avg 9.6"
main_site_links:
  - https://lynkk.ai/blog/google-meet-transcript
  - https://lynkk.ai/blog/google-meet-ai-note-taker
  - https://lynkk.ai/integrations/google-meet
canonical: "none (original article, do not set a canonical)"
cover_image: "Terminal window printing 'Priya: Can we move the rollout to the 28th?' under a Meet logo-free grid"
status: draft
---

# Pulling Google Meet Transcripts With the Meet REST API (Python)

When a Google Meet meeting is transcribed, Meet saves a Google Doc to the organizer's Drive. That's fine for humans, but if you're building anything on top of meetings (search, summaries, a CRM sync) you want structured data: who said what, and when.

The **Google Meet REST API** exposes exactly that. This post shows how to go from a meeting code to a speaker-labelled transcript in Python.

> **Prerequisites.** Transcripts only exist if transcription was turned on during the meeting, on a Google Workspace edition that supports it. If you're not sure whether your plan includes transcripts or where the Doc ends up, start with this non-technical [guide to Google Meet transcripts](https://lynkk.ai/blog/google-meet-transcript).

## The data model in one minute

The API is organized around **conference records**: one record per occurrence of a meeting in a meeting space.

```
spaces/{space}                         the meeting room (has a meeting code)
conferenceRecords/{record}             one occurrence of a meeting
  ├── participants/{participant}       who joined
  ├── recordings/{recording}           video recordings (Drive file)
  └── transcripts/{transcript}         transcript (Google Doc)
        └── entries/{entry}            one utterance: participant, text, start/end time
```

The `entries` collection is what we want. Each entry has a `participant`, the spoken `text`, a `languageCode`, and `startTime`/`endTime`.

## Step 1: Set up a project and OAuth

1. In Google Cloud Console, create a project and **enable the Google Meet REST API**.
2. Configure an OAuth consent screen and create an **OAuth client ID** (Desktop app works for a script).
3. Use a read-only scope: `https://www.googleapis.com/auth/meetings.space.readonly`.

Install dependencies:

```bash
pip install google-auth-oauthlib google-auth requests
```

Get credentials with the installed-app flow:

```python
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/meetings.space.readonly"]

def get_token() -> str:
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    creds = flow.run_local_server(port=0)
    if not creds.valid:
        creds.refresh(Request())
    return creds.token
```

For production, store and refresh credentials properly rather than running the browser flow every time.

## Step 2: A tiny paginated GET helper

Every list endpoint paginates with `pageToken`, so write one helper:

```python
import requests

BASE = "https://meet.googleapis.com/v2"

def list_all(path: str, token: str, key: str, params: dict | None = None):
    params = dict(params or {})
    headers = {"Authorization": f"Bearer {token}"}
    while True:
        r = requests.get(f"{BASE}/{path}", headers=headers, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        yield from data.get(key, [])
        token_next = data.get("nextPageToken")
        if not token_next:
            break
        params["pageToken"] = token_next
```

## Step 3: Find the conference record

If you have the meeting code (the `abc-mnop-xyz` part of the Meet link), filter conference records by it:

```python
def conference_records(token: str, meeting_code: str):
    flt = f'space.meeting_code = "{meeting_code}"'
    return list(list_all("conferenceRecords", token, "conferenceRecords", {"filter": flt}))
```

A recurring meeting reuses the same space, so you'll get one record per occurrence. Each has `startTime` and `endTime`; pick the one you want.

## Step 4: Map participants to names

Entries reference participants by resource name, so build a lookup first. Signed-in users have a `signedinUser.displayName`; others may be `anonymousUser` or `phoneUser`.

```python
def participant_names(token: str, record: str) -> dict[str, str]:
    names = {}
    for p in list_all(f"{record}/participants", token, "participants"):
        user = p.get("signedinUser") or p.get("anonymousUser") or p.get("phoneUser") or {}
        names[p["name"]] = user.get("displayName", "Unknown speaker")
    return names
```

## Step 5: Read transcript entries

```python
def transcript_lines(token: str, record: str):
    names = participant_names(token, record)
    for t in list_all(f"{record}/transcripts", token, "transcripts"):
        for e in list_all(f"{t['name']}/entries", token, "transcriptEntries"):
            yield {
                "speaker": names.get(e.get("participant"), "Unknown speaker"),
                "start": e.get("startTime"),
                "text": e.get("text", "").strip(),
            }
```

Note that transcripts move through states (`STARTED`, `ENDED`, `FILE_GENERATED`). Entries can lag behind the end of the meeting, so if you're processing immediately after a call, poll until the transcript has ended.

## Step 6: Write a readable transcript

Merge consecutive entries from the same speaker so the output reads like a conversation:

```python
from datetime import datetime

def to_text(lines) -> str:
    out, last = [], None
    for line in lines:
        ts = datetime.fromisoformat(line["start"].replace("Z", "+00:00")).strftime("%H:%M:%S")
        if line["speaker"] == last:
            out[-1] += " " + line["text"]
        else:
            out.append(f"[{ts}] {line['speaker']}: {line['text']}")
            last = line["speaker"]
    return "\n".join(out)

if __name__ == "__main__":
    tok = get_token()
    rec = conference_records(tok, "abc-mnop-xyz")[-1]["name"]
    print(to_text(transcript_lines(tok, rec)))
```

Output:

```
[14:02:11] Priya Shah: Can we move the rollout to the 28th?
[14:02:16] Dev Patel: Yes, if QA signs off by Friday.
```

## Gotchas

- **No transcript, no data.** If nobody turned transcription on, the `transcripts` list is empty. The API can't transcribe after the fact.
- **Access is scoped to what the user can see.** You'll only get conference records for meetings the authorizing user organized or has access to, within their Workspace.
- **Want it in real time?** The REST API is post-meeting. For notifications when a transcript is ready, look at Google Workspace Events API subscriptions for Meet.
- **Retention follows your Workspace policies.** Don't assume records live forever.

## When this approach isn't enough

The Meet API is ideal for internal tools inside one Workspace. It's a poor fit when:

- you meet across Meet, Zoom and Teams and want one pipeline;
- your plan doesn't include transcripts;
- you need summaries, action items and search, not just text;
- people code-switch between languages, which native captions may not handle well.

That's the gap third-party notetakers fill. If you're evaluating them rather than building, here's a comparison of [AI note takers for Google Meet](https://lynkk.ai/blog/google-meet-ai-note-taker), including Gemini's own notes. Lynkk's [Google Meet integration](https://lynkk.ai/integrations/google-meet) is one example: it records Meet through a bot, a Chrome extension or the Mac app, without needing Workspace transcripts to be turned on.

---

*Written by the Lynkk team with AI assistance. API shapes current as of October 2026; check Google's Meet REST API reference for changes.*
