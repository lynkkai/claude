"""Generate the Video 2 voiceover with Kokoro TTS and place each line at its scene time.

Usage: python voiceover.py <kokoro-v1.0.onnx> <voices-v1.0.bin> <out.wav> [voice]
"Lynkk" is spelled "Link" in the spoken text so the voice says it right.
"""
import sys
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

# (start second, latest end second, spoken text)
LINES = [
    (0.30, 0.95, "Wrong."),
    (1.05, 3.45, "Your records say yes. Your customer said no."),
    (3.65, 7.85, "On a busy day, your customer says: our budget is on hold."),
    (8.25, 11.85, "Later, all you remember is: it went well."),
    (12.25, 16.85, "In the team meeting, you say: pretty sure this one will close."),
    (17.25, 20.85, "Your boss counts on it. So does everyone else."),
    (21.30, 25.85, "Then the month ends. And the deal doesn't close."),
    (26.40, 29.85, "Now everyone is asking what went wrong."),
    (30.30, 33.85, "The truth was on the call. It just never reached your records."),
    (34.35, 35.85, "Here's the fix."),
    (36.30, 40.85, "Link fills in your sales records with what the customer really said."),
    (41.30, 44.85, "And during calls, a helper only you can see keeps you on track."),
    (45.30, 49.60, "Link. No more surprises. Book a demo, or start free today."),
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
