# Lynkk avatar video (10s)

`lynkk-avatar-10s.mp4`: 1080x1080, 30fps, 10.0s, H.264 + AAC. Square format for LinkedIn, X, Instagram and Product Hunt galleries.

An animated Lynkk avatar sits in a meeting tile and speaks. Its mouth follows the voiceover, and captions highlight each word as it is spoken. Feature chips (past context, notes, tasks, CRM) appear on cue, and the video ends on a "Try it free at lynkk.ai" button.

## Script
> Hi, I'm Lynkk, your AI meeting teammate. I join your calls and speak when you need me. I turn every conversation into notes, tasks, and CRM updates. Try it free.

## Rebuild
The voice is Kokoro TTS (`af_heart` voice), run locally with the `kokoro-onnx` package. The visuals are drawn with Pillow and encoded with ffmpeg.

```bash
pip install kokoro-onnx soundfile pillow numpy
# model files: kokoro-v1.0.int8.onnx + voices-v1.0.bin from
# https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0 into ./kokoro/
python3 tts_chunks.py    # writes voice.wav + timing.json
python3 render.py        # writes lynkk-avatar-10s.mp4
python3 render.py stills 2.0 7.9   # optional: preview frames as PNG
```

Edit the `chunks` list in `tts_chunks.py` to change the script. The TTS reads the spoken text ("Link", so it is pronounced right), and the captions show the second string ("Lynkk").
