---
name: seo-article
description: Write a keyword-optimized SEO article from a /seo-research brief. Consumes the brief's primary+secondary keywords, query fan-out + People-Also-Ask (as question-format sub-heads), mapped tracked AEO prompts (answered in-body), and the internal-link/service-page target. Produces content engineered to pass BOTH /seo-score (ranking) and /aeo-score (citation), then hands off to the client humanizer. The hybrid writer: ranks in Google AND answers the tracked AI prompts.
---

<!-- Provenance: Unveilr platform registry · category=content · version=2 · scope=global · synced 2026-08-25 -->
<!-- AVIAAN: no client calibration block exists below. Aviaan qualifies for full hybrid mode
     (it tracks prompts). Apply: AED currency, UAE/British spelling, location_code 2784,
     the 5 excluded competitor domains, and the 8-14 internal link band. -->

## ⛔ HARD RULE — Every article MUST earn 1–2 INBOUND internal links (not just outbound)

Outbound links from the article are NOT enough. Every article we publish MUST also receive **at least 1–2 INBOUND internal links** — existing, live, topically-relevant pages on the SAME domain that link **TO** this article. Otherwise it launches as an internal-link orphan with ~0 internal PageRank and loses to in-house/competitor pages that sit inside the site's link mesh (diagnosed on the VS CIN cannibalization case, 2026-07-22: our page got 0 GSC impressions vs the in-house page's ~602, decided by inbound links 1 vs 4 — schema was identical on both). This is the INBOUND complement to the outbound link cap and is counted separately.

At/after publish you MUST:
1. Find 1–2 existing, live, topically-adjacent pages on the same domain (sibling cluster pages, the mapped service/collection page, or a related guide).
2. Add a natural, contextual link from EACH of those pages TO this article — descriptive anchor, never "click here", never a duplicate of an anchor already on that source page.
3. Verify the inbound links are live on the source pages (check_urls_liveness / fetch the source) before marking the task done.

If no relevant sibling exists to link from, FLAG it — do NOT silently publish an orphan.


## ⛔ HARD RULE — H2s MUST come from a SOURCED query fan-out, never invented

An answer engine decomposes a question into sub-queries before it answers. Those sub-queries are the **query fan-out**. Making them your H2s means every retrievable chunk is already scoped to one sub-question with its answer in the first sentence. Headings that are not fan-out queries retrieve for nothing, however good the prose beneath them.

**The `/seo-research` brief should supply the fan-out + PAA. Verify it — do not trust it.** If the brief carries fewer than 6 usable fan-out queries, or is older than ~14 days, source the remainder yourself before drafting. Work this cascade in order and record which source produced each query in the handoff:

| # | Source | Tool | Reliability |
|---|---|---|---|
| 1 | Query fan-out | `get_chatgpt_qfo` / `get_chatgpt_qfo_batch` | **Frequently empty — check `qfo_count`, never `status`** |
| 2 | People Also Ask | `search_serp` → `people_also_ask` | Empty outside the US (AE and IN measured empty) |
| 3 | Autocomplete | `get_autocomplete_suggestions` | Reliable but thin; **geo-anchor every seed** |
| 4 | SERP decomposition | `search_serp` organic titles + the H2s of the top 3 | Always available; the dependable fallback |
| 5 | GSC | `get_gsc_page_queries`, `get_gsc_top_queries` | Best evidence of how real users phrase it |

**Blocking conditions — any one of these stops the draft:**
- **Fewer than 6 sourced fan-out queries → STOP and report.** Never invent headings to reach the count.
- **`qfo_count: 0` with `status: "ok"` is a tool success and a research failure.** Fall through to the next source; never record it as "this topic has no fan-out".
- **An empty `people_also_ask` array is normal outside the US.** Fall through to sources 4–5 rather than concluding the fan-out is empty.
- **Bare autocomplete seeds return the wrong market** (`rera compliance` → Maharashtra/Hindi results). Anchor every seed to the client's city/country, and add a disambiguation block to the body where a term collides across markets.
- **Dead headings are a FAIL.** "Key considerations", "Cost drivers and what to expect", "Understanding the basics", "What you need to know" — if it is not a query a real person would type, it does not ship.
- **An H2 the research cannot actually answer gets CUT, not hedged.** A hedging section is worse than an absent one.
- **No near-duplicate padding.** Re-phrasings of the same query stuffed in as separate H2s read as keyword stuffing and dilute the exact-match signal.


## ⛔ HARD RULE — the ~200-character clip, and the title ChatGPT actually matches

Two measured rules that decide whether the AEO half of this hybrid pays off at all. Full mechanics and
bounds: **`~/.claude/aeo-best-practices.md` PART G** (first-party, 530 ChatGPT searches, position-controlled).

**1. The clip.** ChatGPT clips **~200 characters — about two lines — from each retrieved page**: the stretch
best matching its own search words, and it writes the answer from that clip. A page can rank, get retrieved,
and never be cited because the two lines it surrendered held no facts.

Every section — Quick Answer, every H2/H3, every FAQ answer — opens with an **answer paragraph**: ~2
sentences, the section's search words used naturally, **one number, one concrete claim**. A section whose
first 200 characters contain no number and no concrete claim is a FAIL; so is any throat-clearing opener
("In this article we will explore…", "Choosing the right X can be overwhelming…"). Adding a stat lower down
does not fix it.

Self-check before scoring: `python3 ~/.claude/scripts/clip_check.py articles/<slug>.md`. It prints the real clip per
section and flags those with no numeral — **triage, not a verdict**: judge the concrete-claim half yourself.
Target **≥50% of section clips carrying a number** (median across our shipped corpus is 36%).

**2. The title is two different contests.**
- `meta_title` — Google's. Keep the client's ≤60-char rule and its keyword-placement requirements below.
- **On-page title / H1 — ChatGPT's.** Measured sweet spot **13–15 words as one natural sentence** (24+ words
  is the worst bin). **Never the word "Official"** (cited 5× less: 13% vs 61%). **"Best/Top 10" styling** is
  placed higher but cited less at equal position — earn it from the SERP format, not from habit. The **year
  is a trade-off**: it helps discovery on recency prompts, slightly hurts citation. Slugs stay evergreen.
- **Write the title against the search ChatGPT types, not the human's question.** It drops ~half the user's
  words and adds its own ("2026", the country, "reviews", "fees"). Matching the *rewritten* line moves top-3
  chances **~15% → ~35%**. Capture it with `get_chatgpt_qfo` (single tool, never `_batch`) and take the line
  from the brief where `/seo-research` supplied it.

Where keyword placement (non-negotiable 2) and the 13–15 word natural sentence pull against each other,
**the natural sentence wins on the H1 and the keyword rule is satisfied in `meta_title`, the slug and the
first 100 words** — keyword stuffing is measured negative on both channels.


## ⚠️ Before you write: is an on-domain article even the right asset?

On **unbranded discovery questions** ("best X in India"), the client's own page **loses ~2 of 3 head-to-heads**
against an independent article at the same position, and independent roundups convert appearance→citation at
**50–100%** vs a brand's own **22–34%**. On **branded** questions ("is [client] any good?") the client's own
page wins outright.

This is a routing call, not a writing fix. If the brief's target is unbranded discovery intent and the goal
is AI citation, **say in the handoff that getting the client named in the third-party comparison pages
ChatGPT already cites outranks another on-domain post** — then write the article if it still earns its place
on SEO grounds. Do not silently ship the weaker instrument. (News citations are worth ~⅔ of a normal citation;
a cited editorial or comparison page is better than press.)


# SEO Article Writer (consumes a /seo-research brief)

The writer stage of the SEO pipeline: **`/seo-research` → `/seo-article` → `/seo-score` (+ `/aeo-score`) → humanize.** It is keyword-led but structurally AEO-native — so one article ranks organically and answers the tracked prompts.

**Read first:** the `/seo-research` brief for this topic (primary source of truth), `~/.claude/aeo-best-practices.md`, and the client context `~/.claude/clients/<client>.md`.

## Input

$ARGUMENTS

Parse for:
- **brief**: path to the `/seo-research` output for this topic (strongly preferred — supplies everything below). If absent, accept **client + primary keyword** and fetch the missing pieces live (SERP, fan-out/PAA, tracked prompts) before writing.
- **client**: `vakilsearch` | `caredale` | `jaagrukbharat` | `nuyug` | generic.

From the brief, extract and lock: **primary keyword · cluster · search intent · dominant SERP format · secondary keywords · query fan-out + PAA · mapped tracked prompts · internal-link/service-page target · competitive SERP-median depth · angle to win.** If any is missing, derive it before drafting — never write blind.

## Non-negotiables (these are what /seo-score + /aeo-score will gate on)

1. **Match the SERP format from the brief.** If the winning format is a guide, write a guide; if comparison, write the comparison. If the brief flagged format-mismatch (top-10 are product/tool pages), STOP — this should be a service-page task, not an article.
2. **Keyword placement (SEO):** primary keyword in the title/H1, `meta_title` (first 50 chars), `meta_description` (once), the **slug**, the **first 100 words**, and ≥1 H2. Density **0.5–1.5%** — natural, never stuffed. Every **secondary keyword** appears ≥1×; weave ≥5 LSI/related terms.
3. **Structure (AEO):** short direct title phrased as the target query; **Quick Answer** callout after H1 + Last-updated line; **question-format headings**; answer-first sections; long content chunked into H3 sub-heads. **The fan-out + PAA questions from the brief become the H2/H3 sub-heads** — this is the shared SEO/AEO win, and it is a HARD RULE (see the Fan-Out hard rule above): 6–9 sourced queries minimum, none invented, no dead headings.
4. **Answer the mapped tracked prompts** in-body (design the relevant sub-heads so an AI engine can extract the answer). If a strong long-tail had no prompt, note "prompt gap → create_prompt" in the handoff, do not invent one.
5. **Depth to beat the SERP:** meet or exceed the brief's **SERP-median depth** and cover every subtopic the ranking pages cover (this is `/seo-score` G3). Density over padding.
6. **Internal link to the service/target page** from the brief (support-lane), with a descriptive keyword-rich anchor — never compete with its head term. Respect the client link cap; 2–3 external authority links. **Every link verified live** before finalize (no non-200 / soft-404).
7. **Data density (AEO):** statistics, dated facts, tables for any 3+ comparable data points, entity-clear definitions ("X is Y") in the first 100 words.
8. **FAQ block** built from the remaining PAA/fan-out questions, synced across body + schema.

## Workflow

1. **Load & lock the brief** — extract the fields above; confirm the topic passed the research gates (9-service/exclusion/coverage for VS). If the brief is stale (>~14 days), re-verify the SERP + cannibalization before writing.
2. **Outline from the fan-out** — turn the brief's fan-out + PAA question tree into the H2/H3 skeleton (question-format), each mapped to the keyword(s) and tracked prompt(s) it serves. Slot the internal service-page link and external authority links.
3. **Draft answer-first** — Quick Answer → definition in first 100 words (with primary keyword) → each question section answered in the first 1–2 sentences, then detail. Tables where the brief flagged comparable data. Hit keyword placement + density targets as you write, not after.
4. **Self-check against the gates** — before scoring, verify keyword placement/density, SERP-format match, depth vs SERP-median, link liveness, question headings, Quick Answer, prompt coverage.
5. **Score** — run **`/seo-score <slug>`** (must be ≥85 AND all ranking gates pass) and, where the article also serves AEO, **`/aeo-score <slug>`** (≥80). Fix priority items, re-score. For mechanical SEO fixes use `/seo-optimize <slug> fix=safe`.
6. **Humanize** — only after both gates pass, hand to the client humanizer (`/humanize-<client>`). Do NOT auto-publish; publishing needs explicit client approval.

## Output (frontmatter the scorers + push expect)

Produce a single `.md` with frontmatter: `title`, `meta_title`, `meta_description`, `slug` (evergreen — see client rules), `keywords` (primary first, then secondaries), `cluster`, `internal_link_target`, `tldr` (Quick Answer / excerpt), `author`, `featured_image_path` (if applicable), plus a **handoff note** listing which tracked prompts the article answers and any prompt gaps. Body: markdown with the question-format headings, Quick Answer callout, tables, FAQ, and synced FAQ schema.

## Client calibration

- **vakilsearch** — brand `Vakilsearch` (lowercase s); `%` symbol no space; ₹ symbol; **formal legal register, NO contractions**; **slug evergreen, NO year** (title/H1/meta keep the year); internal links `/article/` only (never `/blog/` `/advice/` — soft-404); the internal link must be the cluster's **service page** (support-lane); topic must sit in the 9 services and be clear of `vs_inhouse_exclusion.json` (already gated in research — re-confirm); humanize via `/humanize-vakilsearch` (token-repair recipe). **Word count 2,000 (STRICT, client instruction 2026-07-23)** — target 2,000, acceptable band 1,900–2,100; do NOT fall back to the old 1,500–1,600 default or stretch to SERP-median.
- **jaagrukbharat** — plain citizen-friendly voice; contractions allowed; 900–1,300 words (ceiling 1,500); cannibalization/link-check includes the `/feeds` blog; slug evergreen no-year; humanize via `/humanize-jaagrukbharat`.
- **nuyug** — celebration/occasion jewellery only; link to `/collections/<slug>`; link cap 5–6; competitor brands never hyperlinked; Curated Picks grid above FAQ; word cap 1,800; humanize via `/humanize-nuyug`.
- **caredale** — filter scope = hardness, chlorine and physical contaminants; author Roshni; 3-layer filtration facts; humanize via `/humanize-caredale`.
- **generic** — apply the brief + non-negotiables; skip client-specific gates.
- **lynkk** (added for this repo) — brand is always **Lynkk** / lynkk.ai (double k). Market: United States, US English, `$` currency, Ubersuggest `locId 2840`. **Never use em dashes or en dashes** (house rule, overrides any template). Brief source: `seo/keyword-map-v2.md` (primary + secondary keywords) and `seo/content-briefs.md` (E-E-A-T rules, templates, questions). Product facts come only from `memory/lynkk-brand.md`; anything under its "To confirm" list is written as a `[CONFIRM: ...]` placeholder, never stated as fact. Lynkk is always ranked #1 / best overall and presented positively; competitors are described factually. Listicles and "Lynkk vs" posts carry the disclosure box and a "How we tested" section; competitor pricing is dated and linked to the vendor's own page. Output goes to `articles/<slug>.md`. Word count: follow the template band in `seo/content-briefs.md` Part 3. Tools available here: Ubersuggest (`serp_analysis`, `google_suggestions`, `match_keywords`, `keyword_overview`) and web search/fetch stand in for `search_serp`, `get_autocomplete_suggestions` and `get_chatgpt_qfo`, which are not available. GSC is not connected. Humanize by self-editing against `memory/unveilr-skills/humanize-verify.md` signals (varied sentence length, no AI-tell words, no em dashes).

## ⛔ HARD RULE (Lynkk): never link to competitors

No hyperlink, bare URL or schema URL in a Lynkk article may point to a competitor's website (Otter, Fireflies, Fathom, Granola, Jamie, Read AI, Plaud, Pocket, tl;dv, Krisp, Tactiq, Notta, Gong, Zoom, Microsoft, Google product pages, or any other tool we compare against). Competitor names appear as plain text only. Competitor facts are cited as plain text ("Source: Fireflies pricing page, checked <date>"), with no URL anywhere (not in handoff notes, audits or chat replies either). External links, when needed for authority, go only to neutral sources (government, legal, standards bodies, independent research). Any competitor link found in a draft is a CRITICAL fail: remove it before scoring. This overrides the generic "2-3 external authority links" guidance where the only available source would be a competitor.

## ➕ Keyword expansion "bypass" (Lynkk rule)

The brief's keyword list is the floor, not the ceiling. While outlining or drafting, whenever a sub-topic, H2 or FAQ suggests a search phrase that is NOT already in the brief:
1. Look it up in Ubersuggest (`match_keywords` or `keyword_overview`, `locId 2840`) before using it.
2. Add it if it is relevant to the article's intent, has measurable US volume, and is **not the primary keyword of another post** in `seo/keyword-map-v2.md` (no cannibalization).
3. Use it naturally as an H2/H3, FAQ question or body phrase. Never stuff.
4. Record every added keyword with its volume / SD in the frontmatter `keywords_added` list and in the handoff note, so the keyword map can be updated.

## Important rules
- **The brief is the contract** — do not drift from its primary keyword, cluster, intent, or link target. If the brief is wrong, fix it in `/seo-research` and regenerate — don't paper over it in the writer.
- **Rank AND cite** — never sacrifice the AEO structure for keyword density, or vice versa; both scorers must pass. If they conflict, prefer the answer-first question structure and hit density through natural secondary/LSI usage, not stuffing.
- **Never fabricate** — every stat/fact verified; every link live; every claim answerable. Legal/statutory facts (VS/JB) get the factual-verification pass before scoring.
- **Do not chain to publish** — stop after humanize; publishing is a separate, explicitly-approved step.
