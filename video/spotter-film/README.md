# Spotter, 32 s: the film

The Lynkk launch film for https://lynkk.ai/features/spotter, hosted by Remi. One Remotion
timeline, two formats: a 1080x1920 reel and a 1080x1350 feed post.

- `SCRIPT.md` is the film on the bar grid, with the truth check for every claim on screen.
  Read it first; the timeline is typed from it.
- `src/timing.ts` is the clock. 120 BPM at 30 fps: beat 15 frames, bar 60 frames, 16 bars.
  Every slam, press and cut is a frame in `T`, and `CUES` is the sound the picture asks for.
  Scenes never hold a frame number of their own.
- `src/scenes/` is one file per act: Hook (the keyboard and the press), Ask, Screen, Listen,
  Open, Recap, EndCard.
- `src/mac/` is the drawn Mac: `Keyboard.tsx` and `SpotterMore.tsx` were written for this
  film, the rest comes with the kit.

## Rebuilding it

This folder is the film's own source. It runs inside the Remi video kit, which holds the
engine, the sound skills and the truth files:

```bash
cp -r video/spotter-film <kit>/films/spotter
```

```bash
cd <kit>/films/spotter && npm ci && npx remotion render src/index.tsx Reel out/picture-reel.mp4 --codec h264 --crf 16 --muted
```

Two things this container needed that a Mac will not:

- Inter is served from the film's own `public/fonts` (four .ttf weights, loaded in
  `src/lib.ts`), because the render browser here had no network of its own and could not
  reach Google Fonts. On a machine that can, the kit's `@remotion/google-fonts` loader works
  as it did.
- Renders ran at `--concurrency 4` and took about four and a half minutes per format.

## House rules this film follows

- Every claim on screen is in the kit's `docs/TRUTHS.md` or `docs/TRUTHS-web.md`. The truth
  check under the script's table says which line backs which title.
- No em dashes anywhere a viewer reads. `node scripts/check-copy.mjs` fails the build on one.
- Spotter does not know your past meetings, so the answer it gives in the film comes from the
  pilot plan that is open on screen while it answers.
- No prices, no version numbers, no competitor names, no invented customers.
