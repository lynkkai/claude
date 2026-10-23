# Instagram Reel covers

Branded 1080x1920 cover images for @lynkk.ai Reels. Colors, fonts and the logo mark are taken from lynkk.ai.

- `out/*.png`: ready-to-upload covers, one per topic in `covers.json`
- `out/contact-sheet.jpg`: all covers side by side
- `covers.json`: the text on each cover. Wrap words in `*stars*` to color them with the accent.
  Accents: `violet`, `lavender`, `pink`, `orange`, `leaf`. Set `"live": true` for a red live dot.
- `template.html`: the layout
- `render.mjs`: renders the PNGs

## Make or change a cover

1. Add or edit an entry in `covers.json` (match it to the Reel's topic).
2. Run `node render.mjs` (or `node render.mjs <id>` for one cover).
3. Run `node render.mjs --guides <id>` to check the text sits inside Instagram's crops
   (cyan = 3:4 profile grid, yellow = 4:5 feed).

All text stays inside the 3:4 crop, so nothing gets cut off on the profile grid.

## Setting a cover on an existing Reel

Instagram app: open the Reel, tap `...` > Edit > Edit cover > Add from camera roll, pick the PNG, Save.
