"""Original music bed for the Lynkk reel. Made from code, so there is nothing to license.

120 BPM in A minor (Am F C G, one chord per bar), 20 seconds, matched to the cuts in
post.html: a build under the hook, the drop on the Lynkk mark at 2.0 s, a lift at 10 s
for the feature cuts, a hit on every scene change and a short swish on every website
scroll stop, then a final chord at 19 s.

    python3 music.py            -> out/music.wav (stereo, 44.1 kHz, loudness-normalised)

Needs numpy and ffmpeg.
"""
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

SR = 44100
DUR = 20.0
BEAT = 0.5          # 120 BPM
BAR = 4 * BEAT
N = int(DUR * SR)
rng = np.random.default_rng(7)

L = np.zeros(N)
R = np.zeros(N)
send_l = np.zeros(N)  # reverb send
send_r = np.zeros(N)


def tt(dur):
    return np.arange(int(dur * SR)) / SR


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def smooth(x, n):
    if n <= 1:
        return x
    k = np.ones(n) / n
    return np.convolve(x, k, mode="same")


def place(clip, at, gain=1.0, pan=0.0, rev=0.0):
    i = int(at * SR)
    if i >= N:
        return
    clip = clip[: N - i] * gain
    gl, gr = np.sqrt(0.5 * (1 - pan)), np.sqrt(0.5 * (1 + pan))
    L[i : i + len(clip)] += clip * gl
    R[i : i + len(clip)] += clip * gr
    if rev:
        send_l[i : i + len(clip)] += clip * gl * rev
        send_r[i : i + len(clip)] += clip * gr * rev


# ------------------------------------------------------------------ voices
def kick():
    t = tt(0.45)
    f = 50 + 110 * np.exp(-t * 32)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7.5)
    click = rng.standard_normal(len(t)) * np.exp(-t * 400) * 0.25
    return np.tanh(1.6 * (body + click))


def hp_noise(n, k=6):
    x = smooth(rng.standard_normal(n), 2)  # take the hiss off the top
    return x - smooth(x, k)


def clap():
    t = tt(0.3)
    x = hp_noise(len(t), 10)
    env = np.zeros(len(t))
    for d in (0.0, 0.011, 0.023):
        m = t >= d
        env[m] = np.maximum(env[m], np.exp(-(t[m] - d) * 90))
    env += 0.5 * np.exp(-t * 16) * (t > 0.023)
    return x * env * 0.6


def hat(open_=False):
    t = tt(0.28 if open_ else 0.07)
    return hp_noise(len(t), 5) * np.exp(-t * (11 if open_ else 70)) * 0.3


def snare():
    t = tt(0.25)
    tone = np.sin(2 * np.pi * 190 * t) * np.exp(-t * 22)
    return 0.5 * tone + 0.6 * hp_noise(len(t), 5) * np.exp(-t * 17)


def bass(midi, dur=0.22):
    t = tt(dur)
    f = hz(midi)
    x = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)
    env = np.minimum(1, t / 0.004) * np.exp(-t * 6)
    env *= np.clip((dur - t) / 0.02, 0, 1)
    return np.tanh(1.4 * x * env) * 0.8


def pluck(midi, dur=0.3):
    t = tt(dur)
    f = hz(midi)
    x = sum(np.sin(2 * np.pi * f * k * t) / k * np.exp(-t * (10 + 6 * k)) for k in range(1, 8))
    return x * np.minimum(1, t / 0.002) * 0.45


def pad(midis, dur, bright):
    t = tt(dur)
    x = np.zeros(len(t))
    for m in midis:
        for cents in (-8, 0, 8):
            f = hz(m) * 2 ** (cents / 1200)
            ph = rng.uniform(0, 2 * np.pi)
            for k in range(1, 9):
                x += np.sin(2 * np.pi * f * k * t + ph * k) * (bright ** (k - 1)) / k
    env = np.minimum(1, t / 0.12) * np.clip((dur - t) / 0.25, 0, 1)
    return x * env / (len(midis) * 6)


def riser(dur):
    t = tt(dur)
    p = t / dur
    f = 180 * (12 ** p)
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.25
    noise = hp_noise(len(t), 8) * 0.3
    return (tone + noise) * p ** 2.2


def impact():
    t = tt(1.6)
    f = 45 + 40 * np.exp(-t * 9)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.4)
    burst = smooth(rng.standard_normal(len(t)), 12) * np.exp(-t * 7) * 1.8
    return np.tanh(1.3 * (boom + burst)) * 0.9


def swish(dur=0.22):
    t = tt(dur)
    x = rng.standard_normal(len(t))
    band = smooth(x, 4) - smooth(x, 30)
    return band * np.sin(np.pi * t / dur) ** 2 * 0.9


# ------------------------------------------------------------------ the song
CHORDS = [  # (bass root, pad notes, arp notes) per bar: Am F C G
    (45, [57, 60, 64], [69, 72, 76, 81]),
    (41, [57, 60, 65], [65, 69, 72, 77]),
    (48, [55, 60, 64], [67, 72, 76, 79]),
    (43, [55, 59, 62], [67, 71, 74, 79]),
]
ARP = [0, 1, 2, 1, 3, 2, 1, 2, 0, 2, 1, 3, 2, 1, 2, 3]
FINAL = 19.0
kicks = []

for bar in range(int(DUR / BAR)):
    b0 = bar * BAR
    root, padn, arpn = CHORDS[bar % 4]
    intro = bar == 0
    # pad: dark and rising under the hook, then open
    if b0 < FINAL:
        place(pad(padn, BAR + 0.3, 0.3 if intro else 0.5), b0, 1.3 if intro else 0.9, rev=0.5)
    for s in range(16):
        at = b0 + s * BEAT / 4
        if at >= FINAL:
            break
        beat_i, sub = divmod(s, 4)
        if intro:
            place(hat(), at, 0.15 + 0.35 * s / 16, pan=0.25)
            if s >= 8:  # snare roll into the drop
                place(snare(), at, 0.15 + 0.5 * (s - 8) / 8, rev=0.2)
                place(snare(), at + BEAT / 8, 0.1 + 0.4 * (s - 8) / 8, rev=0.2)
            continue
        if sub == 0:
            place(kick(), at, 0.95)
            kicks.append(at)
        if sub == 0 and beat_i in (1, 3):
            place(clap(), at, 0.55, rev=0.35)
        if sub == 2:
            place(hat(True), at, 0.25, pan=-0.2)
            place(bass(root, 0.2), at, 0.55)
            place(bass(root + 12 if s in (6, 14) else root, 0.1), at + BEAT / 4, 0.4)
        place(hat(), at, 0.22 if sub % 2 else 0.12, pan=0.3)
        lift = 12 if 10 <= at < 14 else 0
        place(pluck(arpn[ARP[s]] + lift), at, 0.6, pan=(-0.35 if s % 2 else 0.35), rev=0.45)

# fills and hits on the scene changes
place(riser(1.9), 0.1, 0.55, rev=0.3)
for at in (9.5, 13.5, 15.5):
    for k in range(4):
        place(snare(), at + k * BEAT / 4, 0.25 + 0.12 * k, rev=0.2)
for at in (0.0, 2.0, 10.0, 14.0, 16.0):
    place(impact(), at, 0.6 if at else 0.4, rev=0.5)
for at in (3.0, 11.0, 12.0, 13.0):
    place(swish(0.25), at - 0.2, 0.35, pan=0.0)
for k, at in enumerate((3.8, 4.8, 5.8, 6.8, 7.8)):  # website scroll snaps
    place(swish(0.2), at, 0.3, pan=(-0.5 if k % 2 else 0.5))
# the end: one chord, let it ring
root, padn, arpn = CHORDS[1]
place(impact(), FINAL, 0.5, rev=0.6)
place(kick(), FINAL, 0.9)
place(pad([57, 60, 64, 69], 1.0, 0.5), FINAL, 1.0, rev=0.8)
place(bass(45, 0.9), FINAL, 0.6)

# ------------------------------------------------------------------ mix
# sidechain: pad, plucks and bass duck under each kick (applied to the whole bus is
# close enough here, the kick itself sits on top of the release)
duck = np.ones(N)
for k in kicks:
    i = int(k * SR)
    t = tt(0.3)
    seg = 1 - 0.45 * np.exp(-t / 0.08)
    duck[i : i + len(seg)] = np.minimum(duck[i : i + len(seg)], seg[: N - i])


def reverb(x, seed):
    g = np.random.default_rng(seed)
    t = tt(1.8)
    ir = g.standard_normal(len(t)) * np.exp(-t * 3.2)
    ir = smooth(ir, 3)
    ir /= np.sqrt(np.sum(ir ** 2))
    n = len(x) + len(ir)
    y = np.fft.irfft(np.fft.rfft(x, n) * np.fft.rfft(ir, n), n)[: len(x)]
    return y * 0.35


L = L * duck + reverb(send_l, 1)
R = R * duck + reverb(send_r, 2)
# gentle top cut on the master
L, R = 0.5 * L + 0.5 * smooth(L, 3), 0.5 * R + 0.5 * smooth(R, 3)
fade = np.clip((DUR - np.arange(N) / SR) / 0.6, 0, 1)
L, R = np.tanh(L) * fade, np.tanh(R) * fade
peak = max(np.abs(L).max(), np.abs(R).max())
L, R = L / peak * 0.9, R / peak * 0.9

here = Path(__file__).parent
out = here / "out"
out.mkdir(exist_ok=True)
raw = out / "music-raw.wav"
with wave.open(str(raw), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((np.stack([L, R], 1) * 32767).astype("<i2").tobytes())

# loudness for social video: -14 LUFS integrated, -1.5 dB true peak
final = out / "music.wav"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw),
                "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", str(SR), str(final)], check=True)
raw.unlink()
print("wrote", final, file=sys.stderr)
