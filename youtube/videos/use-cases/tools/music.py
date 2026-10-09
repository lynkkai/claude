"""Original background music for a use-case video, synthesized so it is royalty free and
safe from Content ID claims. Run from a video folder after tts.py:
  python3 ../tools/music.py            -> out/music.wav (48 kHz stereo, same length as the narration)

The arrangement follows out/timing.json: a sparse, pensive keys and pad intro under the problem
scenes (s1, s2), the groove (bass, soft drums, comping keys) from the first solution scene (s3),
a lift into the CTA (s7) and a resolving chord at the end. The bar grid is aligned so a bar
starts exactly when s3 starts. Deterministic: same input, same file."""
import json
import wave

import numpy as np

SR = 48000
BPM = 96
BEAT = 60 / BPM
BAR = 4 * BEAT
rng = np.random.default_rng(7)


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def tt(dur):
    return np.arange(int(dur * SR)) / SR


def adsr(n, a=0.005, r=0.08):
    e = np.ones(n)
    na, nr = min(n, int(a * SR)), min(n, int(r * SR))
    if na:
        e[:na] = np.linspace(0, 1, na)
    if nr:
        e[n - nr:] *= np.linspace(1, 0, nr)
    return e


class Bus:
    def __init__(self, dur):
        self.n = int(dur * SR)
        self.x = np.zeros((self.n, 2))

    def add(self, sig, t, g=1.0, pan=0.0):
        i = int(round(t * SR))
        if i >= self.n:
            return
        if i < 0:
            sig, i = sig[-i:], 0
        sig = sig[: self.n - i]
        th = (pan + 1) * np.pi / 4
        self.x[i:i + len(sig), 0] += sig * g * np.cos(th) * 1.414
        self.x[i:i + len(sig), 1] += sig * g * np.sin(th) * 1.414


def spectral(x, fn):
    """Filter a mono or stereo signal with a frequency response fn(freqs) via FFT."""
    n = len(x)
    size = 1 << int(np.ceil(np.log2(n + 1)))
    f = np.fft.rfftfreq(size, 1 / SR)
    h = fn(f)
    if x.ndim == 1:
        return np.fft.irfft(np.fft.rfft(x, size) * h, size)[:n]
    return np.stack([np.fft.irfft(np.fft.rfft(x[:, c], size) * h, size)[:n] for c in range(x.shape[1])], 1)


def lowpass(fc, order=2):
    return lambda f: 1 / np.sqrt(1 + (f / fc) ** (2 * order))


def highpass(fc, order=2):
    return lambda f: 1 / np.sqrt(1 + (fc / np.maximum(f, 1e-3)) ** (2 * order))


# ---------- instruments ----------

def epiano(m, dur, vel=1.0):
    """Soft electric piano (two-operator FM), mellow attack, long decay, light tremolo."""
    t = tt(dur + 1.2)
    f = hz(m) * (1 + rng.uniform(-0.0015, 0.0015))
    idx = (1.1 + 0.6 * vel) * np.exp(-t / 0.35)
    tine = 0.06 * vel * np.sin(2 * np.pi * f * 14 * t) * np.exp(-t / 0.05)
    s = np.sin(2 * np.pi * f * t + idx * np.sin(2 * np.pi * f * t)) + tine
    env = np.exp(-t / (1.8 if m < 60 else 1.2)) * adsr(len(t), 0.004, 0.25)
    rel = np.ones(len(t))
    k = int(dur * SR)
    rel[k:] = np.exp(-np.arange(len(t) - k) / SR / 0.25)
    return s * env * rel * (1 + 0.08 * np.sin(2 * np.pi * 4.6 * t)) * vel


def pad(notes, dur):
    """Warm pad: detuned band-limited saws, slow swell, low-passed later on the bus."""
    t = tt(dur + 1.5)
    out = np.zeros(len(t))
    for m in notes:
        for d in (-0.006, 0.0, 0.0055):
            f = hz(m) * (1 + d)
            ph = rng.uniform(0, 2 * np.pi)
            for k in range(1, 9):
                if f * k > 9000:
                    break
                out += np.sin(2 * np.pi * f * k * t + ph * k) / k
    out /= 3 * len(notes)
    e = np.minimum(1, t / 1.2)
    k = int(dur * SR)
    e[k:] *= np.exp(-np.arange(len(t) - k) / SR / 0.6)
    return out * e


def bass(m, dur):
    t = tt(dur + 0.15)
    f = hz(m)
    s = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(4 * np.pi * f * t) + 0.08 * np.sin(6 * np.pi * f * t)
    return np.tanh(1.3 * s) * adsr(len(t), 0.01, 0.15) * np.exp(-t / 1.4)


def kick():
    t = tt(0.4)
    f = 46 + 70 * np.exp(-t / 0.04)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.16) * adsr(len(t), 0.002, 0.05)


def noise(dur):
    return rng.standard_normal(int(dur * SR))


def shaker():
    n = spectral(noise(0.09), lambda f: highpass(5000, 2)(f) * lowpass(11000, 2)(f))
    t = tt(0.09)
    return n * np.exp(-t / 0.018) * np.minimum(1, t / 0.006)


def rim():
    t = tt(0.16)
    n = spectral(noise(0.16), lambda f: highpass(900, 2)(f) * lowpass(3200, 2)(f))
    return (n * 0.9 + 0.4 * np.sin(2 * np.pi * 1800 * t)) * np.exp(-t / 0.035)


def bell(m, dur=2.0):
    t = tt(dur)
    f = hz(m)
    s = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t / 0.4) + 0.12 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t / 0.15)
    return s * np.exp(-t / 0.9) * adsr(len(t), 0.002, 0.3)


def swell(dur):
    """Soft filtered-noise rise into the groove."""
    t = tt(dur)
    p = t / dur
    n = spectral(noise(dur), lowpass(2500, 1))
    return n * p ** 3


def reverb(x, secs=2.6, wet=0.28):
    n = int(secs * SR)
    t = np.arange(n) / SR
    size = 1 << int(np.ceil(np.log2(len(x) + n)))
    out = np.zeros_like(x)
    for c in range(2):
        ir = rng.standard_normal(n) * np.exp(-t / (secs / 6.5))
        ir = spectral(ir, lowpass(6000, 1))
        ir /= np.sqrt(np.sum(ir ** 2))
        out[:, c] = np.fft.irfft(np.fft.rfft(x[:, c], size) * np.fft.rfft(ir, size), size)[: len(x)]
    return x * (1 - wet) + out * wet


# ---------- arrangement ----------

# Chords as (bass note, voicing). Key of C major / A minor.
INTRO = [(45, [57, 60, 64, 67, 71]),   # Am9
         (41, [57, 60, 64, 65, 69]),   # Fmaj7 add9 colour
         (45, [57, 60, 64, 67, 71]),
         (40, [56, 59, 62, 64, 67])]   # E7sus feel, leans into the turn
GROOVE = [(41, [57, 60, 64, 65]),      # Fmaj7
          (43, [55, 59, 62, 67]),      # G6 shape
          (40, [55, 59, 62, 64]),      # Em7
          (45, [55, 60, 64, 69])]      # Am7
OUTRO = [(41, [57, 60, 64, 65]), (43, [55, 59, 62, 67]), (36, [55, 60, 64, 67, 71, 74])]  # F, G, Cmaj9

MOTIF = [(0, 76), (1.5, 74), (2.0, 72), (3.0, 71)]  # bell figure, beats within a bar


def compose(timing):
    dur = sum(v["duration"] for v in timing.values())
    solve = timing["s3"]["offset"]
    cta = timing["s7"]["offset"]
    keys, pads, low, drums, fx = (Bus(dur) for _ in range(5))

    # Intro: from time 0, chords every 2 bars counted back from s3 so the turn lands on the grid.
    n_intro = int(np.ceil(solve / (2 * BAR)))
    for i in range(n_intro):
        t0 = solve - (n_intro - i) * 2 * BAR
        root, notes = INTRO[(i - n_intro) % 4]
        L = 2 * BAR
        if t0 + L <= 0:
            continue
        pads.add(pad(notes[:4], L), t0, 0.5)
        for j, m in enumerate(notes):
            keys.add(epiano(m, BAR * 1.6, 0.55), t0 + j * 0.11, 0.17, pan=-0.3 + 0.15 * j)
        keys.add(epiano(notes[2] + 12, BAR * 0.8, 0.45), t0 + BAR + 0.5 * BEAT, 0.12, pan=0.3)
        low.add(bass(root - 12, 2 * BAR - 0.1), t0, 0.14)
    fx.add(swell(BAR), solve - BAR, 0.05)

    # Groove: s3 to the CTA.
    bar_i = 0
    t = solve
    while t < cta - 0.01:
        root, notes = GROOVE[bar_i % 4]
        pads.add(pad(notes, BAR), t, 0.38)
        # Comping: chord on 1, a lighter stab on the "and" of 2, a push on 4.
        for off, v in ((0, 0.7), (1.5 * BEAT, 0.45), (3.5 * BEAT, 0.4)):
            for j, m in enumerate(notes):
                keys.add(epiano(m, BEAT * (1.4 if off == 0 else 0.7), v), t + off + j * 0.012, 0.16, pan=-0.25 + 0.17 * j)
        low.add(bass(root - 12, 1.5 * BEAT), t, 0.24)
        low.add(bass(root - 12, 0.9 * BEAT), t + 2.5 * BEAT, 0.17)
        low.add(bass(root - 5 if root < 43 else root - 17, 0.8 * BEAT), t + 3.5 * BEAT, 0.13)
        for b in range(4):
            if b in (0, 2):
                drums.add(kick(), t + b * BEAT, 0.34)
            if b in (1, 3):
                drums.add(rim(), t + b * BEAT, 0.22, pan=0.12)
            for s in range(4):
                acc = 1.0 if s == 2 else 0.55
                drums.add(shaker(), t + (b + s / 4) * BEAT + rng.uniform(-0.004, 0.004), 0.18 * acc, pan=0.35)
        if bar_i % 4 == 3:
            for off, m in MOTIF:
                fx.add(bell(m), t + off * BEAT, 0.07, pan=0.2)
        bar_i += 1
        t += BAR

    # CTA: lift and resolve, drums thin out, last chord rings out.
    for i, (root, notes) in enumerate(OUTRO):
        t0 = cta + i * BAR
        if t0 >= dur:
            break
        last = i == len(OUTRO) - 1
        L = max(dur - t0, BAR) if last else BAR
        pads.add(pad(notes, L), t0, 0.4)
        for j, m in enumerate(notes):
            keys.add(epiano(m, min(L, 3 * BAR), 0.6), t0 + j * (0.06 if last else 0.012), 0.16, pan=-0.3 + 0.12 * j)
        low.add(bass(root - 12 if root > 40 else root, min(L, 2 * BAR) - 0.1), t0, 0.24)
        if not last:
            for b in range(4):
                if b in (0, 2):
                    drums.add(kick(), t0 + b * BEAT, 0.28)
                for s in (0, 2):
                    drums.add(shaker(), t0 + (b + s / 4) * BEAT, 0.08, pan=0.35)
        else:
            for off, m in MOTIF:
                fx.add(bell(m + 12 if m < 74 else m), t0 + 0.5 + off * BEAT, 0.06, pan=0.2)

    pads.x = spectral(pads.x, lowpass(1800, 2))
    keys.x = spectral(keys.x, lowpass(7500, 1)) * 1.35
    low.x = spectral(low.x, lowpass(260, 2))
    mix = pads.x + keys.x + fx.x
    mix = reverb(mix, wet=0.3) + low.x + reverb(drums.x, secs=1.2, wet=0.12)
    # Leave room for the voice: a gentle dip around 1 to 4 kHz.
    mix = spectral(mix, lambda f: 1 - 0.25 * np.exp(-((np.log2(np.maximum(f, 1) / 2200)) ** 2) / 0.8))
    mix = spectral(mix, highpass(38, 2))
    n = len(mix)
    fade = np.ones(n)
    fade[: int(0.8 * SR)] = np.linspace(0, 1, int(0.8 * SR))
    fo = int(2.8 * SR)
    fade[n - fo:] *= np.linspace(1, 0, fo) ** 2
    mix *= fade[:, None]
    mix = np.tanh(mix / np.max(np.abs(mix)) * 1.2) / np.tanh(1.2) * 0.89
    return mix


def main():
    timing = json.load(open("out/timing.json"))
    mix = compose(timing)
    pcm = (mix * 32767).astype(np.int16)
    with wave.open("out/music.wav", "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print(f"out/music.wav {len(mix) / SR:.1f}s")


if __name__ == "__main__":
    main()
