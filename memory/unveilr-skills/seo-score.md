---
name: seo-score
description: Score a completed article draft against traditional-SEO ranking best practices before humanization — the SEO twin of /aeo-score. Reuses /seo-optimize's S1–S12 dimensions (scoring-only, no auto-fix) and adds keyword-led RANKING-REALITY gates (search-intent/SERP-format match, keyword-uniqueness/cannibalization, competitive depth vs SERP median). Inherits the shared structural checks from /aeo-score by reference. Gate: score >= 85 AND all ranking gates pass = proceed; else fix first.
---

<!-- Provenance: Unveilr platform registry · category=content · version=2 · scope=global · synced 2026-08-25 -->
<!-- AVIAAN: no calibration block below. GSC is connected as sc-domain:aviaanaccounting.com, so G2a/G2c
     are fully runnable. No exclusion list configured -> G2b skipped. S8 band = generic 1,500-2,500 cluster. -->

## ⛔ HARD RULE (GATE) — INBOUND internal links required

Treat inbound internal links as a HARD scoring gate. Every article MUST earn **at least 1–2 INBOUND internal links** — existing, live, topically-relevant pages on the SAME domain that link **TO** this article — separate from and in addition to the article's own OUTBOUND links. An article with **0** planned/placed inbound links **FAILS this gate** (it launches as an internal-link orphan with ~0 internal PageRank; diagnosed on the VS CIN cannibalization case, 2026-07-22: our page 0 GSC impressions vs the in-house page ~602, decided by inbound links 1 vs 4 — schema was identical). To PASS: name 1–2 live sibling source pages + the exact anchor text that will link to this article, and verify them live. If no relevant sibling exists to link from, FLAG it — do not pass silently.


# SEO Article Scorer (the SEO twin of /aeo-score)

Run this in the **SEO pipeline** (`/seo-research` → `/seo-article` → **`/seo-score`** → humanize), after `/aeo-score` where the article also serves AEO. It is **scoring-only** — it does not auto-fix (that is `/seo-optimize`'s job). Its role is the humanize gate for keyword-led content.

**Reference:** `~/.claude/skills/seo-optimize/SKILL.md` for the detailed row-level criteria of S1–S12 (this skill scores the same rows, it does not restate them), and `~/.claude/skills/aeo-score/SKILL.md` for the shared structural checks inherited in Part 3.

## Input

$ARGUMENTS

Parse for:
- **articles**: one or more slugs or `.md` paths (required); `all` scans `articles/`.
- **client**: `vakilsearch` | `caredale` | `jaagrukbharat` | `nuyug` | generic (optional — enables client calibration).
- **brief**: (optional) path to the `/seo-research` brief for this article — supplies the target primary keyword, cluster, intent, SERP-format, fan-out/PAA, and service-page link target. If absent, derive the primary keyword from frontmatter and fetch a fresh SERP for the ranking gates.

## How to score

Read the article completely. Score **Part 1 (S1–S12, 100 pts)**, evaluate **Part 2 (ranking gates, pass/fail, can hard-cap)**, and confirm **Part 3 (inherited structural, pass/fail)**. Be strict — partial credit only when most criteria are met. Hyphen-insensitive matching for every keyword-presence check.

---

## PART 1 — SEO dimensions (S1–S12, 100 pts) — reused from /seo-optimize, scoring-only

Score each exactly as defined in `/seo-optimize` (do not re-invent thresholds):

| Dim | Dimension | Pts |
|---|---|---|
| S1 | Meta tags & SERP snippet (title ≤60 w/ keyword in first 50, meta 150–160, slug ≤7 words keyword-in-slug no stopwords, OG, canonical) | 15 |
| S2 | Heading hierarchy & keyword placement (keyword in H1 + ≥1 H2, clean H1→H2→H3, heading every 150–250w) | 10 |
| S3 | Primary & secondary keyword usage (keyword in first 100w, density 0.5–1.5%, each secondary present, ≥5 LSI terms) | 15 |
| S4 | Internal linking (count healthy, link to pillar/service page, ≥2 sibling cross-links, descriptive anchors) | 10 |
| S5 | External linking & authority (≥2 authority links, correct rel) | 5 |
| S6 | Image SEO (featured present, alt 8–15w w/ keyword, inline alts, descriptive filenames) | 10 |
| S7 | Schema markup (Article, FAQPage synced, BreadcrumbList, inLanguage; **HARD −10 if @type:Product nested in Article**) | 10 |
| S8 | Content depth & engagement (word count band, sentences ≤22w, paragraphs ≤4 sentences, lists for 3+ points) | 10 |
| S9 | Mobile-friendly markup (tables ≤4 cols, paragraphs ≤100w, sentences ≤40w) | 5 |
| S10 | E-E-A-T signals (author + bio, visible Last Updated, ≥1 source citation) | 5 |
| S11 | URL & link health (all internal 200, all external 200/resolving-redirect — live-check every run) | 5 |
| S12 | Binary checklist (uniqueness, cannibalization-clean, image dims, draft state, noindex not set) — folded into Part 2 gates below | 0 |

**Part 1 total: /100. Publish gate = ≥ 85** (SEO is more sensitive to thin coverage than AEO; 70–84 = minor fixes, <70 = do not publish).

---

## PART 2 — RANKING-REALITY GATES (binary — these can HARD-CAP the article)

These are the checks neither `/aeo-score` nor `/seo-optimize` performs. They answer *"can this article actually rank for its target keyword, and should it exist?"* A perfectly optimized article aimed at an un-winnable or cannibalizing keyword must NOT pass, regardless of its S-score. **Any gate failure caps the verdict at ❌ FIX REQUIRED** and is listed at the top of priority fixes.

- **G1 — Search-intent & SERP-format match.** Fetch the live top 10 for the primary keyword (or read it from the brief). Does the article's format match what ranks (guide/listicle/comparison/tool/product)? If the top 10 are product/category/tool pages and this is a blog → **FAIL** (format-mismatch, cannot rank — route to a service/product page instead). Does the article satisfy the dominant intent (informational vs transactional)? Intent mismatch → **FAIL**.
- **G2 — Keyword-uniqueness / cannibalization.** (a) Run `get_gsc_page_queries` on the nearest existing client URL — if another of our pages already ranks ≤ pos 20 for the primary keyword or close variants → **FAIL** (cannibalization; this article splits the signal). (b) If a client exclusion list is configured, screen the primary keyword/topic against it → any match = **FAIL** (owned by partner/in-house team). (c) `get_gsc_keyword_cannibalization` — cluster already contested → **FAIL**.
- **G3 — Competitive content depth vs SERP median.** Compare the article's word count + subtopic coverage against the **median of the top-10 ranking pages** for the keyword (not an absolute band). Materially thinner than what ranks (e.g. < ~60% of SERP-median depth, or missing subtopics every ranking page covers) → **FAIL**. This replaces S8's absolute word-count band with a competitive benchmark for the ranking verdict.
- **G4 — Query fan-out integrity (headings must be retrieval targets).** Read every H2/H3 and ask: *is this a query a real person would type?* Score the outline as retrieval targets, not as prose signposts.
  - Any **dead heading** ("Key considerations", "Cost drivers and what to expect", "Understanding the basics", "What you need to know", "Who actually writes these") is a defect: list it in priority fixes with a suggested replacement query.
  - **Two or more dead headings → FAIL.** Send it back to the writer to re-derive the outline from a sourced fan-out. This mirrors `/aeo-score`'s Gate A block so the SEO and AEO halves of Gate A cannot disagree.
  - **Fewer than 6 question-format / fan-out H2s → FAIL.** The writers require 6–9 sourced fan-out queries before any heading is written; an article that arrives with fewer did not run the fan-out.
  - If a `/seo-research` brief was supplied, spot-check that the H2s trace to its fan-out/PAA rows rather than to the writer's imagination. **An unsourced H2 is a defect even when it reads well.**
  - This is a scorer: do not re-run the fan-out tools. You DO need to reject headings no query could have produced.

---

## PART 3 — Inherited structural checks (from /aeo-score — binary PASS/FAIL, not re-scored)

The hybrid SEO article shares AEO's structure. **If `/aeo-score` already passed (≥80) for this article, mark this whole section PASS by reference.** Otherwise verify each (detail lives in `/aeo-score` D1/D2/D8):
- [ ] Short, direct title/H1 phrased as the target query (+ year where house rules allow); **slug evergreen, no year**.
- [ ] Question-format headings; answer-first sections.
- [ ] Quick Answer callout after H1 + Last-updated line.
- [ ] Long paragraphs chunked into H3 sub-heads in question format (fan-out/PAA as sub-heads).
- [ ] Link count within the client cap; every link live (no non-200 / soft-404).

A failure here is a structural regression — list it in priority fixes; it does not add points but blocks the gate the same way `/aeo-score` does.

---

## Client calibration

- **vakilsearch** — exclusion list = `clients/vakilsearch/vs_inhouse_exclusion.json` (G2b mandatory). Primary keyword must map to one of the 9 services; internal link (S4) must include the cluster's **service page** (support-lane). Brand `Vakilsearch` (lowercase s), `%` no space, no-year slug (CRITICAL binary fails, per `/aeo-score` D9). **GSC covers `vakilsearch.com` only** — run G2a there; check `zolvit.com` via live SERP, not GSC. Soft-404 guard on `/blog/` `/advice/` for S11/G2. **Word-count for S8: target 2,000 (STRICT, client instruction 2026-07-23) — score full marks at 1,900–2,100; deduct outside that band. Do NOT apply the generic 1,500–2,500 cluster band to Vakilsearch.**
- **jaagrukbharat** — S8 band 900–1,500 (brevity); contractions allowed (do not fail); brand "Jaagruk Bharat"; cannibalization must include the `/feeds` blog.
- **nuyug** — S4 must link `/collections/<slug>`; link cap 5–6; competitor domains never hyperlinked (CRITICAL); word-count cap 1,800; featured image 1500×940.
- **caredale** — cannibalization must enumerate the live Shopify blog; author Roshni.
- **generic** — skip client-specific gates; G2b skipped if no exclusion list configured.

---

## Output format

```
══════════════════════════════════════════════════════════════
SEO SCORE: <X>/100   Article: <title>
══════════════════════════════════════════════════════════════
S1  Meta tags & SERP snippet               XX/15   ✅/⚠️/❌
S2  Heading hierarchy & keyword placement  XX/10
S3  Primary & secondary keyword usage      XX/15
S4  Internal linking                       XX/10
S5  External linking & authority           XX/5
S6  Image SEO                              XX/10
S7  Schema markup                          XX/10
S8  Content depth & engagement             XX/10
S9  Mobile-friendly markup                 XX/5
S10 E-E-A-T signals                        XX/5
S11 URL & link health                      XX/5
──────────────────────────────────────────────────────────────
PART 1 TOTAL                               XX/100   (gate ≥85)

RANKING GATES (binary — any FAIL caps verdict at ❌)
G1 Intent & SERP-format match              ✅/❌
G2 Keyword-uniqueness / cannibalization    ✅/❌
G3 Competitive depth vs SERP median        ✅/❌
G4 Query fan-out integrity (headings)      ✅/❌

INHERITED STRUCTURAL (from /aeo-score)     ✅ PASS / ❌ (list fails)
──────────────────────────────────────────────────────────────
VERDICT: [✅ SEO-READY  (≥85 AND all gates pass) |
          ⚠️ MINOR FIXES (70–84, gates pass) |
          ❌ FIX REQUIRED (<70, OR any ranking gate FAIL, OR structural fail)]
══════════════════════════════════════════════════════════════

PRIORITY FIXES (ranking-gate failures first, then by S-point impact)
1. ...
```

If ✅: "SEO-ready. Proceed to humanization." If ❌/⚠️: "Fix priority items, then re-run /seo-score. For auto-fixes, run /seo-optimize <slug> fix=safe."

## Important rules
- **Scoring-only** — never auto-edit here; hand fixes to `/seo-optimize`. Keeps the gate honest.
- **AEO and SEO stay separate scores** — do not merge (an article can be 88 AEO / 65 SEO; both gate independently). For Nuyug the combined "Gate A" scorecard is produced by `/aeo-score`'s auto-chain, not here.
- **Ranking gates are hard** — a keyword that cannibalizes, is on the exclusion list, or can't win its SERP format is an automatic ❌ no matter how clean the on-page SEO is. This is the whole point of an SEO score over an on-page checklist.
- **Live link + live SERP every run** — never trust cached liveness or a stale SERP for G1/G3/S11.
- **Never invent a pass** — if a check can't be verified, mark partial and say why.
- **Re-run after fixes** — full re-score, report the delta.
