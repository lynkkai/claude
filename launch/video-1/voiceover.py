"""Generate the Video 1 voiceover with Kokoro TTS and place each line at its scene time.

Usage: python voiceover.py <kokoro-v1.0.onnx> <voices-v1.0.bin> <out.wav> [voice]
"Lynkk" is spelled "Link" in the spoken text so the voice says it right.
"""
import sys
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

# (start second, latest end second, spoken text)
LINES = [
    (0.30, 0.95, "Wait!"),
    (1.05, 2.90, "What did we promise them?"),
    (3.30, 7.80, "Five tabs. Three old notes. And you still can't find it."),
    (8.25, 11.85, "You ask your team. Nobody remembers either."),
    (12.25, 15.85, "So you guess. And the customer notices."),
    (16.35, 20.85, "Then you promise: I'll send it today."),
    (21.35, 25.85, "But the next meeting starts. Then another. And another."),
    (26.45, 29.85, "By evening, you've forgotten all about it."),
    (31.45, 33.85, "The deal didn't go cold. You just forgot."),
    (34.35, 35.85, "Here's the fix."),
    (36.30, 39.85, "Link listens to your calls, and remembers every promise."),
    (40.30, 44.85, "It even writes your follow-up email. You check it, and hit send."),
    (45.30, 49.60, "Link. Never forget a customer call. Start free."),
]

model, voices, out = sys.argv[1:4]
voice = sys.argv[4] if len(sys.argv) > 4 else "af_heart"
tts = Kokoro(model, voices)
SR = 24000
track = np.zeros(int(SR * 50.0), dtype=np.float32)

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
    print(f"{start:5.2f}s  {len(audio)/SR:4.2f}s of {window:4.2f}s  speed {speed}  {text}")

track /= max(1e-9, np.abs(track).max()) / 0.9
sf.write(out, track, SR)
print("wrote", out)
