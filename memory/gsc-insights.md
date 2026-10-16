# lynkk.ai: Google Search Console insights

> Source: GSC export "Performance on Search", web search, last 3 months (2026-07-14 to 2026-10-13),
> exported 2026-10-16. Raw CSVs: `data/gsc/2026-10-16/`.
> Full report (doc): https://claude.ai/code/artifact/160e95de-96ae-4eef-9764-7ad19263d989
> Notion copy (private, 6 sub-pages + page briefs + feature keyword update + 16 Oct Ubersuggest refresh): https://app.notion.com/p/3fac0e9b884d81cb87cff1fc55ab2743

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

## Site audit (crawl of 15 Oct 2026, `data/seo/2026-10-15/site-crawl.csv`)

- 64 sitemap URLs, all 200, self-canonical, indexable, unique titles/descriptions, 1 H1 each, llms.txt present.
- Structured data already sitewide (Organization, SoftwareApplication, FAQPage, BreadcrumbList, BlogPosting).
  Risk: homepage AggregateRating (5.0 from 16 reviews) with no visible reviews.
- Mobile LCP 7.3 s on the homepage (desktop 0.9 s). 89 images missing alt text on 31 pages.
- Backlinks: 4 from 3 domains, all nofollow, Ubersuggest DA 1. Biggest blocker.
- Thin pages: /features, /pricing, /integrations, /security, /demo (under 500 words).

## Ubersuggest refresh (16 Oct 2026, `data/seo/2026-10-16/`)

- Project id 9def5d40...cb3 (lynkk.ai), weekly updates. Site audit score 91 (was 89), 68 URLs crawled.
  Errors: low word count on /features (94 body words) and /demo (161); /sign-in and /sign-up noindex (expected).
  Warnings: short titles on /demo, /support, legal pages; "non SEO-friendly URL" on 5 short slugs (false positive).
- PageSpeed: mobile LCP 7.6 s (worse), desktop 0.95 s; 85 KB unused JS; http and www each 308 once to apex.
- Re-crawl: no 15 Oct fixes live yet; alt text missing on 91 images / 32 pages; AggregateRating and wrong Otter
  prices still live. New post /blog/zoom-note-taker (27th, 15 Oct US time) targets "zoom note taker" (880, KD 31);
  /integrations/zoom now takes "ai note taker for zoom" (480) + "zoom ai note taker" (390).
- AI visibility: Lynkk in 0 of 10 tracked ChatGPT prompts (all India). Fireflies 4, Avoma 3, Otter 3, Fathom 2;
  Vaarta and Stenoji win the Hindi/regional prompts. Prompt list: `data/seo/2026-10-16/ai-visibility.csv`.
- Rank tracker: 50 tracked keywords are mostly UK Teams recording and knowledge management terms; competitor list
  still has fathom.video. project_position_info and site_audit_pages API calls fail with a schema error.
- Competitor numbers unchanged (Sep 2026 latest); Fathom DA 46.

## Blog

- 26 posts published 2 to 15 Oct 2026 (27th, /blog/zoom-note-taker, late 15 Oct) (~2 a day, avg 2,520 words, author Samarth Wagh). They caused the
  October impressions spike: 50% of page impressions, 3 clicks.
- Best post: /blog/google-meet-transcript (736 impressions, pos 9.2, 0 clicks).

## Keyword strategy

- Full page-by-page map (primary + secondary keywords, US volume, KD, GSC position):
  `data/seo/2026-10-15/keyword-map.csv`.
- Home owns "ai note taker" (27,100 US/mo, KD 48). Five pillars: AI note taker; recording and transcription;
  templates and meeting productivity (largest, 39,400/mo, needs a /templates hub); voice to text and
  dictation; use cases, industries and languages.
- Easy wins: zoom meeting recorder (2,900, KD 17), legal transcription service (1,300, KD 15),
  board meeting minutes sample (2,400, KD 15), one on one meeting template (1,600, KD 19).
- Gaps: meeting minutes template (22,200), how to record zoom meeting (4,400), how to record google meet (2,400).
- Feature pages retargeted 16 Oct 2026 to higher-volume primaries (US/mo): meeting-notes "ai meeting notes taker"
  3,600; meeting-bot "meeting recorder" 1,900; dictation "speech to text mac" 1,600; chrome-extension "record google
  meet" 1,300; ask-your-meetings "ai knowledge base" 880; action-items "ai task manager" 480; hinglish "hindi
  transcription" (India 1,900). Workspaces and multilingual unchanged. New /languages pages for Telugu (India 2,400),
  Tamil (1,600), Marathi and Bengali (390 each); these languages are in beta. Candidates:
  `data/seo/2026-10-16/feature-keyword-candidates.csv`.
- Ubersuggest project rank tracker API call fails (schema error); use GSC positions instead.

## Competitors (15 Oct 2026, `data/seo/2026-10-15/competitors.csv`)

- Otter (DA 66, ~431k US organic visits/mo, 29.6k ref domains), Fathom (fathom.ai, DA 45, ~154k; moved from
  fathom.video in Aug to Sep 2025), Fireflies (DA 53, ~71k, down ~82% in two years). Lynkk: DA 1, 3 ref domains.
- Their traffic is mostly brand. Open generic terms: "ai powered meeting assistant" (40,500/mo, Otter pos 6,
  now the primary for /blog/ai-powered-meeting-assistants), "note taker" (14,800), "ai transcription" (5,400).
- Price: Lynkk Pro $15/mo ($9.75 yearly) vs Otter $16.99 ($8.49), Fireflies $18 ($10), Fathom $20 ($16).
- Lynkk wins on: in-person recording, Hinglish/Indian languages, 2-hour notes on Free, Ask across calls on a
  single-user plan, Jira. Loses on: no phone/Windows app, fewer languages than Fireflies/Fathom, no CRM sync.
- Lynkk's /compare/otter lists Otter yearly prices ($8.33, $19.99) that differ from otter.ai on 15 Oct 2026.

## Top opportunities

1. /blog/google-meet-transcript: 736 impressions, position 9.2, 0 clicks. Rewrite title and meta.
2. Top-5 pages with 0 clicks: /how-it-works, /use-cases, /compare/otter, /compare/fireflies, /compare/granola.
3. Answer pages for buyer prompts (SSO/SCIM, LLM providers and data residency, CRM sync, team pricing).
4. /features/hinglish-transcription: 7 clicks, "hinglish transcription" at position 8.6.
5. /pricing has only 3 impressions: make it indexable and linked.
6. Add Organization, SoftwareApplication and FAQPage structured data.
