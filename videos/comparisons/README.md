# Lynkk comparison videos

Four videos for the Lynkk social accounts, plus their post copy in `social-posts.md`.

- `lynkk-vs-otter-short.mp4` and `lynkk-vs-granola-short.mp4`: 9:16, about 54 seconds
- `lynkk-vs-otter-long.mp4` and `lynkk-vs-granola-long.mp4`: 16:9, about 2:20 to 2:30

## What's in them

- **Hook first.** Each opens on a single line about the competitor's gap ("Otter understands 6 languages.
  Your team speaks Hinglish." / "Granola writes your notes. Then the recording is gone.").
- **Lynkk design kit.** These use the tokens from lynkk.ai: black #111 and white, the violet accent #7063BE
  with lavender #BEB4FB, Inter and Inter Display for type, JetBrains Mono for labels, the dot grid
  background, and the Lynkk sphere logo. The product cards are modeled on the UI shown on lynkk.ai.
- **Facts.** Every claim comes from lynkk.ai/compare/otter, lynkk.ai/compare/granola and the lynkk.ai
  FAQ and pricing, checked October 2026. Comparison scenes show a source line on screen.
- **Voice.** US English male voiceover ("Adam", Kokoro `am_adam`, picked by the team), with a little pace
  variation, natural pauses, warmth and light compression. Captions are burned in. Set `SARVAM_API_KEY`
  to switch to Sarvam AI's Indian voices (Bulbul v3, `en-IN`) instead.
- **Music.** Original sitar + tabla track (with tanpura drone, keys and bass), synthesized in
  `src/music_indian.py` with no samples and no licensing, ducked under the voice. `LYNKK_MUSIC=bansuri`,
  `lofi` or `synth` picks another style.

## Rebuild

```bash
cd videos/comparisons/src
./make_all.sh                                  # all four, Adam voice + sitar music, to videos/comparisons/*.mp4
./make_all.sh lynkk-vs-otter-short             # just one
LYNKK_VOICE=am_michael ./make_all.sh           # another Kokoro voice
SARVAM_API_KEY=... SARVAM_SPEAKER=shubh ./make_all.sh   # Sarvam AI Indian voice (key set in the environment)
```

Edit the scripts in `src/content.py` (`cap` is what viewers read, `say` is how the voice pronounces it,
for example "Link" for Lynkk). Edit the visuals in `src/stage/stage.html`. Sarvam audio is cached per line in the
build folder, so re-running after a visual change in the same session costs no extra credits.

## Status

- `lynkk-vs-*.mp4`: the four final videos with the Adam voiceover and sitar + tabla music.
- `captions-only/`: the same videos with captions and music but no voice, for sound-off feeds.
- `samples/`: the music and voice previews used to choose the above.
