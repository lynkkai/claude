# Delivery

## What to ship

Ask what it is for, then deliver what the destination needs rather than one master and a
shrug.

| Destination | Aspect | Size | Notes |
|---|---|---|---|
| Site hero, autoplay | 16:9 | 1920x1080 | Muted and looping, so no voiceover reliance and no abrupt last frame |
| YouTube, Vimeo | 16:9 | 1920x1080 or 3840x2160 | Full mix |
| Stories, Shorts, Reels, TikTok | 9:16 | 1080x1920 | Keep type clear of the bottom 15% UI overlay |
| Feed posts | 1:1 or 4:5 | 1080x1080, 1080x1350 | Most views are muted, so burn in captions |
| Product Hunt, launch posts | 16:9 | 1920x1080 | Under 30 seconds reads best |
| GIF or looping preview | matches use | 800 px wide | Short loop, no text that needs sound |

## Reframe, do not crop

Render each aspect from the timeline with its own layout. A 9:16 cut of a 16:9 master
loses the composition and usually the logo. The timeline already knows `window.WIDTH` and
`window.HEIGHT`, so branch layout on aspect ratio and re-render:

```bash
node .claude/skills/motion-graphics-video/scripts/render.mjs \
  --html out/index.html --out out/film-9x16.mp4 --width 1080 --height 1920 --audio out/mix.wav
```

## Encode settings

```bash
# web delivery, high quality, broadly compatible
ffmpeg -i frames/%06d.png -framerate 30 -i mix.wav \
  -c:v libx264 -profile:v high -crf 18 -pix_fmt yuv420p -movflags +faststart \
  -c:a aac -b:a 192k -shortest out/film.mp4

# smaller hero loop, silent
ffmpeg -i out/film.mp4 -an -c:v libx264 -crf 24 -vf scale=1280:-2 -movflags +faststart \
  out/film-hero.mp4

# webm companion for hero video
ffmpeg -i out/film.mp4 -an -c:v libvpx-vp9 -crf 34 -b:v 0 out/film-hero.webm
```

`-pix_fmt yuv420p` matters: without it, some players and most social uploads reject or
mangle the file. `+faststart` lets the browser begin playing before the whole file lands.

## Captions

Anything that plays muted needs burned-in captions, and burned in means styled to the
brand rather than default white boxes. Write the text as timed cards in the timeline so
they inherit the brand font, or burn an ASS subtitle file with brand styling:

```bash
ffmpeg -i out/film.mp4 -vf "ass=out/captions.ass" -c:a copy out/film-captioned.mp4
```

Also ship an `.srt` next to the master for platforms that take one, since real captions
beat burned-in text for accessibility.

## Handover

Tell the user, briefly:

- which route and tools produced it
- where the files are, with full paths
- what the critique scores ended at
- anything substituted: missing fonts, stale screenshots, placeholder claims
- what one more round would improve
