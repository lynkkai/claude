#!/usr/bin/env bash
# Build one comparison video: narration (Kokoro, Adam voice), sitar + tabla music, kit boards, final MP4.
#   ./build.sh <videoDir> <short|long> [stills]
#   e.g. ./build.sh ../lynkk-vs-otter long
# Needs: pip install kokoro-onnx soundfile numpy; the Kokoro model files in $MODELS
# (kokoro-v1.0.onnx, voices-v1.0.bin from the kokoro-onnx GitHub releases); Playwright linked into
# lynkk-post-kit/node_modules (see .claude/skills/lynkk-design/SKILL.md, section 4).
set -euo pipefail
TOOLS="$(cd "$(dirname "$0")" && pwd)"
DIR="$(cd "${1:?video dir}" && pwd)"
V="${2:?short or long}"
MODELS="${MODELS:-/tmp/lynkk-models}"
SLUG="$(basename "$DIR")"
OUT="$DIR/out/$V"
mkdir -p "$OUT"
export CHROME="${CHROME:-/opt/pw-browsers/chromium}"

for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s "$MODELS/$f" ] || { mkdir -p "$MODELS"; curl -sSL -o "$MODELS/$f" "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f"; }
done

# copy check on everything that ships (the guard hook runs it too)
node "$TOOLS/../../../lynkk-post-kit/scripts/check.mjs" "$DIR/$V.html"
# the narration is published too (voice and captions): check it with the same rules, same opt-in
python3 -c "
import json, re; d = json.load(open('$DIR/narration-$V.json'))
allow = re.search(r'<meta name=\"lynkk-allow\"[^>]*>', open('$DIR/$V.html').read())
open('$OUT/narration-check.html', 'w').write((allow.group(0) if allow else '') + '<p>' + ' '.join(l for s in d['scenes'] for l in s['lines']) + '</p>')"
node "$TOOLS/../../../lynkk-post-kit/scripts/check.mjs" "$OUT/narration-check.html"

python3 -I "$TOOLS/tts.py" "$DIR/narration-$V.json" "$OUT" "$MODELS/kokoro-v1.0.onnx" "$MODELS/voices-v1.0.bin"

if [ "${3:-}" = "stills" ]; then
  node "$TOOLS/capture.mjs" stills "$DIR/$V.html" "$OUT/timing.json" "$OUT/storyboard"
  exit 0
fi

W="$OUT/work"; mkdir -p "$W"
python3 -c "
import json; t = json.load(open('$OUT/timing.json'))
open('$W/audios.txt', 'w').write(''.join(f\"file '$OUT/audio/{i}.wav'\n\" for i in t['_order']))
print(t['_total'])" > "$W/total.txt"
TOTAL="$(cat "$W/total.txt")"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$W/audios.txt" -af "aresample=44100,highpass=f=70,equalizer=f=140:t=q:w=1:g=2,equalizer=f=3000:t=q:w=1.2:g=1.5,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120:makeup=2,aecho=0.85:0.5:22|41:0.05|0.03,loudnorm=I=-16:TP=-1.5" -ac 2 -ar 44100 "$W/voice.wav"
python3 -I -c "
import sys; sys.path.insert(0, '$TOOLS')
import soundfile as sf, music_indian as m
sf.write('$W/music.wav', m.build('sitar', $TOTAL + 0.5, seed=3 if 'otter' in '$SLUG' else 9), m.SR)"
ffmpeg -loglevel error -y -i "$W/voice.wav" -i "$W/music.wav" -filter_complex \
  "[1:a]volume=0.2[m];[0:a]apad=whole_dur=$TOTAL,asplit=2[v][k];[m][k]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=400[md];[v][md]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.0:LRA=9[a]" \
  -map "[a]" -ar 48000 "$W/mix.wav"
node "$TOOLS/capture.mjs" video "$DIR/$V.html" "$OUT/timing.json" "$W/video.mp4"
FINAL="$DIR/out/$SLUG-$V.mp4"
ffmpeg -loglevel error -y -i "$W/video.mp4" -i "$W/mix.wav" -map 0:v -map 1:a -c:v copy -af apad -c:a aac -b:a 192k -shortest -movflags +faststart "$FINAL"
cp "$OUT/captions.srt" "$DIR/out/$SLUG-$V.srt"
rm -rf "$W"
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height -of compact "$FINAL"
