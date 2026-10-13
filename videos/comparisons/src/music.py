"""Original background music, synthesized from scratch (no samples, no licensing).

Warm, light, upbeat bed: Rhodes-like keys, soft pad, sub bass, gentle drums.
Usage: python3 music.py <seconds> <out.wav> [seed]
"""
import sys
import numpy as np
import soundfile as sf

SR = 44100
BPM = 98
BEAT = 60.0 / BPM

# I - vi - IV - V in D, voiced warm (MIDI notes)
PROG = [
    [50, 57, 61, 64, 66],   # Dmaj7 (D A C# E F#)
    [47, 54, 57, 62, 66],   # Bm9  (B F# A D F#)
    [43, 55, 59, 62, 66],   # Gmaj7(G G B D F#)
    [45, 57, 61, 64, 66],   # A6/9 (A A C# E F#)
]


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12.0)


def env_adsr(n, a, d, s, r):
    a, d, r = int(a * SR), int(d * SR), int(r * SR)
    e = np.ones(n) * s
    a = min(a, n)
    e[:a] = np.linspace(0, 1, a, endpoint=False)
    dd = min(d, n - a)
    e[a:a + dd] = np.linspace(1, s, dd, endpoint=False)
    if r > 0 and n > r:
        e[-r:] *= np.linspace(1, 0, r)
    return e


def keys_note(f, dur, vel=0.5):
    """Rhodes-ish FM electric piano tone."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    mod_env = np.exp(-t * 7.0)
    mod = np.sin(2 * np.pi * f * 1.0 * t) * (1.6 * mod_env + 0.25)
    car = np.sin(2 * np.pi * f * t + mod)
    tine = np.sin(2 * np.pi * f * 4.0 * t) * np.exp(-t * 18) * 0.25
    amp = np.exp(-t * 1.6) * (1 - np.exp(-t * 400))
    tail = np.ones(n)
    rel = min(int(0.08 * SR), n)
    tail[-rel:] = np.linspace(1, 0, rel)
    return (car + tine) * amp * tail * vel


def pad_chord(notes, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    out = np.zeros(n)
    for m in notes[1:]:
        f = hz(m + 12)
        for det in (-0.07, 0.0, 0.07):
            ff = f * 2 ** (det / 12)
            ph = np.random.rand() * 2 * np.pi
            # soft "saw" from few harmonics
            w = sum(np.sin(2 * np.pi * ff * k * t + ph * k) / k * (0.6 ** (k - 1)) for k in range(1, 6))
            out += w
    out *= env_adsr(n, 0.9, 0.5, 0.8, 0.9)
    return out / (len(notes) * 3)


def sub_bass(f, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    w = np.sin(2 * np.pi * f * t) + 0.18 * np.sin(2 * np.pi * 2 * f * t)
    return w * env_adsr(n, 0.01, 0.15, 0.7, 0.12)


def kick(dur=0.45):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = 46 + 110 * np.exp(-t * 32)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t * 8.5) * 0.95


def hat(dur=0.08, rng=None):
    n = int(dur * SR)
    t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    hp = np.diff(np.concatenate([[0], noise]))  # crude highpass
    hp = np.diff(np.concatenate([[0], hp]))
    return hp * np.exp(-t * 60) * 0.06


def snap(dur=0.25, rng=None):
    n = int(dur * SR)
    t = np.arange(n) / SR
    noise = rng.standard_normal(n)
    hp = np.diff(np.concatenate([[0], noise]))
    body = np.sin(2 * np.pi * 190 * t) * np.exp(-t * 30) * 0.3
    return (hp * np.exp(-t * 22) * 0.12 + body) * 0.55


def place(buf, sig, start, gain=1.0):
    i = int(start * SR)
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain


def build(seconds, seed=7):
    rng = np.random.default_rng(seed)
    np.random.seed(seed)
    total = int((seconds + 2) * SR)
    L = {k: np.zeros(total) for k in ("keys", "pad", "bass", "drums", "arp")}
    bar = BEAT * 4
    nbars = int(np.ceil((seconds + 2) / bar))
    arp_pat = [0, 2, 3, 4, 3, 2, 4, 3]
    for b in range(nbars):
        chord = PROG[b % 4]
        t0 = b * bar
        intro = b < 2
        outro = t0 > seconds - bar * 1.5
        # pad
        place(L["pad"], pad_chord(chord, bar + 0.6), t0, 1.0)
        # keys: stabs on 1 and the "and" of 2, lightly humanised
        for off, vel in ((0.0, 0.5), (1.5, 0.32), (2.5, 0.28)):
            for m in chord[1:]:
                st = t0 + off * BEAT + rng.uniform(0, 0.012)
                place(L["keys"], keys_note(hz(m), BEAT * 1.4, vel * rng.uniform(0.85, 1.0)), st)
        # arp in the upper octave (eighths)
        if not intro:
            for i, idx in enumerate(arp_pat):
                m = chord[idx] + 12
                st = t0 + i * BEAT / 2 + rng.uniform(0, 0.008)
                place(L["arp"], keys_note(hz(m), BEAT * 0.6, 0.16 * rng.uniform(0.8, 1.0)), st)
        # bass
        root = chord[0] - 12
        if not intro:
            for off, d in ((0, 1.4), (1.5, 0.45), (2, 1.4), (3.5, 0.45)):
                place(L["bass"], sub_bass(hz(root), BEAT * d), t0 + off * BEAT, 0.55)
        # drums
        if not intro and not outro:
            for q in range(4):
                if q in (0, 2):
                    place(L["drums"], kick(), t0 + q * BEAT, 0.8)
                if q in (1, 3):
                    place(L["drums"], snap(rng=rng), t0 + q * BEAT, 0.6)
                place(L["drums"], hat(rng=rng), t0 + q * BEAT + BEAT / 2, 1.0)
                place(L["drums"], hat(rng=rng), t0 + q * BEAT, 0.45)
    # sidechain pump from kick grid
    t = np.arange(total) / SR
    beat_phase = (t % BEAT) / BEAT
    pump = 1 - 0.35 * np.exp(-beat_phase * 6)
    started = t > 2 * bar
    pump = np.where(started, pump, 1.0)
    mix_l = (L["pad"] * 0.55 * pump + L["keys"] * 0.5 + L["arp"] * 0.65 + L["bass"] * pump + L["drums"] * 0.75)
    # stereo: delay the arp to the right, pad slightly wide
    d = int(BEAT * 0.75 * SR)
    arp_delay = np.concatenate([np.zeros(d), L["arp"][:-d]]) * 0.35
    left = mix_l + arp_delay * 0.2
    right = (L["pad"] * 0.55 * pump * 0.96 + L["keys"] * 0.48 + L["arp"] * 0.5 + L["bass"] * pump
             + L["drums"] * 0.75 + arp_delay)
    st = np.stack([left, right], axis=1)
    # warm it: gentle soft clip
    st = np.tanh(st * 1.1) / 1.1
    st = st[: int(seconds * SR)]
    # fades
    fi = int(0.4 * SR)
    fo = int(2.5 * SR)
    st[:fi] *= np.linspace(0, 1, fi)[:, None]
    st[-fo:] *= np.linspace(1, 0, fo)[:, None]
    st /= np.max(np.abs(st)) + 1e-9
    return st * 0.85


if __name__ == "__main__":
    secs = float(sys.argv[1])
    out = sys.argv[2]
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 7
    sf.write(out, build(secs, seed), SR)
    print(out, secs)
