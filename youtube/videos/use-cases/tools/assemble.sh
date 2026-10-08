#!/usr/bin/env bash
# Join the scene clips and the narration into out/<name>.mp4
# (1920x1080, 30 fps, H.264 + AAC, -14 LUFS). Run from a video folder:
#   ../tools/assemble.sh <clipsDir> <name>
set -euo pipefail
CL="$(cd "${1:?clips dir}" && pwd)"; NAME="${2:?output name}"
W=out/work; mkdir -p "$W"
: > "$W/videos.txt"; : > "$W/audios.txt"
for id in $(python3 -c "import json; print(' '.join(json.load(open('out/timing.json'))))"); do
  echo "file '$CL/$id.mp4'" >> "$W/videos.txt"
  echo "file '$PWD/out/audio/$id.wav'" >> "$W/audios.txt"
done
ffmpeg -loglevel error -y -f concat -safe 0 -i "$W/videos.txt" -c copy "$W/video.mp4"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$W/audios.txt" -af "loudnorm=I=-14:TP=-1.5:LRA=11" -ar 48000 "$W/narration.wav"
ffmpeg -loglevel error -y -i "$W/video.mp4" -i "$W/narration.wav" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "out/$NAME.mp4"
rm -rf "$W"
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height -of compact "out/$NAME.mp4"
