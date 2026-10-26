#!/usr/bin/env bash
# Build one video end to end: timeline -> music -> frames -> mix -> mp4 + poster + captions.
# usage: tools/build.sh videos/01-best-ai-note-taker
# With ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID set, run tools/vo_elevenlabs.py first
# and this script times the visuals to the real voice and mixes it in.
set -euo pipefail
cd "$(dirname "$0")/.."
V="$1"; ID="$(basename "$V")"; OUT="../../brag-output/$ID"; mkdir -p "$OUT/work"
BPM=96
python3 tools/timeline.py "$V" --bpm $BPM
DUR=$(python3 -c "import json;print(json.load(open('$V/timeline.json'))['duration'])")
python3 tools/music.py "$DUR" "$OUT/work/music.wav" --bpm $BPM
node tools/render.mjs "$V" "$OUT/work/video.mp4"
VO_ARGS=$(python3 - "$V" <<'EOF'
import json, sys
tl = json.load(open(sys.argv[1] + '/timeline.json'))
print(' '.join(f"{c['file']}@{c['at']}" for c in tl['vo_clips']))
EOF
)
if [ -n "$VO_ARGS" ]; then
  # place each scene's voice clip, then duck the music under the voice
  INPUTS=(); FILT=""; n=0
  for c in $VO_ARGS; do f="${c%@*}"; at="${c#*@}"; INPUTS+=(-i "$V/$f"); ms=$(python3 -c "print(int($at*1000))")
    FILT+="[$((n+2)):a]aresample=48000,adelay=${ms}|${ms}[v$n];"; n=$((n+1)); done
  MIXV=$(for i in $(seq 0 $((n-1))); do printf "[v$i]"; done)
  ffmpeg -v error -y -i "$OUT/work/video.mp4" -i "$OUT/work/music.wav" "${INPUTS[@]}" -filter_complex \
    "${FILT}${MIXV}amix=inputs=$n:normalize=0,apad[vo];[vo]asplit[vo1][vo2];[1:a]volume=0.55[m];[m][vo1]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=400[md];[md][vo2]amix=inputs=2:normalize=0,alimiter=limit=0.9[a]" \
    -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest "$OUT/$ID.mp4"
else
  ffmpeg -v error -y -i "$OUT/work/video.mp4" -i "$OUT/work/music.wav" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest "$OUT/$ID-draft-no-voice.mp4"
fi
cp "$V/captions.srt" "$OUT/$ID.srt"
# brag deliverables: poster (strongest settled frame) baked in as frame 0, brag.jpg, share copy, plan
FINAL=$(ls "$OUT"/$ID*.mp4 | head -1)
PT=$(python3 tools/poster_time.py "$V")
node tools/render.mjs "$V" "$OUT/work/poster" --stills "$PT"
ffmpeg -v error -y -i "$OUT/work/poster/still_${PT}.png" -q:v 2 "$OUT/brag.jpg"
ffmpeg -v error -y -i "$FINAL" -i "$OUT/work/poster/still_${PT}.png" -filter_complex "[0:v][1:v]overlay=enable='eq(n,0)'[v]" -map "[v]" -map 0:a -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p -c:a copy "$OUT/work/with-poster.mp4"
mv "$OUT/work/with-poster.mp4" "$FINAL"
python3 -c "import json;print(json.load(open('$V/scenes.json'))['share_copy'])" > "$OUT/share-copy.txt"
python3 tools/plan.py "$V" "$OUT/brag-plan.md"
cp "$OUT/share-copy.txt" "$OUT/brag-plan.md" "$V/"
echo "done: $OUT"
