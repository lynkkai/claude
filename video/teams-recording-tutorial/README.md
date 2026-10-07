# Lynkk tutorial video: How to record a Microsoft Teams meeting

A 3:41 YouTube tutorial with a voiceover, motion graphics, background music and UI sound effects. It's built on the **Lynkk post kit** (`../../lynkk-post-kit`), so it uses the same Grid design system as lynkk.ai, and every claim comes from the kit's `docs/TRUTHS.md`.

| File | What it is |
|---|---|
| `lynkk-how-to-record-teams-meeting.mp4` | The finished video (1080p, 30 fps) |
| `thumbnail.png` | YouTube thumbnail |
| `captions.srt` | English subtitles, timed to the voiceover |
| `youtube-metadata.md` | Title options, description with chapters, tags |
| `script.json` | The voiceover, scene by scene. Edit this to change what Ava says |
| `video.html` | The visuals: 13 kit slides (`data-size="wide"`), animated from timing attributes |
| `check_script.mjs` | Runs the kit's copy and claims checker on the narration |
| `build_audio.py`, `render.cjs`, `mix_audio.py`, `build.sh` | The pipeline that turns the above into the MP4 |

## Storyline

1. **Intro** (0:00): Ava from Lynkk introduces three ways to record Teams.
2. **The problem** (0:10): someone has to press record, guests often can't, an hour of video nobody rewatches, tasks stuck in someone's head.
3. **Three ways** (0:28): meeting bot, Mac app, Chrome extension. The note comes out the same.
4. **Start free** (0:43): what the free plan includes.
5. **Way 1, the meeting bot** (0:53): paste the Teams link or turn on calendar auto-join, admit it from the lobby, live transcript. Free is audio only; video is Pro.
6. **Way 2, the Mac app** (1:14): the "Microsoft Teams call detected" card, Record, no bot, both sides on two channels, the recording column, saves itself when the call ends.
7. **Way 3, the Chrome extension** (1:45): the capsule above the call controls, no bot, tab audio and mic.
8. **After the call** (2:01): transcript in 17 languages, Meeting Brief, play from any timestamp.
9. **Jira** (2:21): send tasks from the note, one issue each, when you choose.
10. **Ask Lynkk, Pro** (2:31): answers from your own notes, with sources.
11. **Who it's for** (2:44), **recap** (3:14), **start free** (3:31).

## Design rules this follows

From `lynkk-post-kit/docs/DESIGN.md`: night band, the ruled column frame (rails, top bar, foot), two inks for emphasis, colour only from the photo plates, violet only for eyebrows, Inter 400/500, no shadows, no gradients, red only for "live". The presenter is the Lynkk mark with live voice levels in the foot, because the kit rules out AI-generated people.

## Check before publishing

- **Listen to it.** The voice is the open source Kokoro TTS voice `af_heart`. It says "Link" so the brand name is pronounced right.
- **Mock UI is illustrative.** It's drawn from what `TRUTHS.md` says each surface has, but some labels are stand-ins: the "Join" button and "Auto-join meetings from my calendar" in the bot window, the "Sent" chip after Send to Jira, and the Chrome capsule's recording state. Swap them for the real labels if they differ.
- **Teams facts in the problem section** ("guests often can't record", depending on company settings) are general Teams behaviour, worded loosely on purpose.
- Sample names and meeting content (Acme, Priya, Sam, March 3) are made up, as the kit recommends.

## Rebuilding

```bash
./build.sh
```

Needs Python 3 with `kokoro-onnx soundfile numpy`, Node with Playwright (Chromium) and ffmpeg. The first run downloads the Kokoro model (about 330 MB) from GitHub. The build runs both copy checks first and stops if either finds an error.

Quick visual checks without a full render: `node render.cjs --stills 10,40,90` writes PNGs to `build/`.

Music and sound effects are synthesized in `mix_audio.py`, so there are no licenses to clear.
