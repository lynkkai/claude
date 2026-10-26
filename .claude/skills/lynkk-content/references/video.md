# Lynkk video workflow

Proven on `launch/video-1/` and `launch/video-2/brag-output/`. Pair it with the `brag-slim` skill for the creative rules
(hook, show the real thing, readable holds, cuts on beats, sound as one piece, poster frame, share copy).

## 0. Folder

```
launch/<video-name>/
  scene.src.html      # from templates/scene-starter.html
  lines.json          # voiceover lines [[start, latest_end, "text"], ...]
  music.py            # from scripts/music_example.py, re-arranged
  brag-output/        # brag-plan.md, brag.mp4, brag.jpg, share-copy.txt (+ work/ for captures, frames, stems; gitignored)
```
The scripts find Playwright in the current folder or the global npm install.

## 1. Plan (write `brag-output/brag-plan.md`)

- Answer the brag rubric (what, who, what sets it apart, hook, real UI, tone, caption).
- Pick the tempo first. **120 BPM makes every whole second a beat**, so put scene cuts on whole seconds.
  Snap animation events to the 1/16 grid (0.125s) or 8ths (0.25s).
- Storyboard table: time, scene, on-screen text, voiceover. Check reading time: each line must stay settled on screen
  for about 0.3s per word (a caption settles 0.5s after its `data-t`).
- Problem act on night backgrounds, fix act on day backgrounds (relief), end card in the lynkk.ai hero style.

## 2. Real UI first

Capture the product from lynkk.ai instead of mocking it (`scripts/capture_ui.mjs`, job examples in `brand-kit.md`):
- `dpr: 2` for crisp text. Crop tightly for vertical video so UI text lands at 28px+ on the 1080px frame.
- `replace` swaps small illustrative text (e.g. a Budget row) so the product shows what your script says. Never invent product claims.
- `sequence` steps the page clock frame by frame (virtual time), so typing and loaders animate smoothly.
  Play it in a `<canvas data-seq="start,end,count,path/f%04d.png">`; the engine preloads and draws frames deterministically.
- Animate stills with masks (`data-fx="out"` on white bands that reveal rows), a violet ring, and a toast.

## 3. Scene engine (`templates/scene-starter.html`)

- `<section class="scene night|day" data-in data-out>` per scene; hard cuts on beats.
- Any element with `class="anim" data-t="<s>" data-fx="fade|up|left|pop|drop|spin|slam|out|none"`;
  optional `data-until` (fade out), `data-dim="a,b"` (dim from a, restore at b), `data-rot`.
- Helpers: `data-type` + `data-cps` (typing), `data-blink`, `data-rec` (REC timer), `data-talk="a,b"` (speaking ring),
  `data-dots`, `data-pulse`, `data-check`, `data-press` (+ `data-sent`), `data-draw="start,dur"` (SVG line draw),
  `data-hot` (row highlight), `canvas[data-seq]` (captured frame sequence).
- `.cam` gets a slow 3% push within each scene. `.cap` is the two-tone headline (`<span class="m">` = muted line).
- `%%LOGO%%` is replaced by the logo SVG at build time.

Build and look before rendering:
```
python3 <skill>/scripts/build.py scene.src.html scene.html
node <skill>/scripts/render.mjs preview scene.html sheet.png 0.4 1.1 6 12 ...   # every scene + mid-animation
```
Fix overflow, collisions, low contrast, toasts covering content, text that is too small. Then:
```
node <skill>/scripts/render.mjs video scene.html brag-output/work/frames.mp4 30 50
```
1500 frames take about 10 minutes. Run it in the background and wait for the notification.
Do not wait with `pgrep -f "render.mjs"` inside a command that itself contains that text: it matches itself and never ends.

## 4. Music and sound effects (`scripts/music_example.py`)

Pure numpy synthesis, no licensing. Write music and SFX as one piece:
- Act 1 minor key (tense: ticking clock on quarters, bass on 8ths, heartbeat kick, hits on bad news, riser, a 1/16 silence before the cut).
- Act 2 relative major (I-V-vi-IV, plucks on 8ths, four-on-the-floor), sparkle on the end card.
- SFX on the same grid and in key: whoosh that ends exactly on each cut, pitched pops on pills/toasts/checks
  (minor pentatonic in act 1, major in act 2), quiet 1/16 clicks while text types, pings tuned to the key.
  They go through one short "room" so they blend in, and sit well under the music.
- Master to about -14 LUFS. Check the waveform image (`showwavespic`) since you cannot listen.

## 5. Voiceover (`scripts/voiceover.py` + `lines.json`)

- Kokoro TTS, offline. `af_heart` (female, default) and `am_fenrir` (male) both transcribe cleanly; `am_michael` merged words in testing.
- Start each line a beat after its scene starts; give it until just before the next cut. The script speeds up a line only if needed;
  anything over 1.15x sounds rushed, so shorten the text instead.
- Write "Link" for Lynkk. Avoid soft contractions that blur ("you've forgotten" came out as "you forgot"; "you've forgotten all about it" was clear).

## 6. Mix, verify, deliver

```
<skill>/scripts/mix.sh brag-output/work/frames.mp4 music.wav brag-output/work/mix.mp4 vo.wav
python3 <skill>/scripts/verify_speech.py brag-output/work/mix.mp4 lines.json     # must be ~1.0 word match
node <skill>/scripts/render.mjs still scene.html brag-output/brag.jpg <poster t>   # strongest settled frame
<skill>/scripts/poster.sh brag-output/work/mix.mp4 brag-output/brag.jpg brag-output/brag.mp4
```
Write `brag-output/share-copy.txt`: 1-3 sentences, postable as is, no "excited to share", no em dashes.
Deliver the MP4 (and a male-voice cut if asked) and keep a music-only cut for a future human voiceover.
Commit sources and finals; keep `work/` (captures, frames, stems) out of git.
