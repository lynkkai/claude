"""Voiceover with Kokoro TTS: each line placed at its scene time, sped up only if it would overrun.

Usage: python voiceover.py <lines.json> <kokoro-v1.0.onnx> <voices-v1.0.bin> <out.wav> [voice=af_heart] [seconds=50]
lines.json: [[start_s, latest_end_s, "spoken text"], ...]
Write "Link" for "Lynkk" in the spoken text so it is pronounced right.
Setup: pip install kokoro-onnx soundfile; model files from
https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0
Voices that work well: af_heart (female, default), am_fenrir (male).
"""
import json
import sys

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

lines_path, model, voices, out = sys.argv[1:5]
voice = sys.argv[5] if len(sys.argv) > 5 else "af_heart"
seconds = float(sys.argv[6]) if len(sys.argv) > 6 else 50.0
LINES = json.load(open(lines_path))
tts = Kokoro(model, voices)
SR = 24000
track = np.zeros(int(SR * seconds), dtype=np.float32)


def trim(x, thresh=0.01):
    idx = np.where(np.abs(x) > thresh)[0]
    return x[max(0, idx[0] - 200): idx[-1] + 1200] if len(idx) else x


for start, end, text in LINES:
    window = end - start
    speed = 1.0
    while True:
        audio, sr = tts.create(text, voice=voice, speed=speed, lang="en-us")
        assert sr == SR
        audio = trim(audio)
        if len(audio) / SR <= window or speed >= 1.4:
            break
        speed = round(speed + 0.05, 2)
    i = int(start * SR)
    audio = audio[: len(track) - i]
    track[i:i + len(audio)] += audio
    flag = "  <- sped up, consider shortening" if speed > 1.15 else ""
    print(f"{start:5.2f}s  {len(audio)/SR:4.2f}s of {window:4.2f}s  speed {speed}  {text}{flag}")

track /= max(1e-9, np.abs(track).max()) / 0.9
sf.write(out, track, SR)
print("wrote", out)
