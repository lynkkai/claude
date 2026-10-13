#!/bin/bash
# Rebuild all four comparison videos into ../ (videos/comparisons/).
# Voice: Sarvam AI when SARVAM_API_KEY is set (optional SARVAM_SPEAKER, default priya), else offline Kokoro.
# Usage: ./make_all.sh [slug ...]
set -euo pipefail
cd "$(dirname "$0")"
WORK=${WORK:-/tmp/lynkk-video-build}
mkdir -p "$WORK/build"
python3 -c "import soundfile, numpy" 2>/dev/null || pip install -q soundfile numpy
if [ -z "${SARVAM_API_KEY:-}" ]; then
  python3 -c "import kokoro_onnx" 2>/dev/null || pip install -q kokoro-onnx
  mkdir -p "$WORK/models"
  for f in kokoro-v1.0.onnx voices-v1.0.bin; do
    [ -s "$WORK/models/$f" ] || curl -sSL -o "$WORK/models/$f" "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f"
  done
fi
SLUGS=("$@")
[ ${#SLUGS[@]} -eq 0 ] && SLUGS=(lynkk-vs-otter-short lynkk-vs-granola-short lynkk-vs-otter-long lynkk-vs-granola-long)
for s in "${SLUGS[@]}"; do python3 build_audio.py "$s" "$WORK/build"; done
export NODE_PATH=${NODE_PATH:-/opt/node22/lib/node_modules}
export CHROME=${CHROME:-/opt/pw-browsers/chromium}
# two renders at a time keeps Chromium from starving on a 4 core box
printf '%s\n' "${SLUGS[@]}" | xargs -P 2 -I{} sh -c 'node render.js "$1/build/{}" "../{}.mp4" > "$1/build/{}/render.log" 2>&1 && echo "done {}" || { echo "FAILED {}"; tail -5 "$1/build/{}/render.log"; }' _ "$WORK"
