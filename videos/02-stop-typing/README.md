# Short #2: Stop Typing During Discovery Calls

Vertical short (1080x1920, 30fps, 38.8s) built from row 2 of `lynkk-shorts-content.csv`.

- `brag.mp4`: current cut (music, SFX, burned-in captions; **no VO yet**)
- `brag.jpg`: poster / thumbnail (also baked in as frame 0)
- `share-copy.txt`: post caption plus the required music credit
- `brag-plan.md`: angle, brand tokens, storyboard, timing

## Rebuild

```sh
python3 src/timeline.py   # timing: scene cuts, VO lines, keystrokes
node src/render.js        # frames -> work/video.mp4 (needs Playwright + Chromium)
python3 src/mix.py        # music + SFX (+ src/assets/vo.wav if present) -> work/brag-noposter.mp4
ffmpeg -y -ss 2.25 -i work/video.mp4 -frames:v 1 -q:v 2 brag.jpg
ffmpeg -y -i work/brag-noposter.mp4 -i brag.jpg -filter_complex "[0:v][1:v]overlay=enable='eq(n\,0)'[v]" \
  -map "[v]" -map 0:a -c:v libx264 -crf 16 -pix_fmt yuv420p -c:a copy -movflags +faststart brag.mp4
```

Review stills: `node src/render.js --stills 1.5,12.8,21`.

## Adding the VO

1. Record the script from the CSV and save it as `src/assets/vo.wav`, starting at 0:00.
2. Update the `LINES` start/end times in `src/timeline.py` to match the read (captions, tab switches,
   the question counter and the pain chip all key off these words).
3. Re-run the steps above. `mix.py` ducks the music under the VO automatically.

## Credits

Music: "Happy Beats / Business Moves Vol. 10" by Sascha Ende, ende.app (CC BY 4.0).
SFX: Kenney.nl (CC0). Built with the /brag skill (github.com/latent-spaces/brag).
Product UI, names and quotes are lynkk.ai's own illustrative data.
