---
name: content-research-strategy
description: "The canonical end-to-end Content Research & Strategy SOP (v1.1) for every Unveilr client \u2014 how we pick which pages need content, run the SEO keyword track and the AEO mention-scan track, find the real gap, gate topics with the Article Scoring Matrix, and build the article (headings, paragraph and section limits, tables, FAQ caps, per-client word counts, link caps, inbound links). Includes the article body blueprint by position, one fully worked example from page to outline, and a glossary. Read before any research, briefing or writing task; per-client contracts inside it override generic defaults."
---

<!-- Pulled from the Unveilr platform registry (scope=global, version=1) on 27 Aug 2026. -->

# Unveilr Content Research & Strategy SOP

**Version 1.1 — 31 July 2026**
**Owner:** Pranjal Rai
**Audience:** every content, SEO and AEO team member. Read this fully before you research, brief, or write a single article.

---

## 0. What this document is

This is the end-to-end record of how we decide **what to write, why, and in what shape** — before any writing happens. It covers:

1. How we pick the **pages** that deserve content support.
2. How we run **keyword research** (SEO track) and **AI mention scans** (AEO track).
3. How we find the **real gap** rather than a topic that already exists.
4. How we **gate** a topic before spending writing budget on it.
5. The **construction rules** every article obeys (headings, paragraph length, links, tables, FAQs, word counts).
6. The **scoring gates** that stand between a draft and publication.

Two things to internalise before anything else:

**Rule A — We research the live web, never our memory.** Every volume, rank, SERP composition, AI citation, and fee comes from a tool call against a live source. If a call fails, we write "no data" and score that factor conservatively. We never estimate a number and present it as measured.

**Rule B — SEO and AEO are separate channels with separate economics.** They are decoupled, and our own backtest proved it: our Vakilsearch comparison articles earned 7 AI citations and close to zero search clicks, while our Udyam how-to articles earned 190 clicks and zero citations. An article that wins one channel does not automatically win the other. Decide the channel up front, then research for that channel.

---

## 1. The five layers of the system

Everything below sits inside a five-layer ecosystem. Know which layer you are in at all times.

| Layer | Name | What it decides | Instrument |
|---|---|---|---|
| **L1** | SELECT | Which topics deserve budget | Article Scoring Matrix v1.1 via `/topic-score` (threshold 70) |
| **L2** | CRAFT | How the article is built | Page Optimization Checklist Part A + client writing skills |
| **L3** | GATE | Whether it may ship | `/aeo-score` (≥80), `/seo-score` (≥85 + ranking gates), auto-fail list |
| **L4** | OPS | Publishing SLAs, cadence, inbound links, prompt registration | Push skills + calendar |
| **L5** | LEARN | Re-weighting the matrix from real outcomes | Fortnightly retro at day 21+ |

**The locked pipeline order (do not rearrange):**

```
topic list
  → /topic-score            (L1 — kill / rework / write)
  → /seo-research  or  /aeo-research   (brief enrichment)
  → /seo-article   or  /aeo-article-<client>   (write)
  → /seo-score (≥85 + gates)  and/or  /aeo-score (≥80)
  → /humanize-<client>
  → /post-humanize-check
  → re-score (must hold)
  → banner generation
  → /push-to-<client>       (requires explicit client approval)
  → inbound internal links + prompt registration
  → measure at day 21+
```

Skipping or reordering a step is how we produce mixed humanized and AI-native content, and it costs hours of rework. There are no exceptions.

### ⛔ THE FREEZE-ORDER RULE — gate once, never twice (binding, all clients)

**Finish every prose-changing edit BEFORE any gate runs.** A gate scores the text in front of it;
the moment prose changes afterwards, that score is stale and the gate must run again. This is the
single largest avoidable cost in a wave.

**Measured, Aviaan valuation wave, 4-5 Sep 2026:** 2h 52m of active time, of which **~35m (20%)
was gates re-run on text that had changed since the last run.** Gate A ran twice because the SEO
pass rewrote H2s and split sentences after the first score. `/final-check-<client>` ran twice
because links were repointed after the first pass. At 10 articles the same pattern costs **~1 hour**.

**The order that carries no rework:**

| # | Do | Prose may change? |
|---|---|---|
| 1 | Write · place `selected_keywords` in body · set meta_title/description · generate banner · set `featured_image_path` | ✅ yes — this is the only window |
| 2 | **FREEZE** | — |
| 3 | Gate A: `/aeo-score-<client>` **and** `/seo-score` in ONE pass | only gate-mandated fixes, then re-gate |
| 4 | `/humanize-<client>` → `/post-humanize-check` → `/humanize-verify` | body prose only, freeze list enforced |
| 5 | `/final-check-<client>` → build DOCX | none |

**The trap is step 1.** Keyword placement, meta rewrites and image wiring feel like finishing
touches and get done *after* the first score. They are prose changes and they belong before the
freeze. If a gate sends work back, fix and re-gate that article — do not carry an edit forward
into the next stage unscored.

**Three corollaries, each of which cost real time on the wave above:**

1. **Verify `selected_keywords` appear in the body at WRITE time, not at humanize time.** Found at
   humanize precondition P2 instead, where the only legal fix is upstream — which throws away the
   whole humanization pass. Hyphen-insensitive check, before the freeze.
2. **Never edit a frozen region during a rewrite** — FAQ, schema, tables, figures, headings, links.
   One FAQ answer touched during humanization broke the 3-way sync and cost a restore.
3. **Validate what a script measures before acting on its number.** `humanize_verify.py` scored
   embedded JSON-LD as prose and understated every article by 11-22 points; `link_liveness.py`
   reports an unpublished article's own canonical as CRITICAL DEAD; `get_ranked_keywords` ignores
   its `target` parameter entirely. Editing an article to satisfy a wrong metric is rework created
   from nothing.

**Checkpoint to disk.** Infrastructure stalls accounted for 8h 06m of that session and are not
preventable. What is preventable is losing position: write each artefact to disk as it clears a
gate, so a restart resumes from files rather than from conversation context.

### ⛔ HARD RULE — KEYWORD SELECTION IS MEASURED AT CREATION, NOT ASSERTED (all clients)

**Before a single heading is written, pull live volumes from DataForSEO for every candidate keyword
at the client's market, and choose from the measured set.** A keyword enters an article only with a
number beside it.

```bash
python3 ~/Unveilr/scripts/kw_gate.py articles/<slug>.md --client <c> --stage create
```

Selection contract:

| Requirement | Test |
|---|---|
| Volume is **measured**, never assumed | `research_keywords` at the resolved market; the figure is recorded in the brief and the report |
| Primary keyword is the **best available in the pillar** | ≥25% of the highest measured volume in the researched set. Choosing a 10/mo term when a 390/mo term was researched and rejected is a fail |
| `no_data` is **not zero** | reported separately, never averaged in, never called "no demand" |
| Difficulty is **read, not guessed** | live SERP composition (who ranks) + the client's GSC top-10 ceiling — `/seo-score` gates G1 and G3 |

**⛔ Organic keyword difficulty is NOT available on this host.** `research_keywords` returns
`search_volume`, `paid_competition`, `competition_index` and `cpc` only. **`competition_index` is
Google Ads PAID competition — it is not organic KD.** Reporting it as difficulty, to a client or in
a gate, is a measurement error of the same class as scoring JSON-LD as prose. Where a difficulty
figure is needed and none exists, say it is unavailable and give the SERP read instead.

**The scarce-market clause is part of the rule, not an excuse.** In regulated B2B niches the whole
pillar can top out in the low hundreds — measured on Aviaan valuation, 5 Sep 2026: ceiling **390/mo**,
median **10**. There the volume gate suspends and the obligation becomes a declaration: state plainly
whether the article is an **AI-citation** play or a **search-volume** play. Never let a low-volume set
be presented as a high-volume one. A rule that cannot be followed in the client's actual market gets
ignored, and an ignored rule is worse than none.

**Enforced twice:** at creation by this rule, and again at `--stage humanize` as precondition P5 of
every `/humanize-<client>` skill, so a keyword cannot be quietly dropped between the brief and the draft.

---

## 2. Phase 0 — Load the client fences before you touch a tool

Client fences kill topics for free. Run them before spending a single API credit.

**Always read first:**
- `~/.claude/clients/<client>.md` — the client config: MCP server, focus-service lock, exclusion list, lane, internal-link namespace, soft-404 paths, prompt set, competitors, credentials, brand voice.
- The client's STRICT memory rules (`~/.claude/projects/.../memory/`).
- `~/.claude/aeo-best-practices.md` — the current scoring rubric.

**The fences as they stand today:**

| Client | Hard fences |
|---|---|
| **Vakilsearch** | 9 primary services only (GST, Company, Pvt Ltd, LLP, OPC, CA, Lawyer, Fundraising, Trademark). **Check for an active narrower sprint** — a sprint fence overrides the 9-service list. In-house exclusion list `clients/vakilsearch/vs_inhouse_exclusion.json` (approx. 948 topics the in-house team owns, DO NOT CREATE). Title = main topic + year only, no colon-subtitles. Slug evergreen, no year. Internal links `/article/...` only (`/blog/` and `/advice/` soft-404 to the homepage). 2,000 words. Brand is `Vakilsearch` with a lowercase "s". Percentages use `%` with no space. |
| **Jaagruk Bharat** | Topics LOCKED to tracked prompts **and** to a service JB actually offers in that state (Maharashtra / Haryana / Karnataka only — no UP, no Bihar). Every article links the most relevant live `/services/` page **for that reader's state**. Never name or link private third-party facilitators. Slug evergreen, no year. 900–1,300 words. `/feeds` is a low-authority surface — apply the surface multiplier. |
| **LexComply** | Locked to the 75 tracked prompts across 5 solutions. Scope narrowed to the Compliance product and legal-compliance subjects (Litigation, ERM and Audit are banned as topics). Zero competitor mentions. No contractions. ₹ and `%` symbols. 1,500–1,800 words. |
| **Care Dale** | Product scope = hardness, chlorine and physical contaminants; 3-layer filtration is the source of truth. Cannibalization checks must enumerate the LIVE Shopify blog, not just our repo. Author Roshni. |
| **Nuyug** | Celebration and occasion wear only, never daily or office. Must link the relevant `/collections/` page. Festive calendar governs timing. Link cap 5–6. Competitor brands never hyperlinked. Word cap 1,800. |

**Output of Phase 0:** every topic that violates a fence is marked `KILLED — fence`, with the fence named. Do not research it further.

---

## 3. Phase 1 — Page-first discovery: which pages need content?

We do not start from a keyword list. We start from **the pages that make the client money**, then work outward to the queries that should be feeding them.

### 3.1 Build the page inventory

| Step | Tool | What you are looking for |
|---|---|---|
| Top organic pages, last 90 days | `get_gsc_top_pages` | Which pages already earn impressions and clicks; the shape of the site's authority |
| Traffic and conversion by page | `get_ga4_top_pages`, `get_ga4_conversions` | Which pages convert, not just which get traffic |
| Money pages | `get_pages_by_type` + client config | Service pages (VS `/…-registration`, JB `/services/…`), collection pages (Nuyug `/collections/…`), product pages (Care Dale PDPs) |
| Section authority | `get_gsc_top_pages`, aggregated by path prefix | Share of total site clicks per section — this drives the surface multiplier in Section 8 |
| Full inventory | `list_articles(status="")`, `search_articles`, the site's `/*sitemap*.xml`, local drafts dir | Everything published, drafted, generating, or archived |

### 3.2 Rank the pages

Priority order for content support:

1. **Money pages with weak query coverage** — a service or collection page that converts but ranks for only a handful of queries. Highest priority: supporting articles funnel authority into it.
2. **Pages at position 5–20 with impressions and low CTR** — the "weak clusters". These rank fastest because the signals already exist.
3. **Decaying pages** — compare current 90 days against prior 90 days. A page losing clicks even at position 3–4 is tagged REFRESH.
4. **Pages with AI visibility but no search visibility (or vice versa)** — an asymmetry that tells you which channel to attack.

### 3.3 Derive the difficulty ceiling (do not use a universal KD)

Take the queries the client currently holds in the top 10, look up those SERPs' keyword difficulty (`bulk_keyword_difficulty`), and take roughly the **75th percentile** as the client's demonstrated ceiling. New or weak domains land around 10–20; established domains 45 or above. **This number, not a generic "KD under 30", is the gate we apply in Section 5.**

If GSC is not connected, say so explicitly, skip the ceiling and decay analysis, use a conservative inferred ceiling, and record it as a data gap in the brief.

---

## 4. Phase 2A — The SEO track: keyword research

Run this track when the target is **Google rankings and clicks**.

### 4.1 Start from the page, not the keyword

For each priority page from Phase 1:

```
get_gsc_page_queries(<page URL>)
```

This returns every query the page already earns impressions for, with position. Sort them into four buckets:

| Bucket | Definition | Action |
|---|---|---|
| **Strong** | Position 1–4, healthy clicks | Do not touch. Any new article targeting this is cannibalization. |
| **Striking distance** | Position 5–20, impressions, poor CTR | **Highest-value bucket.** Either optimize the page itself or write a support article that answers the long-tail around it and links in. |
| **Low visibility** | Position 21–50, tiny impressions | Genuine opportunity — the site is topically relevant but the page does not deserve to win yet. A dedicated article can take it. |
| **No visibility** | Query has volume, page earns nothing | The purest gap. Verify no other page on the domain covers it, then target it. |

This is the core loop: **top pages → what they already rank for → what ranks badly → what has no visibility at all → target the last two.**

### 4.2 Expand the keyword universe

Run 8–12 batches of 10 keywords each (DataForSEO fails on larger batches for some accounts). Batch categories, adapted to the pillar:

1. Head term plus core modifiers
2. `how to [action]`
3. `what is / meaning of`
4. `[X] vs [Y] / difference between`
5. `best / top [pillar] for [use-case]`
6. `cost / price / fees / charges`
7. `[pillar] for [industry / entity type / city]`
8. `near me / online / in [city]`
9. Lifecycle: renewal, transfer, amendment, cancellation
10. Problem-aware: not working, rejected, objection, error

**Tools:** `research_keywords` (preferred, per-client MCP) or DataForSEO `keywords_data/google_ads/search_volume/live`. Capture `monthly_searches` for the 12-month trend — this catches seasonality and decline. Then `dataforseo_labs/google/related_keywords/live` for the top 5 seeds. Then `bulk_keyword_difficulty/live` for every survivor. **Never skip the KD call** — it is the traditional-SEO gate.

### 4.3 Balance high-volume and long-tail

Every brief carries both:

- **High-volume anchors** — the terms that justify the article's existence commercially. Usually the head or near-head term for the cluster. These are what the page is *about*.
- **Long-tail, fast-to-rank terms** — lower competition, specific intent, often "X for Y" or question-shaped. These are what the article actually *wins on* in weeks 1–8, and they compound.

A brief with only head terms will not rank. A brief with only long-tail will rank and earn nothing. The correct shape is one primary keyword, three to four secondaries that become H2s, and four to five long-tails that become H3s and body phrasing.

**KGR is a tiebreaker only:** `allintitle ÷ volume < 0.25`. Do not build a strategy on it.

### 4.4 Mine the questions (this feeds both channels)

- **Google Autocomplete**, roughly 8 per seed, via `get_autocomplete_suggestions`. Use question-prefix seeds: `do i need a [service] for`, `which [service] for`, `can i [verb] without [service]`, `how to check [service]`, `[service] for [situation]`, `[service] near me`.
- **People Also Ask** via `search_serp`. **Note the known limitation:** PAA is unreliable or empty for India (`location_code 2356` / `gl: in`) on both DataForSEO SERP and Serper. Autocomplete is our PAA substitute for India and reliably returns 8 suggestions per query.
- **Question-graph expansion** — take each PAA or autocomplete result and re-query it to map the full question tree. **This tree is the query fan-out that becomes the article's subheadings.**
- **Community mining** — `site:reddit.com <pillar>`, `site:quora.com <pillar>` via `search_serp` for real phrasing and pain points. Also run `ranked_keywords` with `target: reddit.com/r/<sub>` to find proven-demand gaps where Reddit outranks brands.
- **Google Trends** rising and breakout terms; **YouTube autocomplete** (`ds=yt`) for video intent.

**Rule: communities discover, tools validate.** Every community-sourced candidate gets a volume and KD check before it enters a plan. Zero-volume-but-rising terms go on an "emerging watchlist", labelled honestly, never presented as measured demand.

### 4.5 Scarce-volume playbook

Trigger this when most keywords come back at 0–10 volume, `related_keywords` returns under 20 rows, the SERP has fewer than 5 real competitors, or the pillar is new, niche, regulated, hyper-local, or deep B2B.

Then: suspend the volume gate and say so explicitly in the output; gate on relevance × intent × strategic value instead. Ladder the seed **up** (parent category), **down** (every sub-component, spec, standard, failure mode), and **sideways** (jobs-to-be-done, personas, industries, comparisons). Run alphabet-soup and modifier grids. Mine the client's own first-party demand: sales-call transcripts, support tickets, CRM notes, internal-search logs, GSC queries. Community mining becomes the primary source. Do competitor and authority archaeology: full `ranked_keywords`, sitemaps, glossaries, standards bodies.

**Never return "no opportunities" for a scarce niche.** Rank by strategic value and separate "measured volume" from "zero volume but real demand (evidence: …)".

---

## 5. Phase 2B — The AEO track: always start with the AI mention scan

Run this track when the target is **being cited by ChatGPT, Perplexity, Gemini, Claude and Google AI Overviews**.

**The AEO track never starts with keywords. It starts with a mention scan.**

### 5.1 Run or read the scan

```
trigger_mentions_scan            → starts a fresh scan
get_scan_dates                   → confirm the scan finished
get_mention_scan_results         → per-prompt, per-platform results
```

**Operational note:** scans stream over roughly 10 minutes. Poll `get_scan_dates` until the count is stable before reading results, otherwise you will analyse a partial scan and draw the wrong conclusion. Also verify against the live product rather than notes — scan crons have gone dead silently before.

### 5.2 Read the scan properly

| Question | Tool | What it tells you |
|---|---|---|
| Where are we invisible? | `get_zero_visibility_prompts` | The prompt list with no brand presence at all — the raw opportunity set |
| Where are we mentioned but not cited? | `get_mention_results_by_prompt` | Mentioned without a link is a weaker win; cited is the real target |
| Which of our pages get cited? | `get_top_cited_urls_for_domain`, `get_prompts_citing_domain` | Proof of what our citable content looks like |
| Who is winning our prompts? | `get_citation_domains`, `list_top_citation_sources`, `get_competitor_comention` | The displaceable incumbents |
| Which prompts have no article behind them? | `get_prompt_article_coverage` | **The single most actionable AEO gap report** |
| Are we losing ground? | `compare_mention_scans`, `get_prompt_movement`, `get_lost_prompt_analysis` | Regressions to fix before writing anything new |
| Which platform should we target? | `get_platform_visibility_trend`, `get_scan_platforms` | Platform-specific gaps |

**Platform tendencies from our own citation data** (use this to pick the archetype):
- **Gemini** favours brand comparisons
- **ChatGPT** favours definitional/entity content and fee questions
- **Perplexity** favours commercial listicles
- **Claude** favours transactional class and eligibility questions

### 5.3 Diagnose before you write

If a prompt shows zero visibility, find out *why* before assuming the answer is a new article. Use `diagnose_prompt_live`. (The X-Ray sidecar is dead — use `diagnose_prompt_live`, not `xray_*`.)

Real causes we have hit:
- The page exists and is good, but the **CDN or nginx returns 403 to AI crawlers**, so the engine can never read it.
- `robots.txt` blocks the namespace, so the pages are invisible to Googlebot too.
- The page is an **internal-link orphan** with effectively zero internal PageRank.
- The page is **off-sitemap** or was never actually published.

**Zero visibility does not mean "we need another article."** Check liveness, crawlability, indexation and internal links first. Writing a second article on top of an unreadable first one wastes the whole budget.

### 5.4 Select prompts by citability, not volume

This is the most commonly misunderstood rule on the AEO side.

**A prompt is only worth targeting if both are true:** the query triggers an AI Overview or is a genuine AI-assistant question, **and** on that query the engines plausibly cite a player of our client's type.

Validate every candidate with `analyze_ai_overview` **before** `create_prompts`. Read `has_ai_overview`, `ai_overview_sources`, and `top_organic_domains`, then classify:

- ✅ **Good target** — the AIO triggers and the cited sources are the brand's peers (SaaS vendors, law firms, consultancies, advisories, or the brand's named competitors). **A competitor being cited is the strongest winnable-slot signal there is.**
- ❌ **Bad target** — the AIO and organic results are owned by government or state portals (`*.gov.in`, state labour/tax portals) or by pure transaction/filing players, for a brand that is not one of those. Huge Google volume here is worthless because the brand can never be cited.

Worked example (LexComply, 30 July 2026): registration and "how to file" queries were bad targets even at 60,500 and 49,500 volume, because the AIO was filled with government portals and filing services — 16 such prompts were archived. Obligation, interpretation and software-category queries were the good targets, because the AIO cited EY, Deloitte, PwC, law firms and direct competitors. Those are the winnable slots.

**Corollary for client reporting:** never sell a prompt on its Google volume. Lead with AIO citability.

### 5.5 Register the prompt before the article ships

For every surviving AEO topic, map the AI question it will answer to the client's tracked prompt set (`list_prompts`). If the intended prompt is not tracked, create it now with `create_prompts` — **before** the article is written.

This costs nothing and makes the outcome observable. We learned this the expensive way: a batch of 7 Vakilsearch trademark-class articles targeted classes nobody tracked, and those 7 articles are permanently unmeasurable.

---

## 6. Phase 3 — Finding the best gap

"Find the gap" is not a vibe. It is a ranked set of specific gap types. Work down this list.

| # | Gap type | How you detect it | Why it wins |
|---|---|---|---|
| 1 | **Tracked prompt with no article** | `get_prompt_article_coverage` | Demand is already validated and measurable |
| 2 | **Competitor cited, we are absent** | `get_competitor_comention`, `get_citation_domains` | Proves the slot is winnable by a brand of our type |
| 3 | **Striking-distance query with no dedicated page** | `get_gsc_page_queries` positions 5–20 | Signals already exist; fastest ranking route |
| 4 | **High-volume query where we have zero coverage** | Keyword batches minus inventory | Clean gap, but check the SERP is winnable |
| 5 | **Reddit or Quora in the top 10** | Live SERP fetch | The strongest "beatable incumbents" signal in traditional SEO |
| 6 | **Stale incumbents (18+ months) or thin content** | Live SERP fetch plus page scrape | Freshness and depth are cheap to beat |
| 7 | **Fan-out sub-question nobody answers directly** | Question-graph expansion | One article can own several AI sub-queries |
| 8 | **Long-tail with real intent and no measured volume** | Autocomplete plus community mining | Often 10–20x the AI query volume of the Google volume |
| 9 | **Competitor content-gap list** | `ranked_keywords` per competitor minus ours | Systematic coverage expansion |

**Traffic potential over raw volume.** For each cluster, find the **Parent Topic** — the keyword the number-one page ranks for that drives most of its traffic — and estimate traffic potential as the total organic that page pulls from all keywords (`ranked_keywords` on the ranking URL, limit 50). A 200-volume keyword whose parent drives 5,000 visits beats a 1,000-volume dead end. Then **discount for SERP features**: an AI Overview plus a featured snippet plus ads eat organic clicks. Score clicks-potential, not raw volume.

---

## 7. Phase 4 — The coverage and cannibalization gate

**This is the gate that saves the most money, and the one people skip.** A candidate survives only if the client has no existing page — published, drafted, generating, or archived — on it.

Run all five checks. Prefer signals that measure what Google already does over signals that only infer.

1. **All-status inventory** — `list_articles(status="")` plus `search_articles(<topic>)`, the CMS API, the local drafts folder, and the site's sitemap. A drafted-but-unpublished match counts as COVERED. If a tool list looks short against the real site, trust the sitemap.
2. **Semantic title and intent match** — fuzzy, not exact string. Judge a page by what it is *about*, never by its title or format label. "Shell company meaning" and "what is a shell company" are the same topic.
3. **`site:` sweeps** — `site:<domain> "<phrase>" OR "<synonym>"`. These can **confirm** coverage but can never **prove** absence. For Jaagruk Bharat a `site:jaagrukbharat.com` SERP sweep per topic is mandatory: `list_articles` plus GSC miss the in-house ROOT layer entirely.
4. **GSC page-queries on the nearest URL — the decisive test.** `get_gsc_page_queries`. If that page already earns impressions for the candidate keyword or its variants at **any position ≤ 20**, the topic is COVERED. Drop it. **Never mark a topic green without running this.**
5. **Cannibalization report** — `get_gsc_keyword_cannibalization`. If the cluster is already contested, a new page makes it a three-way split. Drop it.

**Then the client-specific layers:**
- **Exclusion list** — Vakilsearch `vs_inhouse_exclusion.json`. Fuzzy-match on intent, not string. A match is `DROPPED — owned by in-house team`.
- **Our own queue** — scheduled-but-unpublished items count as live for collision purposes. **No two same-cluster topics may publish within 14 days.** We lost July's GST spokes partly by stacking four in three days.
- **Sections our tooling does not enumerate** — JB in-house root pages, VS in-house content, Care Dale's legacy Shopify blog.

**Soft-404 guard.** For any namespace listed in the client config's soft-404 paths, an HTTP 200 does **not** mean the page exists. `lexcomply.com` returns 200 on non-existent pages. Vakilsearch `/blog/*` and `/advice/*` soft-404 to the homepage. Verify with `check_page_rendering` or rendered content before treating a 200 as either coverage or as proof a gap is filled.

**Keyword-level verdicts (run per keyword, not just the primary):**

| Situation | Verdict |
|---|---|
| A service or transactional page ranks for the keyword | **Drop the keyword.** A blog must not compete with a lead-gen page. Link *to* the service page instead. |
| An existing blog ranks at position under 20 | **Drop**, unless the new article covers a fundamentally different angle |
| Multiple existing pages already fragment the keyword | **Drop** — do not worsen fragmentation |
| Nothing ranks, or existing pages sit at 50+ with near-zero clicks | **Safe to target** |

**Rating scale used in briefs:**
- 🟢 Clean gap — nearest page ranks for zero candidate queries or only beyond position 20, no inventory match, fewer than 3 shared top-10 URLs. **Almost every recommended row must be green.**
- 🟡 Adjacent — position 11–20 for a few variants, or 3–4 shared URLs. Ship only with a hard-differentiated primary keyword and a stated angle. Otherwise drop.
- 🔴 Cannibalization — nearest page ranks at position ≤10, or a draft or published page targets the same intent, or 5+ shared URLs. **Never ship.**

If more than the occasional row comes back amber or red, the coverage gate was too loose. Tighten it and re-run.

---

## 8. Phase 5 — Score the topic before writing it (`/topic-score`)

Article Scoring Matrix v1.1, validated out-of-sample against 143 May–June 2026 articles. Winner-versus-dud score separation was 17–29 points; a score of 70 or above predicted a winner with 68–100% precision; the kill zone was 90% true-negative on Vakilsearch.

**What it is not:** a traffic forecaster. Correlation with exact click counts is 0.2 or lower. It is a three-band classifier — **write / rework / kill**. Never promise a rank position or a click number from a score.

### 8.1 The kill gates (binary, any FAIL means do not write)

| Gate | Test | Kill condition |
|---|---|---|
| **G1 — Demand exists** | `research_keywords` volume, `get_autocomplete_suggestions` depth, PAA presence via `search_serp`, or an existing tracked prompt | Zero evidence across all four |
| **G2 — Collision-free** | `site:<domain> <intent>` sweep, `get_gsc_page_queries` on suspected siblings, plus the sections tooling misses | Identical intent already live. Same cluster with genuinely distinct intent passes with a penalty and a monitoring note. |
| **G3 — SERP winnable** | `search_serp` on the head query, then `analyze_ai_overview` | Top 3 are marketplaces, government portals, or international authorities we cannot displace. Heavy penalty if an AI Overview already fully answers an informational query — we measure 0.5% CTR at positions 4–9 on AIO-saturated informational SERPs. Commercial and comparison SERPs with an AIO still pay. |
| **G4 — Channel fit** | Does the intended win match the archetype? | Writing an explainer spoke and expecting AI citations, or targeting an untracked prompt and expecting tracked-visibility gains |
| **G5 — ChatGPT winnability** (AEO column only; never kills the SEO column) | Classify the question's shape against `~/.claude/aeo-best-practices.md` PART G1 | ChatGPT searches the web ~100% on year-dated questions, 92% on "best/top", 87% on price/fees, 84% when a city is named — but only **37%** on "what is / how to" and **18%** on general informational. When it answers from memory, **no page can be cited and the contest never happens.** A purely definitional topic — no year, price, city or superlative — caps the AEO column at 40 and is labelled `AEO: low-winnability`. Not a kill: it may be an excellent SEO target. What is killed is the *promise*. The cheapest re-angle in this SOP is giving a definitional topic one of the winning shapes. Enforced by `/topic-score` G5; prompt-level enforcement is `aeo-research` HARD RULE C. |

### 8.2 Archetype is the dominant factor

| Archetype | SEO (/25) | AEO (/35) |
|---|---|---|
| Status / check / tool intent | **25** | 18 |
| Number or threshold answer (H1 promises a number or verdict) | 23 | 30 |
| Fee / pricing table | 23 | 32 |
| Data listicle (top N, statistics, examples) | 21 | 24 |
| City / local data with a proven query | 20 | 12 |
| Best-of / brand listicle | 20 | **33** |
| Comparison / X vs Y | 18 | **35** |
| Definitional entity (what is X, meaning, format) | 12 | 26 |
| How-to with unique intent | 16 (up to 20 on a high-authority surface) | 14 |
| Uncovered symptom / niche | 16 | 14 |
| Decision / situational guide | 14 | 20 |
| Statutory spoke **with** a genuine fresh provision and year | 12 | 10 |
| Generic design or condition explainer | 6 | 5 |
| Statutory spoke with no fresh hook | 3 | 3 |

### 8.3 The two score columns

**SEO column (100):** Archetype 25 · Measured demand 20 · SERP gap including the AIO check 20 · Cannibalization clearance 10 · Timing and freshness 10 · Structural pre-flight 15.

**AEO column (100):** Archetype 35 · Tracked-prompt alignment 25 · Platform fit 10 · Extractability and citability plan 15 · Citation-splitting cannibalization 10 · Timing and freshness 5.

**Surface multiplier** — measure the section's share of site organic clicks over 30 days (`get_gsc_top_pages`, aggregated by path prefix):
- ≥5% of site clicks → ×1.0
- 1–5% → ×0.7
- Under 1% → ×0.3 on the SEO column, ×0.6 on the AEO column, **and no net-new spokes until an authority-building phase completes.**

This is not theoretical. JB's `/feeds` took 0.04% of site clicks while legacy root articles took 74.5% — identical archetypes, zero payoff. VS `/article/` is an established surface at ×1.0.

### 8.4 Verdict bands and routing

| Score | Verdict | Route |
|---|---|---|
| Primary channel ≥70 | **WRITE** | SEO-primary → `/seo-research*` → `/seo-article`. AEO-primary → `/aeo-article-<client>`. |
| **Both** columns ≥70 | **DUAL-PLAY** — the best briefs | `/seo-article` (the hybrid writer) |
| Primary 50–69 | **REWORK the angle**, then rescore | Do not write yet |
| Primary under 50 | **KILL** | — |

### 8.5 Re-angle before killing

For anything scoring 50–69, propose a concrete re-angle that changes the archetype while keeping the demand. This is the highest-value output of the whole scoring step: it converts dead briefs into winners instead of discarding validated research.

Proven moves:
- Generic explainer → **status/check** ("Director Disqualification Under Section 164" → "How to Check If a Director Is Disqualified"). Status/check is the best-performing archetype in our data.
- Generic explainer → **number or threshold answer** — give the H1 a number or a verdict to promise.
- Explainer → **comparison** when the AEO channel is the goal.
- Broad head term on a marketplace SERP → **vernacular or long-tail niche** with the same product intent. Nuyug's "pearl necklace sets" died; "bugadi" pulled 505 impressions.
- Listicle with no data → **data listicle** with measured numbers, a table and real examples.
- Statutory spoke → attach a genuine fresh provision or year hook, or drop it.

### 8.6 Log every score

Append every scored topic to `clients/<client>/topic_scores.csv`: date, topic, archetype, SEO score, AEO score, gate results, verdict, declared channel, and (once published) slug and publish date. Leave outcome columns blank — the fortnightly retro fills them at day 21+ and re-weights the matrix.

**A score logged after the fact is worthless. Log at brief time, including for topics you kill.**

---

## 9. Phase 6 — The brief is the contract

The research phase ends with a brief. The writer does not re-decide anything in it. If the brief is wrong, fix it in the research skill and regenerate — never paper over it in the writer.

**Every brief carries these fields:**

| Field | Source |
|---|---|
| Primary keyword | Phase 2A, post-cannibalization |
| Secondary keyword cluster | Related keywords, SERP-overlap clustering |
| Long-tail set | Autocomplete, community mining, related keywords |
| Search intent | Informational / Commercial / Transactional / Navigational |
| Dominant SERP format | Live top-10 fetch. **If the top 10 are product or tool pages, a blog cannot rank — route to a service or product page instead.** |
| Query fan-out + PAA question tree | Phase 2A section 4.4 — these become the H2/H3 subheads |
| Mapped tracked prompts | `list_prompts`, `get_prompt_article_coverage` |
| Internal-link target | The service, collection or product page this article supports. **Verify live with `check_urls_liveness`, honouring soft-404 paths.** |
| Competitive depth (SERP median word count and subtopics) | Top-10 scrape |
| Angle to win | One sentence |
| Proof of gap | The closest existing URL, or "none" |
| Cannibalization rating | 🟢 / 🟡 / 🔴 |
| Inbound-link plan | 1–2 named live sibling pages that will link **to** this article |

**Topic focus rule:** every article is built around **either one target keyword or one target prompt**, never a blend of several. Secondary keywords support the primary; they do not compete with it. Fan-out questions serve the head topic; they do not wander off it.

---

## 10. Phase 7 — Deep research and factual verification

The research depth determines article quality more than the writing does. Minimum standard:

- 5–7 authoritative web sources
- Official government or regulatory portal pages for any factual data (fees, forms, deadlines)
- The brand's own existing content on related topics (for interlinking and voice)
- Competitor articles currently ranking for the target keywords
- Cross-verification of every fact across multiple sources

**Standards:** every statistic has a verifiable source. Legal and regulatory references carry exact section or rule numbers. Government fees are verified against official `.gov.in` sources. Timelines reflect real current processing times, not textbook answers. Form references are exact form numbers. Where sources disagree, note both and use the more authoritative one.

**Research quality gate (mandatory).** If the topic needs specific pricing or fee data and research finds none, **stop and report** — do not invent pricing. If core factual data is missing for more than half the planned sections, stop and report. If research found only competitor content and zero authoritative sources, flag it before proceeding.

### 10.1 The five verification rounds

Run all five after drafting. Combining or skipping rounds defeats the purpose — in testing, single-round verification introduced *new* errors 40% of the time.

| Round | Question it answers |
|---|---|
| **1 — Primary source** | Is every claim confirmed by the primary source, fetched live? |
| **2 — Completeness** | Is the article misleading by omission? Exceptions, edge cases, all applicant types, all versions. |
| **3 — Internal contradiction** | Does the article contradict itself — body vs body, table vs prose, FAQ vs body, schema vs body? If Round 3 produces fixes, re-run Round 3. |
| **4 — Heading cannibalization** | Does an existing client page already rank for any H1/H2/H3 keyword phrase? |
| **5 — Grammar and readability** | Subject-verb agreement, run-ons, comma splices, ambiguous pronouns, tense, brand-voice compliance, consistent terminology and number formatting. |

**Round 1 is non-negotiable and must involve an actual fetch.** "VERIFIED based on my knowledge" is dishonest and must never be written. If you cannot fetch a source, write "COULD NOT VERIFY" and flag it for manual review. It is better to flag 20 claims than to rubber-stamp one wrong number.

**Where primary and secondary sources disagree, primary always wins.** Where two secondaries disagree and the primary is unavailable, do not pick a side — mark the claim as unverified in the body.

**Verified failure modes from our own history:** a Tele-Law beneficiary count written as "fifty lakh" when the actual figure was 1.12 crore; a Section 35(1) citation that described the wrong thing entirely because a summary was read instead of the section text; an NCRB statistic inflated from 217% to "over 300%"; two different helplines conflated onto one number; a 2013 lawyer count presented as current.

---

## 11. Phase 8 — Content construction rules

These are the rules the writing skills enforce and the scorers gate on.

### 11.1 Title and H1

- **Short, direct, phrased as the target query or prompt, plus the year.** It should read like the exact question a user or an LLM would ask, and nothing more.
- Drop everything after a colon if it is a descriptive subtitle. Drop parenthetical or dash descriptor tails such as "(Complete Guide)" or "— Cheapest Way". **Keep the year.**
- Keep the primary keyword intact — do not abbreviate or singularise it.
- ❌ `Iron in Borewell Water: Why It Stains Your Hair, Skin & Bathroom Orange (2026)`
- ✅ `Why Borewell Water Stains Your Hair & Bathroom (2026)`
- `meta_title` ≤60 characters with the primary keyword in the first 50. `meta_description` 150–160 characters, with the answer or value proposition in the first 70.
- **Slug is evergreen — no year** (VS, JB and others). The title and H1 keep the year; only the URL drops it. Max 7 words, lowercase, hyphenated.

### 11.2 The Quick Answer callout (Vakilsearch, Jaagruk Bharat, LexComply — mandatory)

The first content block after the H1 and the last-updated line, before the intro:

```
# Article Title (2026)
_Last updated: 31 July 2026_
> **Quick Answer:** <direct, self-contained answer to the article's primary query>

<intro paragraph follows>
```

Front-load the actual answer — the definition, the yes/no, the number, the ₹ figure. One to three sentences, roughly 40–60 words. Plain prose only: no links, no lists, no headings inside it. Expand key acronyms once. One per article.

### 11.3 Headings

- **Every H2 and H3 is phrased as the question a customer actually asks or types.** "Which finger do you wear a cocktail ring on?" not "Cocktail Ring Placement".
- **The fan-out and PAA question tree from the brief becomes the heading skeleton.** This is the single shared SEO/AEO win — the same structure ranks in Google and gets extracted by AI engines.
- Short, direct and literal so an answer engine can extract them cleanly. No clever, vague or long headings.
- Strict H1 → H2 → H3 hierarchy with no skipped levels. A heading roughly every 150–200 words.
- Question format is not required for navigational sections ("Quick Reference", "Summary Table"), numbered list sections where the number is the structure, or FAQ headings.

### 11.4 Answer-first structure

- The first one to two sentences under every heading directly answer that heading's question, in 60 words or fewer.
- **The first sentence must be a complete, standalone answer under 29 words.** This is the voice layer — voice assistants read exactly this aloud.
- Pattern: **Answer → Evidence → Detail.** Never open a section with background, history or context.
- Define the primary topic within the **first 100 words** using an "X is Y" or "X refers to Y" pattern.
- Put the most important claim or data point in the first 30% of the article.

### 11.5 Paragraph and section length

| Rule | Threshold |
|---|---|
| Paragraph length | **2–3 sentences ideal; 4 sentences maximum.** At least 85% of body paragraphs must comply. |
| Paragraph word count | ≤80 words, for at least 85% of paragraphs |
| Section length (between two H2s) | **≤300 words.** Ideal extractable passage length is 134–167 words. |
| Multi-paragraph chunking | **If a subhead would carry more than one paragraph or more than one distinct idea, split it into multiple H3 subheads — one idea per chunk.** Never stack two or more paragraphs under a single heading. |
| Sentence length | ≤22 words typical, **never over 40** |

The chunking rule is the one most often broken. A heading with three paragraphs under it buries two of the three extractable answers.

### 11.6 Tables — use them deliberately, they raise relevance

Tables with proper headers have a **47% higher AI citation rate**. Comparative listicles account for 32.5% of all AI citations.

- **Any set of 3 or more comparable data points goes in a table, not prose.** Fees, timelines, eligibility, comparisons, document lists with attributes.
- Descriptive column headers containing keywords. Never "Column 1" or "Item".
- For comparison and guide articles, put a **summary comparison table near the top**.
- Keep tables to 4 columns or fewer for mobile.
- Requirements, documents and features go in bullet lists; sequential processes go in numbered lists; 5–7 items per list, each starting with an imperative verb or a bold key term.
- Include a "Common Mistakes" or "What to Avoid" section — these serve as natural query fan-out targets that AI engines extract independently.
- Include contrasting perspectives (pros and cons, when to do X versus when not to). Balanced content outperforms purely factual content.

### 11.7 FAQs — required, with a hard word limit

- **5–10 question-and-answer pairs** (6–8 is the working target).
- **Each answer is capped at 65 words.** This is a hard cap, tightened from the old 40–80 range, because AI engines extract only the first 50–60 words. The voice-optimal sweet spot is 40–60 words.
- **Every answer is answer-first and self-contained.** Lead with the direct answer.
- At least one specific data point per answer.
- **No brand mentions in FAQ answers.**
- **FAQ questions come from real search data — never invented.** Sources, in priority order: the remaining fan-out and PAA questions not used as subheads, high-volume question-format queries from `research_keywords`, Google Autocomplete question-prefix seeds, and the client's tracked prompts (embedded close to verbatim).
- **Every FAQ must add depth the body does not already cover.** Before finalising, literally ask of each one: "Is this answer already in the body?" If yes, replace it. Common violations: restating the fee table, summarising a "types" section, repeating processing timelines, paraphrasing eligibility criteria. FAQs that echo the body add zero value for AI extraction.
- **Three-way sync rule:** after any FAQ edit, the body text, the `sc_fs_multi_faq` shortcode (WordPress clients) and the JSON-LD `FAQPage` schema must all be updated together. Fixing one without the others is a scored failure.
- **Pre-humanization risk:** humanization adds roughly 10–15 words. An answer at 70–80 words before humanizing will blow the cap. Flag those.
- Note for context: Google deprecated FAQ rich results on 7 May 2026. We keep FAQ schema for **AI extraction**, not for SERP appearance.

### 11.8 Word counts

**General principle (house default):** non-legal articles stay **under 1,500 words**; legal and statutory content may run to **2,200**. Extra length must be deeper fan-out H3s, worked examples and tables — never padding. A high-density 1,700-word article outperforms a low-density 3,000-word one.

**Binding per-client contracts (these override the general default, and the scorers gate on them):**

| Client | Target | Scored band |
|---|---|---|
| **Vakilsearch** | **2,000 (strict, client instruction 23 Jul 2026)** | Full marks 1,900–2,100 |
| **LexComply** | 1,500–1,800 | — |
| **Jaagruk Bharat** | 900–1,300 | Full marks 900–1,500; ceiling 1,500 |
| **Nuyug** | 1,400–1,800 | Hard cap 1,800 |
| **Care Dale / generic** | 1,500–1,600 default | — |

There is one live tension to be aware of: the house default of "under 1,500 for non-legal" and the generic skill default of 1,500–1,600 are close but not identical. **When a client contract exists, the client contract wins.** When it does not, use 1,500–1,600 and stay under 1,500 for non-legal subjects.

**Depth check:** for SEO-primary articles, compare against the **median word count of the top-10 ranking pages**, not an absolute band. Materially thinner than what ranks (under roughly 60% of SERP-median depth, or missing subtopics every ranking page covers) fails the `/seo-score` G3 gate.

### 11.9 Linking

**Outbound in-body link caps:**

| Client | Total in-body links | Of which external authority |
|---|---|---|
| **Vakilsearch, Jaagruk Bharat** | **8–9 hard cap**, soft floor 6, target band 7–9 | **2–3 mandatory.** Zero external links is a fail, not a style choice. |
| **Care Dale, Nuyug, generic** | **6–8 hard cap** | 0–2 |
| **Nuyug** | 5–6 contextual; the approved Curated Picks product grid (8–12 cards) is **exempt** from the cap | — |

Only `[anchor](url)` patterns in the body markdown count. Frontmatter URLs, FAQ shortcode URLs, JSON-LD URLs and the citations block do not count.

**What each link type is for:**

| Link category | Target | Rule |
|---|---|---|
| **Pillar / service page** | The service or pillar page for the article's primary topic | **At least 1, mandatory.** For JB it must be the `/services/` page relevant to that reader's state. |
| **Product / collection keywords** | **Product keywords always link to the product or collection page.** Nuyug articles must link `/collections/<slug>` (never product pages only, never the homepage); Care Dale product claims link the PDP. | At least one in-body, in context with a product callout, plus one in the conclusion or CTA |
| **Prompt-driven links** | A prompt-led mention links to **either the service page or a related blog article** — whichever reads more naturally and serves the reader better at that point in the sentence | Judgement call; naturalness wins |
| **Sibling article cross-links** | 2–3 topically adjacent articles in the same cluster | The number-one gap in our audits. Clustered content receives roughly 3.2x more AI citations than standalone posts. |
| **External authority** | `.gov.in` portals first, then inter-governmental (`wipo.int`), then `.edu` and standards bodies | 2–3 for VS/JB. Promote sources already verified in the fact-check rounds — do not research twice. |

**Hard link rules:**
- **Never link a competitor domain.** VS blocklist: indiafilings, legalwiz, lawrato, myonlineca, cleartax, setindiabiz. JB blocklist: vakilsearch, indiafilings, cleartax, lawrato, bankbazaar, paisabazaar. Nuyug: competitor brand names appear as plain text only — a hyperlink to a competitor domain is a critical failure.
- **Never hyperlink the same URL twice** in one article. Unlink the duplicate and convert it to plain text.
- **Never render a URL as plain text.** Weave it into a descriptive anchor.
- **Never use a non-live URL.** Verify every link with `check_urls_liveness` (batches of 20) before saving. If a link is dead, replace it with a verified-live alternative on the same domain or strip the link and keep the anchor as plain text. Never ship `[anchor](dead-url)`.
- **Anchor text is descriptive topic text** — never "click here", never a bare URL, never the brand name. VS anchors must not contain the brand name.
- **No more than 2 links in a single paragraph.** At least one full sentence of prose between links.
- **No stacked link lists** ("Read also: A, B, C, D, E") and no closing paragraph that fires off six collection links in a row.
- **No inline citation markers** — no `[1]`, no `(source: …)`, no footnote markers in the visible body. The `---CITATIONS---` block is stripped before client delivery. If a fact needs sourcing, name the source in prose ("according to BIS hallmarking standards") or anchor it.
- **Note the trap:** "no citations in the published article" bans citation *markers* and a *Sources section*. It does **not** ban authority hyperlinks. Read quickly, that rule once caused 11 Vakilsearch articles to ship with all 78 links pointing at vakilsearch.com and zero external links, while `---CITATIONS---` was full of IP India and WIPO primary sources.

**Government portal exception:** several `.gov.in` portals (indiacode, gst, mca, parivahan, india.gov.in, aaplesarkar) return 403 or 404 to the liveness checker while being perfectly live. Confirm those with WebFetch before dropping them. Conversely, indiacode handles silently resolve to the *wrong* Act — title-check via curl.

**Inbound internal links — a separate, mandatory dimension.** Outbound links do not satisfy this.

Every published article must **receive** at least 1–2 inbound internal links from existing, live, topically-relevant pages on the same domain. At or after publish:
1. Find 1–2 existing live topically-adjacent pages (sibling cluster pages, the mapped service or collection page, a related guide).
2. Add a natural contextual link from **each** of those pages **to** the new article, with a descriptive anchor, never duplicating an anchor already on the source page.
3. Verify those inbound links are live before closing the task.
4. If no relevant sibling exists, **flag it — do not silently publish an orphan.**

Why this is a hard rule: on the Vakilsearch CIN case (22 July 2026) our `/article/cin-number-meaning-format-india/` got **0 GSC impressions** while the in-house `/article/cin-number/` got roughly **602** — same domain, same day, identical schema. The only material difference was inbound links: theirs had 4 referring URLs, ours had 1.

### 11.10 Data density, entities and citations

- **A named statistic with a source at least once every 200 words.** Named means "according to X" or "X reports that Y%". Compute the minimum: word count ÷ 200.
- **Specific over vague:** "₹4,500 per class" beats "a few thousand rupees"; "76.2% of inmates" beats "most inmates".
- **15–20% proper-noun density** in key sections — name the Acts, organisations, government bodies, forms and portals. Pages with 15 or more recognised entities show roughly 4.8x higher citation probability.
- **Full official names on first mention**, then the short form.
- **8–12 external citations per 1,500 words** with specific attribution. Triangulate major claims across two or more sources, preferring primary sources over secondary blogs.
- At least one expert quote or direct reference to an official body's stated position, and at least one original data point or analysis not available elsewhere.

*(Jaagruk Bharat calibration: for citizen procedural content, real process figures — fees, "7–10 working days", document counts, portal names — plus citations to the official `.gov.in` portal satisfy the density expectation. Do not penalise a how-to for lacking a statistic every 200 words.)*

### 11.11 Formatting and voice

- **Acronyms fully capitalised** in prose: DPIIT, LLP, OPC, PAN, ITR, GST, FSSAI, MSME, WIPO, CBDT. (Exception: deliberately lowercase SEO anchors.)
- **Indian Rupees always use ₹**, never "Rs", "Rs." or "INR", with no space before the number: ₹4,500, ₹10,000 crore.
- **Percentages use `%` with no space** (Vakilsearch and LexComply): `8%`, never "8 per cent" or "8 %". For noun usage, write "share" or "rate".
- **No em dashes anywhere.** Use a spaced hyphen.
- **Brand mentions: 1–2 times maximum in the body, never in FAQs.** Brand casing is exact — `Vakilsearch` with a lowercase "s", `Jaagruk Bharat` as two words.
- **Register:** VS and LexComply are formal with **no contractions**; JB is plain citizen-friendly with contractions allowed; Nuyug and Care Dale follow their own brand voice files.
- **Schema:** Article, FAQPage (synced word-for-word with the visible FAQ), BreadcrumbList, Organization, and HowTo where genuinely step-by-step. **Never nest `@type: Product` inside an Article's `about`, `mentions` or `isPartOf` arrays** — Google's Product validator demands `offers`, `review` or `aggregateRating`, which an article legitimately lacks, and it triggers a GSC Product Snippets error. Use `@type: Thing` or `Brand` instead.
- `datePublished` = `dateModified` = today's date. Visible "Last Updated" line in the body, not only in schema.

---

## 12. Phase 9 — The scoring gates

Scoring is read-only. **Never score and fix in the same pass** — agents that do both inflate scores.

### 12.1 `/aeo-score` — threshold 80/100

| Dim | Dimension | Points |
|---|---|---|
| D1 | Heading format and answer structure | 20 |
| D2 | Section and paragraph structure | 10 |
| D3 | FAQ quality | 15 |
| D4 | Structured formats and extractability | 15 |
| D5 | Data density, entity salience and citations | 20 |
| D6 | Multi-intent coverage and completeness | 10 |
| D7 | E-E-A-T and trust signals | 5 |
| D8 | Internal linking | 5 |
| D9 | Meta and keyword checklist | binary pass/fail, unscored |

Any non-live hyperlink is a **critical D8 failure** — full D8 points deducted and the article cannot pass the gate until every link is verified.

### 12.2 `/seo-score` — threshold 85/100 **and** all ranking gates pass

Part 1 scores S1–S12 (meta, headings, keyword usage, internal linking, external authority, image SEO, schema, depth, mobile markup, E-E-A-T, link health). Part 2 is the set of binary ranking gates that neither `/aeo-score` nor `/seo-optimize` performs:

- **G1 — Search-intent and SERP-format match.** Fetch the live top 10. If the top 10 are product, category or tool pages and this is a blog, **FAIL** — route it to a service or product page instead.
- **G2 — Keyword uniqueness and cannibalization.** `get_gsc_page_queries` on the nearest existing URL; if one of our pages already ranks at position 20 or better for the primary keyword or close variants, **FAIL**. Plus the exclusion-list screen and `get_gsc_keyword_cannibalization`.
- **G3 — Competitive depth versus SERP median.** Materially thinner than what ranks, **FAIL**.

**Any ranking gate failure caps the verdict at FIX REQUIRED regardless of the on-page score.** That is the entire point of an SEO score over an on-page checklist: a perfectly optimised article aimed at an unwinnable or cannibalizing keyword must not pass.

**AEO and SEO stay separate scores.** An article can be 88 AEO and 65 SEO; both gate independently.

### 12.3 Auto-fail list

These fail the article outright regardless of score: an em dash anywhere; a competitor outbound link; a fabricated statistic; a JS-only body; a missing byline; a dead or soft-404 link; a year in the slug (VS); `VakilSearch` with a capital S; "per cent" instead of `%` (VS/LC); a `@type: Product` node nested in Article schema.

---

## 13. Phase 10 — Humanize, verify, publish, measure

1. **Humanize** via the client skill (`/humanize-<client>`), which calls the aihumanize.io API. Never substitute manual rewriting. Never re-humanize an already-humanized article without restoring from `.original` first.
2. **Post-humanize checks.** The humanizer corrupts Indian statutory content in predictable ways: reversed organisation names, wrong acronym expansions, fabricated terms, garbled characters, broken numbered lists, terminology drift ("attorney" for "advocate", "license" for "licence"), contractions in a formal register, and FAQ sync breaks. Verify keywords still present, numbers and section references unchanged, links intact, and the FAQ synced across all three locations. Fix corruption surgically at the token level — **never revert whole blocks to `.prenew`**, or the article stops being 100% humanized.
3. **Re-score.** The score must hold above threshold. If it drops, restore from `.original`, fix the structural issue at the pre-humanize stage, and re-humanize. **Never add net-new prose after humanization** — anything added post-humanize is in AI-native voice.
4. **Banner generation** via the client image skill.
5. **Push** via `/push-to-<client>`. **Every push requires explicit chat approval from the client.** Do not chain a push after humanization. Every push needs an excerpt (from the frontmatter `tldr`, never blank).
6. **Place the inbound internal links** and verify them live.
7. **Confirm the tracked prompt is registered** and the article is mapped to it.
8. **Measure at day 21+** and feed the outcome back into `topic_scores.csv` for the fortnightly retro.

---

## 14. Tooling map — which tool answers which question

| Question | Tool |
|---|---|
| What pages does the client have, and how do they perform? | `get_gsc_top_pages`, `get_ga4_top_pages`, `get_pages_by_type` |
| What does this page already rank for? | `get_gsc_page_queries` |
| What are the quick wins? | `get_gsc_quick_wins`, `get_gsc_content_gaps` |
| Are we cannibalizing? | `get_gsc_keyword_cannibalization`, `get_gsc_page_queries`, `search_serp` with `site:` |
| What is the search volume / difficulty? | `research_keywords`, DataForSEO `search_volume`, `related_keywords`, `bulk_keyword_difficulty` |
| What do people actually ask? | `get_autocomplete_suggestions`, `search_serp` (PAA), `get_chatgpt_qfo` (query fan-out), `mine_social_questions` |
| Where are we invisible in AI? | `trigger_mentions_scan` → `get_scan_dates` → `get_mention_scan_results`, `get_zero_visibility_prompts` |
| Which prompts have no article? | `get_prompt_article_coverage` |
| Who is being cited instead of us? | `get_citation_domains`, `get_competitor_comention`, `list_top_citation_sources` |
| Is this prompt worth targeting? | `analyze_ai_overview` |
| Why is this prompt failing? | `diagnose_prompt_live` |
| What does the SERP actually look like? | `search_serp` |
| Is this URL live and rendered? | `check_urls_liveness`, `check_page_rendering`, `fetch_page_content` |
| What is already in our inventory? | `list_articles(status="")`, `search_articles`, `get_unpublished_articles` |
| Can I create a tracked prompt? | `suggest_prompts`, `create_prompts` |

---

## 15. Hard rules, condensed

1. Never invent a number. Every metric comes from a tool call.
2. Fences and kill gates run **before** scoring. Never spend API budget on a topic a fence already killed.
3. Coverage is decided by GSC page-queries on the nearest URL, not by a `site:` glance.
4. An HTTP 200 is not proof a page exists on soft-404 namespaces.
5. One article = one target keyword **or** one target prompt.
6. Every article opens with the Quick Answer callout (VS, JB, LC).
7. Every heading is a question; every section answers it in the first sentence.
8. Paragraphs 2–3 sentences, 4 maximum; sections under 300 words; chunk anything longer into H3s.
9. FAQ answers capped at 65 words, driven by real search data, adding depth beyond the body, synced across all three locations.
10. Respect the link cap (VS/JB 8–9 with 2–3 external; others 6–8). Never link a competitor. Never duplicate a hyperlink. Never ship a dead link.
11. Product keywords link to product or collection pages; prompt-driven links go to whichever of service page or related blog reads more naturally.
12. Every article earns 1–2 inbound internal links, or gets flagged rather than published as an orphan.
13. Register the tracked prompt before the article ships.
14. Apply strict rules **at creation**, not as deferred gate flags.
15. Never write to a client production system without explicit approval. Back up and verify first.
16. Publishing requires explicit client approval, every time.

---

## 16. Failure modes we have already paid for

Read these once; they are the reason most rules above exist.

| Failure | What happened | The rule it produced |
|---|---|---|
| **Validation theatre** | Agents marked claims "VERIFIED" from training data without fetching a source. Three articles passed verification; a separate pass then found 7 factual errors. | Round 1 requires an actual fetch. "COULD NOT VERIFY" is an acceptable answer; "verified based on my knowledge" is not. |
| **The orphan page** | Our CIN article: 0 impressions against an in-house page's 602, identical schema, decided by 4 inbound links versus 1. | Inbound internal links are mandatory and separately counted. |
| **The unpaginated catalog** | A Nuyug article claimed the brand sold AD bracelets at ₹1,499–₹15,000. The "correction" queried only 250 of 902 products and produced a *second* wrong answer. The full catalog showed 124 bracelet SKUs at ₹1,499–₹5,999. | Never write a brand product claim from memory, brand identity, or an unpaginated sample. Run the truth-card gate. |
| **Untracked prompts** | Seven VS trademark-class articles targeted classes nobody tracked. Permanently unmeasurable. | Register the prompt before writing. |
| **The wrong surface** | JB's `/feeds` took 0.04% of site clicks while legacy root pages took 74.5%. Identical archetypes, zero payoff. | Surface-authority multiplier; no net-new spokes on a sub-1% surface. |
| **Stacked cluster publishing** | Four GST spokes published in three days competed with each other. | No two same-cluster topics within 14 days. |
| **Zero external links** | 11 VS articles shipped with 78 of 78 links pointing at vakilsearch.com, because "no citations" was read as "no external links". | 2–3 external authority links are mandatory for VS and JB; zero is a fail. |
| **Over-linking** | A Nuyug audit found 9–15 links per article; a VS batch found up to 15. | Hard caps with a priority drop list. |
| **Body-restating FAQs** | Three VS articles had every FAQ answer restating the body — fee tables, types sections, timelines. Zero new information, zero extraction value. | FAQs must add depth the body does not cover. |
| **Keywords stripped by humanization** | The primary keyword "trademark status check" (8,100 volume) vanished from the article after humanizing. | Re-verify keyword presence after any rewrite; `/post-humanize-check` auto-restores. |
| **Uncrawlable content** | 23 live AEO articles were blocked from Googlebot by `robots.txt`; a CDN 403'd AI crawlers site-wide. | Diagnose liveness and crawlability before concluding "we need more content". |
| **Content-gap false positives** | Pages called "thin" from raw `<h2>` counts on a JS-rendered site. | Verify rendered content, never raw heading counts. |

---

## 17. New team member: your first two weeks

**Days 1–2 — Read.**
This document. Then `~/.claude/aeo-best-practices.md`, `Article_Scoring_Matrix_v1.md`, and `Blog_Retro_4Clients_Jul13-27_2026.md` Section 8. Then the client config for the client you are assigned to, plus that client's STRICT memory rules.

**Days 3–4 — Observe the data, change nothing.**
Run `get_gsc_top_pages`, `get_gsc_page_queries` on the top 5 pages, and a mention scan read (`get_mention_scan_results`, `get_zero_visibility_prompts`, `get_prompt_article_coverage`) for your client. Write down which pages are strong, which sit at positions 5–20, and which tracked prompts have no article. Do not propose topics yet.

**Days 5–7 — Score someone else's topics.**
Take an existing topic list and run `/topic-score` on it. Compare your verdicts against the logged scores in `clients/<client>/topic_scores.csv`. Understand *why* the matrix killed what it killed.

**Week 2 — Produce one brief, then one article.**
Run the full research phase for one topic. Get the brief reviewed before writing. Write to the construction rules in Section 11. Run both scorers. Do not push anything without approval.

**The three mistakes new members make most often:**
1. Starting from a keyword list instead of from the client's pages and prompts.
2. Skipping the GSC page-queries cannibalization check because a `site:` search looked clean.
3. Treating high Google volume as proof that a prompt is worth targeting in AI.

---

## 18. Change log

| Version | Date | Change |
|---|---|---|
| 1.0 | 31 Jul 2026 | First consolidated release. Merges the research method (page-first discovery, SEO keyword track, AEO mention-scan track, gap taxonomy), the Article Scoring Matrix v1.1 gate, the construction rules from the article skills, and the per-client contracts into one reference. |
| 1.1 | 31 Jul 2026 | Added Appendix A (article body blueprint and section anatomy — what actually goes in the body, in order), Appendix B (one fully worked example from page to outline, using our own documented FSSAI case), Appendix C (glossary). Section 11 states the rules by dimension; Appendix A states them by position, which is how a writer actually needs them. |

**Maintenance:** this document is re-checked at every fortnightly retro. When the matrix is re-weighted at day 21+, or when a client changes a contract (word count, link cap, service lock), update the relevant section here in the same session and bump the version.

---
---

# Appendix A — The article body blueprint

Section 11 states the construction rules **by dimension**. This appendix states them **by position** — what goes into the article, in the order it appears. Use Section 11 as the rulebook and this appendix as the build sheet.

## A1. The full document skeleton

Every article we publish has this shape, top to bottom.

| # | Element | Required? | Rules |
|---|---|---|---|
| 1 | **Frontmatter** | Always | `title`, `meta_title`, `meta_description`, `slug`, `keywords` (primary first), `cluster`, `internal_link_target`, `tldr`, `author`, `featured_image_path`, `project_id`, `brand`, `generated_date`, plus the handoff note listing which tracked prompts this answers |
| 2 | **H1** | Always | Short, phrased as the target query, plus the year. No colon-subtitle, no descriptor tail. Primary keyword intact. |
| 3 | **Last-updated line** | Always | `_Last updated: 31 July 2026_` — visible in the body, not only in schema |
| 4 | **Quick Answer blockquote** | VS / JB / LC mandatory; recommended for all | 40–60 words, 1–3 sentences, plain prose, no links or lists. Front-loads the actual answer: the number, the ₹ figure, the yes/no, the definition. |
| 5 | **Intro paragraph** | Always | 2–3 sentences. **Must contain the "X is Y" definition of the primary topic inside the first 100 words of the article**, with the primary keyword. No throat-clearing, no history. |
| 6 | **Summary / comparison table** | Comparison and guide articles | Sits near the top, before the deep sections. This is the block AI engines lift most often. |
| 7 | **Body sections (H2, question-format)** | Always | See A2 for the anatomy of one section. Ordered by the fan-out question tree from the brief, most-asked first. |
| 8 | **H3 chunks under any H2 carrying more than one idea** | Whenever triggered | One idea per chunk. Never stack two paragraphs under one heading. |
| 9 | **Common Mistakes / What to Avoid** | Strongly recommended | Scored under D4. Acts as an independent fan-out target that AI extracts on its own. |
| 10 | **"What happens after" / post-completion section** | Whenever a process is described | The most commonly missed section. What the reader does once the thing is done, renewed, rejected, or expired. |
| 11 | **FAQ block** | Always | 5–10 pairs (6–8 target). Each answer ≤65 words, answer-first, one data point, no brand mention. Drawn from leftover fan-out/PAA questions and tracked prompts. |
| 12 | **Closing / CTA paragraph** | Optional | One service or collection link maximum, and it counts toward the link cap. No stacked link lists. |
| 13 | **`---SCHEMA---` and `---FAQ_JSON---` blocks** | Always | Machine-readable, not visible to readers. FAQ text must match the body word-for-word. |
| 14 | **`---CITATIONS---` block** | During drafting only | **Stripped before client delivery and before push.** Its sources get promoted into body anchors instead. |

## A2. The anatomy of one body section

This is the unit that gets cited. Build every H2 this way.

```
## <The question, phrased exactly as a user would type or ask it>

<Sentence 1 — a complete, standalone answer, under 29 words.>      ← the voice layer
<Sentences 2–3 — finish the capsule. Total capsule ≤60 words.>     ← the AI snippet

<Evidence: a named statistic with its source, or the statutory
 reference with its exact section number.>

| <table — whenever there are 3+ comparable data points> |
  or
- <bullet list — requirements, documents, features; 5–7 items>
- <numbered list — sequential process steps>

<Detail paragraph: ≤4 sentences, ≤80 words. The "why" and the
 "how", never the answer itself.>

### <Second distinct idea becomes its own H3 question — do not
     stack it under the H2 above>
```

**Test each section against these four before moving on:**
1. Could sentence 1 be read aloud by a voice assistant and be a complete answer on its own?
2. If this section were lifted out of the article entirely, would it still make sense? (The Information Island test.)
3. Is the whole section under 300 words, and does every paragraph run 4 sentences or fewer?
4. Are the 3+ comparable data points in a table rather than buried in prose?

## A3. Heading budget by word count

Rule: a heading roughly every 150–200 words. FAQ headings and the H1 are excluded from this count.

| Client / band | Word target | Total H2 + H3 | Suggested split | FAQ pairs |
|---|---|---|---|---|
| Jaagruk Bharat | 900–1,300 | 5–8 | 5–6 H2, 0–2 H3 | 5–6 |
| Care Dale / generic | 1,500–1,600 | 8–10 | 6–7 H2, 2–3 H3 | 6–8 |
| LexComply | 1,500–1,800 | 8–12 | 6–8 H2, 2–4 H3 | 6–8 |
| Nuyug | 1,400–1,800 (cap 1,800) | 9–12 | 7–8 H2, 2–4 H3 | 6–8 |
| Vakilsearch | 2,000 (band 1,900–2,100) | 10–13 | 8–9 H2, 2–4 H3 | 6–8 |

**Budget note:** an FAQ block of 7 answers at roughly 55 words each is about 400 words. That is inside the word count, not on top of it. Plan the body around 1,600 words for a 2,000-word Vakilsearch article.

**Where the extra length goes on a 2,000-word article:** deeper fan-out H3s, one more worked example, one more table. Never padding, never a longer intro.

## A4. Link placement map

Where the links physically sit, so the cap is hit naturally rather than trimmed afterwards.

**Vakilsearch and Jaagruk Bharat (8–9 total, 2–3 external mandatory):**

| Position | Link | Type |
|---|---|---|
| Intro or first body section | The pillar / service page for the primary topic (JB: the `/services/` page for that reader's state) | Internal — mandatory |
| First factual claim carrying a fee, deadline or threshold | Official `.gov.in` portal | External authority |
| Mid-body, where a sub-topic is mentioned in passing | Sibling article in the same cluster | Internal |
| Mid-body, second statutory or numeric claim | Second `.gov.in` or inter-governmental source | External authority |
| Later body section | Second sibling article | Internal |
| Where the process references the official application portal | The portal itself | External authority (3rd) |
| Later body section | Third sibling, or a second service page if genuinely relevant | Internal |
| Closing / CTA paragraph | One service-page CTA | Internal — optional, counts toward the cap |

**Care Dale, Nuyug, generic (6–8 total):** 2–3 collection / pillar / service links · 2–3 sibling blog cross-links · 0–2 external authority · 1–2 product CTAs maximum, and only when the article is genuinely a shoppable listicle. Nuyug's Curated Picks grid is exempt from the cap.

**Spacing rules that apply to every client:** never more than 2 links in one paragraph · at least one full sentence of prose between two links · never the same URL twice · never a bare URL as text · never a competitor domain · every link liveness-verified before save.

## A5. Element-by-element "what to add" checklist

Run down this list while drafting, not afterwards.

- [ ] **H1** — the query, the primary keyword, the year, nothing else
- [ ] **Quick Answer** — the actual number or verdict in the first clause
- [ ] **First 100 words** — contains "X is Y" plus the primary keyword
- [ ] **Every H2** — is a question a real person types or asks
- [ ] **Every section's first sentence** — under 29 words and complete on its own
- [ ] **Every 200 words** — carries a named statistic with an attributed source
- [ ] **Every set of 3+ comparable data points** — is a table with keyword-bearing headers
- [ ] **Every process** — has a numbered list and a "what happens after" section
- [ ] **Every article** — has a Common Mistakes section
- [ ] **Every secondary keyword** — appears at least once; every long-tail appears in an H3 or body phrasing
- [ ] **Every mapped tracked prompt** — has a section whose heading and opening sentence answer it near-verbatim
- [ ] **Every FAQ** — under 65 words, sourced from real search data, adding something the body does not cover
- [ ] **Every link** — in the cap, live, non-duplicate, descriptive anchor, non-competitor
- [ ] **Inbound links** — 1–2 sibling source pages named, with their anchor text, before publish
- [ ] **Schema** — FAQ text matches the body word-for-word; no `@type: Product` nested in Article
- [ ] **Formatting** — ₹ symbol, `%` no space, acronyms capitalised, zero em dashes, register matches the client

---

# Appendix B — One worked example, page to outline

**This walkthrough uses our own documented case file.** Every keyword volume and impression figure below is a real recorded number from our FSSAI work, not an invented illustration. Steps whose output was not recorded are marked `[reconstructed]` and exist to show the shape of the step.

**Read the Phase 0 result first — it is the most important lesson in the example.**

### Phase 0 — Client fences

Client: Vakilsearch. Candidate pillar: FSSAI licensing.

**Under today's fence this topic is `KILLED — fence`.** Vakilsearch is locked to 9 primary services — GST, Company, Pvt Ltd, LLP, OPC, CA, Lawyer, Fundraising, Trademark — and FSSAI is not among them. A candidate that fails Phase 0 costs zero API credits, and that is the entire point of running fences first.

The rest of this walkthrough follows the topic as it was actually worked **before** the current fence existed, because the keyword and cannibalization stages are the clearest teaching case we have.

### Phase 1 — Page-first discovery

Priority page identified: the `/fssai-registration` service page — a money page, converting, with query coverage worth checking.

`get_gsc_page_queries` on that URL returned the queries it already earns. The material finding: **the service page held 429+ impressions across 10+ state-level pages** for the FSSAI cluster.

That single number decides most of what follows.

### Phase 2A — Keyword expansion

Batches run across the standard categories. The head terms came back large:

| Keyword | Volume |
|---|---|
| fssai license | 90,500 |
| fssai registration | 49,500 |

Both were initially placed in the article's selected keywords. `[reconstructed: the full batch set]`

### Phase 4 — The coverage and cannibalization gate

This is where the article was saved.

**Per-keyword verdict, not just the primary:**

| Keyword | GSC finding | Verdict |
|---|---|---|
| fssai license (90,500) | Our own `/fssai-registration` service page ranks, 429+ impressions across 10+ state pages | ❌ **DROP** — a blog must not compete with a lead-gen page |
| fssai registration (49,500) | Same service page, same cluster | ❌ **DROP** |

**The rule applied:** where one of our own service or transactional pages ranks for a keyword, the keyword leaves the article's target set and the article **links to the service page instead**. The blog's job is to funnel authority into the money page, not to fight it.

Note what would have happened without the per-keyword check: the primary keyword alone might have looked clean while the two largest secondaries quietly cannibalized a converting page.

**Replacement keywords found after the drops:**

| Keyword | Volume | Existing coverage |
|---|---|---|
| fssai central license | 880 | None |
| fssai state license | 590 | None |
| fssai documents required | 590 | None |

Lower volume, zero existing coverage, clean intent — these are the terms the article can actually win, and they compound. This is the high-volume-anchor versus long-tail-winner balance from Section 4.3, resolved in favour of the winnable set because the anchors were taken by our own page.

### Phase 2A.4 — Question mining for the FAQ set

Autocomplete and volume checks produced the contrast that defines our FAQ rule:

| Candidate FAQ question | Volume | Verdict |
|---|---|---|
| fssai license for cloud kitchen | 2,900 | ✅ Use — high demand, and the body does not cover it |
| what is fssai basic registration | 0 | ❌ Drop — no demand, and the body already answers it |

The same pattern held on the trademark side: `trademark class for restaurant` at 1,000 volume beat `how many trademark classes in india` at 0.

**The rule this produced:** FAQ questions come from measured search data, and each one must answer something the body does not. An FAQ that restates the fee table adds nothing for extraction.

### Phase 5 — AEO side

`analyze_ai_overview` on the head terms. For a filing-service brand, an AIO citing filing services is a **winnable** slot; for a management-software brand it would be unwinnable. Same query, opposite verdict, depending on what the client is. `[reconstructed: this classification post-dates the original FSSAI work]`

Tracked prompt registered before writing, so the outcome is measurable.

### Phase 5 (Matrix) — Topic score

`[reconstructed]` Archetype: fee/pricing table — 23 SEO, 32 AEO, one of the strongest pairs available. Demand: measured and strong. SERP gap: checked against the live top 10. Cannibalization clearance: full marks only *after* the two head terms were dropped; it would have scored 0 with them in. Surface: VS `/article/` is an established section at ×1.0.

Verdict: **WRITE**, dual-play.

### Phase 6 — The brief that came out of it

| Field | Value |
|---|---|
| Primary keyword | fssai central license (880) |
| Secondary cluster | fssai state license (590), fssai documents required (590) |
| Dropped, with reason | fssai license (90,500) and fssai registration (49,500) — cannibalize `/fssai-registration` |
| Internal-link target | `/fssai-registration` — verified live |
| Fan-out / PAA subheads | Which FSSAI licence do I need? · What is the turnover threshold for each? · What documents are required? · How long does approval take? · What does it cost? · What happens if it expires? |
| FAQ sources | fssai license for cloud kitchen (2,900) + remaining fan-out questions |
| Cannibalization rating | 🟢 after drops (🔴 before) |
| Inbound-link plan | 2 named sibling pages, anchors drafted |

### Phase 8 — The outline that came out of the brief

```
H1        Which FSSAI Licence Do You Need in 2026?
          _Last updated: …_
> Quick Answer: FSSAI licences split into three types by annual turnover —
  Basic up to ₹12 lakh... [the number leads]

Intro     "An FSSAI licence is …"  ← definition + primary keyword, first 100 words

[Summary table: licence type × turnover threshold × validity × fee]  ← near the top

H2  Which FSSAI Licence Do You Need for Your Turnover?
H2  What Is the Turnover Threshold for Each Licence?
      H3  What Counts Toward Annual Turnover?
H2  What Documents Are Required for an FSSAI Central Licence?
H2  How Long Does FSSAI Approval Take?
H2  How Much Does an FSSAI Licence Cost?
H2  What Happens When Your FSSAI Licence Expires?        ← the "what happens after"
H2  Common Mistakes in FSSAI Applications
FAQ  7 pairs, ≤65 words each, led by the cloud-kitchen question
CTA  one link to /fssai-registration
```

Every H2 is a fan-out question. Every one opens with a standalone answer under 29 words. The two dropped head terms appear nowhere as targets — but `/fssai-registration` is linked from the first body section, which is how the article serves them.

### What this example teaches, in one line each

1. Fences run first and cost nothing.
2. The page tells you what to research, not the keyword tool.
3. Check **every** keyword against GSC, not just the primary.
4. Our own service page ranking is a reason to link, not to compete.
5. 880 volume with zero coverage beats 90,500 volume already owned by our own page.
6. FAQ questions come from measured demand, and must add something new.
7. The fan-out tree becomes the heading skeleton, unchanged.

---

# Appendix C — Glossary

**AEO** — Answer Engine Optimization. Optimizing to be cited inside AI answers (ChatGPT, Perplexity, Gemini, Claude, Google AI Overviews) rather than to rank in a list of blue links.

**AIO** — AI Overview. Google's generated answer block above the organic results.

**AIO citability** — whether AI engines plausibly cite a brand *of our client's type* on a given query. Judged from the AIO's cited sources, not from whether an AIO exists. Peers or competitors cited means a winnable slot; government portals or filing services cited means unwinnable at any volume.

**Answer capsule** — the first 1–2 sentences under a heading, ≤60 words, that directly answer the heading's question. The block AI engines extract.

**Archetype** — the structural shape of an article (status/check, fee table, comparison, definitional entity, statutory spoke…). The dominant predictor of outcome in our backtest, scored differently on each channel.

**Cannibalization** — two or more of our own pages competing for the same query, splitting the signal so both lose. *Backward* cannibalization is against pages that already exist; *forward* is between new topics we are about to create.

**Citation-splitting** — the AEO equivalent of cannibalization: two of our pages splitting the citations for one tracked prompt.

**Clicks potential** — search volume discounted for SERP features (AI Overview, featured snippet, ads) that absorb clicks before the organic results. Always preferred over raw volume.

**Coverage gate** — the check that drops any topic the client already has a page on, in any status.

**Dual-play** — a topic scoring ≥70 on both the SEO and AEO columns. Our best briefs; routed to the hybrid writer.

**Fan-out (query fan-out)** — an AI engine decomposing one user prompt into several sub-queries behind the scenes. We map the tree and turn each sub-question into a heading, so one article answers many prompts.

**Information Island test** — could this section be lifted out of the article and still make complete sense? If not, it is not extractable.

**Information gain** — original data, analysis or insight not available elsewhere. Independently raises citation probability.

**KD ceiling** — the client's demonstrated difficulty limit, derived as roughly the 75th percentile of the keyword difficulty of SERPs where they already hold top-10. Used instead of a universal difficulty threshold.

**KGR** — Keyword Golden Ratio. `allintitle ÷ volume < 0.25`. A tiebreaker only, never a strategy.

**Orphan page** — a published page with no inbound internal links, carrying effectively zero internal PageRank.

**PAA** — People Also Ask. Unreliable or empty for India on our SERP tools; Google Autocomplete is our substitute.

**Parent topic** — the keyword the #1 ranking page actually gets most of its traffic from. Used to estimate traffic potential.

**Prompt registration** — creating the tracked prompt *before* the article is written, so the AEO outcome is measurable. An article answering an untracked prompt is permanently unmeasurable.

**Quick Answer** — the mandatory blockquote callout after the H1 (VS, JB, LC), 40–60 words, front-loading the actual answer.

**Soft-404** — a URL returning HTTP 200 while serving a generic page or the homepage instead of real content. Makes a 200 status meaningless as proof a page exists.

**Striking distance** — queries at position 5–20 with impressions and poor CTR. The fastest-moving opportunity bucket because the ranking signals already exist.

**Support lane** — an article whose job is to feed authority into a service or collection page, never to compete with it on the head term.

**Surface multiplier** — a score adjustment based on what share of the site's organic clicks the target section earns. A section under 1% of site clicks gets heavily discounted and takes no net-new spokes.

**Three-way sync** — the rule that FAQ text must match across the visible body, the CMS FAQ shortcode, and the JSON-LD schema. Editing one without the others is a scored failure.

**Token repair** — the humanization fix method: repairing only the small spans the humanizer corrupted, never reverting whole blocks, so the article stays fully humanized.

**Tracked prompt** — a question registered in the client's AI visibility tracking, scanned on a schedule for brand mentions and citations.

**Voice layer** — the first sentence under a heading, which must be a complete answer in under 29 words because voice assistants read exactly that aloud.

**Zero-visibility prompt** — a tracked prompt where the brand appears in no AI answer. A candidate for work, **not** automatically a candidate for a new article — diagnose crawlability, indexation and internal links first.