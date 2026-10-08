# Use-case videos: Lynkk for sales, HR and consulting teams

Three narrated videos of about one minute each for the official Lynkk YouTube channel. Each one runs
problem first, then the solution: record the meeting, the Meeting Brief, Ask Lynkk, Lynkk for
Slack and Mac dictation, then the CTA.

Built with the `lynkk-design` skill: every claim is from `lynkk-post-kit/docs/TRUTHS.md`
(checked 2026-09-29), every screen is drawn with the kit's design system, and all copy passes
`lynkk-post-kit/scripts/check.mjs`. Narration is the channel voice (Kokoro `af_heart`).

## Upload these

| Video | File | Thumbnail | Captions |
|---|---|---|---|
| Sales | `sales/out/lynkk-for-sales-teams.mp4` (0:58) | `out/sales-thumbnail.png` | `sales/out/captions.srt` |
| HR | `hr/out/lynkk-for-hr-teams.mp4` (0:59) | `out/hr-thumbnail.png` | `hr/out/captions.srt` |
| Consulting | `consulting/out/lynkk-for-consulting-teams.mp4` (1:03) | `out/consulting-thumbnail.png` | `consulting/out/captions.srt` |

All videos: 1920x1080, 30 fps, H.264 + AAC, -15 LUFS. Thumbnails: 1280x720. The CTA board holds
for about 10 seconds at the end: put a YouTube end screen (subscribe, next video) on the ember plate.

## Sales

**Title:** Lynkk for Sales Teams: Every Call Recorded, Every Follow-up Owned

```
Back-to-back sales calls leave no time to write anything down. Follow-ups lose their owner and the next call starts cold. This video shows how sales teams use Lynkk before, during and after a call.

Start free: https://lynkk.ai

In this video:
• Record calls with the Mac app (it notices Zoom, Google Meet and Teams, and no bot joins) or the meeting bot
• The Meeting Brief: decisions, open questions, and action items with an owner and a due date
• Every timestamp plays the recording from that moment
• A morning briefing email with what's still open before your next call
• Ask Lynkk (Pro): answers from your own notes, with sources
• Lynkk for Slack (Pro): ask about any deal with @Lynkk
• Dictation on the Mac: hold a key, talk, and the words land where your cursor is

CHAPTERS
0:00 The problem
0:13 Record, then the Meeting Brief
0:31 Ask, Slack and dictation
0:46 Start free

The company, people and data shown are fictional. Product screens are simplified drawings. Always tell everyone on a call when you are recording it.

#Lynkk #SalesProductivity #MeetingNotes #AIMeetingAssistant
```

**Tags:** lynkk, ai meeting assistant, ai note taker, sales call notes, sales follow up, meeting brief, action items, sales productivity, ask lynkk, slack, dictation

## HR

**Title:** Lynkk for HR Teams: Interview Notes and Feedback Without the Typing

```
Interview after interview, and the feedback lives in someone's head. Scorecards come in late and the debrief turns into a guessing game. This video shows how HR and people teams use Lynkk for interviews and 1:1s.

Start free: https://lynkk.ai

In this video:
• Record interviews online or in person: the Mac app (no bot joins), the meeting bot, or your mic in the browser
• The Meeting Brief: takeaways with timestamps, open questions, and next steps with an owner
• Ask Lynkk (Pro): what a candidate said in any round, with the source
• Personal notes: set a sensitive 1:1 to Personal, so only you can see it
• Lynkk for Slack (Pro): ask from Slack with /lynkk
• Dictation on the Mac: write feedback by talking, in any app

CHAPTERS
0:00 The problem
0:15 Record, then the Meeting Brief
0:32 Ask, Slack and dictation
0:48 Start free

The company, people and data shown are fictional. Product screens are simplified drawings. Always tell everyone in a meeting when you are recording it.

#Lynkk #HR #Recruiting #MeetingNotes
```

**Tags:** lynkk, ai for hr, interview notes, interview feedback, hiring, recruiting, one on one meeting notes, ai note taker, meeting brief, slack, dictation

## Consulting

**Title:** Lynkk for Consultants: Client Meetings and Workshops, Captured and Sent to Jira

```
A dozen workshops a week, and one memory trying to keep up. Decisions get lost, write-ups take your evenings, and tasks never reach the delivery team. This video shows how consultants use Lynkk across client calls and workshops.

Start free: https://lynkk.ai

In this video:
• Record client calls on the Mac (no bot joins) or with the meeting bot, and workshops in the room with your mic in the browser
• Transcripts in 17 languages, four of them in beta, with the language detected automatically
• The Meeting Brief keeps decisions with their context, and action items with owners
• Send action items to Jira from the note, one issue each
• Ask Lynkk (Pro): find notes by person, company or project, and play the moment it was said
• Lynkk for Slack (Pro) and dictation on the Mac for reports

CHAPTERS
0:00 The problem
0:15 Record, then send to Jira
0:35 Ask, Slack and dictation
0:51 Start free

The company, people and data shown are fictional. Product screens are simplified drawings. Always tell everyone in a meeting when you are recording it.

#Lynkk #Consulting #MeetingNotes #Jira
```

**Tags:** lynkk, ai for consultants, client meeting notes, workshop notes, send tasks to jira, meeting brief, ai note taker, multilingual transcription, ask lynkk, slack, dictation

## Pinned comment (all three)

> Which part of your meetings takes the most time afterwards?
> Try Lynkk free: https://lynkk.ai

## How it was made (to edit or rebuild)

Run these from a video folder (`sales/`, `hr/` or `consulting/`):

| Step | File | Command |
|---|---|---|
| Narration text | `narration.json` | edit the lines, then `node ../../../../lynkk-post-kit/scripts/check.mjs narration.json` |
| Voice | `../tools/tts.py` | `python3 -I ../tools/tts.py kokoro-v1.0.onnx voices-v1.0.bin` writes `out/audio/`, `out/timing.json`, `out/captions.srt`, `out/chapters.txt` |
| Scenes | `video.html` | seven wide kit boards; `data-s="n"` reveals an element when narration line n starts (`../tools/render.js`) |
| Stills | `../tools/capture.mjs` | `node ../tools/capture.mjs stills out/storyboard` |
| Clips | `../tools/capture.mjs` | `node ../tools/capture.mjs video <clipsDir>` (1920x1080, 30 fps) |
| Final video | `../tools/assemble.sh` | `../tools/assemble.sh <clipsDir> lynkk-for-<name>-teams` |
| Thumbnails | `thumbnails.html` | `node lynkk-post-kit/scripts/render.mjs youtube/videos/use-cases/thumbnails.html --scale 0.8` (from the repo root) |

Voice model files: `kokoro-v1.0.onnx` and `voices-v1.0.bin` from the kokoro-onnx GitHub releases
(`pip install kokoro-onnx soundfile`).

## Claims left out

Parts of the original brief asked for features that `lynkk-post-kit/docs/TRUTHS.md` lists under
"Don't claim", so they are not in these videos. Slack is shown as it really works: you ask Lynkk
a question and it answers from your notes.
