"""Synthesize a soft ambient bed (no samples, no licensing) and mix it under the voice.

Usage: python3 music.py   (reads build/voice.wav, writes build/mix.wav)
"""
import numpy as np
import soundfile as sf

HERE = __file__.rsplit("/", 1)[0] or "."
voice, sr = sf.read(f"{HERE}/build/voice.wav", dtype="float32")
n = len(voice)
t = np.arange(n) / sr


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


# Fmaj9 - Am7 - Dm9 - Bbmaj7, gentle voicings, ~6.4 s per chord at 75 bpm (2 bars).
chords = [[53, 60, 64, 67, 69], [57, 60, 64, 67, 72], [50, 57, 60, 64, 65], [46, 57, 62, 65, 69]]
bar = 6.4
pad = np.zeros(n, dtype=np.float64)
rng = np.random.default_rng(7)
for k in range(int(np.ceil(n / sr / bar)) + 1):
    start = k * bar - 0.8
    notes = chords[k % len(chords)]
    i0 = max(int(start * sr), 0)
    i1 = min(int((start + bar + 1.6) * sr), n)
    if i1 <= i0:
        continue
    lt = t[i0:i1] - start
    dur = bar + 1.6
    env = np.clip(lt / 1.6, 0, 1) * np.clip((dur - lt) / 1.6, 0, 1)
    env = np.sin(env * np.pi / 2) ** 2
    for j, m in enumerate(notes):
        f = hz(m)
        ph = rng.uniform(0, 2 * np.pi)
        tone = np.sin(2 * np.pi * f * lt + ph) + 0.5 * np.sin(2 * np.pi * f * 1.003 * lt) + 0.18 * np.sin(4 * np.pi * f * lt)
        pad[i0:i1] += tone * env * (0.6 if j == 0 else 0.35)

# Soft high "glass" arpeggio every half bar for a bit of motion.
arp = np.zeros(n)
step = bar / 8
for k in range(int(n / sr / step)):
    s = k * step
    notes = chords[int(s // bar) % len(chords)]
    m = notes[1:][k % 4] + 12
    i0 = int(s * sr)
    i1 = min(i0 + int(1.8 * sr), n)
    lt = t[i0:i1] - s
    arp[i0:i1] += np.sin(2 * np.pi * hz(m) * lt) * np.exp(-lt * 2.6) * (1 - np.exp(-lt * 80))

music = pad / np.abs(pad).max() * 0.8 + arp / max(np.abs(arp).max(), 1e-9) * 0.22
# Simple one-pole low-pass to keep it warm.
a = np.exp(-2 * np.pi * 2400 / sr)
out = np.empty_like(music)
acc = 0.0
for i in range(0, n, 4096):
    blk = music[i:i + 4096]
    y = np.empty_like(blk)
    for j, x in enumerate(blk):
        acc = (1 - a) * x + a * acc
        y[j] = acc
    out[i:i + 4096] = y
music = out / np.abs(out).max()

# Duck under speech, fade in and out.
win = int(0.05 * sr)
venv = np.convolve(np.abs(voice), np.ones(win) / win, mode="same")
duck = 1 - 0.45 * np.clip(venv / 0.05, 0, 1)
duck = np.convolve(duck, np.ones(int(0.3 * sr)) / int(0.3 * sr), mode="same")
fade = np.clip(t / 2.0, 0, 1) * np.clip((t[-1] - t) / 3.0, 0, 1)
music = music * duck * fade * 0.13

mix = voice + music.astype(np.float32)
mix = mix / max(np.abs(mix).max(), 1e-6) * 0.93
sf.write(f"{HERE}/build/mix.wav", np.stack([mix, mix], axis=1), sr)
print("mix written", n / sr, "s")
