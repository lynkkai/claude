# Lynkk YouTube Short: Record a Teams meeting, three ways

A 40 second vertical cut (1080x1920) of `../teams-recording-tutorial`, on the post kit's `story` board. Same voice (Ava), same design system, same claims rules.

| File | What it is |
|---|---|
| `lynkk-teams-recording-short.mp4` | The finished Short, with burned-in captions |
| `captions.srt` | The same captions as a file |
| `youtube-metadata.md` | Title, description, settings |
| `script.json` | The voiceover. Edit this to change what Ava says |
| `video.html` | The 7 slides, animated from timing attributes (see `../pipeline/player.js`) |
| `build.sh` | Copy checks, voiceover, render, mix, mux |

## Beats

1. **Hook** (0:00): "Record a Teams meeting. Three ways." with the three ways on screen in the first second.
2. **Meeting bot** (0:05): paste the Teams link, Join, calendar auto-join, recording.
3. **Mac app** (0:12): the "Microsoft Teams call detected" card, Record, nothing joins the call.
4. **Chrome extension** (0:18): the capsule above the call controls, Record.
5. **The note** (0:24): a transcript in 17 languages, the Meeting Brief.
6. **Jira** (0:31): send tasks from the note.
7. **Start free** (0:34): the ember CTA plate.

## Shorts layout

YouTube draws the title, channel name and buttons over the bottom quarter and the lower right edge. So every slide keeps its content above y = 1250, the captions sit at y 1300 to 1420, and the narrator chip sits in the top bar. The kit's foot ("lynkk.ai" and the next hint) stays at the bottom for the frame, but expect it to be covered.

## Rebuilding

```bash
./build.sh
```

Quick stills: `node ../pipeline/render.cjs . --stills 2,10,30` writes PNGs to `build/`.
