"""Generate a calm, warm music bed on a fixed beat grid (no samples, pure synthesis).

Soft kick, sub bass, detuned pad and light shaker, all in A minor at one tempo, so
scene cuts (snapped to the same grid in timeline.py) land on the beat.

usage: python3 music.py <duration_seconds> <out.wav> [--bpm 96]
"""
import sys, wave
import numpy as np

SR = 48000


def lowpass(x, cutoff):
    # one-pole low-pass, applied twice for a gentler slope
    a = np.exp(-2 * np.pi * cutoff / SR)
    for _ in range(2):
        y = np.empty_like(x); acc = 0.0
        b = 1 - a
        for i in range(len(x)):
            acc = b * x[i] + a * acc; y[i] = acc
        x = y
    return x


def note(f, dur, kind='pad'):
    t = np.arange(int(dur * SR)) / SR
    if kind == 'pad':
        w = sum(np.sin(2 * np.pi * f * d * t + d) for d in (0.996, 1.0, 1.004)) / 3
        w += 0.35 * np.sin(2 * np.pi * 2 * f * t)
        env = np.minimum(1, t / 0.9) * np.minimum(1, (dur - t) / 0.9)
    else:  # bass
        w = np.sin(2 * np.pi * f * t) + 0.2 * np.sin(2 * np.pi * 2 * f * t)
        env = np.minimum(1, t / 0.02) * np.exp(-t * 1.2)
    return w * env


def main():
    dur = float(sys.argv[1]); out = sys.argv[2]
    bpm = float(sys.argv[sys.argv.index('--bpm') + 1]) if '--bpm' in sys.argv else 96.0
    beat = 60 / bpm; bar = 4 * beat
    n = int((dur + 1) * SR)
    mix = np.zeros((n, 2))
    # A minor: Am - F - C - G, two bars each
    chords = [(220.0, 261.63, 329.63), (174.61, 220.0, 261.63), (196.0, 261.63, 329.63), (196.0, 246.94, 293.66)]
    roots = [55.0, 43.65, 65.41, 49.0]
    t0 = 0.0; k = 0
    while t0 < dur:
        c = chords[k % 4]; r = roots[k % 4]
        seg = sum(note(f, 2 * bar, 'pad') for f in c) / 3
        i = int(t0 * SR); j = min(n, i + len(seg)); seg = seg[: j - i]
        mix[i:j, 0] += 0.16 * seg; mix[i:j, 1] += 0.16 * np.roll(seg, 240)
        for b in range(8):  # bass on beats 1 and 3
            if b % 2 == 0:
                bs = note(r, beat * 1.8, 'bass'); bi = int((t0 + b * beat) * SR); bj = min(n, bi + len(bs))
                if bi >= n: continue
                mix[bi:bj] += 0.22 * bs[: bj - bi, None]
        t0 += 2 * bar; k += 1
    # soft kick every beat, shaker on off-beats (starts after 2 bars)
    kt = np.arange(int(0.35 * SR)) / SR
    kick = np.sin(2 * np.pi * (48 + 70 * np.exp(-kt * 30)) * kt) * np.exp(-kt * 9)
    rng = np.random.default_rng(7)
    shk = rng.standard_normal(int(0.08 * SR)) * np.exp(-np.arange(int(0.08 * SR)) / SR * 60)
    shk = shk - lowpass(shk.copy(), 4000)
    bt = 2 * bar
    while bt < dur - bar:
        i = int(bt * SR); j = min(n, i + len(kick)); mix[i:j] += 0.30 * kick[: j - i, None]
        i = int((bt + beat / 2) * SR); j = min(n, i + len(shk)); mix[i:j, 0] += 0.035 * shk[: j - i]; mix[i:j, 1] += 0.03 * shk[: j - i]
        bt += beat
    mix = mix[: int(dur * SR)]
    fade_in = np.minimum(1, np.arange(len(mix)) / (1.5 * SR))
    fade_out = np.minimum(1, (len(mix) - np.arange(len(mix))) / (4 * SR))
    mix *= (fade_in * fade_out)[:, None]
    mix = mix / (np.abs(mix).max() + 1e-9) * 0.5
    with wave.open(out, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((mix * 32767).astype(np.int16).tobytes())
    print(f'music: {dur:.1f}s at {bpm:.0f} bpm -> {out}')


if __name__ == '__main__':
    main()
