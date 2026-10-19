---
name: aeo-score
description: Score a completed article draft against AEO best practices before humanization. Produces a scored report (0-100) with pass/fail per dimension. Acts as a humanization gate: score >= 80 = proceed, < 80 = fix first.
---

<!-- Provenance: Unveilr platform registry · category=content · version=2 · scope=global · synced 2026-08-25 -->
<!-- AVIAAN: no calibration block exists for Aviaan — it falls through to "non-Nuyug" defaults.
     D6 word count = 1,500-2,500 cluster / 2,500-4,000 pillar. D7 needs named author PLUS bio URL.
     D8 internal links = 8-14. aeo-score does NOT auto-chain into seo-optimize for Aviaan. -->

# AEO Article Scorer

Run this **before Phase 8 (Humanization)** to verify the article meets AEO standards. Do not proceed to humanization if the score is below 80.

**Reference:** `.claude/aeo-best-practices.md` for detailed guidance on each dimension.

## ⛔ HARD RULE — flag any non-live hyperlink as a CRITICAL D8 failure

As part of D8 (Internal Linking) scoring, run a liveness check on every URL in the article. Any URL that returns non-200, or that soft-404s to a generic page (homepage, "page not found" wrapper), is a CRITICAL failure: deduct full D8 points AND list the dead URL in the priority-fix block. The article cannot pass the humanization gate (score ≥ 80) until every link is verified live. Soft-404 traps: VakilSearch `/blog/*` → homepage; Nuyug unpublished `/blogs/news/<slug>`; Care Dale archived PDPs.

**Run it with the wave-scoped cache** — articles in one wave share most of their external
anchors, so checking each URL once per wave instead of once per article per pass removes
~3 of every 4 round-trips:

```bash
python3 ~/.claude/scripts/link_liveness.py --urls-from <article.md>
```

6h TTL, 12-way parallel, browser UA (a bare UA gets a false 403 on some hosts), gov 403
treated as LIVE, and the soft-404 traps above encoded. `/final-check-*` MUST re-run this
with `--no-cache` before delivery — `audit-data-integrity` G5/G6 do not accept a cached
row as proof a URL is live.

## ⛔ HARD RULE — headings that are not fan-out queries are a CRITICAL D1+D6 failure

Score the headings as retrieval targets, not as prose signposts. Read every H2/H3 and ask: **is this a query a real person would type?**

- Any **dead heading** ("Key considerations", "Cost drivers and what to expect", "Understanding the basics", "What you need to know", "Who actually writes these") is a CRITICAL failure: deduct it in D1 AND list it in the priority-fix block with a suggested replacement query.
- **Fewer than 6 question-format / fan-out H2s** caps D6 at 4/10 regardless of how complete the coverage reads.
- **Two or more dead headings blocks the humanization gate outright** — the article cannot pass to Gate A on total score alone. Send it back to the writer to re-derive the outline from a sourced fan-out.
- This is a scorer: you do not need to re-run the fan-out tools. You DO need to reject headings that no query could have produced.

## ⛔ HARD RULE — run the CLIP CHECK: the first ~200 characters of every section

ChatGPT clips **~200 characters — about two lines — from each retrieved page**: the stretch best matching its
own search words, and it writes its answer from that clip. A page that is retrieved and clipped badly is
never cited, however good the prose below it. (`~/.claude/aeo-best-practices.md` **PART G3** — first-party,
530 recorded ChatGPT searches, position-controlled. PART G3 **supersedes the unsourced "134-167 word passage"**
figure at §31 of that file.)

```bash
python3 ~/.claude/scripts/clip_check.py articles/<slug>.md
```

The script prints the actual ~200-character clip for every H2/H3, flags clips with no numeral, and hard-flags
throat-clearing openers. It skips FAQ/CTA container headings and counts spelled-out numbers ("seven components").

**The rule has two halves and the script only decides one of them.** It decides *does the clip carry a number*.
**You** decide *does the clip make a concrete claim* — by reading every clip it prints. A clip with no numeral
can still be excellent: *"A business plan explains how a business will operate and repay. A feasibility study
tests whether the project is viable in the first place"* is highly citable. **Never report the script's output
as the verdict.**

### Calibrated thresholds (measured against 44 shipped articles / 595 sections, 2026-09-02)

| Finding | Verdict | Why this threshold |
|---|---|---|
| **A throat-clearing opener anywhere** | **CRITICAL — blocks the gate** | Base rate in our shipped corpus is **0.2%** (1 of 595). It is rare, unambiguous, and the exact measured failure mode. Blocking costs nothing. |
| **Quick Answer clip carries neither a number nor a concrete claim** | **CRITICAL — blocks the gate** | It is the single clip most likely to be taken for the head prompt. |
| **Under 50% of section clips carry a number** | **Deduct up to −3 in D5 (data density); does not block** | Median across our shipped corpus is **36%**, p75 is **50%**. 50% is "as good as our best quartile already is" — a real target, not a fantasy. |
| **An individual clip with no number AND no concrete claim** | **−2 each in D1** | This is the laptop-review failure: retrieved, clipped, useless. |

**Do NOT block on the numeral count alone.** 61% of clips in our own shipped corpus carry no numeral; a hard
numeral gate would fail work that is genuinely good and would push writers to bolt digits onto clean prose.
The numeral share is a density signal, not a defect.

**Throat-clearing openers** (automatic CRITICAL): "In this article we will explore…", "Choosing the right X
can be overwhelming…", "You have come to the right place…", "Understanding X is essential…", "When it comes
to…", "Tired of…".

**Report in the scored output** as: `clip check: N/M sections carry a number (target ≥50%) · K throat-clearing
· J clips with no number and no concrete claim`, then list the failing clips verbatim so the writer can see
exactly what ChatGPT would have taken.


## Input

$ARGUMENTS

Parse for:
- **file**: Path to the article `.md` file (required). Can be slug (e.g. `do-you-need-lawyer-india-guide`) or full path.
- **client**: `vakilsearch` | `caredale` | `jaagrukbharat` | `nuyug` | generic (optional — enables client-specific checks)

**⚠️ Jaagruk Bharat calibration (client=jaagrukbharat).** `/aeo-score`'s defaults are tuned for long, stat-heavy legal/regulatory articles and will contradict the Jaagruk Bharat skills unless you apply these overrides while scoring. See `~/.claude/clients/jaagrukbharat.md` and `~/.claude/skills/aeo-article/SKILL.md`.
- **D6 word count**: JB target is **900-1,300 words, hard ceiling 1,500** (brevity is deliberate — immediate answers, not padding). Score **3/3 if 900-1,500**; deduct 1 pt if 700-899 (too thin to answer fully); deduct 2 pts if **over 1,500** (violates the JB ceiling) or under 700. Do NOT apply the 1,500-2,500 "non-Nuyug" band and do NOT flag a 950-word JB article as "thin".
- **D5 data density**: for citizen procedural/how-to content, **specific figures that actually exist in the process** (fees, timelines like "7-10 working days", number/list of documents, portal names) PLUS citations to the official `.gov.in` portal SATISFY the density expectation. Do NOT penalise the absence of "a named statistic every 200 words" or "8-12 external citations" — a how-to has few natural statistics. Full official body names on first mention (UIDAI, Parivahan) still count for entity salience.
- **D9 contractions**: JB voice **permits light natural contractions** — treat the contraction check as PASS ("matches brand voice"). Do NOT flag contractions for JB.
- **D9 brand name**: check for exactly "Jaagruk Bharat" (two words, capital J+B); the Vakilsearch `VakilSearch`/`per cent` checks do NOT apply to JB.
- Everything else (D1 question headings + answer-first, D3 FAQ 40-60, D8 links 8-14, D4 tables/lists) applies as written and already matches the JB skills.

**⚠️ Vakilsearch calibration (client=vakilsearch).**
- **D6 word count**: VS target is **2,000 words (STRICT, client instruction 2026-07-23)**. Score **3/3 if 1,900-2,100**; deduct 1 pt if 1,700-1,899 or 2,101-2,300; deduct 2 pts outside those ranges. Do NOT apply the old 1,500-1,600 default or the generic 1,500-2,500 band to Vakilsearch.

If only a slug is given, look for the file at `articles/<slug>.md`.

---

## ⚡ STEP 0 — run the deterministic scorers FIRST (do not hand-score what a script computes)

Eight of the twelve dimensions are regex-detectable. Hand-scoring them is the single largest
avoidable cost in Gate A, and a script is also more consistent than a reading pass. Run these
three before you read the article, then spend your judgment only on what they cannot measure:

**⛔ `--client` is not optional.** `pre_score.py` defaults to `vakilsearch`, so omitting it
silently applies the wrong client's word band, contraction rule and Quick Answer requirement
(measured: 87.8 vs 97.6 on the same Aviaan article). `batch_gate.py` makes it mandatory.

```bash
python3 ~/.claude/scripts/pre_score.py   articles/<slug>.md --client <c> --json
python3 ~/.claude/scripts/clip_check.py  articles/<slug>.md
python3 ~/.claude/scripts/link_liveness.py --urls-from articles/<slug>.md
```

| Covered deterministically by `pre_score.py` | Left to your judgment |
|---|---|
| D1 heading question ratio | D1 answer quality — is the first sentence a *real* standalone answer |
| D2 paragraph / sentence length (full) | D3 FAQ **depth** — do FAQs add angles the body lacks |
| D3 FAQ count + answer word bands | D5 named attribution, triangulation, info-gain, expert quote |
| D4 tables / lists / Common Mistakes presence | D5 proper-noun density judgment |
| D7 Last-Updated + author + Quick Answer | D6 whether the sub-intents are genuinely distinct |
| D8 internal / external / total link counts | D9 brand voice beyond the mechanical checks |
| META meta-title / meta-desc / em-dash / contractions / US-vs-UK | |

`clip_check.py` settles the CLIP CHECK hard rule; `link_liveness.py` settles D8 liveness.

**Rule:** if a scorer output disagrees with your reading, the scorer wins on anything countable
(counts, lengths, presence) and you win on anything qualitative. Never silently overrule a count.

**Cost:** ~3 s of script time replaces ~4-6 min of hand-scoring per article.

---

## How to Score

Read the article file completely. Then run each check below. For each dimension, assign a score out of its max. Be strict — partial credit only when most criteria are met.

At the end, output the full scored report in the format shown at the bottom.

---

## Scoring Dimensions (100 pts total)

### D1 — Heading Format & Answer Structure (20 pts)

This is the highest-impact dimension. Research shows question-format headings are cited 2x more, and answer-first structure drives 65% more AI citations.

**Question-format headings (6 pts):**
- **(3 pts)** Are ≥ 50% of H2 headings phrased as questions matching user query patterns? E.g. "How Much Does Trademark Registration Cost in India?" not "Trademark Registration Cost"
- **(3 pts)** Are H3 sub-headings phrased as questions when they answer distinct sub-queries? E.g. "### What Happens If You File Without a Lawyer?" not "### Filing Without a Lawyer"

**When question headings are NOT required** (do not deduct for these):
- Navigational/structural sections: "Quick Reference", "Summary Table", "How to Decide"
- Numbered list sections where the number IS the structure: "1. Consumer Court Complaint"
- FAQ headings (already questions by definition)

**Answer capsule quality (8 pts):**
- **(3 pts)** Does every H2/H3 open with a direct answer in the first 1-2 sentences (≤ 60 words)? Pattern: Answer > Evidence > Story — never open with background, history, or context.
- **(3 pts)** Is the first sentence after each question heading a **complete, standalone answer under 29 words**? This is the "voice layer" — voice assistants read exactly this aloud. If the first sentence is not a complete answer by itself, deduct.
- **(2 pts)** Is the most important claim or data point in the **first 30% of the article** (before halfway point of word count)?

**Definition patterns (3 pts):**
- **(2 pts)** Does the article define the primary topic within the **first 100 words** using an "X is Y" or "X refers to Y" pattern? Cited passages are 2x more likely to use clear definitions.
- **(1 pt)** Do major section openings include a one-sentence definition before elaboration?

**Heading hierarchy (3 pts):**
- **(2 pts)** Is there a strict H1 > H2 > H3 hierarchy with NO skipped levels (e.g., no H2 jumping to H4)? 68.7% of AI-cited pages follow clean hierarchy.
- **(1 pt)** Is there a heading approximately every 150-200 words?

**Deductions:** -2 pts per H2 that opens with background/history instead of an answer. -3 pts if intro buries the lead past sentence 3.

---

### D2 — Section & Paragraph Structure (10 pts)

- **(4 pts)** Do ≥ 85% of body paragraphs have ≤ 4 sentences? Flag every paragraph with 5+ sentences.
- **(3 pts)** Does each H2 section (all content between two H2 headings) stay ≤ 300 words? Over 300 words without H3 sub-sections = deduction. Ideal passage length for AI extraction is **134-167 words**.
- **(3 pts)** Do ≥ 85% of body paragraphs have ≤ 80 words?

**Deductions:** -1 pt per paragraph with 5+ sentences (max -4). -1 pt per H2 section exceeding 300 words without H3 breakdowns (max -3).

---

### D3 — FAQ Quality (15 pts)

FAQs with FAQPage schema achieve 2.7x AI citation rate. Score strictly.

- **(5 pts)** FAQ answer word count — tiered scoring:
  - **All answers 40-60 words** = 5/5 pts ✅ Voice-optimised sweet spot. Backlinko research: voice assistants read answers of ~29 spoken words = ~43 written. AI citations favour this range.
  - **Any answer 61-80 words** = 4/5 pts ✅ AI-extractable but not voice-optimal. Deduct 1 pt from this sub-dimension if the majority land here.
  - **Any answer 81-100 words** = -2 pts per answer (over-long; AI summarises instead of quotes)
  - **Any answer over 100 words** = -3 pts per answer
  - **Any answer over 150 words** = -5 pts per answer
  - **Any answer under 40 words** = -1 pt per answer (too brief; incomplete answer signal)
  - **Count words precisely** — do not estimate. Humanization adds ~10-15 words; answers at 70-80 words pre-humanization are at high risk of blowing over the limit. Flag as ⚠️ pre-humanization risk.
  - **3-way sync rule**: after any word-count fix, all three locations must be updated together (body + sc_fs_multi_faq shortcode + JSON-LD schema). Fixing one without the others = -2 pts per FAQ for the sync check.
- **(4 pts)** Do the visible FAQ answers **match word-for-word** with both the `sc_fs_multi_faq` shortcode AND the JSON-LD `FAQPage` schema (if present)? Any mismatch = -2 pts per FAQ.
- **(3 pts)** Do FAQs add new depth NOT already covered in the body? ≥ 80% of FAQs must answer angles/edge cases the body does not cover.
- **(3 pts)** Is the FAQ count between 5 and 10 pairs? Are FAQ questions driven by real search data (not invented)?

---

### D4 — Structured Formats & Extractability (15 pts)

Tables with `<thead>` have 47% higher AI citation rate. Comparative listicles make up 32.5% of all AI citations.

**Tables (5 pts):**
- **(3 pts)** Are fee structures, timelines, and comparison data in **tables** (not prose)? Any paragraph with 3+ comparable data points that could be tabulated = deduction.
- **(2 pts)** Do tables have descriptive column headers (not "Column 1", "Item")? Headers should contain keywords.

**Lists (4 pts):**
- **(2 pts)** Are requirements, documents, and features in **bullet lists**? Are sequential processes in **numbered lists**?
- **(2 pts)** Are lists optimised: 5-7 items per list, each starting with an imperative verb or bold key term?

**Comparison & contrast structures (4 pts):**
- **(2 pts)** For comparison/guide articles: is there a summary comparison table near the top of the article?
- **(2 pts)** Is there a "Common Mistakes" or "What to Avoid" section? These serve as natural query fan-out targets that AI extracts independently.

**Negative/contrasting content (2 pts):**
- **(2 pts)** Does the article include contrasting perspectives (pros/cons, when to do X vs when NOT to)? Balanced content with subjectivity ~0.47 outperforms purely factual content.

---

### D5 — Data Density, Entity Salience & Citations (20 pts)

This is the second highest-impact dimension. Princeton GEO research shows statistics (+40%), citations (+30%), and quotations (+41%) each independently boost visibility.

**Named statistics (6 pts):**
- **(4 pts)** Is there a **named statistic with a source** at least once every 200 words? Named = "according to X" or "X reports that Y%". Unnamed/generic stats do not count. Calculate: word_count / 200 = minimum stats needed.
- **(2 pts)** Are numbers **specific** rather than vague? "₹4,500 per class" beats "a few thousand rupees". "76.2% of inmates" beats "most inmates".

**Entity density (6 pts):**
- **(3 pts)** Does the article maintain **15-20% proper noun density** in key sections? Name specific Acts, organisations, government bodies, people, forms, portals — not generic descriptions. Pages with 15+ recognised entities show 4.8x higher citation probability.
- **(3 pts)** Does the article use **full official names** on first mention? E.g. "Controller General of Patents, Designs, and Trademarks under the Ministry of Commerce and Industry" not just "trademark office".

**Source triangulation (5 pts):**
- **(3 pts)** Are there **8-12 external citations per 1,500 words** with specific attribution (named source, date)? AI-cited content averages this density. For lower-ranked sites, source citation produces up to +115% visibility improvement.
- **(2 pts)** Are major claims **triangulated with 2+ sources**? Do citations link to **primary sources** (.gov.in, official reports) rather than just secondary blog posts?

**Expert voice (3 pts):**
- **(2 pts)** Is there at least **one expert quote** or direct reference to an official body's stated position?
- **(1 pt)** Is there at least one **original data point, analysis, or insight** not available elsewhere? (Information gain — up to +30% visibility improvement)

---

### D6 — Multi-Intent Coverage & Completeness (10 pts)

AI's query fan-out generates 3-5 sub-queries per prompt. Pages covering all sub-queries get preferential citation.

- **(4 pts)** Does the article address **6+ distinct sub-intents**, each phrased as a query rather than a topic label (Fan-Out hard rule: fewer than 6 question-format H2s caps this dimension at 4/10), related to the primary topic? Common sub-intents: "what is it", "how it works", "how much it costs", "who needs it", "alternatives", "common mistakes", "step-by-step process". Each should have its own H2/H3.
- **(3 pts)** Is the article **complete** — no gaps in numbered sequences, no promised sections missing, all stages of a process covered including "what happens after"?
- **(3 pts)** Is the word count appropriate? **Nuyug standard: body content must NOT exceed 1,800 words (strict cap).** Target band 1,400-1,800 words. Score 3/3 if 1,400-1,800; deduct 1 pt if 1,200-1,399 (thin); deduct 2 pts if over 1,800 (violates the Nuyug strict cap) or under 1,200. For non-Nuyug brands the older guidance applies (1,500-2,500 cluster / 2,500-4,000 pillar). A high-density 1,700-word article outperforms a low-density 3,000-word article. **Jaagruk Bharat EXCEPTION: target 900-1,300, ceiling 1,500 — 3/3 if 900-1,500; deduct if over 1,500 or under 700. Do NOT apply the 1,500-2,500 band to JB (see client calibration note at top).**

---

### D7 — E-E-A-T & Trust Signals (5 pts)

- **(2 pts)** Named author present in frontmatter. **Nuyug standard: a named author byline is sufficient — an author bio URL is NOT required** (Nuyug does not run author bio pages; the byline alone earns full marks). For non-Nuyug brands, an author bio URL is still expected for full credit.
- **(1 pt)** "Last Updated" date visible in the article body (not just schema). Year in title/H1.
  > **⚠️ REFINED 2026-09-02 (PART G4 + G8) — the point is retained; two conditions now apply.**
  > **(a) The year in title/H1 is a trade-off, not a free win.** It helps a page get *found* on
  > recency-flavoured prompts and **slightly hurts being cited and quoted** once retrieved. Award the point
  > for a year on a contested/recency-flavoured topic; **do not deduct** for its absence on a genuinely
  > evergreen one — a missing year there is now a defensible editorial choice, not a defect. `meta_title`
  > keeps the year per client rule (D9); slugs stay evergreen.
  > **(b) A "Last Updated" date must be TRUE.** On a refreshed article, if the date was moved without the
  > content changing, **award 0 and flag it** — at equal position, stale-dated pages are cited *less than
  > undated ones*, making a decorative date worse than none. On a genuinely new article the date is correct
  > by construction and the point stands.
- **(2 pts)** No unverified claims. If claims were flagged as unverifiable during research, they should be marked or removed.

---

### D8 — Internal Linking (5 pts)

- **(2 pts)** Link count is healthy and non-spammy. **Nuyug standard: 5-6 total links per article is the correct, full-marks range** (Nuyug's editorial rule caps links at 6 to avoid spam). Score 2/2 if 5-6 links; 1/2 if exactly 4 or 7; 0/2 if ≤3 or ≥8. For non-Nuyug brands the older 8-14 guidance applies.
- **(2 pts)** At least one link to the **pillar/parent collection page**. Sibling-article cross-links: if the sibling articles are not yet published/live, this requirement is **waived with no deduction** — do NOT penalise missing sibling links when the cluster is not yet live. Award the full 2 pts when the pillar link is present and any genuinely-live sibling links that exist are included.
- **(1 pt)** Anchor text is descriptive topic text (not "click here", not brand name).
- **Nuyug hard rule:** competitor brand names must NEVER be hyperlinked. A hyperlink whose URL points to a competitor domain (giva.co, palmonas.com, caratlane.com, miabytanishq.com, etc.) is a CRITICAL failure — deduct full D8 and list it in priority fixes. Competitor names must appear as plain text only.

---

### D9 — Meta & Keyword Checklist (0 pts — binary pass/fail only)

These do not affect the score but are flagged as PASS/FAIL in the report:

- [ ] `meta_title` ≤ 60 characters, includes primary keyword + year *(the ≤60 rule is Google's; see the on-page title items below, which are a different contest)*
- [ ] **No "Official" anywhere in the title, H1 or `meta_title`** — pages saying "official" are cited **5× less** (13% vs 61%). CRITICAL fail. *(PART G4)*
- [ ] **On-page title / H1 reads as one natural sentence, ideally 13–15 words** — 24+ words is the worst-performing bin. Flag a keyword chain even if it is under 60 characters. Waived where a client contract locks H1 to the tracked prompt verbatim (Aviaan HR4, `/prompt-led-article`) — the prompt wins.
- [ ] **"Best/Top 10" styling is earned from the SERP format, not habit** — it is placed higher but **cited less at equal position**. Flag (do not fail) where the SERP does not demand a ranked list.
- [ ] `meta_description` 150-160 characters, first 70 chars = answer/value prop
- [ ] Primary keyword appears in H1
- [ ] All `target_keywords` from frontmatter appear in at least one heading or body paragraph
- [ ] `suggested_url` is ≤ 7 words, lowercase, hyphenated, and **contains NO year** (evergreen slug)
- [ ] No em dashes (—) — use ` - ` instead
- [ ] `tldr` is 50-80 words
- [ ] No sentence over 40 words
- [ ] No contractions (for formal legal/business content) OR matches brand voice
- [ ] **Vakilsearch ONLY — Brand name**: zero occurrences of `VakilSearch` (capital S). Must be `Vakilsearch` (lowercase 's'). Domain URL `vakilsearch.com` stays as-is. CRITICAL fail if violated.
- [ ] **Vakilsearch ONLY — Percentages**: zero occurrences of `per cent`, `percent`, or `percentage` / `percentages`. All percentage values must use the `%` symbol with no space (`8%`, not `8 per cent` / `8 %` / `eight per cent`). For noun usage use `share` / `rate`. CRITICAL fail if violated.
- [ ] **Vakilsearch ONLY — No year in URL/slug**: the `slug` / `suggested_url` must contain NO 4-digit year (no `-2026`, `2025`, etc.) — URLs must be evergreen so they never need re-slugging next year. The **title/H1/meta_title still KEEP the year** (per the short-direct-title rule); only the URL drops it. CRITICAL fail if a year appears in the slug.

---

## Output Format

Produce this exact report structure:

```
══════════════════════════════════════════════════════════════
AEO SCORE REPORT
Article: [title]
File: [path]
Date scored: [date]
══════════════════════════════════════════════════════════════

DIMENSION SCORES
──────────────────────────────────────────────────────────────
D1  Heading Format & Answer Structure   [X] / 20
D2  Section & Paragraph Structure       [X] / 10
D3  FAQ Quality                         [X] / 15
D4  Structured Formats & Extractability [X] / 15
D5  Data Density, Entity & Citations    [X] / 20
D6  Multi-Intent & Completeness         [X] / 10
D7  E-E-A-T & Trust Signals             [X] /  5
D8  Internal Linking                    [X] /  5
──────────────────────────────────────────────────────────────
TOTAL                                   [X] / 100

GATE: [✅ PROCEED TO HUMANIZATION | ⛔ FIX REQUIRED FIRST]
(Threshold: 80/100)
══════════════════════════════════════════════════════════════

DIMENSION BREAKDOWN
────────────────────

D1 — Heading Format & Answer Structure: [X]/20
  ✅ [what passed — be specific about which headings, word counts]
  ❌ [what failed — list specific headings with issues]
  → Fix: [specific action]

D2 — Section & Paragraph Structure: [X]/10
  ✅ ...
  ❌ [list every paragraph/section that fails, with sentence/word count]
  → Fix: ...

[... repeat for each dimension ...]

══════════════════════════════════════════════════════════════

META CHECKLIST (non-scored)
  [✅/❌] meta_title [X chars]: "[value]"
  [✅/❌] meta_description [X chars]: "[value]"
  [✅/❌] Primary keyword in H1
  [✅/❌] All target keywords covered
  [✅/❌] suggested_url format
  [✅/❌] No em dashes
  [✅/❌] tldr word count
  [✅/❌] No sentence over 40 words
  [✅/❌] No contractions (or matches brand voice)

══════════════════════════════════════════════════════════════

PRIORITY FIXES (ordered by score impact)
1. [highest impact fix — dimension, specific issue, how to fix]
2. ...
3. ...

If score >= 80: "Article is AEO-ready. Proceed to humanization (Phase 8)."
If score < 80: "DO NOT humanize yet. Fix Priority Fixes 1-N, then re-run /aeo-score."
══════════════════════════════════════════════════════════════
```

---

## Important Rules

- **Be strict on FAQ word counts.** Count actual words. Do not give partial credit for 100-word answers when the limit is 80.
- **Question headings are high-impact.** Research shows 2x citation rate. Flag every H2 that could be a question but is not.
- **Entity density matters.** Count proper nouns in a representative 200-word sample. If below 15%, flag.
- **Do not invent passes.** If you cannot verify a check, mark it as partial score and explain why.
- **The gate is hard.** If total < 80, do not proceed to humanization even if the user asks.
- **Re-run after fixes.** If the user fixes the article and wants to re-score, run the full check again.
- **Skip schema scoring.** RankMath auto-generates most schema. Only check FAQ sync (body vs shortcode vs JSON-LD) as part of D3.
- **Post-humanization review is mandatory.** After running the aihumanize.io API, review the entire article for logical issues introduced by the humanizer. Common problems:
  - **Factual errors**: reversed organisation names ("Authority for National Legal Services" instead of "National Legal Services Authority"), wrong acronym expansions (VLE = "Village Level Entrepreneur" not "Village Level Officer"), fabricated terms ("Means-Test Agencies"), wrong dates
  - **Garbled text**: random characters (Japanese text artifacts), broken numbered lists (steps losing their numbers), "/" slashes in prose
  - **Terminology drift**: "attorney" instead of "lawyer/advocate" (Indian context), "license" instead of "licence" (UK English)
  - **Style violations**: contractions ("There's", "you'll") in formal register, Title Case On Every Word in bullet items, em dashes
  - **Grammar errors**: "an lawyer" instead of "a lawyer"
  - **Meaning changes**: "goods and service centres" instead of "Common Service Centres", "family quality of life issues" instead of "matrimonial matters"
  - **FAQ answer sync break**: the humanizer changes body FAQ text but not shortcode or JSON-LD — restore all 3 locations to match after humanization

## Research Sources

Key research backing this rubric:
- Kevin Indig: 1.2M AI answer analysis, 18K citations (Search Engine Land)
- Princeton GEO Paper: ACM SIGKDD 2024 (arXiv:2311.09735)
- The Digital Bloom: 2025 AI Visibility Report
- Frase.io: AEO Complete Guide 2026
- Wellows: AI Overviews Ranking Factors 2026
- Backlinko: Voice Search Study (29-word answer length)
- Previsible: 5,000-prompt AI citation study

---

## 🔗 GATE A AUTO-CHAIN — Nuyug only

**Conditional behaviour: after producing the AEO scorecard, if the article's frontmatter `brand` field is `Nuyug` (case-insensitive), automatically invoke `/seo-optimize <slug>` next and present a combined Gate A scorecard. For all other brands (VakilSearch, Care Dale, etc.), STOP after the AEO scorecard — no auto-chain.**

### How to detect

Read the article frontmatter — the `brand:` field. If `brand: "Nuyug"` (or `brand: nuyug`, case-insensitive), trigger the auto-chain. Otherwise (VakilSearch, Care Dale, any other brand, or no brand specified), STOP after the AEO scorecard. This keeps other brand workflows untouched.

### Combined Gate A output format

After running both `/aeo-score` and `/seo-optimize` for a Nuyug article, present a single combined scorecard:

```
══════════════════════════════════════════════════════════════
GATE A — COMBINED AEO + SEO SCORECARD (Nuyug)
Article: <title>
File: articles/<slug>.md
══════════════════════════════════════════════════════════════

AEO SCORE:  X/100   [✅ ≥80 PASS | ⛔ <80 FAIL]
SEO SCORE:  X/100   [✅ ≥85 PASS | ⚠️ 70-84 MINOR | ❌ <70 FIX]
──────────────────────────────────────────────────────────────
GATE A VERDICT:  ✅ READY FOR HUMANIZE   (AEO ≥80 AND SEO ≥85)
              OR ⛔ FIX REQUIRED          (either threshold missed)
══════════════════════════════════════════════════════════════

PRIORITY FIXES (sorted by combined score impact)
1. [highest-impact fix — dimension, specific issue, action]
2. ...
```

### When Gate A fails

If either score is below threshold, surface the **merged priority-fix punch list** (top items from both AEO and SEO priority lists, deduplicated, ordered by combined point impact). Do NOT proceed to humanize. The user fixes, then re-runs `/aeo-score <slug>` which re-triggers the full Gate A loop.

### Why this is Nuyug-only

VakilSearch articles use a different workflow (managed by `humanize_pipeline.py` with its own Stage 0 structural gate). Care Dale articles are scored differently. Auto-chaining both AEO and SEO only fits the Nuyug pipeline where SEO + AEO carry equal weight and humanize happens after both gates pass.

### Implementation

When the auto-chain triggers:
1. Run the standard `/aeo-score` workflow (D1–D8 dimensions, 100 pts) and capture the score
2. Read the same article file's brand frontmatter — confirm `brand == "Nuyug"`
3. Invoke `/seo-optimize <slug>` next (S1–S12 dimensions, 100 pts) and capture the score
4. Render the combined Gate A scorecard (above)
5. Merge priority-fix lists from both, deduplicate, sort by point impact, present
6. Set verdict: `✅ READY FOR HUMANIZE` only if AEO ≥80 AND SEO ≥85; otherwise `⛔ FIX REQUIRED`

### Batch invocation

For batch runs (e.g., `/aeo-score all client=nuyug`), the auto-chain triggers per-article. The final output is a table of Gate A verdicts:

```
| Article slug | AEO | SEO | Verdict |
|---|---|---|---|
| imitation-jewellery-looks-like-real-gold | 84 | 87 | ✅ READY |
| gold-plated-vs-real-gold-wedding-calculator | 78 | 82 | ⛔ FIX |
...
```

Followed by a per-article priority-fix punch list for any that failed.
