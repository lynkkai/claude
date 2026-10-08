#!/usr/bin/env bash
# Join the scene clips, the narration and the 12 s end screen into
# out/lynkk-ask-your-meetings.mp4 (1920x1080, 30 fps, H.264 + AAC, -14 LUFS).
#   ./assemble.sh <clipsDir>     (clips from: node capture.mjs video <clipsDir> s1 ... s12 end)
set -euo pipefail
CL="$(cd "${1:?clips dir}" && pwd)"
cd "$(dirname "$0")"
W=out/work; mkdir -p "$W"
: > "$W/videos.txt"; : > "$W/audios.txt"
for i in $(seq 1 12); do
  echo "file '$CL/s$i.mp4'" >> "$W/videos.txt"
  echo "file '$PWD/out/audio/s$i.wav'" >> "$W/audios.txt"
done
echo "file '$CL/end.mp4'" >> "$W/videos.txt"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$W/videos.txt" -c copy "$W/video.mp4"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$W/audios.txt" -af "apad=pad_dur=12,loudnorm=I=-14:TP=-1.5:LRA=11" -ar 48000 "$W/narration.wav"
ffmpeg -loglevel error -y -i "$W/video.mp4" -i "$W/narration.wav" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart out/lynkk-ask-your-meetings.mp4
rm -rf "$W"
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height -of compact out/lynkk-ask-your-meetings.mp4
