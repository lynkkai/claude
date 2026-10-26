"""Generate the voiceover locally with Kokoro-82M (the engine behind `hyperframes tts`).

Voice: am_fenrir at 1.0x, matched to the narration in Lynkk's brag.mp4 (pitch, tone
and pace). Each sentence is synthesized on its own, so every on-screen beat gets an
exact start time. Writes <video_dir>/vo/scene_XX.wav and scene_XX.json for timeline.py.

Needs the Kokoro model that `npx hyperframes tts` downloads to ~/.cache/hyperframes/tts/
and a Python with kokoro-onnx + soundfile (set HYPERFRAMES_PYTHON or run with that python).

usage: python vo_kokoro.py <video_dir> [--voice am_fenrir] [--speed 1.0]
"""
import json, os, re, sys
import numpy as np
import kokoro_onnx
import soundfile as sf

GAP = 0.45  # pause between sentences, as in brag.mp4
SAY = [  # how the voice should say things; captions and screen keep the real spelling
    (r'\blynkk\.ai\b', 'Link dot AI'), (r'\bLynkk\b', 'Link'),
    (r'\$9\.75', 'nine seventy-five'), (r'\$15\b', 'fifteen dollars'),
    (r'\bput ours in\b', 'put our own in'),  # "ours" was heard as "hours"
]  # plain "AI" and "CRM" are already read correctly; spelling them out made them worse


def spoken(s):
    for pat, rep in SAY:
        s = re.sub(pat, rep, s)
    return s


def main():
    vdir = sys.argv[1]
    voice = sys.argv[sys.argv.index('--voice') + 1] if '--voice' in sys.argv else 'am_fenrir'
    speed = float(sys.argv[sys.argv.index('--speed') + 1]) if '--speed' in sys.argv else 1.0
    m = os.path.expanduser('~/.cache/hyperframes/tts/')
    k = kokoro_onnx.Kokoro(m + 'models/kokoro-v1.0.onnx', m + 'voices/voices-v1.0.bin')
    spec = json.load(open(os.path.join(vdir, 'scenes.json'), encoding='utf-8'))
    os.makedirs(os.path.join(vdir, 'vo'), exist_ok=True)
    for i, s in enumerate(spec['scenes'], 1):
        chunks, starts, ends, t, sr = [], [], [], 0.0, 24000
        for sent in s['vo']:
            a, sr = k.create(spoken(sent), voice=voice, speed=speed, lang='en-us')
            a = np.asarray(a, dtype=np.float32)
            nz = np.flatnonzero(np.abs(a) > 0.01)          # trim edge silence
            if len(nz): a = a[max(0, nz[0] - int(0.03 * sr)): nz[-1] + int(0.08 * sr)]
            starts.append(t); t += len(a) / sr; ends.append(t)
            chunks += [a, np.zeros(int(GAP * sr), dtype=np.float32)]; t += GAP
        audio = np.concatenate(chunks[:-1])
        f = f'scene_{i:02d}.wav'
        sf.write(os.path.join(vdir, 'vo', f), audio, sr)
        json.dump({'file': f'vo/{f}', 'sentence_starts': starts, 'sentence_ends': ends,
                   'duration': len(audio) / sr, 'voice': voice, 'speed': speed},
                  open(os.path.join(vdir, 'vo', f'scene_{i:02d}.json'), 'w'))
        print(f'scene {i}: {len(audio) / sr:.1f}s')


if __name__ == '__main__':
    main()
