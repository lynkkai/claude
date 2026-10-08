# Video 4 (finished): AI Note Taker for Sales Calls

A complete, narrated explainer, ready to upload to the official Lynkk YouTube channel.
Built with the `lynkk-design` skill: every claim is from `lynkk-post-kit/docs/TRUTHS.md`
(checked 2026-09-29), every screen is drawn with the kit's design system, and all copy
passes `lynkk-post-kit/scripts/check.mjs`.

## Upload these

| File | Use |
|---|---|
| `out/lynkk-sales-calls.mp4` | The video. 4:16, 1920x1080, 30 fps, H.264 + AAC, loudness -14.9 LUFS |
| `out/thumbnail.png` | Thumbnail, 1280x720. Alternates for "Test & Compare": `../04-assets/out/thumbnail-1.png`, `thumbnail-2.png` |
| `out/captions.srt` | English captions, timed to the narration. Upload under Subtitles |
| `out/chapters.txt` | Chapters (already in the description below) |

The last 12 seconds are the end screen: add a video element over the orange plate and a
subscribe element under the button in YouTube Studio.

## Title

**AI Note Taker for Sales Calls: How Lynkk Works Before, During and After**

## Description

```
Every sales call ends with the same admin: notes, next steps, a recap, and booking the next meeting. This video walks through how Lynkk handles that work, from the morning briefing before the call to the follow-up after it.

Start free: https://lynkk.ai

In this video:
• Four ways to record: the Mac app and the Chrome extension (no bot in the call), the meeting bot for Google Meet, Zoom and Teams, and your mic in the browser for meetings in person
• Before the call: a morning briefing email with who you're meeting, your last note with them, and the action items still open
• During the call: recording on the Mac with live words on the edge of your screen, kept out of your screen share on macOS 15.4 and later (best effort)
• After the call: the Meeting Brief, with key takeaways, decisions, open questions and action items with owners and due dates
• Summary Shapes (Pro), sharing, and the summary emailed to attendees if you opt in
• Tasks as a list or kanban, and Send to Jira, one issue per action item
• Ask Lynkk (Pro): answers from your own notes with sources, and actions like booking a Google Calendar event behind a confirm card
• Workspaces of up to 10 seats where everyone gets Pro, and Personal notes

Transcripts in 17 languages, four of them in beta. Lynkk never trains on your conversations. The Mac app needs Apple silicon and macOS 14.2 or later.

CHAPTERS
0:00 Intro
0:16 What Lynkk is
0:30 Four ways to record
0:54 Before the call
1:14 During the call
1:38 Built for real calls
1:59 The Meeting Brief
2:23 Summary Shapes and sharing
2:45 Tasks and Jira
3:04 Ask Lynkk
3:27 For sales teams
3:45 Start free

The company, people and data shown are fictional. Product screens are simplified drawings. Always tell everyone on a call when you are recording it.

#AINoteTaker #SalesCalls #MeetingNotes #Productivity #Lynkk
```

## Tags

```
ai note taker, ai note taker for sales, ai sales assistant, sales call notes, ai meeting notes, meeting notes app, bot free ai note taker, ai note taker for zoom, meeting brief, action items, send tasks to jira, lynkk
```

## Pinned comment

> Which part of a sales call takes you longest once it ends: the notes, the recap, or booking the next meeting?
> Try Lynkk free: https://lynkk.ai

## How it was made (to edit or rebuild)

| Step | File | Command (from this folder) |
|---|---|---|
| Narration text | `narration.json` | edit the lines; run the copy check |
| Voice | `tts.py` | Kokoro open TTS model (`af_heart`), run locally: `<venv>/bin/python -I tts.py kokoro-v1.0.onnx voices-v1.0.bin` writes `out/audio/`, `out/timing.json`, `out/captions.srt` |
| Scenes | `video.html` | 12 wide kit boards; `data-s="n"` reveals an element when narration line n starts |
| Frames | `capture.mjs` | `node capture.mjs /tmp/frames s1 s2 ...` (1920x1080, 30 fps) |
| Final video | `assemble.sh` | `./assemble.sh /tmp/frames` joins scenes, narration (normalised to -14 LUFS) and the end screen |

Voice model files: `kokoro-v1.0.onnx` and `voices-v1.0.bin` from the kokoro-onnx GitHub
releases (`pip install kokoro-onnx soundfile`). `out/storyboard/` has a still of every scene.
