# Lynkk comparison videos

Four videos for the Lynkk social accounts, plus their post copy in `social-posts.md`.

- `lynkk-vs-otter-short.mp4` and `lynkk-vs-granola-short.mp4`: 9:16, about 54 seconds
- `lynkk-vs-otter-long.mp4` and `lynkk-vs-granola-long.mp4`: 16:9, about 2:20 to 2:30

## What's in them

- **Hook first.** Each opens on a single line about the competitor's gap ("Otter understands 6 languages.
  Your team speaks Hinglish." / "Granola writes your notes. Then the recording is gone.").
- **Lynkk design kit.** These use the tokens from lynkk.ai: black #111 and white, the violet accent #7063BE
  with lavender #BEB4FB, Inter and Inter Display for type, JetBrains Mono for labels, the dot grid
  background, and the Lynkk sphere logo. The product cards are modeled on the UI shown on lynkk.ai.
- **Facts.** Every claim comes from lynkk.ai/compare/otter, lynkk.ai/compare/granola and the lynkk.ai
  FAQ and pricing, checked October 2026. Comparison scenes show a source line on screen.
- **Voice.** Indian English female voice (Kokoro TTS, `hf_alpha`), with a little speed variation per
  line, natural pauses, warmth and compression so it sounds like a mic read. Captions are burned in.
- **Music.** An original track synthesized in `src/music.py`, with no samples and no licensing, ducked
  under the voice.

## Rebuild

```bash
pip install kokoro-onnx soundfile numpy
# model files: kokoro-v1.0.onnx and voices-v1.0.bin from github.com/thewh1teagle/kokoro-onnx releases,
# placed in <work>/../models/
cd src
python3 build_audio.py lynkk-vs-otter-short <work>          # voice, music, mix, timeline.json
node render.js <work>/lynkk-vs-otter-short ../lynkk-vs-otter-short.mp4
```

Edit the scripts in `src/content.py` (`cap` is what viewers read, `say` is how the voice pronounces it,
for example "Link" for Lynkk). Edit the visuals in `src/stage/stage.html`. Set `LYNKK_VOICE=hm_omega`
for an Indian English male voice.
