#!/usr/bin/env bash
# Put the background music under the narration and remux out/<name>.mp4 (video stream copied).
# Run from a video folder after tts.py, music.py and assemble.sh:
#   ../tools/mix.sh lynkk-for-<name>-teams
# The music sits about 18 dB under the voice while she speaks (sidechain ducking) and rises
# between lines and on the CTA hold. Final loudness -14 LUFS, true peak -1.5 dB.
set -euo pipefail
NAME="${1:?output name}"
W=out/work; mkdir -p "$W"
: > "$W/audios.txt"
for id in $(python3 -c "import json; print(' '.join(json.load(open('out/timing.json'))))"); do
  echo "file '$PWD/out/audio/$id.wav'" >> "$W/audios.txt"
done
ffmpeg -loglevel error -y -f concat -safe 0 -i "$W/audios.txt" -ar 48000 -ac 2 "$W/voice.wav"
ffmpeg -loglevel error -y -i "$W/voice.wav" -i out/music.wav -filter_complex "\
[0:a]loudnorm=I=-16:TP=-2:LRA=11,aresample=48000,asplit=2[v][key];\
[1:a]volume=-9dB[m];\
[m][key]sidechaincompress=threshold=0.02:ratio=4:attack=40:release=650:knee=4[duck];\
[v][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[out]" \
  -map "[out]" "$W/mix.wav"
ffmpeg -loglevel error -y -i "out/$NAME.mp4" -i "$W/mix.wav" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "$W/out.mp4"
mv "$W/out.mp4" "out/$NAME.mp4"
rm -rf "$W"
ffprobe -v error -show_entries format=duration:stream=codec_name -of compact "out/$NAME.mp4"
