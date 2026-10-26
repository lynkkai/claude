#!/usr/bin/env bash
# Mix picture + music (+ optional voiceover) into the final MP4.
# Voice on top, music ducked under it (sidechain), loudness normalized to -14 LUFS for social.
# Usage: mix.sh <frames.mp4> <music.wav> <out.mp4> [voice.wav]
set -euo pipefail
frames="$1"; music="$2"; out="$3"; voice="${4:-}"
if [[ -z "$voice" ]]; then
  ffmpeg -v error -y -i "$frames" -i "$music" \
    -filter_complex "[1:a]loudnorm=I=-14:TP=-1.5:LRA=9[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest -movflags +faststart "$out"
else
  ffmpeg -v error -y -i "$frames" -i "$music" -i "$voice" -filter_complex "\
[2:a]aresample=44100,aformat=channel_layouts=stereo,highpass=f=85,acompressor=threshold=-20dB:ratio=3:attack=5:release=120:makeup=2,asplit=2[vo][sc];\
[1:a]volume=0.62[mu];[mu][sc]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=350[duck];\
[duck][vo]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=9[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$out"
fi
ffmpeg -hide_banner -i "$out" -af ebur128=framelog=quiet -f null - 2>&1 | grep ' I:' || true
