#!/usr/bin/env bash
# Encode scene frames, join them with the narration, add the end screen, and
# write out/lynkk-sales-calls.mp4 (1920x1080, 30 fps, H.264 + AAC, -14 LUFS).
#   ./assemble.sh <framesRoot>
set -euo pipefail
FR="${1:?frames root}"
cd "$(dirname "$0")"
W=out/work; mkdir -p "$W"
: > "$W/videos.txt"; : > "$W/audios.txt"
for i in $(seq 1 12); do
  ffmpeg -loglevel error -y -framerate 30 -i "$FR/s$i/f%05d.png" -c:v libx264 -pix_fmt yuv420p -crf 18 -preset medium "$W/s$i.mp4"
  echo "file 's$i.mp4'" >> "$W/videos.txt"
  echo "file '../audio/s$i.wav'" >> "$W/audios.txt"
done
# End screen: 12 s of the kit end screen from 04-assets, with silence under it.
ffmpeg -loglevel error -y -i ../04-assets/out/motion/end-screen.mp4 -t 12 -c:v libx264 -pix_fmt yuv420p -crf 18 -r 30 "$W/end.mp4"
echo "file 'end.mp4'" >> "$W/videos.txt"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$W/videos.txt" -c copy "$W/video.mp4"
ffmpeg -loglevel error -y -f concat -safe 0 -i "$W/audios.txt" -af "apad=pad_dur=12,loudnorm=I=-14:TP=-1.5:LRA=11" -ar 48000 "$W/narration.wav"
ffmpeg -loglevel error -y -i "$W/video.mp4" -i "$W/narration.wav" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart out/lynkk-sales-calls.mp4
rm -rf "$W"
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height -of compact out/lynkk-sales-calls.mp4
