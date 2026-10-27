"""Builds the shared timeline (timing.js) used by both the visuals and the audio mix."""
import json, random

W = json.load(open('vo/words.json'))
FPS = 30
TOTAL = 47.0

# Voice lines: (key, file, absolute start). Every scene cut sits on the 120 BPM grid (0.5s).
LINES = [
    ('l1', 'hook_take2', 0.00),
    ('l2', 'l2', 4.10),
    ('l3', 'l3', 8.10),
    ('l4', 'l4', 13.60),
    ('l5', 'l5', 19.10),
    ('l6', 'l6', 26.10),
    ('l7', 'l7', 33.10),
    ('l8', 'l8', 39.60),
]
SCENES = {'s1': [0, 4.7], 's2': [4.0, 8.0], 's3': [8.0, 13.5], 's4': [13.5, 19.0],
          's5': [19.0, 26.0], 's6': [26.0, 33.0], 's7': [33.0, 39.5], 's8': [39.5, TOTAL]}

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
print(len(keys), 'keystrokes; pad chars typed:', repr(PAD[:len(keys)]))
