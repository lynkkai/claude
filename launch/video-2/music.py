"""Music and sound effects for Lynkk Video 2 (brag edition), written as one piece.
120 BPM, beat 0.5s, bar 2s, counted from frame 0, so every whole-second scene cut is on a beat.
Act 1 (0-34s): D minor, half-time pulse, clock ticks, heartbeat kick, a hit on the lost deal, riser, 1/16 silence.
Act 2 (34-50s): F major I-V-vi-IV, plucks on 8ths, four-on-the-floor.
SFX are in key (D minor pentatonic in act 1, F major in act 2), on the 1/16 grid, sitting under the music
with a shared short room so they blend in.
"""
import sys, wave
import numpy as np

SR = 44100
DUR = 50.0
N = int(SR * DUR)
L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(7)
BEAT = 60 / 120  # 120 BPM

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

def ping(t0, gain, f1=1174.66, f2=1760.0, pan=0.0):   # D6 + A6, in key
    t = tt(0.6)
    s = (np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)*np.exp(-t*3)) * np.exp(-t*7)
    s[:40] *= np.linspace(0, 1, 40)
    sfx(s, t0, gain, pan)

# ---- SFX bus: everything here gets the same short room so it blends with the music ----
SL = np.zeros(N); SR_ = np.zeros(N)
def sfx(sig, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR)
    if i >= N: return
    sig = sig[: N - i]
    l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
    SL[i:i+len(sig)] += sig * gain * l * 1.414
    SR_[i:i+len(sig)] += sig * gain * r * 1.414

def whoosh(t_cut, gain=0.10, d=0.375):        # swells into the cut, ends exactly on it
    t = tt(d); x = t / d
    s = band(rng.standard_normal(len(t)), 300, 5000) * (x ** 2.5) * (1 - np.clip((x - 0.96) / 0.04, 0, 1))
    sfx(s, t_cut - d, gain)

def pop(note, t0, gain=0.12, pan=0.0):        # soft pitched UI pop, in key
    t = tt(0.35); f = hz(note)
    s = (np.sin(2*np.pi*f*t) + 0.25*np.sin(2*np.pi*2*f*t)) * np.exp(-t*14)
    s[:30] *= np.linspace(0, 1, 30)
    sfx(s, t0, gain, pan)

def clicks(t0, t1, gain=0.035):              # quiet typing on the 1/16 grid
    step = BEAT / 4; t = t0; k = 0
    while t < t1:
        c = tt(0.02); s = band(rng.standard_normal(len(c)), 2000, 8000) * np.exp(-c*300)
        sfx(s, t, gain * (1.0 if k % 2 == 0 else 0.7), 0.15 if k % 2 else -0.15)
        t += step; k += 1

# ---------------- ACT 1: the problem (0 - 34s) ----------------
CUT = 34.0
pad(['D2', 'A2', 'D3'], 0.0, 21.2, 0.18, bright=0.15)
impact(0.25, 0.95)                          # Wrong.
b = 0; t = 1.0
while t < 21.0:                             # clock on quarter notes
    tick(t, 0.13 if b % 2 == 0 else 0.09, 2349 if b % 2 == 0 else 1760, 0.35 if b % 2 == 0 else -0.35)
    t += BEAT; b += 1
prog1 = [('D2', ['D3','F3','A3']), ('A#1', ['A#2','D3','F3']), ('G1', ['G2','A#2','D3']), ('A1', ['A2','C#3','E3'])]
t = 3.0; i = 0                              # bass on 8ths from the first cut
while t < 21.0:
    root, chord = prog1[(i // 8) % 4]
    g = 0.30 if t < 12 else 0.40
    bass(root, t, BEAT/2*0.95, g * (1.0 if i % 2 == 0 else 0.65))
    if i % 8 == 0 and t >= 12.0:
        pad(chord, t, BEAT*8.2, 0.15, bright=0.3)
    t += BEAT/2; i += 1
t = 12.0
while t < 21.0:                             # heartbeat on beat 1 of each bar
    kick(t, 0.55); kick(t + BEAT/4, 0.30)
    t += BEAT*4
impact(21.0, 0.75)                          # the month ends
impact(22.5, 0.30)                          # "Lost" pill
pad(['D2', 'F2', 'A2'], 21.0, 9.2, 0.22, bright=0.1)
for k in range(5):
    bass('D2', 21.0 + k*BEAT*4, 1.2, 0.30)
t = 26.0
while t < 30.0:
    tick(t, 0.08, 1760, 0.0); t += BEAT
t = 30.0; gap = 0.5                         # the gap: ticks speed up on the 1/16 grid
while t < CUT - 0.13:
    tick(t, 0.14, 2349, 0.3); t += gap; gap = max(0.125, gap - 0.0625)
pad(['A1', 'E2', 'A2', 'C#3'], 30.0, 4.0, 0.18, bright=0.4)
riser(30.5, CUT - 30.5 - 0.125, 0.30)
impact(30.25, 0.35)                         # "The truth was on the call"

# act 1 SFX
for c in (3, 8, 12, 17, 21, 26, 30):
    whoosh(c)
pop('A5', 4.5, 0.10, 0.3)                   # meeting alert drops
clicks(8.5, 9.25); clicks(9.5, 11.0)        # typing "Looking good", notes
pop('D5', 11.25, 0.14); pop('A5', 11.375, 0.10)   # Save, Saved
pop('F5', 17.5, 0.09, -0.2); pop('A5', 18.0, 0.11, 0.2); pop('D6', 18.75, 0.10)
for k, tp in enumerate((26.25, 27.0, 27.75, 28.5)):
    ping(tp, 0.12, pan=-0.2 + 0.13*k)
pop('D5', 30.5, 0.09)                       # the gap line

gap_i = int((CUT - BEAT/4)*SR)              # 1/16 of silence before the cut
L[gap_i:] = 0; R[gap_i:] = 0; SL[gap_i:] = 0; SR_[gap_i:] = 0

# ---------------- ACT 2: the fix (34 - 50s) ----------------
impact(CUT, 0.55)
prog2 = [('F1', ['F2','A2','C3','F3']), ('C2', ['C3','E3','G3','C4']), ('D2', ['D3','F3','A3','D4']), ('A#1', ['A#2','D3','F3','A#3'])]
arps = {'F1':['C4','F4','A4','C5'], 'C2':['C4','E4','G4','C5'], 'D2':['D4','F4','A4','D5'], 'A#1':['D4','F4','A#4','D5']}
bar = BEAT*4
for k in range(8):
    t0 = CUT + k*bar
    if t0 >= DUR: break
    root, chord = prog2[k % 4]
    pad(chord, t0, min(bar*1.05, DUR - t0), 0.16, bright=0.35)
    for s in range(8):
        tb = t0 + s*BEAT/2
        if tb >= DUR - 0.3: break
        bass(root, tb, BEAT/2*0.9, 0.28 if s % 2 == 0 else 0.18)
        pluck(arps[root][[0,1,2,3,2,1,2,3][s]], tb, 0.17, (-0.4 if s % 2 else 0.4))
    if t0 >= 36.0:
        for q in range(4):
            tb = t0 + q*BEAT
            if tb < DUR - 0.5:
                kick(tb, 0.40)
                hat(tb + BEAT/2, 0.09)
                if q in (1, 3): clap(tb, 0.20)
for j, n in enumerate(['F5', 'A5', 'C6', 'F6']):
    pluck(n, 45.0 + j*0.125, 0.13, -0.3 + j*0.2)

# act 2 SFX
for c in (36, 41, 45):
    whoosh(c, 0.08)
for k, n in enumerate(['F5', 'A5', 'C6', 'F6']):    # note rows reveal
    pop(n, 36.5 + k*0.5, 0.09, -0.3 + 0.2*k)
pop('C6', 38.5, 0.13); pop('A5', 38.625, 0.08)     # ring on Budget
pop('F5', 39.25, 0.10)                              # toast
clicks(41.0, 41.5, 0.03)                            # Cue question typing
pop('A5', 41.75, 0.10)                              # "Only visible to you"
pop('F5', 46.0, 0.10); pop('C6', 46.125, 0.08)      # buttons

# room on the SFX bus (short stereo reflections), then fold into the music
room = lambda x, d, g: np.concatenate([np.zeros(int(d*SR)), x[:-int(d*SR)]]) * g
SLw = SL + room(SL, 0.043, 0.30) + room(SR_, 0.071, 0.22) + room(SL, 0.113, 0.12)
SRw = SR_ + room(SR_, 0.051, 0.30) + room(SL, 0.067, 0.22) + room(SR_, 0.127, 0.12)
L += SLw; R += SRw

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
