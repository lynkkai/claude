# Batch 4: the 5 missing posts (#11-#15), audit summary (2026-10-01)

These were the only posts from the 30-post plan not yet written. They had been on hold because
lynkk.ai already has /compare/otter, /compare/granola, /compare/fireflies and /compare/fathom.
To avoid competing with those pages, each post targets the competitor's own review, pricing or
alternatives searches (the keyword-map-v2 primaries) instead of a "Lynkk vs X" title, follows
Template B, and links to the matching compare page. None are published.

| # | Article | Primary keyword (vol / SD) | Words | Audit |
|---|---|---|---|---|
| 11 | [Otter AI Note Taker Review: Pricing, Limits and How Lynkk Compares for Busy Teams](../../articles/otter-ai-note-taker-review.md) | otter ai note taker (5,400 / 57) | 2219 | 74 checks passed |
| 12 | [Granola AI Review: How the Bot-Free Notepad Works and When Lynkk Fits Better](../../articles/granola-ai-review.md) | granola ai (27,100 / 29) | 1904 | 69 checks passed |
| 13 | [Plaud Note AI Voice Recorder vs Pocket vs Lynkk: Do You Need a Device?](../../articles/plaud-note-ai-voice-recorder-vs-pocket.md) | plaud note ai voice recorder (8,100 / 34) | 1828 | 69 checks passed |
| 14 | [Fireflies AI Pricing, Features and Limits Explained, Plus How Lynkk Compares for Your Team](../../articles/fireflies-ai-pricing.md) | fireflies ai (27,100 / 59) | 1864 | 73 checks passed |
| 15 | [Fathom AI Review: A Free Note Taker or a Full Meeting Assistant Like Lynkk?](../../articles/fathom-ai-review.md) | fathom ai (9,900 / 49) | 1876 | 70 checks passed |

All 5 pass `scripts/audit_article.py` (0 failed), `scripts/truths_check.py` (0 issues) and
`scripts/check_competitor_links.py`. Lynkk claims come only from `lynkk-post-kit/docs/TRUTHS.md`:
no Lynkk price is printed, no CRM, regions, speaking bot, knowledge graph, phone app or speed claims.
Each post includes a "Where X is stronger" section (phone apps, CRM sync, more languages, Windows).

## Needs your decision
- The titles differ from the plan's "Lynkk vs X" titles on purpose (cannibalization). If you would
  rather keep "Lynkk vs X", fold these into the /compare pages instead of publishing them as posts.
- #13 has no /compare/plaud page to support it; it links to /download. Consider adding Plaud to /compare.
- Banners: not generated yet. Run `lynkk-post-kit/posts/blog-banners/build.py` for the 5 new slugs.
