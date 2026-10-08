# Video 4 assets: sales calls with Lynkk

Graphics for `../04-sales-calls.md`, built with the `lynkk-design` skill and the kit in
`lynkk-post-kit/` (Grid design system, night band, photo plates, Inter 400/500, two inks).
The screen recordings (Mac app, Zoom, the briefing email, the note, Jira) are filmed in the demo
setup described in the script; everything here sits on top of or between that footage.

## Files in `out/`

| File | Size | Where it goes |
|---|---|---|
| `thumbnail-1.png` | 1280x720 | Main thumbnail: "Record the call. Nothing joins it." (Mac call card, night plate) |
| `thumbnail-2.png` | 1280x720 | Test: "The call ends. The brief is written." (Meeting Brief, ember plate) |
| `thumbnail-3.png` | 1280x720 | Test: "One app for the whole sales call." (before, during, after) |
| `motion/after-every-call.mp4` | 1920x1080, 8 s | Scene 2 (0:15): the four jobs after a sales call |
| `motion/whole-call.mp4` | 1920x1080, 14 s | Scene 3 (0:35) and Scene 9 (6:05): each stage lights up in turn (4-7 s before, 7-10 s during, 10-13 s after) |
| `motion/end-screen.mp4` | 1920x1080, 20 s | Last 20 s. Put the YouTube end-screen video element over the ember plate, subscribe under the button |
| `overlays/lt-before.png` | 1920x1080, transparent | Scene 4 lower third |
| `overlays/lt-during.png` | 1920x1080, transparent | Scene 5 lower third |
| `overlays/lt-after.png` | 1920x1080, transparent | Scene 6 lower third |
| `overlays/lt-ask.png` | 1920x1080, transparent | Scene 4 (Ask moment) and Scene 7 |
| `overlays/notice-fictional-demo.png` | 1920x1080, transparent | Scene 3, bottom left |
| `overlays/notice-consent.png` | 1920x1080, transparent | Scene 5, while Maya asks to record |
| `voiceover-script.txt` | text | The brand host's read, scene by scene |
| `captions-draft.srt` | captions | Draft cues spread over the target timings. Re-time after the edit, or upload the transcript to YouTube Studio and let it set the timing |

Overlays are full-frame PNGs with alpha: drop them on a track above the footage and fade them
in and out in the editor (about 0.3 s).

## Sources and re-rendering

| Source | Output | Command (from this folder) |
|---|---|---|
| `thumbnails.html` | `out/thumbnail-*.png` | `node ../../../lynkk-post-kit/scripts/render.mjs thumbnails.html --scale 0.8` |
| `after-every-call.html`, `whole-call.html`, `end-screen.html` | `out/motion/*.mp4` | `node tools/capture.mjs whole-call.html /tmp/f/wc 14` then `ffmpeg -framerate 30 -i /tmp/f/wc/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 16 out/motion/whole-call.mp4` (end screen: capture 1.5 s, add `-vf tpad=stop_mode=clone:stop_duration=18.5`) |
| `overlays.html` | `out/overlays/*.png` | `node tools/overlays.mjs` |
| `../04-sales-calls.md` | `out/voiceover-script.txt`, `out/captions-draft.srt` | `python3 tools/captions.py ../04-sales-calls.md` |

Every source links the kit by relative path, so brand changes in `lynkk-post-kit/kit/` flow
through on the next render. Run the copy check on any file you change:
`node ../../../lynkk-post-kit/scripts/check.mjs <file>`.
