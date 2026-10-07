"""Mix voiceover + generated background music + UI sound effects into build/mix.wav.

The music and effects are synthesized here (no third-party audio), so the
soundtrack is free to publish. Run after build_audio.py and render.cjs
(render.cjs writes build/sfx.json).
"""
import json
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf

HERE = Path(__file__).resolve().parent
BUILD = HERE / "build"
SR = 48000
rng = np.random.default_rng(7)


def midi(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):  # fine for short effects
        acc = (1 - a) * x[i] + a * acc
        y[i] = acc
    return y


def lowpass_fast(x, cutoff, passes=2):
    # FFT brick-wall-ish low pass with a soft knee, for long signals
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / (1 + (f / cutoff) ** (2 * passes))
    return np.fft.irfft(X, len(x))


def music(duration):
    n = int(duration * SR)
    t = np.arange(n) / SR
    bpm = 96
    beat = 60 / bpm
    bar = beat * 4
    # Cmaj9 - Am9 - Fmaj9 - G6/9, voiced low and open
    chords = [[48, 55, 59, 62, 64], [45, 52, 55, 59, 62], [41, 48, 52, 55, 60], [43, 50, 54, 57, 62]]
    chords[3] = [43, 50, 55, 57, 62]
    pad = np.zeros(n)
    for ci in range(int(duration / bar) + 2):
        notes = chords[ci % 4]
        a, b = ci * bar, (ci + 1) * bar
        i0, i1 = int(max(0, a - .6) * SR), min(n, int((b + 1.2) * SR))
        if i0 >= n:
            break
        tt = t[i0:i1]
        env = np.clip((tt - (a - .6)) / 1.2, 0, 1) * np.clip(((b + 1.2) - tt) / 1.4, 0, 1)
        seg = np.zeros(len(tt))
        for k, m in enumerate(notes):
            f = midi(m)
            seg += np.sin(2 * np.pi * f * tt + k) * (1.0 if k else .8)
            seg += .35 * np.sin(2 * np.pi * f * 1.004 * tt + k * 2)
            seg += .12 * np.sin(2 * np.pi * f * 2 * tt)
        pad[i0:i1] += seg * env
    pad *= .05
    # gentle pluck arpeggio, eighth notes
    pl = np.zeros(n)
    step = beat / 2
    pattern = [0, 2, 4, 3, 1, 3, 4, 2]
    k = 0
    while k * step < duration:
        st = k * step
        ci = int(st / bar) % 4
        m = chords[ci][pattern[k % 8]] + 24
        i0 = int(st * SR)
        L = min(int(.9 * SR), n - i0)
        if L <= 0:
            break
        tt = np.arange(L) / SR
        f = midi(m)
        tone = np.sin(2 * np.pi * f * tt) + .3 * np.sin(4 * np.pi * f * tt) + .1 * np.sin(6 * np.pi * f * tt)
        acc = 1.0 if k % 2 == 0 else .7
        pl[i0:i0 + L] += tone * np.exp(-tt * 6) * np.clip(tt / .004, 0, 1) * acc
        k += 1
    pl = lowpass_fast(pl, 2600) * .028
    # soft sub pulse on beats 1 and 3
    sub = np.zeros(n)
    k = 0
    while k * beat * 2 < duration:
        i0 = int(k * beat * 2 * SR)
        L = min(int(.5 * SR), n - i0)
        tt = np.arange(L) / SR
        f = midi(chords[int(k * beat * 2 / bar) % 4][0] - 12)
        sub[i0:i0 + L] += np.sin(2 * np.pi * f * tt) * np.exp(-tt * 7) * np.clip(tt / .01, 0, 1)
        k += 1
    sub *= .06
    out = pad + pl + sub
    # simple stereo widening: delayed copy on the right
    d = int(.013 * SR)
    left = out
    right = np.concatenate([np.zeros(d), out[:-d]])
    # fade in/out
    fade = np.clip(t / 2.0, 0, 1) * np.clip((duration - t) / 3.0, 0, 1)
    return np.stack([left * fade, right * fade], axis=1)


def sfx(kind):
    if kind == "click":
        L = int(.05 * SR); tt = np.arange(L) / SR
        s = rng.standard_normal(L) * np.exp(-tt * 260) * .5 + np.sin(2 * np.pi * 2100 * tt) * np.exp(-tt * 180) * .5
        return lowpass(s, 6000) * .5
    if kind == "pop":
        L = int(.14 * SR); tt = np.arange(L) / SR
        f = 520 + 900 * tt / .14
        ph = 2 * np.pi * np.cumsum(f) / SR
        return np.sin(ph) * np.exp(-tt * 34) * np.clip(tt / .003, 0, 1) * .28
    if kind == "tick":
        L = int(.08 * SR); tt = np.arange(L) / SR
        return np.sin(2 * np.pi * 1800 * tt) * np.exp(-tt * 70) * .16
    if kind == "ding":
        L = int(1.0 * SR); tt = np.arange(L) / SR
        s = (np.sin(2 * np.pi * 1318.5 * tt) + .55 * np.sin(2 * np.pi * 1975.5 * tt) * np.exp(-tt * 3)
             + .25 * np.sin(2 * np.pi * 2637 * tt) * np.exp(-tt * 6))
        return s * np.exp(-tt * 4.2) * np.clip(tt / .002, 0, 1) * .16
    if kind == "whoosh":
        L = int(.7 * SR); tt = np.arange(L) / SR
        noise = rng.standard_normal(L)
        env = np.sin(np.pi * np.clip(tt / .7, 0, 1)) ** 2
        return lowpass(noise, 1400) * env * .22
    raise ValueError(kind)


def main():
    tl = json.loads((BUILD / "timeline.json").read_text())
    duration = tl["duration"]
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(BUILD / "voice.wav"), "-ar", str(SR), str(BUILD / "voice48.wav")], check=True)
    voice, _ = sf.read(BUILD / "voice48.wav")
    n = int(duration * SR)
    voice = np.pad(voice, (0, max(0, n - len(voice))))[:n]

    mus = music(duration)
    # duck the music under the voice
    hop = SR // 100
    frames = len(voice) // hop + 1
    act = np.array([np.max(np.abs(voice[i * hop:(i + 1) * hop])) if i * hop < len(voice) else 0 for i in range(frames)]) > .02
    env = np.zeros(frames)
    g = 0.0
    for i in range(frames):
        target = 1.0 if act[max(0, i - 25):i + 8].any() else 0.0  # hold ~250 ms
        g += (target - g) * (.25 if target > g else .03)
        env[i] = g
    duck = np.interp(np.arange(n), np.arange(frames) * hop, env)
    music_gain = 10 ** ((-7.0 * duck) / 20) * 0.25  # about -34 dB alone, -41 dB under the voice
    mus = mus[:n] * music_gain[:, None]

    fx = np.zeros(n)
    for e in json.loads((BUILD / "sfx.json").read_text()):
        s = sfx(e["type"])
        i0 = int(e["t"] * SR)
        if i0 < 0 or i0 >= n:
            continue
        L = min(len(s), n - i0)
        fx[i0:i0 + L] += s[:L]

    mix = mus + (voice * 1.0 + fx * .9)[:, None]
    peak = np.max(np.abs(mix))
    mix = mix / peak * .95 if peak > .95 else mix
    sf.write(BUILD / "mix.wav", mix.astype(np.float32), SR)
    print(f"mix.wav {duration:.1f}s peak {peak:.2f}")


if __name__ == "__main__":
    main()
