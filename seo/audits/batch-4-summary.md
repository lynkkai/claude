# Batch 4: the 5 missing posts (#11-#15), audit summary (2026-10-01)

These were the only posts from the 30-post plan not yet written. They were first drafted as competitor
reviews, then rewritten the same day as "best / top" listicles (Template A, 2,500+ words) on request.
Each ranks Lynkk #1 among 6-7 tools, targets the competitor's own searches plus its "alternatives"
keyword, and links to the matching lynkk.ai/compare page, so it supports that page rather than
competing with it. None are published.

| # | Article | Primary keyword (vol / SD) | Words | Audit |
|---|---|---|---|---|
| 11 | [Best Otter AI Note Taker Alternatives for 2026, Compared on Price, Limits and Follow-Up](../../articles/otter-ai-note-taker-alternatives.md) | otter ai note taker (5,400 / SD 57) | 2671 | 84 checks passed |
| 12 | [Best Granola AI Alternatives in 2026 for Teams Who Want Notes Written for Them](../../articles/granola-ai-alternatives.md) | granola ai (27,100 / SD 29) | 2552 | 85 checks passed |
| 13 | [Top Plaud Note AI Voice Recorder Alternatives in 2026, From Pocket to No-Device Apps](../../articles/plaud-note-ai-voice-recorder-alternatives.md) | plaud note ai voice recorder (8,100 / SD 34) | 2578 | 86 checks passed |
| 14 | [Best Fireflies AI Alternatives in the USA for 2026, Compared on Price and Follow-Up](../../articles/fireflies-ai-alternatives.md) | fireflies ai (27,100 / SD 59) | 2533 | 85 checks passed |
| 15 | [Top Fathom AI Alternatives for 2026 When Free Recordings Are Not Enough for Your Team](../../articles/fathom-ai-alternatives.md) | fathom ai (9,900 / SD 49) | 2550 | 86 checks passed |

All 5 pass `scripts/audit_article.py` (0 failed), `scripts/truths_check.py` (0 issues) and
`scripts/check_competitor_links.py`. Lynkk claims come only from `lynkk-post-kit/docs/TRUTHS.md`:
no Lynkk price is printed, no CRM, regions, speaking bot, knowledge graph, phone app or speed claims.
Every Lynkk entry has a "What could be better?" section (no phone app, no CRM, 2 hour cap).

## Needs your decision
- #13 overlaps #6 (Top AI Voice Recorders). Link them to each other at publish, or merge them.
- #13 has no /compare/plaud page to support it; it links to /download. Consider adding Plaud to /compare.
- Banners: not generated yet. Run `lynkk-post-kit/posts/blog-banners/build.py` for the 5 new slugs.
