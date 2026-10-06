# Content profile: Lynkk Medium articles

Read by the `create-medium-article` skill (`.claude/skills/create-medium-article/`).
Explicit user instructions override anything here.

## Brand

- Product: **Lynkk** (double "k"), https://lynkk.ai. Never Lynk, Linnk, or Link AI.
- Authoritative product facts: `memory/lynkk-brand.md`. Use only facts listed there.
  Anything under "To confirm" in that file (pricing, CRMs, meeting platforms,
  languages, data regions, certifications) must not appear in an article until the
  team fills it in.
- Topic backlog and keyword data: `content/medium/topic-research.md`.

## Audience

Professionals who live in back-to-back meetings: sales and customer-facing teams,
product and engineering leads, founders, managers, and consultants. Some work in
regulated industries or multilingual teams. They read Medium for practical advice,
not product pitches.

## Voice

- Informed, direct, conversational. Write like a practitioner, not a vendor.
- Teach first. The article must be useful to someone who never signs up for Lynkk.
- Mention Lynkk at most two or three times, where it is a natural example of the
  idea being discussed, plus the closing CTA.
- Never disparage competitors. Name them only for verifiable, sourced facts.
- Do not invent customer stories, quotes, metrics, or results. Third-party
  statistics need a link to the original source; vendor blog stats should be traced
  to their primary source or left out.
- Legal and compliance topics: describe what is alleged or required, cite the
  source, and add that this is not legal advice. Do not claim Lynkk is compliant
  with any specific law or certification unless `memory/lynkk-brand.md` confirms it.

## Writing rules (from CLAUDE.md, mandatory)

- **No em dashes or en dashes anywhere** (title, deck, body, captions, alt text).
  Use a comma, colon, parentheses, or two sentences. Plain hyphens for ranges and
  compound words.
- Spell the brand "Lynkk" every time.

## Output

```text
content/medium/<article-slug>/
|-- article.md
`-- hero-<article-slug>.png   optional
```

`article.md` starts with frontmatter:

```yaml
---
title: ""
subtitle: ""
slug: ""
target_keyword: ""
status: draft        # draft | ready-for-review | published
medium_tags: []      # up to 5 Medium tags
canonical_url: ""    # set if the piece is also on lynkk.ai
---
```

## Links and CTA

- Close with one short CTA line linking to https://lynkk.ai ("Lynkk is free to
  start" is fine; do not quote prices).
- Link to specific pages over homepages when citing sources.

## Images

Hero image optional. Wide (about 1400x788), no embedded text, no third-party logos.
Always provide alt text and a one-line caption.

## Validation before marking ready-for-review

1. Search the article for em and en dashes; there must be none.
2. Search for misspellings of the brand (Lynk, Linnk, Link AI).
3. Every statistic and legal claim has a source link.
4. No item from the "To confirm" list in `memory/lynkk-brand.md` is stated as fact.

## Notes

- The final language pass uses the `humanizer` skill (`.claude/skills/humanizer/`)
  in `written-prose` mode. Its checker can be run on its own:
  `python3 -I .claude/skills/humanizer/scripts/check_prose.py <article.md>`.
- Drafting never authorizes publishing to Medium. Publish only on explicit request.
