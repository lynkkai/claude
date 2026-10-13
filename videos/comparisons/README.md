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
- **Voice.** Indian English from Sarvam AI (Bulbul v3, `en-IN`), one request per line, with a little pace
  variation, natural pauses, warmth and light compression so it sits like a mic read. Captions are burned
  in. Without a Sarvam key the pipeline falls back to offline Kokoro, which sounds robotic and is only
  useful for checking timing.
- **Music.** An original track synthesized in `src/music.py`, with no samples and no licensing, ducked
  under the voice.

## Rebuild

1. Add a Sarvam AI API key to the cloud environment as `SARVAM_API_KEY` (environment menu in the session
   title bar, then Edit). A new session picks it up.
2. Run:

```bash
cd videos/comparisons/src
./make_all.sh                          # all four videos, written to videos/comparisons/*.mp4
./make_all.sh lynkk-vs-otter-short     # just one
SARVAM_SPEAKER=shubh ./make_all.sh     # another Bulbul v3 voice (e.g. shubh, ritu, neha, kavya, rahul)
```

Edit the scripts in `src/content.py` (`cap` is what viewers read, `say` is how the voice pronounces it,
for example "Link" for Lynkk). Edit the visuals in `src/stage/stage.html`. Sarvam audio is cached per line in the
build folder, so re-running after a visual change in the same session costs no extra credits.

## Status

- `captions-only/`: all four videos with captions and background music, no narration. Ready to post on
  feeds where most people watch with the sound off.
- Narrated versions: the first cut used the offline Kokoro voice and was rejected as robotic, so it was
  removed. To make them, add `SARVAM_API_KEY` and run `./make_all.sh` in a new session.
