# Lynkk SEO baseline (as of 2026-09-27)

Facts established during the 2026-09-27 audit. Update this file when new Search
Console exports land or when the site changes. Full report: `audit/lynkk-seo-audit-2026-09-27.md`

## Data on hand

`memory/data/gsc-ai-features-2026-09-27/` holds a Search Console export titled
**"Performance on Search > Generative AI Features"**, filters: Search type = Web,
Date = last 3 months (2026-06-25 to 2026-09-24).

This is the **AI Overviews / AI Mode subset only**, not total Search performance.
The export carries the Impressions metric only: no clicks, no CTR, no average
position, and no Queries.csv. Do not quote these as site-wide traffic numbers.

## What the export says

| Measure | Value |
|---|---|
| AI-surface impressions, 92 days | 105 |
| Days with zero impressions | 47 of 92 (51%) |
| Jul 2026 | 7 impressions, 26 of 31 days at zero |
| Aug 2026 | 39 impressions, 13 of 31 days at zero |
| Sep 2026 (to the 24th) | 59 impressions, 2 of 24 days at zero |
| Last 14 days vs prior 14 | 34 vs 34 (growth flattened in September) |
| Desktop / Mobile / Tablet | 71 / 32 / 2 (68% / 30% / 2%) |
| Countries | 34, led by India 37 (35%), Spain 7, UK 7, US 5 |

Page totals sum to 117 while device and country totals sum to 105. Expected
dimension-aggregation difference in Search Console, not a data error.

### Pages surfaced in AI features

| Impressions | URL |
|---|---|
| 72 | https://lynkk.ai/ |
| 10 | /features/hinglish-transcription |
| 10 | /features/meeting-bot |
| 6 | /terms |
| 4 | /features/knowledge-graph |
| 4 | /how-it-works |
| 3 | /features/action-items |
| 3 | /privacy |
| 2 | /refund |
| 1 | /download |
| 1 | /use-cases/sales-calls |
| 1 | /use-cases/team-standups |

## Site architecture inferred from those URLs

Confirmed to exist: `/`, `/how-it-works`, `/download`, `/terms`, `/privacy`,
`/refund`, `/features/{hinglish-transcription, meeting-bot, knowledge-graph,
action-items}`, `/use-cases/{sales-calls, team-standups}`.

Not observed in any export or SERP result: `/pricing`, `/blog`, `/about`,
`/integrations`, comparison or alternatives pages. Their absence is unconfirmed,
not proven: verify against the sitemap.

## SERP observations (2026-09-27, via search, not a crawl)

- Google returns two different titles for the homepage across queries:
  "Lynkk: AI Meeting Notes & Conversation Intelligence" and
  "Lynkk: Record any conversation. Get notes, tasks, and answers."
  Consistent with Google rewriting the title tag.
- The brand SERP for "Lynkk" is contested: LYNKK LTD (UK Companies House), a
  Nigerian crypto/bill-payment brand, Instagram @lynkkup, X @LynkkHQ, and two
  musicians all rank. lynkk.ai does not own its own brand query.
- Confirmed social handles: X @LynkkHQ, Instagram @lynkkup, a Facebook page.
  These belong in Organization schema `sameAs` and in `memory/lynkk-brand.md`
  (currently listed there as "to confirm"). Verify each is the AI company and
  not a namesake before using.
- lynkk.ai appears in **no** "best AI meeting assistant 2026" listicle, no
  Granola/Otter/Fireflies alternatives roundup, and no AI tool directory found.
- New product claims seen in SERP snippets, not yet in `memory/lynkk-brand.md`:
  conversations are never used to train anyone's model; automatic meeting
  detection with an offer to record; captures the room and remote participants
  at once; keeps running when the window is closed; can start when the Mac does.

## Environment constraint

Outbound HTTPS is blocked for every host in this Claude cloud environment
(egress proxy answers 403 to CONNECT), so no crawl, no Core Web Vitals, no
header inspection and no schema validation could be run on 2026-09-27. Allow
`lynkk.ai` in the environment's network settings to lift this. See
@memory/seo-toolkit.md.
