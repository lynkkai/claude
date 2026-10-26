# Video 1: "Wait!" (brag edition)

50-second vertical video (1080x1920, 30 fps), rebuilt with the `brag-slim` and `lynkk-content` skills (`.claude/skills/`).
Script: `../video-scripts-revenue-story.md` (Video 1). Plan: `brag-output/brag-plan.md`.

- `brag-output/brag.mp4`: female voice (Kokoro `af_heart`) + music and sound effects.
- `brag-output/brag-male.mp4`: male voice (`am_fenrir`).
- `brag-output/brag-music-only.mp4`: no voice.
- `brag-output/brag.jpg`: poster, baked in as frame 0. `brag-output/share-copy.txt`: post caption.

The fix act shows real lynkk.ai UI (hero call summary, Ask Lynkk follow-up draft), the account is lynkk.ai's demo account
(Corvane Logistics), cuts land on beats at 120 BPM, and sound effects are written into the music in key.

## Re-render (from this folder, `K=../../.claude/skills/lynkk-content/scripts`)

```bash
(cd brag-output/work && node ../../$K/capture_ui.mjs ../jobs/summary.json && node ../../$K/capture_ui.mjs ../jobs/ask.json)
python3 $K/build.py scene.src.html scene.html
node $K/render.mjs video scene.html brag-output/work/frames.mp4 30 50
python3 music.py brag-output/work/music.wav
python3 $K/voiceover.py lines.json kokoro-v1.0.onnx voices-v1.0.bin brag-output/work/vo.wav af_heart
bash $K/mix.sh brag-output/work/frames.mp4 brag-output/work/music.wav brag-output/work/mix.mp4 brag-output/work/vo.wav
python3 $K/verify_speech.py brag-output/work/mix.mp4 lines.json
node $K/render.mjs still scene.html brag-output/brag.jpg 1.1
bash $K/poster.sh brag-output/work/mix.mp4 brag-output/brag.jpg brag-output/brag.mp4
```
