---
name: lynkk-design
description: Required for ANY Lynkk design or video work - social posts, carousels, thumbnails, YouTube motion graphics, overlays, end screens, video scripts, descriptions, captions, or any visual or copy that will be published for Lynkk. Uses the Lynkk post kit (Grid design system, product truths, copy rules, renderer and checker) in lynkk-post-kit/.
---

# Lynkk design and video guardrail

Everything Lynkk publishes (posts, thumbnails, video graphics, video scripts, descriptions,
captions) is built with the kit in `lynkk-post-kit/`. Never invent a new look, never draw in an
image tool, never write a claim the kit doesn't back.

## 1. Read first, every time

1. `lynkk-post-kit/docs/TRUTHS.md`: what the product really does. **Every claim must be in it.**
   It overrides `memory/lynkk-brand.md` and anything older in this repo.
2. `lynkk-post-kit/docs/DESIGN.md`: the Grid visual laws.
3. `lynkk-post-kit/docs/COPY.md`: voice and copy rules.
4. `lynkk-post-kit/docs/BLOCKS.md`: the classes to build with.
5. Look at `lynkk-post-kit/posts/example-lynkk-vs-notetakers/out/*.png` and
   `lynkk-post-kit/gallery/out/*.png`. Match that level.

Also follow `lynkk-post-kit/CLAUDE.md` (the kit's own workflow).

## 2. Hard rules (from the kit, they apply to video too)

- Claims only from TRUTHS.md. If a request needs a claim that isn't there, say so and ask.
  Common traps: Lynkk does **not** speak in meetings, has **no CRM** integration, **no region /
  data residency** setting, **no knowledge graph screen**, **no phone app**, Jira send is
  **manual**, no speed claims ("notes in 30 seconds"), no "offline-first", no audio file upload.
- No competitor names in anything published (titles, thumbnails, descriptions, scripts,
  captions). Say "a typical notetaker". Internal research docs may name them.
- No em or en dashes. No prices. No accuracy percentages. No invented customers or quotes.
  No exclamation marks, no filler words, no "not just X, but Y".
- Only kit classes and `--gr-*` tokens. Inter 400/500 only. No hex colours, gradients, shadows,
  emoji, green ticks or red crosses. Colour lives in the photo plates. Violet is a label.
- Mark Pro features "Pro". CTA: "Start free at lynkk.ai" / "Try it free at lynkk.ai".
- Product UI is drawn with the mock parts, faithful to TRUTHS.md, with neutral sample data
  (Acme renewal, Design review, Sam, Priya). Real platform logos only from `kit/assets/logos`.

## 3. Workflow

Posts: follow `lynkk-post-kit/CLAUDE.md` (`scripts/new.mjs`, edit, `scripts/render.mjs`).

Video (YouTube), per video `youtube/videos/NN-<slug>/`:

| Asset | How |
|---|---|
| Thumbnails 1280x720 | `<section class="post" data-size="wide">` in an HTML file, render with `node lynkk-post-kit/scripts/render.mjs <file> --scale 0.8` |
| Full-frame graphics 1920x1080 (explainers, end screen) | `data-size="wide"` sections captured at deviceScaleFactor 1.2. Animate only `opacity`/`transform` (and kit state classes like `.is-off`) from a `window.render(t)` function, then encode with ffmpeg |
| Overlays with alpha (lower thirds, notices) | Kit tokens and type on a transparent page, no ruled frame. Solid night surfaces (`--gr-black`, `--gr-coal`), eyebrow pill, two inks |
| Script, description, captions, Shorts | Markdown/SRT held to TRUTHS.md and COPY.md |

HTML files link the kit by relative path (`.../lynkk-post-kit/kit/post.css` and `post.js`).
Run `node lynkk-post-kit/scripts/check.mjs <file>` on every HTML, script, description and
caption file before calling it done. A PostToolUse hook (`.claude/settings.json` ->
`lynkk-post-kit/scripts/guard.mjs`) runs the same check automatically on files under
`youtube/videos/` and `lynkk-post-kit/posts/` and blocks on errors.

**Always render and look at every frame or PNG before saying it is done.**

## 4. Setup in a fresh environment

`cd lynkk-post-kit && npm run setup`. In a cloud container where Chromium is preinstalled,
skip the download and link the global Playwright instead:
`mkdir -p lynkk-post-kit/node_modules && ln -sfn "$(npm root -g)/playwright" lynkk-post-kit/node_modules/playwright`.
