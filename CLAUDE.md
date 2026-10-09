# Project memory

This repo supports marketing work for **Lynkk** (https://lynkk.ai), an AI meeting assistant.
Brand spelling is always "Lynkk" (double k), not Lynk, Linnk, or Link AI.

Full brand/product details and ready-to-use tool-submission copy: @memory/lynkk-brand.md

## Design and video guardrail (mandatory)

- **Any design or video for Lynkk** (posts, carousels, reels, thumbnails, motion graphics,
  overlays, video scripts, descriptions, captions) must use the **`lynkk-design` skill** and the
  kit in `lynkk-post-kit/`. No other look, no other tools. Read its docs before building.
- **Product truth:** `lynkk-post-kit/docs/TRUTHS.md` is the only source for product claims. It
  overrides `memory/lynkk-brand.md` wherever they disagree (checked against the product 2026-09-29).
- Videos: `node lynkk-post-kit/scripts/video.mjs posts/<name>` (see the dictation and reel posts).
- A hook runs the kit's copy check on files under `lynkk-post-kit/posts/` and blocks on errors.

## Writing rules

These apply to all Lynkk copy, marketing text, and anything written in this repo.

- **Never use em dashes (—) or en dashes (–).** Use a comma, colon, parentheses, or
  split the sentence instead. Use a plain hyphen for ranges and compound words.
