# Short #2: Stop Typing During Discovery Calls

Vertical short (1080x1920, 30fps, 38.8s) built from row 2 of `lynkk-shorts-content.csv`.

- `brag.mp4`: current cut with a **scratch TTS voice-over** (Kokoro `am_fenrir` at 1.1x, the voice of the earlier "Your records say yes" Lynkk short), music, SFX, burned-in captions
- `brag.jpg`: poster / thumbnail (also baked in as frame 0)
- `share-copy.txt`: post caption plus the required music credit
- `brag-plan.md`: angle, brand tokens, storyboard, timing

## Rebuild

```sh
python3 src/timeline.py   # timing: scene cuts, VO lines, keystrokes
node src/render.js        # frames -> work/video.mp4 (needs Playwright + Chromium)
python3 src/mix.py        # music + SFX (+ src/assets/vo.wav if present) -> work/brag-noposter.mp4
ffmpeg -y -ss 1.5 -i work/video.mp4 -frames:v 1 -q:v 2 brag.jpg
ffmpeg -y -i work/brag-noposter.mp4 -i brag.jpg -filter_complex "[0:v][1:v]overlay=enable='eq(n\,0)'[v]" \
  -map "[v]" -map 0:a -c:v libx264 -crf 16 -pix_fmt yuv420p -c:a copy -movflags +faststart brag.mp4
```

Review stills: `node src/render.js --stills 1.5,12.8,21`.

## Voice-over

The current VO is a scratch read from Kokoro TTS, voice `am_fenrir` at speed 1.1. That is the voice of the
earlier Lynkk short (`brag-male.mp4`): Kokoro output for that video's first line matches its audio sample for sample.
It's for timing; swap in a real read if you want one before publishing.

**Regenerate the scratch VO** (after editing `LINES` in `src/timeline.py`):

```sh
python3 -m venv /tmp/tts && /tmp/tts/bin/pip install kokoro-onnx
curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
curl -LO https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
KOKORO_MODEL=kokoro-v1.0.onnx KOKORO_VOICES=voices-v1.0.bin /tmp/tts/bin/python src/vo_scratch.py
```

`KOKORO_VOICE` and `KOKORO_SPEED` override the voice and speed. Setting `PIPER_MODEL` instead of the Kokoro
variables uses Piper (the first scratch read was Piper `en_US-lessac-high`).

This writes `src/assets/vo.wav` and `src/vo_timing.json` (measured line timing). `timeline.py` uses `vo_timing.json` over its own estimates, so captions and word-keyed animation
follow the read. Word timing is weighted by phoneme count. "Lynkk" is spoken as "Link" and lynkk.ai as "link dot A I".

**Swapping in the real VO:** save it as `src/assets/vo.wav` (starting at 0:00, each line at its `LINES` start),
delete `src/vo_timing.json`, set the `LINES` start/end times to the real read, and re-run the build.
`mix.py` ducks the music under the voice and sets the voice about 11 dB over the bed automatically.

## Credits

Music: "Happy Beats / Business Moves Vol. 10" by Sascha Ende, ende.app (CC BY 4.0).
SFX: Kenney.nl (CC0). Scratch VO: Kokoro TTS (Apache 2.0), am_fenrir voice. Built with the /brag skill (github.com/latent-spaces/brag).
Product UI, names and quotes are lynkk.ai's own illustrative data.
