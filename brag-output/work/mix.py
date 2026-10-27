"""Mix voice, music bed and SFX on the same timeline the visuals use (timing.json)."""
import json, random, subprocess
import numpy as np

SR = 48000
T = json.load(open('timing.json'))
TOTAL = T['total']
SFX = 'web/brag-repo/skills/brag/assets/sfx/'
MUSIC = 'web/brag-repo/skills/brag/assets/music/happy-beats-business-moves-vol-1-by-ende-dot-app.mp3'


def load(path, ss=None, t=None, af=None):
    cmd = ['ffmpeg', '-loglevel', 'error']
    if ss is not None: cmd += ['-ss', str(ss)]
    if t is not None: cmd += ['-t', str(t)]
    cmd += ['-i', path]
    if af: cmd += ['-af', af]
    cmd += ['-ac', '2', '-ar', str(SR), '-f', 'f32le', '-']
    a = np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, dtype=np.float32)
    return a.reshape(-1, 2).copy()


def db(x): return 10 ** (x / 20)


N = int(TOTAL * SR)
vo = np.zeros((N, 2), np.float32)
music = np.zeros((N, 2), np.float32)
fx = np.zeros((N, 2), np.float32)


def place(buf, a, t, g=1.0):
    i = int(round(t * SR))
    if i >= N: return
    a = a[: N - i] * g
    buf[i:i + len(a)] += a


def wt(line, i):
    L = T['lines'][line]
    return L['start'] + L['words'][i]['s']


# ---- voice: level-match every line on its voiced frames
for k, L in T['lines'].items():
    a = load(f"vo/{L['file']}.wav", af='highpass=f=70')
    fr = a[: len(a) // 480 * 480, 0].reshape(-1, 480)
    rms = np.sqrt((fr ** 2).mean(1))
    voiced = rms[rms > rms.max() * 0.1]
    level = np.sqrt((voiced ** 2).mean())
    a *= db(-19) / level
    fade = int(0.01 * SR); a[:fade] *= np.linspace(0, 1, fade)[:, None]; a[-fade:] *= np.linspace(1, 0, fade)[:, None]
    place(vo, a, L['start'])

# ---- music: muffled under the hook, opens up on the beat at the reveal
m0 = T['musicStart']           # video time of the drop
P0 = 16.02                     # strong beat in the track that lands on the drop
pre = load(MUSIC, ss=P0 - m0, t=m0, af='lowpass=f=420,lowpass=f=420')
env = np.linspace(0, 1, len(pre)) ** 1.5
place(music, pre * env[:, None], 0, db(-6))
full = load(MUSIC, ss=P0, t=TOTAL - m0)
f = int(0.03 * SR); full[:f] *= np.linspace(0, 1, f)[:, None]
fo = int(2.6 * SR); full[-fo:] *= (np.linspace(1, 0, fo) ** 1.6)[:, None]
place(music, full, m0)

# duck the bed under the voice (attack 60ms, release 350ms)
act = np.abs(vo[:, 0])
hop = 480
lvl = np.array([act[i:i + hop].max() for i in range(0, N, hop)])
on = (lvl > 0.02).astype(float)
sm = np.zeros_like(on); g = 0
for i, v in enumerate(on):
    c = 0.5 if v > g else 0.08
    g += (v - g) * c; sm[i] = g
gain_db = -10 + sm * -9          # idle -10 dB, under voice -19 dB
gain = np.repeat(db(gain_db), hop)[:N]
music *= gain[:, None]

# ---- sfx
rng = random.Random(5)
keys = [load(f'{SFX}keyboard/keypress-{i:03d}.wav') for i in range(1, 11)]
for i, k in enumerate(keys): keys[i] = k / (np.abs(k).max() + 1e-9)
for t in T['keys']:
    place(fx, rng.choice(keys), t, db(-21) * rng.uniform(0.6, 1.0))
for t in T['qkeys'][::2]:
    place(fx, rng.choice(keys), t, db(-34))


def s(name):
    a = load(SFX + name); return a / (np.abs(a).max() + 1e-9)


soft = s('impact/impactSoft_heavy_000.ogg')
pop = s('interface/click_002.ogg')
tick = s('interface/click_003.ogg')
bong = s('interface/bong_001.ogg')
slide = s('casino/card-slide-1.ogg')
press = s('ui/click2.ogg')

# hook: buyer's bubble
place(fx, bong, 2.55, db(-24))
# riser into the drop: band-limited noise swell
n = int(0.7 * SR); r = np.random.default_rng(1).standard_normal(n).astype(np.float32)
r = np.convolve(r, np.ones(24) / 24, 'same')
r = (r * (np.linspace(0, 1, n) ** 3))[:, None].repeat(2, 1)
place(fx, r, m0 - 0.7, db(-30))
# reveal
place(fx, soft, wt('l2', 3) - 0.08, db(-12))
# capture cards
for t in [8.0, 13.5, 19.0, 26.0]: place(fx, slide, t, db(-26))
for i in [1, 2, 3, 7]: place(fx, pop, wt('l3', i) - 0.08, db(-20))
place(fx, tick, wt('l3', 10) - 0.05, db(-22))
# notes
place(fx, pop, wt('l4', 5) - 0.05, db(-20)); place(fx, pop, wt('l4', 7) - 0.05, db(-20))
place(fx, bong, wt('l4', 8) + 0.25, db(-24)); place(fx, bong, wt('l4', 8) + 0.85, db(-26))
# ask
for i in range(3): place(fx, tick, wt('l5', 15) + i * 0.16, db(-24))
# follow-up click + toast
click = wt('l6', 8) + 0.1 + 0.75
place(fx, press, click, db(-14)); place(fx, bong, click + 0.2, db(-24))
# hand off
for i in [4, 7, 10]: place(fx, pop, wt('l7', i) - 0.05, db(-19))
place(fx, bong, wt('l7', 5) - 0.2, db(-26))
# outro
place(fx, soft, wt('l8', 6) - 0.1, db(-12))
place(fx, pop, wt('l8', 7) - 0.05, db(-20))

mix = vo + music + fx
mix = np.tanh(mix * 1.1) / 1.1   # gentle safety saturation, inaudible at these levels
mix.astype(np.float32).tofile('mix.f32')
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', 'mix.f32',
                '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11', '-ar', str(SR), 'mix.wav'], check=True)
print('peak', float(np.abs(mix).max()))
