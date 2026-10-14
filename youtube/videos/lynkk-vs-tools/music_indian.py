"""Original Indian-style background music, synthesized from scratch (no samples, no licensing).

Styles:
  sitar   upbeat: sitar hook, tabla (keherwa), tanpura drone, soft keys and bass
  bansuri calm: bansuri flute over tanpura, light tabla
  lofi    modern: Rhodes chords, tabla groove, sitar answers
Usage: python3 music_indian.py <style> <seconds> <out.wav> [seed]
"""
import sys
import numpy as np
import soundfile as sf

SR = 44100
TONIC = 146.83  # D3 is Sa


def hz_deg(deg, octave=0):
    """Scale degree in Bilawal (major) from Sa=D, any integer degree."""
    steps = [0, 2, 4, 5, 7, 9, 11]
    o, d = divmod(deg, 7)
    return TONIC * 2 ** ((steps[d] + 12 * (o + octave)) / 12)


def phase(freq):
    return 2 * np.pi * np.cumsum(freq) / SR


def place(buf, sig, t, gain=1.0):
    i = int(t * SR)
    if i >= len(buf) or i < 0:
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain


def fade_tail(x, sec=0.05):
    n = min(len(x), int(sec * SR))
    x[-n:] *= np.linspace(1, 0, n)
    return x


# ---------------- instruments ----------------

def sitar(f0, dur, rng, glide_from=None):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = np.full(n, f0)
    if glide_from:  # meend: slide up into the note
        g = min(n, int(0.12 * SR))
        f[:g] = glide_from * (f0 / glide_from) ** np.linspace(0, 1, g)
    ph = phase(f)
    out = np.zeros(n)
    for k in range(1, 18):
        # jawari "bloom": upper harmonics swell a moment after the pluck, then decay
        bloom = 1 - np.exp(-t * (40 / k))
        amp = (1 / k ** 0.9) * np.exp(-t * (1.6 + 0.55 * k)) * (0.35 + 0.65 * bloom)
        out += np.sin(k * ph + rng.uniform(0, 6.28)) * amp
    out *= 1 - np.exp(-t * 900)
    return fade_tail(out * 0.22)


def tanpura_note(f0, dur, rng):
    n = int(dur * SR)
    t = np.arange(n) / SR
    out = np.zeros(n)
    for k in range(1, 22):
        # each harmonic breathes slowly, the shimmer of the jawari
        lfo = 0.55 + 0.45 * np.sin(2 * np.pi * (0.25 + 0.07 * k) * t + rng.uniform(0, 6.28))
        out += np.sin(2 * np.pi * f0 * k * t + rng.uniform(0, 6.28)) * (1 / k ** 1.1) * lfo
    env = (1 - np.exp(-t * 30)) * np.exp(-t * 0.5)
    return fade_tail(out * env * 0.05, 0.3)


def tabla(stroke, rng):
    """Dayan (treble) and bayan (bass) strokes."""
    def dayan(f0, decay, dur=0.6, bright=1.0):
        n = int(dur * SR); t = np.arange(n) / SR
        s = sum(np.sin(2 * np.pi * f0 * k * t) * (bright ** (k - 1)) / k * np.exp(-t * decay * (1 + 0.4 * k))
                for k in range(1, 6))
        click = rng.standard_normal(n) * np.exp(-t * 400) * 0.25
        return (s + click) * 0.5

    def bayan(dur=0.8, rise=1.25):
        n = int(dur * SR); t = np.arange(n) / SR
        f = 78 * (1 + (rise - 1) * (1 - np.exp(-t * 6)))  # palm pressure bends the pitch up
        return np.sin(phase(f)) * np.exp(-t * 5.0) * 0.9

    d = TONIC * 2  # dayan tuned to Sa
    if stroke == "na":
        return dayan(d, 9, bright=0.7)
    if stroke == "tin":
        return dayan(d, 5, bright=0.45) * 0.8
    if stroke == "ti":
        n = int(0.12 * SR); t = np.arange(n) / SR
        return (rng.standard_normal(n) * np.exp(-t * 60) * 0.2 + np.sin(2 * np.pi * d * 3 * t) * np.exp(-t * 50) * 0.2)
    if stroke == "ge":
        return bayan()
    if stroke == "ka":
        n = int(0.1 * SR); t = np.arange(n) / SR
        return np.sin(2 * np.pi * 120 * t) * np.exp(-t * 45) * 0.5
    if stroke == "dha":
        a, b = dayan(d, 8, bright=0.65), bayan()
        m = max(len(a), len(b)); out = np.zeros(m); out[:len(a)] += a; out[:len(b)] += b
        return out
    if stroke == "dhin":
        a, b = dayan(d, 5, bright=0.5), bayan(rise=1.15)
        m = max(len(a), len(b)); out = np.zeros(m); out[:len(a)] += a * 0.8; out[:len(b)] += b
        return out
    return np.zeros(1)


def bansuri(f0, dur, rng, prev=None):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = np.full(n, f0)
    if prev:
        g = min(n, int(0.09 * SR))
        f[:g] = prev * (f0 / prev) ** np.linspace(0, 1, g)
    vib = 1 + 0.006 * np.sin(2 * np.pi * 5.2 * t) * np.clip((t - 0.25) / 0.3, 0, 1)
    ph = phase(f * vib)
    tone = np.sin(ph) + 0.18 * np.sin(2 * ph) + 0.06 * np.sin(3 * ph)
    # soft breath: low-passed noise that follows the tone, well under it
    breath = np.convolve(rng.standard_normal(n), np.ones(48) / 48, mode="same")
    breath = np.convolve(breath, np.ones(48) / 48, mode="same") * 0.35 * (0.5 + 0.5 * np.abs(np.sin(ph)))
    env = np.clip(t / 0.08, 0, 1) * np.clip((dur - t) / 0.12, 0, 1)
    return (tone + breath) * env * 0.28


def rhodes(f, dur, vel=0.4):
    n = int(dur * SR); t = np.arange(n) / SR
    mod = np.sin(2 * np.pi * f * t) * (1.4 * np.exp(-t * 7) + 0.2)
    s = np.sin(2 * np.pi * f * t + mod) * np.exp(-t * 1.4) * (1 - np.exp(-t * 400))
    return fade_tail(s * vel, 0.08)


def bass(f, dur):
    n = int(dur * SR); t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) + 0.15 * np.sin(4 * np.pi * f * t)
    return fade_tail(s * np.clip(t / 0.01, 0, 1) * np.exp(-t * 1.5), 0.1)


# ---------------- arrangement ----------------

KEHERWA = ["dha", "ge", "na", "ti", "na", "ka", "dhin", "na"]          # 8 strokes per cycle
DADRA = ["dha", "dhin", "na", "dha", "tin", "na"]                     # 6 strokes per cycle
# I, vi, IV, V as scale-degree triads (Sa = 0)
CHORDS = [[0, 2, 4], [5, 7, 9], [3, 5, 7], [4, 6, 8]]
HOOK = [(4, 1), (5, .5), (4, .5), (2, 1), (1, .5), (2, .5), (0, 2),            # degree, beats
        (2, 1), (4, .5), (5, .5), (7, 1), (5, .5), (4, .5), (4, 2)]
FLUTE = [(4, 2), (5, 1), (4, 1), (2, 3), (1, 1), (0, 4),
         (2, 2), (4, 1), (5, 1), (7, 3), (5, 1), (4, 4)]


def build(style, seconds, seed=5):
    rng = np.random.default_rng(seed)
    bpm = {"sitar": 104, "bansuri": 76, "lofi": 88}[style]
    beat = 60 / bpm
    total = int((seconds + 3) * SR)
    L = {k: np.zeros(total) for k in ("drone", "tabla", "lead", "keys", "bass")}

    # tanpura: Pa, Sa', Sa', Sa (low), over and over
    cyc = 2.6 if style != "bansuri" else 3.2
    t = 0.0
    while t < seconds + 2:
        for i, f in enumerate((hz_deg(4, -1), hz_deg(0), hz_deg(0), hz_deg(0, -1))):
            place(L["drone"], tanpura_note(f, cyc * 1.6, rng), t + i * cyc / 4)
        t += cyc

    # tabla
    if style == "bansuri":
        theka, step, start = DADRA, beat / 2, beat * 8
    else:
        theka, step, start = KEHERWA, beat / 2, beat * 4
    t, i = start, 0
    while t < seconds - 1.5:
        s = theka[i % len(theka)]
        place(L["tabla"], fade_tail(tabla(s, rng), 0.03), t + rng.uniform(-0.004, 0.006), rng.uniform(0.8, 1.0))
        if style == "sitar" and i % 16 in (11, 15):  # little fills
            place(L["tabla"], tabla("ti", rng), t + step / 2, 0.7)
        t += step
        i += 1

    # lead melody
    phrase = FLUTE if style == "bansuri" else HOOK
    lead_start = beat * (4 if style == "bansuri" else 8)
    t, prev = lead_start, None
    while t < seconds - 3:
        for deg, b in phrase:
            d = b * beat
            if style == "bansuri":
                place(L["lead"], bansuri(hz_deg(deg, 1), d * 1.02, rng, prev), t)
                prev = hz_deg(deg, 1)
            else:
                glide = hz_deg(deg - 1, 1) if rng.random() < 0.25 else None
                place(L["lead"], sitar(hz_deg(deg, 1), max(d, 0.6) + 0.5, rng, glide), t)
            t += d
            if t > seconds - 3:
                break
        t += beat * (2 if style == "lofi" else 0)   # lo-fi leaves space between answers

    # chords and bass (not in the calm style)
    if style != "bansuri":
        bar = beat * 4
        t, b = 0.0, 0
        while t < seconds:
            ch = CHORDS[b % 4]
            hits = [(0, .45), (1.5, .3), (2.5, .28)] if style == "sitar" else [(0, .5), (2, .35)]
            for off, vel in hits:
                for deg in ch:
                    place(L["keys"], rhodes(hz_deg(deg, 1), beat * 1.6, vel * 0.5), t + off * beat + rng.uniform(0, .01))
            if b >= 1:
                root = hz_deg(ch[0], -1)
                for off in (0, 2.5) if style == "sitar" else (0, 2):
                    place(L["bass"], bass(root, beat * 1.8), t + off * beat, 0.5)
            t += bar
            b += 1

    gains = {"sitar": dict(drone=.8, tabla=.9, lead=.75, keys=.45, bass=.7),
             "bansuri": dict(drone=1.1, tabla=.55, lead=.8, keys=0, bass=0),
             "lofi": dict(drone=.6, tabla=.85, lead=.55, keys=.7, bass=.75)}[style]
    mono = sum(L[k] * g for k, g in gains.items())
    # light stereo: lead and tabla slightly apart, a short slap echo on the lead
    d = int(0.19 * SR)
    echo = np.concatenate([np.zeros(d), L["lead"][:-d]]) * 0.22 * gains["lead"]
    left = mono + echo * 0.4 + L["tabla"] * 0.08
    right = mono + echo - L["tabla"] * 0.08
    st = np.stack([left, right], axis=1)
    st = np.tanh(st * 1.2) / 1.2
    st = st[: int(seconds * SR)]
    fi, fo = int(0.3 * SR), int(2.5 * SR)
    st[:fi] *= np.linspace(0, 1, fi)[:, None]
    st[-fo:] *= np.linspace(1, 0, fo)[:, None]
    return st / (np.max(np.abs(st)) + 1e-9) * 0.85


if __name__ == "__main__":
    style, secs, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    sf.write(out, build(style, secs, seed), SR)
    print(out)
