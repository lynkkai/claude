---
name: lynkk-post-kit
description: Make Lynkk social media posts (Instagram/LinkedIn carousels, single images, stories, wide banners) in the lynkk.ai Grid design system, with the Inter font, brand mark, photo plates and platform logos. HTML slides rendered to PNG/PDF with Playwright. Use whenever the user asks for a Lynkk post, carousel, social graphic, slide, or anything visual that should match lynkk.ai's fonts and look.
---

# Lynkk post kit

The kit lives in `lynkk-post-kit/` at the repo root. All work happens there.

## Before anything else

Read `lynkk-post-kit/CLAUDE.md` and follow it exactly. It points to the docs to
read every time:

1. `lynkk-post-kit/docs/TRUTHS.md`: the only claims allowed on a post.
2. `lynkk-post-kit/docs/DESIGN.md`: visual rules (night band, two inks, plates, Inter 500/400 only).
3. `lynkk-post-kit/docs/COPY.md`: voice and copy rules.
4. `lynkk-post-kit/docs/BLOCKS.md`: the classes you build with.
5. Reference images: `lynkk-post-kit/posts/example-lynkk-vs-notetakers/out/*.png`
   and `lynkk-post-kit/gallery/out/*.png`.

## Workflow (run from `lynkk-post-kit/`)

```bash
npm run setup                                   # once: installs Playwright + Chromium
node scripts/new.mjs <kebab-name> --slides 5    # --size portrait|square|story|wide|linkedin
# edit posts/<name>/post.html and posts/<name>/captions.md
node scripts/render.mjs posts/<name> --pdf      # checks copy, renders, audits layout
```

In cloud sessions Chromium is preinstalled at `/opt/pw-browsers`, so skip
`npx playwright install` and only run `npm install`.

## Fonts and look

- Font is **Inter** only (`kit/fonts/InterVariable.woff2`, SIL OFL), weights
  500 and 400. No other fonts, no bold, no light.
- Only kit classes and `--gr-*` tokens. No hex colours, gradients, shadows or emoji.
- Never edit `kit/grid/*` (copied unchanged from the website).

## Hard rules

- No em dashes or en dashes anywhere (also a repo-wide rule in the root `CLAUDE.md`).
- No competitor names, prices, phone apps, accuracy percentages, or invented customers/quotes.
- Render and look at every PNG before saying a post is done.
