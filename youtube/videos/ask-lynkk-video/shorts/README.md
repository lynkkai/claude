# Ask your meetings: YouTube Short

The vertical cut of `../out/lynkk-ask-your-meetings.mp4`, for YouTube Shorts (also fits Instagram Reels and TikTok).
Built with the `lynkk-design` skill: every claim is from `lynkk-post-kit/docs/TRUTHS.md`, every
screen is a kit `story` board, and all copy passes `lynkk-post-kit/scripts/check.mjs`.

## Upload these

| File | Use |
|---|---|
| `out/lynkk-ask-your-meetings-short.mp4` | The Short. 0:48, 1080x1920, 30 fps, H.264 + AAC, loudness -15 LUFS |
| `out/captions.srt` | English captions, timed to the narration |

The headline on every scene repeats what the voice says, so it works with the sound off.
Key content sits in the top two thirds, clear of the Shorts title and buttons.

## Title

**Ask your meetings anything #productivity #meetings**

Alternates: "Find what was said in any meeting #worktips", "Stop searching your meetings. Ask them. #productivity".

## Description

```
Someone said the answer in a meeting. Ask Lynkk finds it in your own notes, shows the sources, and plays the moment it was said. Ask Lynkk is part of Lynkk Pro.

Start free: https://lynkk.ai
Full video: [link to the long video once it's live]

The company, people and data shown are fictional. Product screens are simplified drawings.

#AskLynkk #MeetingNotes #Productivity #Lynkk
```

## Link it to the long video

In YouTube Studio, set the Short's "Related video" to the full Ask Your Meetings video, so viewers can tap through to it.

## The script (0:48)

| Time | Scene | Voice |
|---|---|---|
| 0:00 | Hook | You had the answer once. Someone said it in a meeting, three weeks ago. Now nobody can find it. |
| 0:07 | Problem | It's in a recording nobody rewatches, or in notes spread across different places. So the same meeting happens twice. |
| 0:16 | Ask Lynkk (Pro) | Ask Lynkk answers from your own meeting notes. What did Acme say about the renewal? You get the answer with its sources, and it plays the moment it was said. |
| 0:26 | What's open | Ask what's still open, and it lists the open tasks and decisions across your notes. |
| 0:32 | Act on it | Then act on it: create a Google Calendar event or a Jira issue. Nothing happens until you confirm. |
| 0:40 | Start free | Stop searching your meetings. Ask them. Ask Lynkk is part of Lynkk Pro. Start free at lynkk.ai. |

## How it was made (to edit or rebuild)

From this folder: edit `narration.json`, then
`python3 -I tts.py kokoro-v1.0.onnx voices-v1.0.bin` (voice, `out/timing.json`, captions),
`node capture.mjs video <clipsDir> v1 v2 v3 v4 v5 v6` (scenes from `short.html`), and
`./assemble.sh <clipsDir>`. `node capture.mjs stills out/storyboard v1 ... v6` writes a still of each scene.
