# Video 1: "Wait! What did we promise them?"

50-second vertical video (1080x1920, 30 fps) with background music, built on the lynkk.ai design kit.
Script: `../video-scripts-revenue-story.md` (Video 1).

- **Final video:** `lynkk-video-1-wait.mp4`
- **Look:** lynkk.ai tokens (night `#111` with dot grid and hairline frame, stone day sections, violet `#7063be` pill tags,
  two-tone Inter headlines, Schibsted Grotesk UI text, striped Lynkk mark, warm studio backdrop behind product shots).
- **Story:** 0-34s problem on night backgrounds, hard cut at 34s to the fix on day backgrounds, 45-50s end card styled like the lynkk.ai hero.
- **Music:** original, synthesized by `music.py` (no licensing needed). Tense minor-key pulse with a ticking clock for the problem,
  a riser into the cut, then a bright major-key groove for the fix. About -14 LUFS.
- **No voiceover yet.** All lines are on screen. A voiceover can be recorded over it using the script's "What we hear" column.

## Re-render

Needs Python 3 with numpy, Node with Playwright (Chromium), and ffmpeg.

```bash
python3 build.py                                   # inline the logo into scene.html
python3 music.py music.wav                         # background music
node render.mjs preview sheet.png 1 7 20 39 49     # optional: stills to check
node render.mjs video frames.mp4 30 50             # 1500 frames, a few minutes
ffmpeg -i frames.mp4 -i music.wav -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart lynkk-video-1-wait.mp4
```

Edit copy or timing in `scene.src.html`: each scene has `data-in`/`data-out` seconds and each element a `data-t` start time.
If you move the 34s cut, move `CUT` in `music.py` too.
