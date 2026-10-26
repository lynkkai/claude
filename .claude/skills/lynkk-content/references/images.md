# Lynkk images (social posts, thumbnails, link previews, blog headers)

Same kit, same engine, one frame. Start from `templates/image-starter.html`.

## Sizes

| Use | Size |
|---|---|
| Feed portrait (Instagram, LinkedIn) | 1080x1350 |
| Square | 1080x1080 |
| Story / Reel cover | 1080x1920 |
| Link preview (Open Graph, X) | 1200x630 |
| Blog header | 1600x900 |
| Product Hunt gallery | 1270x760 |

Set the size in the template's `html,body,#stage` rule and pass the same numbers to `render.mjs still`.

## Recipe

1. One message per image, taken from the site's own lines (see `brand-kit.md`). Two-tone headline: claim in ink, payoff in muted.
2. Show the real product: capture UI from lynkk.ai with `scripts/capture_ui.mjs` (dpr 2) and frame it in the studio backdrop
   (`.studio` + `.realwin`). Swap only small illustrative text; never invent stats, quotes or logos.
3. Pick night or day per message: problem statements on night, product and outcomes on day or on the studio backdrop.
4. Accent sparingly: one violet pill tag, at most one live-red moment. Logo (mark + "Lynkk") in a corner or top-left.
5. Keep text big: headline 72-104px at 1080 wide; nothing important within 60px of the edges (feed crops, UI overlays).
6. Build and export:
   ```
   python3 <skill>/scripts/build.py post.src.html post.html
   node <skill>/scripts/render.mjs still post.html post.png 5 1080 1350
   ```
   Use `t=5` (any time after every `data-t`) so all elements are settled.
7. Look at the PNG before sharing: contrast, clipping, overlaps, spelling of Lynkk, no em dashes.

## Video thumbnails

The brag poster is the strongest settled frame of the video itself (`render.mjs still scene.html brag.jpg <t>`), baked in as frame 0
with `scripts/poster.sh`. Choose a frame where the hook and the headline are both fully in.
