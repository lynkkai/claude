#!/usr/bin/env bash
# Build the YouTube Shorts cut (1080 x 1920, about 40 s) with the shared pipeline.
# Same rules as ../teams-recording-tutorial: the look comes from the Lynkk post kit,
# every claim must be in lynkk-post-kit/docs/TRUTHS.md, and both copy checks must pass.
set -euo pipefail
cd "$(dirname "$0")"

KOKORO_DIR="${KOKORO_DIR:-../pipeline/models}"
if [ ! -f "$KOKORO_DIR/kokoro-v1.0.onnx" ]; then
  mkdir -p "$KOKORO_DIR"
  base=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
  curl -sSL -o "$KOKORO_DIR/kokoro-v1.0.onnx" "$base/kokoro-v1.0.onnx"
  curl -sSL -o "$KOKORO_DIR/voices-v1.0.bin" "$base/voices-v1.0.bin"
fi

node ../pipeline/check_script.mjs .
node ../../lynkk-post-kit/scripts/check.mjs video.html

KOKORO_DIR="$KOKORO_DIR" python3 ../pipeline/build_audio.py .
node ../pipeline/render.cjs .
python3 ../pipeline/mix_audio.py .

ffmpeg -y -loglevel error -i build/video-silent.mp4 -i build/mix.wav \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart \
  -metadata title="Record a Microsoft Teams meeting, three ways | Lynkk" \
  lynkk-teams-recording-short.mp4
echo "done: lynkk-teams-recording-short.mp4"
