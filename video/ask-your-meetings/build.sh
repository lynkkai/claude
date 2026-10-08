#!/usr/bin/env bash
# Rebuild the Ask Your Meetings video from source.
# Needs: python3 (kokoro-onnx, soundfile, numpy), node with playwright + Chromium, ffmpeg.
# Kokoro model files: https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0
set -euo pipefail
cd "$(dirname "$0")"
MODEL=${KOKORO_MODEL:?set KOKORO_MODEL to kokoro-v1.0.onnx}
VOICES=${KOKORO_VOICES:?set KOKORO_VOICES to voices-v1.0.bin}
mkdir -p build

python3 tts.py "$MODEL" "$VOICES"      # voice.wav, timeline.json, captions.srt
python3 music.py                       # mix.wav (voice + ambient bed)

N=$(python3 -c "import json,math;t=json.load(open('build/timeline.json'));print(math.ceil(t['duration']*t['fps']))")
Q=$(( (N + 3) / 4 ))
for i in 0 1 2 3; do
  s=$((i * Q)); e=$(( (i + 1) * Q < N ? (i + 1) * Q : N ))
  node render.mjs $s $e build/part$i.mp4 &
done
wait

printf "file 'part%d.mp4'\n" 0 1 2 3 > build/parts.txt
ffmpeg -y -v error -f concat -safe 0 -i build/parts.txt -i build/mix.wav \
  -map 0:v -map 1:a -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:a aac -b:a 192k -ar 48000 \
  -movflags +faststart -shortest lynkk-ask-your-meetings.mp4
node thumbnail.mjs thumbnail.png
echo "done: lynkk-ask-your-meetings.mp4"
