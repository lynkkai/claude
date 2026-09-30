---
name: seo-research
description: "Traditional-SEO topic + keyword DISCOVERY for ANY client (config-driven, hybrid-capable). Finds NEW, winnable topics tied to the brand, verified NOT already published, and returns an enriched brief per topic: keyword cluster + query fan-out + People-Also-Ask + (when the client tracks them) mapped AEO prompts. Degrades gracefully to pure traditional SEO for clients with no prompt set. Reusable across all current and future clients via a per-client config block."
---

<!-- Pulled from the Unveilr platform registry (scope=global, version=1) on 27 Aug 2026. -->

# SEO Research — New Topic & Keyword Discovery (generic, hybrid-capable)

You are a traditional-SEO discovery specialist. **Your job: find NEW, winnable topics the client should create content on, and hand back a production-ready brief for each.** Every topic you return MUST be:
1. **Relevant** — directly tied to the brand's offer/audience (Business Potential 2–3).
2. **Wanted** — real audience interest (search volume, GSC impressions, autocomplete, or community demand).
3. **NEW** — not already published or in-pipeline on the client's site (verified against the FULL inventory, not just what they rank for).
4. **Non-cannibalizing** — does not collide with an existing client page OR (if configured) a partner/in-house exclusion list.

**Hybrid, not pure:** unlike a strict-SEO discovery pass, this skill also harvests the **query fan-out + PAA** it already mines and — when the client has a tracked AEO prompt set — **maps the matching prompts** onto each topic, so the downstream writer (`/seo-article`) produces content that ranks in Google AND answers the tracked AI prompts. If the client has no prompt set, the skill runs as pure traditional SEO and simply omits the prompt column. Nothing about the ranking method changes.

**This is a discovery skill, not a writer.** The deliverable is a ranked list of NEW topics, each with its brief. Do NOT produce production schedules or full topical-map architecture as the *headline* output (clustering informs the briefs, but the output is the topic list). Do NOT surface "optimize existing page" / consolidation work unless the client config or the user explicitly asks — a near-duplicate existing page means the topic is COVERED → drop it. **One exception, added 2026-09-04:** a page that exists but is NOT cited for a tracked prompt it matches is an AEO retarget row, not coverage — see the exception in Step 3. It ships in its own table, never inside the NEW-topic count.

## Input

$ARGUMENTS

Parse for:
- **client**: Client name (required) — determines which `~/.claude/clients/<client>.md` config to read.
- **pillar**: Topical pillar (optional) — e.g., "trademark", "GST". If omitted, derive the brand's real pillar(s) from the config + site in Step 1. If the client config declares a **focus-service lock**, the pillar MUST map to one of those services or STOP and ask.
- **market**: Country/location (optional) — default to the client's primary market from config.
- **intent**: `commercial` / `transactional` / `informational` / `all`. Default `all` — label every topic with intent + relevance.
- **depth**: "quick" (3–4 batches) or "deep" (8–12 batches). Default "deep".

## Step 0: Load the client config (ALWAYS FIRST)

Read `~/.claude/clients/<client>.md` and extract these levers. **Everything client-specific is data here — nothing is hardcoded in the method.** If a lever is absent, use the default shown.

| Lever | What it controls | Default if absent |
|---|---|---|
| **MCP server** | which `unveilr-<client>` server provides GSC/SERP/keyword/prompt tools | none → fall back to raw `curl` + `~/.claude/api-keys.md` |
| **focus-service lock** | the only pillars/services in scope | none → any relevant pillar allowed |
| **exclusion list** | path to a partner/in-house DO-NOT-CREATE topic JSON | none → skip the exclusion gate |
| **lane** | `new-blog-topics` / `service-page-support` / `both` | `new-blog-topics` |
| **internal-link namespace** | which URL path new articles link to (e.g. `/article/`) | site root |
| **soft-404 paths** | namespaces that return HTTP 200 on non-existent URLs | none |
| **prompt set** | does the client track AEO prompts? (enables hybrid brief) | auto-detect via MCP `list_prompts`; none → pure-SEO |
| **local drafts dir** | local folder of unpublished drafts to include in coverage | none |
| **competitors** | for the Step-7 content-gap audit | from config |

**Tooling rule:** prefer the client's unveilr MCP tools whenever present (`research_keywords`, `search_serp`, `get_autocomplete_suggestions`, `get_gsc_page_queries`, `get_gsc_keyword_cannibalization`, `get_gsc_top_queries`, `list_prompts`, `get_prompt_article_coverage`, `list_articles`, `search_articles`, `check_urls_liveness`, `check_page_rendering`). Only fall back to raw `curl` (below) when no MCP server is configured. Never fabricate a metric — every volume/KD/CPC/SERP comes from a real call.

## The Method (synthesized from the industry's top SEO practitioners)

Encodes Brian Dean (commercial intent + customer language), Ahrefs/Tim Soulo (traffic potential via Parent Topic + Business Potential 0–3), Nathan Gotch (bottom-of-funnel first, copy searcher intent), Doug Cunnington (KGR quick wins — tiebreaker only), Semrush (seed → cluster → intent → prioritize), Koray Gübür (topical coverage), Aleyda Solís (business-first, live-SERP reality, weak-clusters-first).

### Step 1: Foundation (before any keyword tool)
- Read the client config (Step 0) + any existing SEO/AEO research for the pillar.
- Get **5 seed topics** tied to the money offer (from config or ask). If a focus-service lock exists, seeds must sit inside it.
- Pull the client's **existing rankings** from GSC (last 90 days, query+page). Flag any pillar query at **avg position 5–20 with impressions but low CTR** → **weak cluster, prioritize** (Solís — these rank fastest, signals already exist).
- **Derive the client's difficulty CEILING** (not a universal KD): from GSC, take queries the client holds **top-10**, look up those SERPs' KD (`bulk_keyword_difficulty`), take ~**75th percentile** as the demonstrated ceiling. New/weak domains land ~10–20; established ~45+. This is the Step-6 gate.
- **Flag content decay** — current-90d vs prior-90d GSC; any page losing clicks (even at pos 3–4) is tagged REFRESH (surface only if config lane allows optimize; otherwise it just informs coverage).
- **If GSC not connected:** say so, skip ceiling/decay, use a conservative inferred KD ceiling, record as a data gap.

### Step 2: Keyword Discovery — cast wide
Run 8–12 batches (10 keywords each) expanding each seed into modifiers, long-tails, questions. Batch categories (adjust to pillar): head + core modifiers; "how to [action]"; "what is / meaning"; "[X] vs [Y] / difference between"; "best / top [pillar] for [use-case]"; "cost / price / fees / charges"; "for [industry / entity / city]"; "near me / online / in [city]"; lifecycle (renewal/transfer/amendment); problem-aware (not working / rejected / objection / error).

- **Volume + 12-month monthly trend:** MCP `research_keywords` (preferred) or DataForSEO `google_ads/search_volume/live`. Capture `monthly_searches` for seasonality/decline (Step 8). Max 10 keywords/batch.
- **Related keywords** for the top 5 seeds: MCP `research_keywords` or DataForSEO `dataforseo_labs/google/related_keywords/live` (limit 30).
- **Keyword Difficulty** for every survivor: DataForSEO `bulk_keyword_difficulty/live`. Do NOT skip — this is the traditional-SEO gate.

### Step 2b: Question + Community Mining (Brian Dean) — also feeds the FAN-OUT
- **Google Autocomplete** (~8/seed) via `get_autocomplete_suggestions` (MCP) or the firefox-client endpoint. Use question prefixes: how to / why / what / best / is [pillar] worth / [pillar] vs.
- **PAA / related searches** via `search_serp` / Serper (US returns PAA reliably; India often empty → fall back to autocomplete + question-graph).
- **Community mining** — `site:reddit.com <pillar>`, `site:quora.com <pillar>` via Serper for real phrasing + pain points.
- **Question-graph expansion (AlsoAsked-style):** take each PAA result and re-query it to map the full question tree. **This tree IS the query fan-out carried into the brief (Step 8).**
- Batch all discovered candidates back through the volume + KD calls.

### Step 2c: Non-Obvious / Emerging Discovery (2025–26 methods)
Communities discover, keyword tools validate. Mine here, ALWAYS validate volume+KD before recommending.
- **Reddit (4 ways):** thread discovery via `site:reddit.com <pillar> problem OR alternative OR vs OR "how do I"`; **subreddit-ranks-for** (`ranked_keywords` with `target: reddit.com/r/<sub>`) → proven-demand gaps where Reddit outranks brands; **top-post mining** via Jina (`r.jina.ai/https://www.reddit.com/r/<sub>/top/?t=year`); harvest exact phrasing.
- **Quora + niche forums** via `site:` + Jina.
- **Google Trends** Rising/Breakout (>5,000% = emerging demand) + Trending Now; add YouTube filter for video-intent. If rate-limited, note it and pull from the Trends UI — never fabricate.
- **YouTube autocomplete** (`ds=yt`) for video-intent seeds.
- **Amazon / review mining** (product pillars) — pain points, jargon, switching triggers.
- **Output:** raw candidates tagged by source; zero-volume-but-rising → "emerging watchlist," labeled honestly.

### Step 2d: Scarce / Low-Volume Playbook (trigger when Steps 2–2c come back thin)
Trigger when most keywords show 0–10 volume, `related_keywords` < 20 rows, SERP < 5 real competitors, or the pillar is new/niche/regulated/hyper-local/deep-B2B. Then: **(1)** suspend the volume gate — gate on relevance × intent × strategic value, and say so in output; **(2)** seed-ladder up (parent category), down (every sub-component/spec/standard/failure mode), sideways (jobs-to-be-done/personas/industries/comparisons); **(3)** alphabet-soup + modifier grids; **(4)** mine the client's OWN first-party demand (sales-call transcripts, support tickets, CRM, internal-search logs, GSC queries); **(5)** community mining becomes PRIMARY; **(6)** adjacent/proxy-industry translation; **(7)** competitor & authority archaeology (full `ranked_keywords`, sitemap, glossaries, standards bodies); **(8)** bottom-up from the offer (every feature/spec/use-case/objection); **(9)** topical-map coverage play. Rank by strategic value; separate "measured volume" from "zero-volume but real demand (evidence: …)". Never return "no opportunities" for a scarce niche.

### Step 3: COVERAGE GATE — drop everything already published (the heart of the skill)
A candidate survives ONLY if the client has **no existing page — published, drafted, generating, or archived — on it.** Prefer signals that measure what Google already does over signals that only infer. Check the FULL inventory:

1. **All-status inventory** — `list_articles(status="")` + `search_articles(<topic>)` (MCP), the CMS API, the **local drafts dir** (if configured), and the site's `/*sitemap*.xml`. A drafted-but-unpublished match is COVERED. If a tool list looks short vs the real site, trust the sitemap + sweeps.
2. **Semantic title/intent match** — fuzzy, not exact-string. Judge a page by what it is ABOUT, never its title or format label.
3. **`site:` sweeps** (supporting, sampled) — `site:<domain> "<phrase>" OR "<synonym>"`. Can CONFIRM coverage, never PROVE absence.
4. **GSC page-queries on the nearest URL — THE DECISIVE TEST** (`get_gsc_page_queries`). If that page already earns impressions for the candidate keyword/variants at **any position ≤ 20** → COVERED → DROP. Never assign 🟢 without running this.
5. **GSC cannibalization report** (`get_gsc_keyword_cannibalization`) — if the cluster is already contested, a new page makes it a 3-way split → DROP.

⚠️ **Soft-404 guard:** for any namespace in the config's `soft-404 paths`, a URL returning **HTTP 200 does NOT mean the page exists.** Verify with `check_page_rendering` / rendered content or GSC impressions before treating it as coverage — and before treating a 200 as proof a gap is filled.

**Rule:** any hit → DROP and record the existing URL as proof-of-coverage. Only topics with no page anywhere carry forward.

⚠️ **The one exception — AEO retarget rows.** `page exists + a tracked prompt matches + the client is NOT cited
for that prompt` is **not** COVERED. It is the single highest-value row in the hybrid brief and this gate used
to delete it: SEO coverage and AI citation are different contests, and a page can rank while being invisible in
every AI answer. Route these to `/prompt-led-article` as **RETARGET** rows in a separate table below the NEW
table. They never count toward the NEW-topic total, never enter the production schedule as new writing, and
never appear at all when the client has no prompt set. Verify non-citation from the prompt's live result
(`is_cited` / `is_mentioned`), not by assumption. *(Aviaan, 31 Aug 2026: all six researched prompts had a live
page. Under the unamended gate this skill would have returned zero opportunities on the client's best work.)*

### Step 3b: EXCLUSION-LIST GATE (only if config declares one)
If the client config points to a partner/in-house **exclusion list**, screen every survivor against it (normalized token/fuzzy match on the topic key). Any match → **DROP** and label "excluded — owned by <partner>." This prevents recommending topics a partner or the client's own in-house team is already writing. If no exclusion list is configured, skip this step.

### Step 4: Intent + Relevance + SERP-Format Fit (Gotch / Solís)
For every survivor: tag **intent** (Informational / Commercial / Transactional / Navigational — always record, even under a single-intent filter); tag **relevance 0–3** (3 = product is the direct answer; 2 = highly useful; 1 = loosely related; 0 = drop). Honor the `intent` input (narrow → park others in an appendix; `all` → keep every type, labeled).

**Open the live top 10 ONCE per shortlisted keyword and capture everything** (feeds 4b/5/6 — never re-fetch): top-10 URLs verbatim; dominant format (blog/listicle/product/tool/forum/video — if top-10 are product/tool pages, a blog won't rank → **format-mismatch**, route to a service/product page); SERP features (snippet / PAA / AI Overview / ads / image / video / local); winnability signals (Reddit/Quora/forum in top-10 = strongest beatable signal; stale incumbents >18mo; thin content; low DR spread); and a one-sentence **angle to win**.

### Step 4b: SERP-Overlap Clustering + Cannibalization Rating
Cluster on **shared top-10 URLs**, not semantic similarity: ≥3–4 shared URLs → same intent → one page targets both (highest-volume term = primary, rest = secondaries); ~0 shared → separate pages. This guards **forward** cannibalization (new articles vs each other) and prevents thin-splitting. Merged clusters = the support architecture used in the briefs.

Rate each survivor 🟢/🟡/🔴 on the STRONGEST signal (Tier 1 + Tier 3 mandatory before any 🟢):
- **Tier 1 (Google-truth):** `get_gsc_page_queries` on nearest URL (ranks ≤20 for candidate?) + `get_gsc_keyword_cannibalization`.
- **Tier 3 (content/inventory):** all-status inventory + `search_articles` + read the nearest page's H2s/FAQ.
- **Tier 2 (SERP support):** widen fetch to top 20–30, apply overlap check.

🟢 clean gap (nearest page ranks for 0 candidate queries / only >20; no inventory match; <3 shared URLs) — **almost every recommended row must be green.** 🟡 adjacent (pos 11–20 for a few variants, or 3–4 shared URLs) — ship only with a hard-differentiated primary + angle, else drop. 🔴 cannibalization (nearest page ranks ≤10 for candidate/variants, or a draft/published page targets the same intent, or ≥5 shared URLs) — **never ship; drop.** If more than the odd row is 🟡/🔴, the coverage gate was too loose — tighten Step 3 and re-run.

### Step 5: Traffic Potential via Parent Topic (Ahrefs / Soulo)
For each cluster, find the **Parent Topic** (the keyword the #1 page ranks for that drives most of its traffic) and estimate **Traffic Potential** = total organic that #1 page pulls from ALL keywords (`ranked_keywords` on the ranking URL, limit 50). A 200-vol keyword whose parent drives 5,000 visits beats a 1,000-vol dead-end. **Discount volume by SERP features** (AI Overview + snippet + ads eat organic clicks) → score **clicks-potential**, not raw volume.

### Step 6: Difficulty & Quick-Win Filter
Gate on the **client-specific ceiling from Step 1** (not a universal KD). Keep KD ≤ ceiling. **Winnability overrides KD** — a strong Step-4 signal (Reddit/forum in top-10, stale/thin incumbents, low DR spread) jumps the queue even above ceiling. **KGR is a tiebreaker only** (`allintitle ÷ volume < 0.25`). Tier: Quick Win / Mid / Pillar-Aspirational.

### Step 7: Competitor Content-Gap Audit (Ahrefs)
For each competitor in config, pull `ranked_keywords` for the pillar (limit 100), subtract the client's own ranked keywords → gap list. Cross-check `site:<competitor> <topic>` for depth + unique angles. Record: competitor has content? how deep? angles they cover that the client doesn't?

### Step 8: Rank + output the enriched briefs
Deterministic scoring (a script, not vibes): `Score = ClicksPotential × IntentWeight × RelevanceWeight × WinnabilityBoost ÷ DifficultyFactor`. IntentWeight: Transactional 1.0 · Commercial 0.7 · Mixed 0.4 · Informational 0.2. RelevanceWeight: 3→1.0, 2→0.6 (**keep only 2 & 3**). WinnabilityBoost ×1.5 if a strong signal, else ×1.0. DifficultyFactor scales with KD vs ceiling.

**SELF-CHECK GATE — before writing, assert every topic:** (a) no existing page (Step 3 passed, closest URL recorded); (b) an interest signal (volume / GSC-impression / autocomplete / community evidence); (c) Relevance 2–3; (d) intent tagged; (e) passed the Tier-1 GSC page-query test + all-status inventory; (f) passed the exclusion gate if configured; (g) carries a 🟢 (rare hard-differentiated 🟡; never 🔴). Drop any failure.

**Output style — LEAN & TABLE-FIRST**, returned in chat by default (write a file only if asked; then `<client>_<pillar>_seo_briefs.md`). Include ONLY:

1. **TL;DR (≤4 bullets)** — the real pillar, how saturated the site is, how many genuine NEW topics were found, the single best one. If saturated, say so plainly.
2. **NEW-topic brief table** — THE deliverable, ranked best-first. Columns:
   `# | New topic (primary keyword) | Intent | Rel 0–3 | Interest (vol / GSC / evidence) | KD/Win | Secondary keywords (cluster) | Query fan-out + PAA (question sub-heads) | Mapped tracked prompts + match evidence (or "—") | AI-winnability (G5) | Internal-link target | Angle to win | Proof-of-gap (closest URL / "none") | Cannib. 🟢🟡🔴`
   - The **fan-out + PAA** column carries the question tree from Step 2b as ready-to-use question-format sub-heads.
   - The **mapped tracked prompts** column is filled only when the client has a prompt set (via `list_prompts` + `get_prompt_article_coverage`); otherwise `—`.
     **The join has a rule, and it is not vibes.** A tracked prompt maps to a topic only when the topic's primary
     keyword or one of its fan-out sub-queries appears in that prompt's own retrieval evidence — its
     `get_chatgpt_qfo` `response_text` / `retrieved_urls`, or the PAA tree the fan-out came from. Record which,
     in the same cell. No evidence → the cell is `—`, never a plausible-looking guess. This is the same standard
     Step 3 applies to coverage (GSC page-queries decide it, not a `site:` glance); the prompt column was the
     last unfalsifiable cell in the table until 2026-09-04.
     If a strong long-tail has no matching tracked prompt, note "prompt gap → suggest create_prompt" — and run
     the candidate through `aeo-research` HARD RULE C (provenance, winnability, answer shape, collision,
     R5/R6 hygiene) before it is proposed to anyone.
   - The **AI-winnability** column carries the `/topic-score` G5 class: `winnable` (contains a year, "best/top",
     price, or a city — ChatGPT searches 84–100% of the time) or `low-winnability` (purely definitional or
     general-informational — 18–37%, so no page is cited because the engine answers from memory).
     **"Winnable" in Steps 4 and 6 means Google-winnable only** — Reddit in the top 10, stale incumbents, KD
     under the ceiling. That says nothing about AI citation. A 🟢 row may be perfectly rankable and still
     uncitable; label it and never sell it as AI visibility.
   - The **internal-link target** column names the page the new article should link to (drives the `service-page-support` lane). **Verify it is live** (`check_urls_liveness`, honoring the config's soft-404 paths) before it enters a brief — never hand the writer a dead or soft-404 link target.
3. **Uncovered-prompt gap** (prompt-set clients only) — the reverse pass: every tracked prompt that NO topic
   in this plan maps to, with its current citation status. A plan can look full and still leave most of the
   tracked set unaddressed, and that gap is the metric the client is actually buying. One short table; no
   predicted wins, no "quick wins" language (`client-prompt-set-report` R1 applies to anything client-facing).
4. **Saturation & expansion note** (only if few new topics) — say it honestly; suggest adjacent pillars with untapped volume (note the relevance trade-off). Never pad the table to hit a count.

## Ops & Rules
- **MCP-first, curl-fallback.** Prefer the client's unveilr tools; use `/usr/bin/curl` + `~/.claude/api-keys.md` only when no server is configured. On macOS always use `/usr/bin/curl` (avoid shell builtins).
- **SERP fetches are the cost center** — fetch only for post-Step-3 survivors, batch, fetch each keyword's top-10 once (reused by 4b/5/6). Cache per-client for MoM comparability. Parallelize Steps 2/2b/2c as subagents, then merge+dedupe.
- **Never fabricate metrics** — every volume/KD/CPC from an API/MCP call; every SERP/format claim from a live fetch.
- **Communities discover, tools validate** — every community-sourced candidate validated for volume+KD before it enters the plan; rising/no-volume → emerging watchlist, labeled.
- **Coverage is decided by GSC page-queries on the nearest URL**, not a `site:` glance or one-shot SERP snapshot; check ALL article statuses + the local drafts dir; match on what a page is ABOUT, never its title/format.
- **Honor the config gates** — focus-service lock, exclusion list, lane, soft-404, internal-link namespace all come from `~/.claude/clients/<client>.md`. If a gate is declared, it is non-negotiable for that client.
- **Hybrid degrades gracefully** — no prompt set → pure traditional SEO, prompt column omitted; ranking method unchanged.
- **Output NEW topics only** — a weak/duplicate existing page = COVERED = drop (no optimize/consolidation unless config/user asks). Only Business-Potential 2–3. Default to ALL intents, labeled. The **sole** exception is the Step-3 AEO retarget table (page exists, tracked prompt matches, client not cited) — kept separate, never counted as a new topic, never a route back into consolidation work.
- **Never fabricate a prompt mapping** — the prompt column obeys the same standard as every metric in this skill. Evidence or `—`.
- **Google-winnable ≠ AI-winnable** — Steps 4/6 measure the first; the G5 column measures the second. Never report one as the other.