#!/usr/bin/env bash
# Rebuild the whole video from script.json + video.html.
# The look comes from ../../lynkk-post-kit (the Lynkk Grid design system); every
# claim must be in lynkk-post-kit/docs/TRUTHS.md. Both copy checks must pass.
# Needs: python3 (kokoro-onnx, soundfile, numpy), node + playwright (Chromium), ffmpeg.
set -euo pipefail
cd "$(dirname "$0")"

KOKORO_DIR="${KOKORO_DIR:-../pipeline/models}"
if [ ! -f "$KOKORO_DIR/kokoro-v1.0.onnx" ]; then
  mkdir -p "$KOKORO_DIR"
  base=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
  curl -sSL -o "$KOKORO_DIR/kokoro-v1.0.onnx" "$base/kokoro-v1.0.onnx"
  curl -sSL -o "$KOKORO_DIR/voices-v1.0.bin" "$base/voices-v1.0.bin"
fi

node ../pipeline/check_script.mjs .                       # narration vs the kit's copy and claims rules
node ../../lynkk-post-kit/scripts/check.mjs video.html     # on-screen copy, same rules

KOKORO_DIR="$KOKORO_DIR" python3 ../pipeline/build_audio.py .   # voiceover, timeline, narrator levels, captions.srt
node ../pipeline/render.cjs .                     # frames -> build/video-silent.mp4, build/sfx.json
python3 ../pipeline/mix_audio.py .                # music + sound effects + voice -> build/mix.wav
node ../pipeline/render.cjs . --thumbnail thumbnail.png

ffmpeg -y -loglevel error -i build/video-silent.mp4 -i build/mix.wav \
  -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart \
  -metadata title="How to record a Microsoft Teams meeting with Lynkk" \
  lynkk-how-to-record-teams-meeting.mp4
echo "done: lynkk-how-to-record-teams-meeting.mp4"
