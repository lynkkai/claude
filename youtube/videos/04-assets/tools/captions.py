"""Build the voiceover script and draft captions from the video script.
Run from 04-assets/:  python3 tools/captions.py ../04-sales-calls.md
Cues are spread across each scene's target timing by word count; re-time
after the edit, or let YouTube Studio auto-sync the transcript."""
import re, sys

src = open(sys.argv[1]).read()
script = src.split('## Script')[1].split('### End screen')[0]
scenes = re.split(r'\n### ', script)[1:]

def ts(s):
    h, r = divmod(s, 3600); m, sec = divmod(r, 60)
    return f"{int(h):02}:{int(m):02}:{int(sec):02},{int(round((sec - int(sec)) * 1000)):03}"

vo, srt, n = [], [], 1
for sc in scenes:
    head = sc.split('\n')[0]
    m = re.search(r'\((\d+):(\d+)-(\d+):(\d+)\)', head)
    start, end = int(m[1]) * 60 + int(m[2]), int(m[3]) * 60 + int(m[4])
    lines = []
    for row in sc.split('\n'):
        if row.startswith('| **VO** |'):
            lines.append(('', row.split('|')[2].strip().strip('"')))
        elif row.startswith('| **SCREEN** |'):
            lines += re.findall(r'(Daniel|Maya): "([^"]+)"', row)
    vo += [f"[{head}]"] + [t for w, t in lines if not w] + ['']
    words = [len(t.split()) for _, t in lines]
    total, t, span = sum(words) or 1, start + 0.3, end - start - 0.6
    for (who, text), w in zip(lines, words):
        dur, ws = span * w / total, text.split()
        while ws:
            chunk, ws = ws[:12], ws[12:]
            d = dur * len(chunk) / w
            label = f"{who.upper()}: " if who else ''
            srt.append(f"{n}\n{ts(t)} --> {ts(t + d - 0.05)}\n{label}{' '.join(chunk)}\n")
            n, t = n + 1, t + d

open('out/voiceover-script.txt', 'w').write(
    "Video 4 voiceover, brand host. Calm, plain, a little dry. Scene timings are targets.\n"
    "Maya and Daniel's lines are recorded live in the call scene.\n\n" + '\n'.join(vo))
open('out/captions-draft.srt', 'w').write('\n'.join(srt))
print(f"{n - 1} cues")
