# lynkk.ai: Google Search Console insights

> Source: GSC export "Performance on Search", web search, last 3 months (2026-07-14 to 2026-10-13),
> exported 2026-10-16. Raw CSVs: `data/gsc/2026-10-16/`.
> Full report (doc): https://claude.ai/code/artifact/160e95de-96ae-4eef-9764-7ad19263d989

## Baseline (3 months)

| Metric | Value |
|---|---|
| Clicks | 74 |
| Impressions | 4,477 |
| CTR | 1.65% |
| Avg. position (impression-weighted) | ~27 |
| Clicks by month | Jul (18 days) 5, Aug 19, Sep 34, Oct (13 days) 16 |
| Non-brand clicks (known queries) | 2 |

## Key facts

- Brand ("lynkk", "lynkk ai") = 42 of 74 clicks, avg position 2.4.
- Homepage = 55 of 74 clicks (13.4% CTR, position 5.5).
- Impressions jumped from ~23/day (Sep avg) to 1,058 on 2026-10-13; take-off on 2026-10-07. Cause not yet confirmed.
- US = 49% of impressions (2,177) at 0.09% CTR; India = 58% of clicks (43), 10.3% CTR.
- Desktop = 81% of impressions. No rich results (search appearance empty).
- Brand misspellings seen: linnnk, linnkk, liknkk, lknnk, lknkk, flynkk, meetlynk, linkkk, lynk.
- 74 long AI Mode style prompts (10+ words) rank at avg position ~6 with 0 clicks (SSO/SCIM, CRM sync,
  LLM data handling, pricing).

## Top opportunities

1. /blog/google-meet-transcript: 736 impressions, position 9.2, 0 clicks. Rewrite title and meta.
2. Top-5 pages with 0 clicks: /how-it-works, /use-cases, /compare/otter, /compare/fireflies, /compare/granola.
3. Answer pages for buyer prompts (SSO/SCIM, LLM providers and data residency, CRM sync, team pricing).
4. /features/hinglish-transcription: 7 clicks, "hinglish transcription" at position 8.6.
5. /pricing has only 3 impressions: make it indexable and linked.
6. Add Organization, SoftwareApplication and FAQPage structured data.
