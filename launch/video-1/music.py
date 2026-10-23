"""Synthesize a 50s background track for Lynkk Video 1.
Act 1 (0-34s): tense A minor, ticking clock, pulsing bass, heartbeat kick, riser into the cut.
Act 2 (34-50s): bright C major groove (I-V-vi-IV), plucked arpeggio, soft four-on-the-floor.
"""
import sys, wave
import numpy as np

SR = 44100
DUR = 50.0
N = int(SR * DUR)
L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(7)
BEAT = 60 / 100  # 100 BPM

def hz(note):
    names = {'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
    n, o = note[:-1], int(note[-1])
    return 440.0 * 2 ** ((names[n] + 12 * (o + 1) - 69) / 12)

def add(sig, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR)
    if i >= N: return
    sig = sig[: N - i]
    l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
    L[i:i+len(sig)] += sig * gain * l * 1.414
    R[i:i+len(sig)] += sig * gain * r * 1.414

def tt(d): return np.arange(int(d * SR)) / SR

def band(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    X[(f < lo) | (f > hi)] = 0
    return np.fft.irfft(X, len(x))

def env_adsr(n, a, r):
    e = np.ones(n); na = int(a * SR); nr = int(r * SR)
    if na: e[:na] = np.linspace(0, 1, na)
    if nr: e[-nr:] *= np.linspace(1, 0, nr)
    return e

def pad(notes, t0, d, gain, bright=0.25, detune=0.004):
    t = tt(d); s = np.zeros(len(t))
    for n in notes:
        f = hz(n)
        for dt in (-detune, 0, detune):
            ff = f * (1 + dt)
            s += np.sin(2*np.pi*ff*t) + bright*np.sin(2*np.pi*2*ff*t)*0.5 + bright*0.3*np.sin(2*np.pi*3*ff*t)
    s /= len(notes) * 3
    s *= env_adsr(len(t), min(1.2, d/3), min(1.2, d/3))
    s *= 1 + 0.08*np.sin(2*np.pi*0.25*t)
    add(s, t0, gain, -0.25); add(s * 0.9, t0 + 0.012, gain, 0.25)

def bass(note, t0, d, gain):
    t = tt(d); f = hz(note)
    s = np.sin(2*np.pi*f*t) + 0.35*np.sin(2*np.pi*2*f*t) + 0.12*np.sin(2*np.pi*3*f*t)
    s *= np.exp(-t*5) * env_adsr(len(t), 0.004, 0.03)
    add(s, t0, gain)

def kick(t0, gain):
    t = tt(0.45)
    f = 45 + 85*np.exp(-t*28)
    ph = 2*np.pi*np.cumsum(f)/SR
    s = np.sin(ph) * np.exp(-t*7.5)
    s[:60] += rng.standard_normal(60)*0.15
    add(s, t0, gain)

def tick(t0, gain, pitch=2400, pan=0.3):
    t = tt(0.05)
    s = np.sin(2*np.pi*pitch*t)*np.exp(-t*140) + band(rng.standard_normal(len(t)), 3000, 9000)*np.exp(-t*200)*0.5
    add(s, t0, gain, pan)

def hat(t0, gain, pan=0.2, d=0.07):
    t = tt(d)
    s = band(rng.standard_normal(len(t)), 6000, 16000) * np.exp(-t*60)
    add(s, t0, gain, pan)

def clap(t0, gain):
    t = tt(0.22)
    n = band(rng.standard_normal(len(t)), 900, 5000)
    e = np.exp(-t*22)
    for k in (0.0, 0.011, 0.022):
        e += np.exp(-np.clip(t - k, 0, None)*120) * (t >= k) * 0.6
    add(n*e*0.6, t0, gain, -0.1)

def pluck(note, t0, gain, pan):
    t = tt(0.9); f = hz(note)
    s = (np.sin(2*np.pi*f*t) + 0.4*np.sin(2*np.pi*2*f*t)*np.exp(-t*6) + 0.15*np.sin(2*np.pi*3*f*t)*np.exp(-t*9))
    s *= np.exp(-t*4.2) * env_adsr(len(t), 0.003, 0.05)
    add(s, t0, gain, pan)

def impact(t0, gain):
    t = tt(2.2)
    f = 30 + 70*np.exp(-t*6)
    s = np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t*2.2)
    nz = band(rng.standard_normal(len(t)), 80, 3000) * np.exp(-t*9) * 0.6
    add(s + nz, t0, gain)

def riser(t0, d, gain):
    t = tt(d); x = t/d
    nz = rng.standard_normal(len(t))
    lo = band(nz, 200, 1500); hi = band(nz, 1500, 9000)
    s = (lo*(1-x) + hi*x) * x**2.2
    tone = np.sin(2*np.pi*np.cumsum(180 + 700*x**2)/SR) * x**2 * 0.35
    add(s + tone, t0, gain)

# ---------------- ACT 1: the problem (0 - 34s) ----------------
CUT = 34.0
# drone under everything
pad(['A2', 'E3', 'A3'], 0.0, 16.4, 0.20, bright=0.15)
impact(0.35, 0.95)                         # WAIT! slam
# clock ticks on every beat, tick-tock
b = 0; t = 0.9
while t < 26.0:
    tick(t, 0.20 if b % 2 == 0 else 0.13, 2400 if b % 2 == 0 else 1800, 0.35 if b % 2 == 0 else -0.35)
    t += BEAT; b += 1
# pulsing bass from 3s
prog1 = [('A1', ['A2','C3','E3']), ('F1', ['F2','A2','C3']), ('D2', ['D3','F3','A3']), ('E1', ['E2','G#2','B2'])]
t = 3.0; i = 0
while t < 26.0:
    root, chord = prog1[(i // 8) % 4]
    g = 0.33 if t < 16 else 0.42
    bass(root, t, BEAT/2*0.95, g * (1.0 if i % 2 == 0 else 0.7))
    if i % 8 == 0 and t >= 16.0:
        pad(chord, t, BEAT*4.1, 0.16, bright=0.3)
    t += BEAT/2; i += 1
# heartbeat kick from the promise onward
t = 16.0
while t < 26.0:
    kick(t, 0.55); kick(t + 0.18, 0.32)
    t += BEAT*2
# night (26-30): sparse, low, slow ticks
pad(['A2', 'C3', 'E3'], 26.0, 4.6, 0.22, bright=0.1)
for k in range(4):
    tick(26.3 + k*1.2, 0.10, 1600, 0.0)
bass('A1', 26.0, 1.4, 0.35)
# three days later (30-34): accelerating ticks + riser
t = 30.0; gap = 0.5
while t < CUT - 0.1:
    tick(t, 0.16, 2400, 0.3); t += gap; gap = max(0.09, gap*0.86)
pad(['E2', 'B2', 'E3', 'G#3'], 30.0, 4.0, 0.18, bright=0.4)
riser(30.4, CUT - 30.4 - 0.08, 0.32)
impact(32.0, 0.45)                         # "The deal didn't go cold"

# hard silence right before the cut
gap_i, cut_i = int((CUT - 0.08)*SR), int(CUT*SR)
L[gap_i:cut_i] *= np.linspace(1, 0, cut_i - gap_i)[::-1] * 0 ; R[gap_i:cut_i] *= 0
L[cut_i:] = 0; R[cut_i:] = 0   # act 1 tails never bleed into act 2

# ---------------- ACT 2: the fix (34 - 50s) ----------------
impact(CUT, 0.55)
prog2 = [('C2', ['C3','E3','G3','C4']), ('G1', ['G2','B2','D3','G3']), ('A1', ['A2','C3','E3','A3']), ('F1', ['F2','A2','C3','F3'])]
arps = {'C2':['C4','E4','G4','C5'], 'G1':['B3','D4','G4','B4'], 'A1':['C4','E4','A4','C5'], 'F1':['C4','F4','A4','C5']}
bar = BEAT*4
for k in range(7):
    t0 = CUT + k*bar
    if t0 >= DUR: break
    root, chord = prog2[k % 4]
    pad(chord, t0, bar*1.05 if k < 6 else DUR - t0, 0.17, bright=0.35)
    for s in range(8):
        tb = t0 + s*BEAT/2
        if tb >= DUR - 0.3: break
        bass(root if s % 4 != 3 else root, tb, BEAT/2*0.9, 0.30 if s % 2 == 0 else 0.2)
        notes = arps[root]
        if k >= 0:
            pluck(notes[[0,1,2,3,2,1,2,3][s]], tb, 0.20, (-0.4 if s % 2 else 0.4))
    if k >= 1:
        for q in range(4):
            tb = t0 + q*BEAT
            if tb < DUR - 0.5:
                kick(tb, 0.42)
                hat(tb + BEAT/2, 0.10)
                if q in (1, 3): clap(tb, 0.22)
# end card sparkle
for j, n in enumerate(['C5', 'E5', 'G5', 'C6']):
    pluck(n, 45.0 + j*0.12, 0.14, -0.3 + j*0.2)

# ---------------- master ----------------
mix = np.stack([L, R], 1)
# gentle fade in / out
fi = int(0.02*SR); mix[:fi] *= np.linspace(0, 1, fi)[:, None]
fo0 = int(47.4*SR); mix[fo0:] *= np.linspace(1, 0, N - fo0)[:, None] ** 1.5
mix = np.tanh(mix * 1.3) / np.tanh(1.3)
mix /= np.max(np.abs(mix)) / 0.89          # peak about -1 dBFS
out = (mix * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(out.tobytes())
print('wrote', sys.argv[1])
