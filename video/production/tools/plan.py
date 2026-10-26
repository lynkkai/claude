"""Write brag-plan.md for one video (the /brag-slim planning deliverable).

usage: python3 tools/plan.py <video_dir> <out.md>
"""
import json, os, sys

vdir, out = sys.argv[1], sys.argv[2]
spec = json.load(open(os.path.join(vdir, 'scenes.json'), encoding='utf-8'))
tl = json.load(open(os.path.join(vdir, 'timeline.json'), encoding='utf-8'))
p = spec['plan']
fmt = lambda t: f"{int(t // 60)}:{t % 60:04.1f}"
lines = [f"# brag-plan: {spec['title']}", '',
         f"- **What it is:** {p['what']}", f"- **Who it's for:** {p['who']}", f"- **Angle:** {p['angle']}",
         f"- **Hook:** {p['hook']}", '- **Highlights:**'] + [f"  - {h}" for h in p['highlights']] + [
         f"- **Punchline:** {p['punchline']}", f"- **Tone:** {p['tone']}",
         '- **Visual identity:** lynkk.ai brand: Inter, ink #111111, stone #f5f5f4, lavender pill #e3dff3 with purple #7063be, '
         'lynkk.ai vector logo, real product panels captured from lynkk.ai (illustrative data, labeled), orange grain outro from Lynkk\'s in-person video.',
         f"- **Music:** original synthesized bed, A minor, {tl['bpm']:.0f} BPM; every scene cut lands on a beat.",
         '- **Voice:** Kokoro-82M `am_fenrir` at 1.0x via Hyperframes (matched to brag.mp4).',
         f"- **Share caption:** {p['caption']}", '',
         '**Length note:** /brag-slim targets 15-25s launch videos. These are long-form YouTube videos (under 5 minutes) by request, '
         'so the skill\'s other creative laws are applied scene by scene: hook first, show the real thing, readable holds, alive motion, every frame postable.', '',
         '## Storyboard', '', '| # | In | Out | Length | Scene | On screen |', '|---|---|---|---|---|---|']
for i, s in enumerate(tl['scenes'], 1):
    head = ' / '.join(s['head'])
    card = s.get('card', {})
    shown = ', '.join(os.path.basename(x['src']) for x in card.get('images', [])) or card.get('type', s['layout'])
    lines.append(f"| {i} | {fmt(s['start'])} | {fmt(s['end'])} | {s['end'] - s['start']:.1f}s | {s['pill']}: {head} | {shown} |")
lines += ['', f"Total: {fmt(tl['duration'])}"]
open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('wrote', out)
