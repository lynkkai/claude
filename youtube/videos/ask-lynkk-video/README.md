# Ask your meetings (finished): Ask Lynkk explainer

A narrated explainer for the Ask Lynkk feature (lynkk.ai/features/ask-your-meetings), ready to upload to the official Lynkk YouTube channel. It runs problem first, then the solution, then use cases.
Built with the `lynkk-design` skill: every claim is from `lynkk-post-kit/docs/TRUTHS.md`
(checked 2026-09-29), every screen is drawn with the kit's design system, and all copy
passes `lynkk-post-kit/scripts/check.mjs`.

## Upload these

| File | Use |
|---|---|
| `out/lynkk-ask-your-meetings.mp4` | The video. 3:18, 1920x1080, 30 fps, H.264 + AAC, loudness -15 LUFS |
| `thumb/out/thumbnail-1.png` | Thumbnail, 1280x720. Alternate for "Test & Compare": `thumb/out/thumbnail-2.png` |
| `out/captions.srt` | English captions, timed to the narration. Upload under Subtitles |

The last 12 seconds are the end screen: add a video element over the orange plate and a
subscribe element under the button in YouTube Studio.

## Title

**Ask Your Meetings: Get Answers From Your Own Meeting Notes | Ask Lynkk**

Alternates: "Stop Searching Your Meetings. Ask Them. | Lynkk", "How to Find Anything Said in a Meeting | Ask Lynkk".

## Description

```
Someone said the answer in a meeting three weeks ago. Now nobody can find it. This video shows how Ask Lynkk turns your meeting notes into answers you can ask for in plain words.

Start free: https://lynkk.ai

In this video:
• Why meeting knowledge gets lost: recordings nobody rewatches, notes spread across places
• How Lynkk records: the Mac app and the Chrome extension (no bot in the call), the meeting bot for Google Meet, Zoom and Teams, and your mic in the browser for meetings in person
• Ask Lynkk (Pro): a chat that answers only from your own notes, with citation chips, and "Play from" to hear the moment it was said
• Find notes by person, company or project, and list open tasks and decisions
• Attach a PDF, Word, text, Markdown or CSV file
• Act on the answer behind a confirm card: a Google Calendar event with a Meet link, share a note, mark a task done, or create a Jira issue
• The morning briefing email before your meetings, and answers in Slack (Pro)
• Use cases for sales, product and engineering, managers and teams

Transcripts in 17 languages, four of them in beta. Lynkk never trains on your conversations. Recording, transcripts and the Meeting Brief are on the Free plan; Ask Lynkk is part of Pro.

CHAPTERS
0:00 The answer you lost
0:11 Where meeting knowledge goes
0:38 Ask Lynkk
0:57 Record the meeting
1:13 Ask in plain words
1:30 Open tasks and decisions
1:42 Files and actions
2:01 Before the meeting, and in Slack
2:23 Use cases
2:47 Private by default
3:00 Start free

The company, people and data shown are fictional. Product screens are simplified drawings. Always tell everyone on a call when you are recording it.

#AskLynkk #MeetingNotes #AIMeetingAssistant #Productivity #Lynkk
```

## Tags

```
ask lynkk, ask your meetings, ai meeting assistant, ai note taker, meeting notes ai, search meeting notes, meeting transcript search, action items, open decisions, meeting brief, send tasks to jira, lynkk
```

## Pinned comment

> What's one thing from a past meeting you wish you could ask about right now?
> Try Lynkk free: https://lynkk.ai

## Presenter

No drawn avatar: the kit rules out drawn people. The voice is a female narrator (Kokoro `af_heart`).
For an on-camera presenter, record one in a presenter tool and the clip can be placed in a kit frame.

## How it was made (to edit or rebuild)

| Step | File | Command (from this folder) |
|---|---|---|
| Narration text | `narration.json` | edit the lines; run the copy check |
| Voice | `tts.py` | Kokoro open TTS model (`af_heart`), run locally: `python3 -I tts.py kokoro-v1.0.onnx voices-v1.0.bin` writes `out/audio/`, `out/timing.json`, `out/captions.srt` |
| Scenes | `video.html` | 12 wide kit boards plus the end screen; `data-s="n"` reveals an element when narration line n starts |
| Clips | `capture.mjs` | `node capture.mjs video <clipsDir> s1 s2 ... s12 end` (1920x1080, 30 fps); `stills out/storyboard ...` for a still of each scene |
| Final video | `assemble.sh` | `./assemble.sh <clipsDir>` joins the clips and the narration (normalised to -14 LUFS) |
| Thumbnails | `thumb/thumbnails.html` | `node lynkk-post-kit/scripts/render.mjs <file> --scale 0.8` |

Voice model files: `kokoro-v1.0.onnx` and `voices-v1.0.bin` from the kokoro-onnx GitHub
releases (`pip install kokoro-onnx soundfile`). `out/storyboard/` has a still of every scene.
