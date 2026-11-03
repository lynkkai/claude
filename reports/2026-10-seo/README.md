# Lynkk SEO report, October 2026

Live report: https://claude.ai/artifact/NcijU7n5SobPmpW4YewzNe

Covers 1 to 31 October 2026, web (text-based) search, property `https://lynkk.ai/`.

## Headline numbers

| Metric | October 2026 |
|---|---|
| Clicks | 99 |
| Impressions | 26,771 |
| Click-through rate | 0.37% |
| Average position (impression-weighted) | 21.7 |
| Ranking queries | 1,000 (Search Console export cap) |
| Pages with impressions | 114 (85 took no click) |
| Domain authority | 1 |
| Referring domains | 5 (9 backlinks, 0 follow) |
| Site health score | 93 / 100 |

## The short version

Impressions grew roughly sixfold across the month, from 47 per day in week 1 to
1,683 per day in week 5. Clicks did not follow. The cause is position, not
demand: 55.7% of ranking keywords sit past position 20, and the pages that do
rank well are informational, so they collect impressions without collecting the
click. Brand queries ("lynkk") took 21 of the 30 clicks the query table
accounts for, on 1.3% of its impressions.

Three things stand out beyond the headline:

1. **120 conversational queries** of ten words or more averaged position 7.8 and
   returned zero clicks. These are AI Mode and AI Overview style prompts asking
   about SSO and SCIM, transcript retention, which third-party models see call
   data, volume discounts and source-linked meeting search. Lynkk is being cited
   inside answers without being visited.
2. **Mobile performance is bad.** LCP 4.7s and time to interactive 10.1s against
   a 2.5s good threshold for LCP. Mobile is also where click-through rate is
   highest (0.46% against desktop's 0.35%), so this costs real clicks.
3. **Authority is the ceiling.** Five referring domains and no follow links
   explain the deep average position better than any content gap.

## Priorities for November

1. Rewrite titles and intros for the 28 striking-distance queries (position 4 to
   20, 20+ impressions, zero clicks, 1,160 impressions in total).
2. Fix mobile performance: 202 KB unused JavaScript, 528 ms server response,
   630 ms of redirects.
3. Start link acquisition. Target 20 to 30 referring domains by the end of Q1.
4. Build out conversational and AI-surface answers as short factual pages.
5. Push the commercial pages. Comparison, use-case and integration pages took
   one click between them on 672 impressions.
6. Concentrate on Google Meet and Zoom clusters; park generic voice-to-text.
7. Clear the small crawl issues: 4 thin pages, 6 short titles, 1 page blocked by
   a meta robots tag, 1 temporary redirect, 5 unfriendly URLs.

## Files

| File | What it is |
|---|---|
| `data/daily.csv` | Clicks, impressions, CTR and position for each day of October |
| `data/queries.csv` | All 1,000 ranking queries, tagged with topic cluster and query type |
| `data/pages.csv` | All 114 pages with impressions, tagged with site section |
| `data/countries.csv` | 181 countries |
| `data/devices.csv` | Desktop, mobile, tablet |
| `data/keywords.csv` | 12 priority keywords with Ubersuggest volume, difficulty and CPC |
| `data/audit.csv` | Ubersuggest site audit issues |
| `data/speed.csv` | Core Web Vitals, desktop against mobile |
| `data/authority.csv` | Domain authority, backlinks, referring domains, health score |
| `build-datasets.py` | Turns the raw Search Console export into the files above |
| `dashboard-page.html` | The page published to the live report |

## Sources and caveats

- Search Console: export of 3 November 2026, web search only.
- Ubersuggest: pulled 3 November 2026, United States location, via the
  Ubersuggest MCP tools.
- **No month-on-month comparison.** September was not exported, so every
  trend here is within October.
- **No conversion data.** There is no analytics export, so clicks are the
  furthest down the funnel this report reaches.
- Search Console caps the query export at 1,000 rows, so query-table totals
  (30 clicks, 10,534 impressions) are a floor and do not match the site
  totals. Query, page, country and device tables each carry Google's own
  anonymisation, so their sums differ slightly from the daily totals.
- Topic clusters and query types are keyword-match classifications applied in
  `build-datasets.py`, not Google's own groupings.
- "Clicks at top three" in the keyword table assumes an 11% click-through rate,
  a rule of thumb, not a measurement.
