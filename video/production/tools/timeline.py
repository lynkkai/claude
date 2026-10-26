"""Build timeline.json (scene times + beat times) and captions.srt for one video.

Timing comes from the real voiceover when vo/scene_XX.json files exist (written by
vo_elevenlabs.py), otherwise it is estimated at the reference pace of Lynkk's
in-person video (160 words per minute). Scene cuts snap to the music's beat grid.

usage: python3 timeline.py <video_dir> [--bpm 96]
"""
import json, math, os, re, sys

WPM = 160          # measured from Lynkk's reference voiceover
GAP = 0.35         # pause between sentences
LEAD = 0.6         # silence before the first sentence of a scene
TAIL = 0.8         # hold after the last sentence of a scene


def est(sentence):
    words = len(re.findall(r"[\w$.']+", sentence))
    return words / WPM * 60


def srt_time(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def main():
    vdir = sys.argv[1]
    bpm = float(sys.argv[sys.argv.index('--bpm') + 1]) if '--bpm' in sys.argv else 96.0
    beat = 60.0 / bpm
    spec = json.load(open(os.path.join(vdir, 'scenes.json'), encoding='utf-8'))
    t, out, caps, vo_clips = 0.0, [], [], []
    for i, s in enumerate(spec['scenes']):
        start = t
        voj = os.path.join(vdir, 'vo', f'scene_{i + 1:02d}.json')
        if os.path.exists(voj):
            v = json.load(open(voj))
            rel = v['sentence_starts']
            ends = v['sentence_ends']
            vo_len = v['duration']
            vo_clips.append({'file': v.get('file', f'vo/scene_{i + 1:02d}.mp3'), 'at': start + LEAD})
        else:
            rel, ends, x = [], [], 0.0
            for sent in s['vo']:
                rel.append(x); x += est(sent); ends.append(x); x += GAP
            vo_len = x - GAP
        beats = [start + LEAD + r for r in rel]
        for sent, r, e in zip(s['vo'], rel, ends):
            caps.append((start + LEAD + r, start + LEAD + e, sent))
        length = LEAD + vo_len + TAIL
        length = max(length, s.get('minDuration', 0))
        end = start + math.ceil(length / beat) * beat      # cut on the beat
        out.append({**{k: v for k, v in s.items() if k != 'vo'}, 'start': round(start, 3),
                    'end': round(end, 3), 'beats': [round(b, 3) for b in beats], 'vo': s['vo']})
        t = end
    tl = {'id': spec['id'], 'duration': round(t, 3), 'bpm': bpm, 'scenes': out, 'vo_clips': vo_clips,
          'estimated': not vo_clips}
    json.dump(tl, open(os.path.join(vdir, 'timeline.json'), 'w'), indent=1)
    with open(os.path.join(vdir, 'captions.srt'), 'w', encoding='utf-8') as f:
        for n, (a, b, txt) in enumerate(caps, 1):
            f.write(f"{n}\n{srt_time(a)} --> {srt_time(b)}\n{txt}\n\n")
    print(f"{spec['id']}: {len(out)} scenes, {t:.1f}s ({int(t // 60)}:{int(t % 60):02d}),"
          f" timing from {'voiceover' if vo_clips else 'estimate'}")


if __name__ == '__main__':
    main()
