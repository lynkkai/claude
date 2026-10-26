# Video 2: "Wrong." (brag edition)

50-second vertical video (1080x1920, 30 fps), rebuilt with the `brag-slim` skill and the `lynkk-content` skill
(both in `.claude/skills/`). Script: `../video-scripts-revenue-story.md` (Video 2). Plan: `brag-output/brag-plan.md`.

- `brag-output/brag.mp4`: female voice (Kokoro `af_heart`) + music and sound effects.
- `brag-output/brag-male.mp4`: male voice (`am_fenrir`).
- `brag-output/brag-music-only.mp4`: no voice, for a human voiceover.
- `brag-output/brag.jpg`: poster, also baked in as frame 0. `brag-output/share-copy.txt`: post caption.

What changed from the first version: the fix act shows real lynkk.ai product UI (the Sales Call note and the live Cue demo,
captured from the site), the account is the site's own demo account (Corvane Logistics), every cut lands on a beat at 120 BPM,
sound effects are written into the music in key, captions hold long enough to read, and the poster is frame 0.

## Re-render

Uses the lynkk-content scripts (`K=.claude/skills/lynkk-content/scripts`, from the repo root):
```bash
node $K/capture_ui.mjs brag-output/jobs/cue.json   # run inside brag-output/work so frames land there
node $K/capture_ui.mjs brag-output/jobs/note.json
python3 $K/build.py scene.src.html scene.html
node $K/render.mjs video scene.html brag-output/work/frames.mp4 30 50
python3 music.py brag-output/work/music.wav
python3 $K/voiceover.py lines.json kokoro-v1.0.onnx voices-v1.0.bin brag-output/work/vo.wav af_heart
bash $K/mix.sh brag-output/work/frames.mp4 brag-output/work/music.wav brag-output/work/mix.mp4 brag-output/work/vo.wav
python3 $K/verify_speech.py brag-output/work/mix.mp4 lines.json
node $K/render.mjs still scene.html brag-output/brag.jpg 1.1
bash $K/poster.sh brag-output/work/mix.mp4 brag-output/brag.jpg brag-output/brag.mp4
```
