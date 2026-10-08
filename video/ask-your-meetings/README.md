# Ask Your Meetings: YouTube explainer video

A 2:46 explainer for https://lynkk.ai/features/ask-your-meetings, structured problem first, then solution, then use cases. It has a female voiceover and an animated illustrated presenter, and it's styled with the Lynkk design kit.

| File | What it is |
|---|---|
| `lynkk-ask-your-meetings.mp4` | Final video, 1920x1080, 30 fps, AAC audio normalized to -14 LUFS (YouTube target) |
| `thumbnail.png` | 1280x720 YouTube thumbnail |
| `captions.srt` | English captions, timed to the voiceover |
| `youtube.md` | Title options, description, chapters, tags, pinned comment |
| `script.md` | The voiceover script, by scene |

## Design kit

The colors and type come from the Lynkk Homepage Design canvas:

- Type: Fraunces (display), IBM Plex Sans (body), both bundled in `assets/fonts/`
- Colors: ink `#16181d`, cream `#f7f6f2`, indigo `#3346d3`, periwinkle `#aab4ff`, teal `#0f766e`, rust `#b4541f`

## How it's built

1. `segments.json` holds the script, one sentence per segment, tagged with its scene.
2. `tts.py` generates the voice with Kokoro TTS (`af_heart` female voice). It also writes the timeline, a per-frame mouth envelope for the avatar's lip sync, and `captions.srt`.
3. `music.py` synthesizes a soft ambient bed, so there's no stock-music licensing to worry about. The bed ducks under the voice.
4. `scenes.html` animates every scene as a pure function of time. `render.mjs` steps through it frame by frame in headless Chromium and pipes the frames to ffmpeg.
5. `build.sh` runs the whole pipeline and muxes the final MP4.

To change a line, edit `segments.json` and run `./build.sh`. The scene timing follows the new audio automatically.
