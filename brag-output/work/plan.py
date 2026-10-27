"""Builds the shared timeline (timing.js) used by both the visuals and the audio mix."""
import json, math, random

W = json.load(open('vo/words.json'))
FPS = 30

# The first 20 seconds are fixed. After that each scene starts where the previous one ends,
# its line begins 0.2s in, and it holds after the line before cutting. Every cut sits on the
# 120 BPM grid (0.5s) counted from the music drop at 4.0s.
FIXED = [('s1', 'l1', 'hook_take2', 0.00, 0.0, 4.7), ('s2', 'l2', 'l2', 4.10, 4.0, 8.0),
         ('s3', 'l3', 'l3', 8.10, 8.0, 13.5), ('s4', 'l4', 'l4', 13.60, 13.5, 19.0)]
FLOW = [('s5', 'l5', 1.6), ('sM', 'lm', 1.6), ('sC', 'lc', 1.6), ('s6', 'l6', 1.0),
        ('s7', 'l7', 1.0), ('sG', ['lg1', 'lg2', 'lg3'], 1.2), ('sD', 'ld', 1.4), ('sP', 'lp', 1.4), ('s8', 'l8', 2.2)]
grid = lambda x: 4.0 + math.ceil((x - 4.0) / 0.5 - 1e-9) * 0.5
LINES, SCENES = [], {}
for sid, key, f, ls, a, b in FIXED:
    LINES.append((key, f, ls)); SCENES[sid] = [a, b]
cur = 19.0
for sid, keys, hold in FLOW:
    ls = cur + 0.2
    for key in (keys if isinstance(keys, list) else [keys]):
        LINES.append((key, key, round(ls, 2))); last = ls + W[key]['dur']; ls = last + 0.7
    end = grid(last + hold)
    SCENES[sid] = [cur, end]; cur = end
TOTAL = cur

rng = random.Random(11)
PAD = "corvane disc. call\nbudget 30k?? maybe 50\nIT approval - who??\npilot 15 ppl\nsend sec overvw by fri"
keys, t = [], 0.06
while t < 3.95 and len(keys) < len(PAD):
    keys.append(round(t, 3))
    gap = rng.uniform(0.035, 0.085)
    if PAD[len(keys) - 1] in '\n?' and rng.random() < 0.7:
        gap += rng.uniform(0.08, 0.16)
    t += gap
backspace = [round(4.18 + i * 0.045, 3) for i in range(9)]

Q = "What did we promise Corvane?"
q0 = 0.0
lines = {}
for k, f, s in LINES:
    lines[k] = dict(start=s, file=f, dur=W[f]['dur'], words=[dict(w=w['w'], s=w['s'], e=w['e']) for w in W[f]['words']])
q0 = lines['l5']['start'] + lines['l5']['words'][6]['s'] - 0.1
qkeys = [round(q0 + i * 0.034, 3) for i in range(len(Q))]

timing = dict(fps=FPS, total=TOTAL, lines=lines, scenes=SCENES, pad=PAD, keys=keys,
              backspace=backspace, question=Q, qkeys=qkeys, musicStart=4.0)
open('build/timing.js', 'w').write('window.TIMING=' + json.dumps(timing) + ';\n')
json.dump(timing, open('timing.json', 'w'), indent=1)
print('total', TOTAL); print(SCENES)
