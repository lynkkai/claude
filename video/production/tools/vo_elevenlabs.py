"""Generate the voiceover with ElevenLabs, one clip per scene, with sentence timings.

Reads ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID from the environment (never hard-code
them). Writes <video_dir>/vo/scene_XX.mp3 and scene_XX.json, which timeline.py uses
to time every on-screen beat to the real voice.

usage: python3 vo_elevenlabs.py <video_dir> [--model eleven_multilingual_v2]
"""
import base64, json, os, re, sys, urllib.request

API = 'https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128'

# How the voice should say things (display text stays unchanged on screen and in captions)
SAY = [
    (r'\blynkk\.ai\b', 'Link dot A I'), (r'\bLynkk\b', 'Link'),
    (r'\$9\.75', 'nine seventy-five'), (r'\$15\b', 'fifteen dollars'),
    (r'\bAI\b', 'A I'), (r'\bCRM\b', 'C R M'),
]


def spoken(s):
    for pat, rep in SAY:
        s = re.sub(pat, rep, s)
    return s


def main():
    vdir = sys.argv[1]
    model = sys.argv[sys.argv.index('--model') + 1] if '--model' in sys.argv else 'eleven_multilingual_v2'
    key, voice = os.environ.get('ELEVENLABS_API_KEY'), os.environ.get('ELEVENLABS_VOICE_ID')
    if not key or not voice:
        sys.exit('Set ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID in the environment first.')
    spec = json.load(open(os.path.join(vdir, 'scenes.json'), encoding='utf-8'))
    os.makedirs(os.path.join(vdir, 'vo'), exist_ok=True)
    for i, s in enumerate(spec['scenes'], 1):
        parts = [spoken(x) for x in s['vo']]
        text = ' '.join(parts)
        body = json.dumps({'text': text, 'model_id': model,
                           'voice_settings': {'stability': 0.5, 'similarity_boost': 0.8, 'style': 0.15}}).encode()
        req = urllib.request.Request(API.format(voice=voice), data=body, method='POST',
                                     headers={'xi-api-key': key, 'Content-Type': 'application/json'})
        r = json.load(urllib.request.urlopen(req, timeout=180))
        al = r['alignment']; starts = al['character_start_times_seconds']; ends = al['character_end_times_seconds']
        s_starts, s_ends, pos = [], [], 0
        for p in parts:  # map each sentence's first and last character to times
            a = pos; b = pos + len(p) - 1
            s_starts.append(starts[min(a, len(starts) - 1)]); s_ends.append(ends[min(b, len(ends) - 1)])
            pos += len(p) + 1
        open(os.path.join(vdir, 'vo', f'scene_{i:02d}.mp3'), 'wb').write(base64.b64decode(r['audio_base64']))
        json.dump({'sentence_starts': s_starts, 'sentence_ends': s_ends, 'duration': ends[-1]},
                  open(os.path.join(vdir, 'vo', f'scene_{i:02d}.json'), 'w'))
        print(f'scene {i}: {ends[-1]:.1f}s')


if __name__ == '__main__':
    main()
