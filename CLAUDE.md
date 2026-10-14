# Project memory

This repo supports marketing work for **Lynkk** (https://lynkk.ai), an AI meeting assistant.
Brand spelling is always "Lynkk" (double k), not Lynk, Linnk, or Link AI.

Full brand/product details and ready-to-use tool-submission copy: @memory/lynkk-brand.md

## Content creation guardrail (read before any design or video work)

All Lynkk content (posts, videos, thumbnails, scripts, captions, descriptions, blog copy) is
built with the **Lynkk post kit** in `lynkk-post-kit/` (the Lynkk design kit). Load the
`lynkk-design` skill (`.claude/skills/lynkk-design/`) before any design or video work. Never
build a new look, never take the style from another source (a homepage canvas, an artifact),
and never write a claim the kit doesn't back.

**`lynkk-post-kit/docs/TRUTHS.md` overrides `memory/lynkk-brand.md`.** Where they disagree,
TRUTHS.md wins: no voice answers in meetings, no CRM, manual Jira send, no regions or data
residency, no knowledge-graph screen, no phone app, no "notes in 30 seconds", no
"offline-first". Run `node lynkk-post-kit/scripts/check.mjs <file>` on every published file.
Videos are built with `youtube/videos/lynkk-vs-tools/build.sh` (kit boards, Kokoro `am_adam`
voice, original sitar track), one folder per video in `youtube/videos/NN-<slug>/`.

## Writing rules

These apply to all Lynkk copy, marketing text, and anything written in this repo.

- **Never use em dashes (—) or en dashes (–).** Use a comma, colon, parentheses, or
  split the sentence instead. Use a plain hyphen for ranges and compound words.
