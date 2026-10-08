"""Generate the female voiceover with Kokoro TTS, plus the timeline, lip-sync
envelope and YouTube captions used by the renderer.

Usage: python3 tts.py <kokoro-v1.0.onnx> <voices-v1.0.bin>
"""
import json
import sys

import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro

FPS = 30
HERE = __file__.rsplit("/", 1)[0] or "."

cfg = json.load(open(f"{HERE}/segments.json"))
kokoro = Kokoro(sys.argv[1], sys.argv[2])

sr = None
pieces = []
timeline = []
cursor = cfg["lead_in"]
prev_scene = None

for seg in cfg["segments"]:
    if prev_scene is not None:
        cursor += cfg["gap_in_scene"] if seg["scene"] == prev_scene else cfg["gap_between_scenes"]
    audio, sr = kokoro.create(seg.get("tts", seg["text"]), voice=cfg["voice"], speed=cfg["speed"], lang="en-us")
    # Trim leading/trailing near-silence so gaps are controlled by the config.
    idx = np.where(np.abs(audio) > 0.01)[0]
    audio = audio[max(idx[0] - int(0.03 * sr), 0): idx[-1] + int(0.08 * sr)]
    pieces.append((cursor, audio))
    timeline.append({"id": seg["id"], "scene": seg["scene"], "text": seg["text"],
                     "start": round(cursor, 3), "end": round(cursor + len(audio) / sr, 3)})
    cursor += len(audio) / sr + seg.get("pause_after", 0)
    prev_scene = seg["scene"]

total = cursor + cfg["tail"]
voice = np.zeros(int(total * sr), dtype=np.float32)
for start, audio in pieces:
    i = int(start * sr)
    voice[i:i + len(audio)] += audio
voice = voice / max(np.abs(voice).max(), 1e-6) * 0.89
sf.write(f"{HERE}/build/voice.wav", voice, sr)

# Per-frame mouth openness (0..1) from RMS, smoothed, for the avatar lip sync.
hop = sr // FPS
n = int(np.ceil(len(voice) / hop))
rms = np.array([np.sqrt(np.mean(voice[i * hop:(i + 1) * hop] ** 2) + 1e-12) for i in range(n)])
env = np.clip((rms - 0.012) / 0.11, 0, 1) ** 0.7
env = np.convolve(env, [0.25, 0.5, 0.25], mode="same")

json.dump({"fps": FPS, "duration": round(total, 3), "segments": timeline,
           "mouth": [round(float(v), 3) for v in env]},
          open(f"{HERE}/build/timeline.json", "w"))


def ts(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)):03d}"


with open(f"{HERE}/captions.srt", "w") as f:
    for i, seg in enumerate(timeline, 1):
        f.write(f"{i}\n{ts(seg['start'])} --> {ts(seg['end'] + 0.15)}\n{seg['text']}\n\n")

print(f"duration {total:.1f}s, {len(timeline)} segments")
for seg in timeline:
    print(f"{seg['start']:7.2f} {seg['end']:7.2f} {seg['id']}")
