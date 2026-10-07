# Video 4 assets: How Sales Teams Update Their CRM Automatically After Every Call

Graphics package for the editor. Script and production decisions: `../04-sales-crm-auto-update.md`.

These are the parts of the video that **don't** need the real product. The screen recordings
(Lynkk, the Zoom call, HubSpot, Calendly, Jira) still need to be filmed in the demo workspace
described in the script. Everything here goes on top of, or between, that footage.

## What's in `out/`

| File | Type | Use in the edit |
|---|---|---|
| `thumbnails/thumbnail-1.png` | 1280x720 | Main thumbnail: "CRM updated. 0 typing." before/after cards |
| `thumbnails/thumbnail-2.png` | 1280x720 | A/B test: "Call ends. CRM done." with 0:30 timer |
| `thumbnails/thumbnail-3.png` | 1280x720 | A/B test: "One AI. Whole call." before/during/after |
| `motion/stopwatch-overlay.mov` | 4.5 s, alpha | Scene 1 (0:00) and Scene 6 (3:40): counts 0:00 to 0:30, top right |
| `motion/chores-problem.mp4` | 8 s, full frame | Scene 2 (0:12): the four after-call chores |
| `motion/lifecycle-explainer.mp4` | 14 s, full frame | Scene 3 (0:35), reuse in Scene 9 (6:25): before / during / after, each card spotlighted in turn |
| `motion/lowerthird-before.mov` | 5 s, alpha | Scene 4 (0:50) |
| `motion/lowerthird-during.mov` | 5 s, alpha | Scene 5 (1:55) |
| `motion/lowerthird-after.mov` | 5 s, alpha | Scene 6 (3:40) |
| `motion/lowerthird-search.mov` | 5 s, alpha | Scene 7 (5:20) |
| `motion/voice-caption-pilot.mov` | 7 s, alpha | Scene 5: on-screen caption while Lynkk answers the pilot question (waveform animates while it "speaks") |
| `motion/voice-caption-security.mov` | 3.5 s, alpha | Scene 5: caption when Lynkk pulls up the security overview |
| `motion/endscreen.mp4` | 20 s, full frame | Last 20 s. Outlined slots line up with YouTube end-screen elements (video left, subscribe right) |
| `overlays/notice-fictional-demo.png` | 1920x1080, alpha | Scene 3, bottom left: "Demo uses a fictional company and data" |
| `overlays/notice-recording-consent.png` | 1920x1080, alpha | Scene 5 and Scene 8: recording consent reminder |
| `voiceover-script.txt` | text | Brand host's read, scene by scene (actor and Lynkk lines are recorded in the call scene) |
| `captions-draft.srt` | captions | Draft captions spaced by the script's scene timings. Re-time after the final edit, or upload the transcript to YouTube Studio and let it auto-sync |

All video is 1920x1080, 30 fps. `.mov` files use the PNG codec with an alpha channel, which
Premiere Pro, Final Cut Pro, and DaVinci Resolve import directly as transparent overlays.

## Brand colors and logo

The palette and the "Lynkk" wordmark are **placeholders** (Lynkk's official logo files and colors are
still on the to-confirm list in `memory/lynkk-brand.md`). To swap them:

1. Edit the color tokens at the top of `src/theme.css`.
2. Replace the `.wordmark` text with the logo image in `src/thumb.html`, `src/lifecycle.html`, and `src/endscreen.html`.
3. Re-render (below).

## Re-rendering

Needs Node with Playwright (Chromium) and ffmpeg. From `src/`:

```bash
# stills: page, output, width, height, transparent (1/0)
node still.mjs "thumb.html?v=1" ../out/thumbnails/thumbnail-1.png 1280 720 0

# animations: page, frames dir, seconds; then encode
node capture.mjs lifecycle.html /tmp/frames/lc 14
ffmpeg -framerate 30 -i /tmp/frames/lc/f%04d.png -c:v libx264 -pix_fmt yuv420p -crf 16 ../out/motion/lifecycle-explainer.mp4
# alpha overlays: -c:v png -pix_fmt rgba out.mov
```

Each animated page exposes `window.render(t)`, so frames are rendered one at a time and come out
identical on every run. Page variants use a query string: `lowerthird.html?i=0..3`, `voice.html?i=0..1`,
`notice.html?i=0..1`, `thumb.html?v=1..3`.
