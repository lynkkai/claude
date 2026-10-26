#!/usr/bin/env bash
# Bake a poster frame in as frame 0 (the idle thumbnail on every platform), brag-style:
# frame 0 is replaced, not added, so duration and audio sync stay the same. Audio is copied untouched.
# Usage: poster.sh <in.mp4> <poster.jpg> <out.mp4>
set -euo pipefail
in="$1"; poster="$2"; out="$3"
read -r w h fps < <(ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate -of csv=p=0 "$in" | tr ',' ' ')
ffmpeg -v error -y -i "$in" -loop 1 -i "$poster" -filter_complex \
  "[1:v]scale=${w}:${h},format=yuv420p,fps=${fps},trim=end_frame=1,setpts=PTS-STARTPTS[p];\
   [0:v]trim=start_frame=1,setpts=PTS-STARTPTS[rest];[p][rest]concat=n=2:v=1:a=0[v]" \
  -map "[v]" -map 0:a? -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a copy -movflags +faststart "$out"
echo "poster baked into frame 0 -> $out"
