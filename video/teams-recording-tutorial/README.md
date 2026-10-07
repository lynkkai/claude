# Lynkk tutorial video: How to record a Microsoft Teams meeting

A 3 minute YouTube tutorial with an animated presenter (Ava), an AI voiceover, motion graphics, background music and UI sound effects.

| File | What it is |
|---|---|
| `lynkk-how-to-record-teams-meeting.mp4` | The finished video (1080p, 30 fps, 3:02) |
| `thumbnail.png` | YouTube thumbnail |
| `captions.srt` | English subtitles, timed to the voiceover |
| `youtube-metadata.md` | Title options, description with chapters, tags |
| `script.json` | The voiceover script, scene by scene (edit this to change what Ava says) |
| `video.html` | All visuals: scenes, avatar, mock UI, animation timing |
| `build_audio.py`, `render.cjs`, `mix_audio.py`, `build.sh` | The pipeline that turns the above into the MP4 |

## Storyline

1. **Intro** (0:00): Ava introduces the tutorial.
2. **The problem** (0:12): recording switched off by IT policy, guests can't record, AI recaps need an add-on license, recordings buried in OneDrive or SharePoint and auto-expiring, nobody rewatches an hour of video, in-person talks never captured.
3. **Meet Lynkk** (0:49): one AI for before, during and after the meeting.
4. **Six tutorial steps** (1:05): start free, connect calendar, Lynkk joins and records (or the Mac app), ask live by voice, notes + action items + CRM + Jira in about 30 seconds, search the knowledge graph.
5. **Use cases** (2:16): sales, product and engineering, founders and managers, consultants and recruiters, global teams, regulated industries.
6. **Recap and call to action** (2:41): start free at lynkk.ai, subscribe.

## Check before publishing

The video is built from `memory/lynkk-brand.md`. lynkk.ai wasn't reachable from the build environment, so a few things are stand-ins:

- **Brand look.** The colors (violet, blue, cyan on dark navy), the Inter typeface and the "link" logo mark are placeholders in the Lynkk style, not the official brand kit. To switch, edit the color tokens at the top of `video.html` and `logoHTML()`, then rebuild.
- **Product UI.** The app screens are illustrative mockups, not real screenshots. Make sure the flow matches the real product, especially: the **Start free** button and the signup step, the **Connect calendar** step, Lynkk joining Teams as a participant that you admit from the lobby, and the Mac app notification. If the real flow differs, change the matching line in `script.json` and the scene in `video.html`.
- **Teams support.** The brand memory lists supported meeting platforms as "to confirm". This video assumes Teams works.
- **Sample data.** Names (Priya, Lucía, Dana, Acme), "PROD-482", the 12% discount and other meeting content are made up for the demo.
- **Teams limitations** in the problem section are worded loosely on purpose ("may", "often", "usually"), because they depend on the customer's Microsoft 365 license and admin policy.

## Rebuilding

```bash
./build.sh
```

Needs Python 3 with `kokoro-onnx soundfile numpy`, Node with Playwright (Chromium) and ffmpeg. The first run downloads the open source Kokoro TTS model (about 330 MB) from GitHub. The voice is Kokoro `af_heart`. To use a different voice, set `"voice"` in `script.json` (for example `af_bella`, or `am_michael` for a male voice).

Quick visual checks without a full render: `node render.cjs --stills 10,40,90` writes PNGs to `build/`.

The music and sound effects are synthesized in `mix_audio.py`, so there are no third-party licenses to clear.
