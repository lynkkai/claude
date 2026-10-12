---
name: post-humanize-check
description: Gate B — lightweight regression check that runs automatically after any humanize-* skill. Verifies humanization did not strip keywords, break headings, drop internal links, or introduce em-dashes/banned words. Also gates the defects that survive humanization untouched and ship to clients: unsourced figures, draft-artifact hedges like "(industry estimate)", brand-positioning claims that contradict the client's own live site, duplicate CTAs and tables across a batch, and unlinked pages in an existing content cluster. Auto-restores missing keywords using surgical injection. Cheap, fast, no DataForSEO/GSC calls.
---

<!-- DURABILITY / RECOVERY (read this before trusting a passing report).
     This local file is the OPERATIVE version for /post-humanize-check in Claude Code.
     C1-C11 are platform global v1 verbatim; C12-C16 (2026-08-26) and C17 (2026-09-04)
     are the additions.

     A platform backup of this content is stored as the Aviaan project skill
     "post-humanize-check-aviaanaccounting-com". It carries a suffix because
     create_skill rejected the bare name as already taken, so it does NOT shadow the
     global skill: get_skill("post-humanize-check") still returns global v1, with only
     11 checks. Consequence — if a registry sync overwrites this file, C12-C16 vanish
     locally and the report quietly drops back to C1-C11 while still saying PASS.
     If you see a Gate B report with no C12-C16 rows, that is the failure; recover the
     procedure from "post-humanize-check-aviaanaccounting-com".

     ⛔ C17 CARRIES AN EXTRA RISK. Journey A step 7 (the standalone full /aeo-score
     re-score) was REMOVED on 2026-09-04 because C17 subsumes it. If a registry sync
     drops C17, the wave loses its post-humanize score gate entirely and still reports
     PASS. FAIL-SAFE RULE: if a Gate B report has no C17 row, treat the delta re-score
     as NOT RUN and run the full `/aeo-score <slug> client=<c>` before the image step.
     Never let an article reach /push-to-* on a Gate B report missing C17.
     Permanent fix when someone has appetite: promote C12-C16 into global v2 (they are
     written client-agnostic and fail-safe precisely so this is a safe move) and delete
     the suffixed copy, instead of letting the two drift apart. -->
<!-- Provenance: Unveilr platform registry · category=content · version=1 · scope=global · synced 2026-08-25 -->
<!-- AVIAAN PATCHES: C4 must match aviaanaccounting.com (not nuyug.com). C10 brand specs for Aviaan = AED figures, CT/VAT rates and thresholds, regulator names. -->
<!-- C12-C16 added 2026-08-26 after a 4-article Aviaan batch reached founder review carrying: two AED price figures with no citation entry, an "(industry estimate)" hedge left inline, a brand-positioning claim that read as contradicting aviaanaccounting.com's own live pages, a word-for-word duplicate CTA across two articles, and a 5th page added to a 4-page cluster with 2 siblings left unlinked. Humanization did not cause any of these, which is exactly why nothing caught them. -->

# Post-Humanize Regression Check (Gate B)

The humanize-* skills repeatedly damage AEO and SEO work — keyword phrases get reworded, exact-match headings get softened, link counts drop, em-dashes sneak back in. This skill runs **automatically after every successful humanize call** as a cheap regression gate.

It is **not a re-run of `/aeo-score` or `/seo-optimize`** (those are expensive). It only checks the dimensions humanize is known to break, and only auto-restores when the fix is safe and surgical.

## Input

$ARGUMENTS

Parse for:
- **article**: Path or slug of the freshly humanized article (required)
- **strict**: If `true`, FAIL the gate on any regression (no auto-restore). If `false` (default), auto-restore safe items and only fail on hard structural damage.

---

## What this skill checks

| # | Check | Auto-restore? | If fails |
|---|---|---|---|
| C1 | Every target keyword from frontmatter still present in body (hyphen-insensitive, ≥1 occurrence) | ✅ Yes — inject natural one-sentence mention | Restore + re-verify |
| C2 | Primary keyword appears in H1 (verbatim or close paraphrase) | ❌ No — too invasive | FAIL, ask user |
| C3 | ≥ 50% of H2 are question-format (preserves AEO D1 score) | ❌ No — too invasive | FAIL, ask user |
| C4 | Every internal link (`<client domain>/...`, from `get_client_context`) present in the pre-humanize backup is still present | ✅ Yes — restore missing link in its original sentence | Restore + log |
| C5 | Em-dash count is 0 (body only) | ✅ Yes — replace `—` with `-` | Auto-fix |
| C6 | Banned words count is 0 (delve, crucial, leverage, robust, seamless, moreover, furthermore, additionally, exquisite, mesmerising, etc.) | ✅ Yes — replace with neutral synonym from a lookup table | Auto-fix |
| C7 | Internal link count within ±10% of pre-humanize count | ⚠️ Restore missing links from backup | Restore + log |
| C8 | Frontmatter unchanged (title, meta_title, meta_description, suggested_url, keywords, brand, project_id, generated_date) | ❌ No — fail loud | FAIL, ask user |
| C9 | Schema and FAQ_JSON blocks unchanged (machine-readable, not humanizable) | ❌ No — fail loud | FAIL, ask user |
| C10 | Every brand spec phrase still intact (e.g., for Nuyug: "1-year warranty", "hypoallergenic", "nickel-free", "anti-tarnish", "AAA-grade", "thick gold plating") | ✅ Yes — restore from pre-humanize backup | Restore + log |
| C11 | All ₹/$/£/AED amounts, gram weights, refractive indices, year mentions, section numbers from backup are still present in humanized version | ❌ No — too risky to auto-restore numerically | FAIL, ask user |
| C12 | **Every figure in the body is traceable.** Each currency amount, percentage, threshold and count either sits in a citation-bearing context or is repeated from one elsewhere in the article | ❌ No — a source cannot be invented | FAIL, list each orphan figure |
| C13 | **Zero draft artifacts.** No `(industry estimate)`, `(approx)`, `(TBD)`, `TODO`, `[source needed]`, `(verify)`, `(unverified)`, `XX`, `TK` anywhere in the body | ❌ No — needs a rewrite, not a deletion | FAIL, show line |
| C14 | **Brand positioning does not contradict the client's live site.** Every sentence positioning the brand is checked against `get_client_context` core offerings and against live pages | ❌ No — a positioning call belongs to the client | FAIL, show both claims |
| C15 | **No cross-article duplication in a batch.** Across articles delivered together, no body paragraph >40 chars and no markdown table is byte-identical. CTAs especially | ❌ No — needs distinct copy | FAIL, show duplicate pairs |
| C16 | **Cluster siblings are linked.** If the client already has ≥3 live pages on the same primary intent, each is either linked from the new article or logged as a deliberate exclusion | ⚠️ Report only | WARN + list unlinked siblings |
| C17 | **Delta re-score ≥80.** Recompute ONLY the prose-mutable AEO dimensions and carry the frozen dimensions forward from Gate A. Replaces the standalone full re-score (old Journey A step 7) | ❌ No — a score is a measurement | FAIL, show which dimension dropped |

---

## Workflow

### STEP 1: Locate the pre-humanize backup

The humanize-nuyug skill writes a `.md.original` backup before running. Find it:

```bash
if [ -f "${article}.md.original" ]; then
  BACKUP="${article}.md.original"
else
  echo "❌ No pre-humanize backup found. Cannot run regression check."
  exit 1
fi
```

If no backup exists, **fail the gate** with a loud message. The humanize skill should have created one — if it didn't, that's a bug to surface.

### STEP 2: Extract metadata from frontmatter

Get the target keyword list, primary keyword, and brand from the article frontmatter. Same logic as `/keywords-prompts-report`.

### STEP 3: Run C1–C17 against humanized article

Each check produces one of: ✅ pass, ⚠️ auto-restored, ❌ FAIL.

Implementation skeleton:

```python
import re, itertools, frontmatter
from pathlib import Path

# batch_paths = every article being delivered together (C15).
# raw          = the unsliced file text, needed for the ---CITATIONS--- block (C12).

def normalize(s):
    return s.lower().replace('-', ' ')

def body_only(text):
    # Strip frontmatter, ---CITATIONS---, ---SCHEMA---, ---FAQ_JSON---, KEYWORDS_PROMPTS_BLOCK
    text = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.DOTALL)
    text = re.sub(r'---CITATIONS---.*$', '', text, flags=re.DOTALL)
    text = re.sub(r'<!--\s*KEYWORDS_PROMPTS_BLOCK_START.*?KEYWORDS_PROMPTS_BLOCK_END\s*-->',
                  '', text, flags=re.DOTALL)
    return text

# C1: keyword presence
backup_body  = body_only(open(backup).read())
current_body = body_only(open(article).read())
backup_norm  = normalize(backup_body)
current_norm = normalize(current_body)

missing_kw = []
for kw in keywords:
    if normalize(kw) not in current_norm:
        missing_kw.append(kw)

# C5: em-dashes
em_dashes = current_body.count('—')

# C6: banned words
BANNED = ['crucial','comprehensive','delve','leverage','robust','seamless','moreover',
          'furthermore','additionally','underscores','multifaceted','exquisite',
          'mesmerising','enchanting','captivating','breathtaking','intricate']
banned_hits = [w for w in BANNED if re.search(rf'\b{w}\b', current_body, re.I)]

# C7: link count
backup_links  = set(re.findall(r'\]\((https?://[^)]+)\)', backup_body))
current_links = set(re.findall(r'\]\((https?://[^)]+)\)', current_body))
missing_links = backup_links - current_links

# ---------------------------------------------------------------- C13 first:
# cheapest check in the file, and the one that most embarrasses you in review.
DRAFT_ARTIFACTS = [
    r'\(industry estimate\)', r'\(approx\.?\)', r'\(approximate\)',
    r'\(TBD\)', r'\bTODO\b', r'\[source needed\]', r'\(source\?\)',
    r'\(verify\)', r'\(check\)', r'\(unverified\)', r'\(citation needed\)',
    r'\bXX\b', r'\bTK\b', r'\bLOREM\b',
]
artifacts = []
for i, line in enumerate(current_body.splitlines(), 1):
    for pat in DRAFT_ARTIFACTS:
        if re.search(pat, line, re.I):
            artifacts.append((i, pat, line.strip()[:160]))
# Never auto-strip these. "(industry estimate)" is load-bearing: deleting the
# parenthesis leaves an unsourced claim asserted as fact, which is worse than
# the hedge. Either source the number or cut the sentence. FAIL and show it.

# ---------------------------------------------------------------- C12
# Every figure must be traceable. Scope is the H2 SECTION, not the sentence:
# you cite a number once, and the citation covers every repeat of it.
FIGURE = re.compile(r'(?:AED|USD|SAR|₹|\$|£|€)\s?[\d,]+(?:\.\d+)?'
                    r'(?:\s?(?:million|billion|m|bn))?|\b\d+(?:\.\d+)?%')

# Provenance must be something that CANNOT occur as ordinary prose.
# Learned the hard way: a first version accepted bare nouns (authority, agency,
# department, register, portal) as provenance. In regulatory writing those are
# everyday vocabulary — "visa authority", "business-setup agency" — so every
# section matched, the check returned 0 on an article with two uncited prices,
# and it was worse than no check. Require links or NAMED sources only.
#
# GENERIC CORE — valid for every client, no configuration needed.
PROVENANCE_CORE = (
    r'\]\(https?://'                                          # a real outbound link
    r'|(?:per|according to|cited in|sourced from|published by)'
    r'\s+(?:the\s+)?[A-Z][A-Za-z&.\-]+'                       # attribution to a proper noun
    r'|cited at the end|per the sources below'                 # citation pointer
    r'|(?:Act|Law|Rule|Regulation|Decree|Decree-Law|Circular|Notification)'
    r'\s+No\.'                                                 # legal instruments, any jurisdiction
)

# PER-CLIENT NAMED SOURCES — the regulators and systems that client's articles
# cite by name without always linking. Read from client context; empty is fine.
#   ctx = get_client_context()
#   NAMED = ctx.get('brand_details', {}).get('named_sources', [])
# Worked example, Aviaan / UAE:
#   ["Ministry of Economy", "Ministry of Finance", "Dubai Land Department",
#    "Federal Tax Authority", "Real Estate Regulatory Agency",
#    "Commercial Companies Law", "Trakheesi", "Mollak", "UAE Government portal"]
# Worked example, an India-market client:
#   ["Reserve Bank of India", "SEBI", "MCA", "Income Tax Department", "GSTN"]
NAMED = [re.escape(n) for n in named_sources]        # [] when unconfigured
PROVENANCE = re.compile(
    PROVENANCE_CORE + ('|' + '|'.join(NAMED) if NAMED else '')
)
# Illustrative numbers are not factual claims and must not be flagged.
HYPO = re.compile(r'\bsay\b|for example|for instance|imagine|suppose|'
                  r'projecting|hypothetical|e\.g\.', re.I)

def h2_sections(body):
    """Split on H2. H3s stay with their parent H2 — that is the citation scope."""
    out, cur = [], ['(preamble)', []]
    for line in body.splitlines():
        if line.startswith('## '):
            out.append(cur); cur = [line[3:].strip(), []]
        else:
            cur[1].append(line)
    out.append(cur)
    return [(h, '\n'.join(ls)) for h, ls in out]

def figure_key(f):
    return f.replace(' ', '').upper().rstrip(',.')

sourced, orphans = set(), {}
for head, txt in h2_sections(current_body):
    has_prov = bool(PROVENANCE.search(txt))
    for para in txt.split('\n\n'):
        if HYPO.search(para):
            continue
        for fig in FIGURE.findall(para):
            key = figure_key(fig)
            if has_prov:
                sourced.add(key)                  # cited once = cited everywhere
            else:
                orphans.setdefault(key, (head, para.strip()[:95]))
orphans = {k: v for k, v in orphans.items() if k not in sourced}

# SEVERITY IS FAIL-SAFE. C12 hard-fails only when the client has a configured
# named_sources list, because only then is a "no provenance" verdict trustworthy.
# With named_sources empty it WARNS and lists the figures for a human to eyeball.
# A new global check must never block a client whose conventions it cannot read.
#
# Measured on the Aviaan batch that triggered this check:
#   pre-fix  -> 2 orphans, exactly the two uncited AED price figures
#   post-fix -> 0 orphans
#   false positives across ~40 cited government figures -> 0
# If a change to PROVENANCE moves either number, it is wrong. Re-run both
# directions against a known-bad and known-good article before shipping it.

# ---------------------------------------------------------------- C15
# Batch duplication. Run when >1 article is delivered together.
def paras(path):
    b = body_only(open(path, encoding='utf-8').read())
    return [p.strip() for p in b.split('\n\n') if len(p.strip()) > 40]

dupes = []
for a, b in itertools.combinations(batch_paths, 2):     # batch_paths = the delivery set
    shared = set(paras(a)) & set(paras(b))
    for para in shared:
        dupes.append((a, b, para[:160]))
# Shared ---CITATIONS--- lines are fine (same regulator, same source), and a
# shared factual table drawn from one government fee schedule can be a
# deliberate call — log it, do not fail it. Shared BODY PROSE is never fine.
# A CTA repeated verbatim across two articles publishing together is the most
# visible version of this and the one a founder spots first.
```

#### C14 and C16 — the two checks that need the network

Gate B is otherwise offline. These two cost **one cheap call each** and are the
only way to catch a contradiction between the draft and what the client already
published. Run them before client delivery; skip with `skip_network=true` for a
mid-pipeline run.

**C14 — brand positioning vs the live site.** Pull the brand's own claims and
compare:

```python
# 1. what the client says it does
ctx = get_client_context()                     # core_offerings, brand_context
# 2. every sentence in the draft that positions the brand
BRAND_CLAIM = re.compile(rf'{brand}\s+(works|sits|does not|cannot|only|supports|'
                         rf'operates|handles|provides|is not|specialis)', re.I)
claims = [s_ for s_ in sents if BRAND_CLAIM.search(s_)]
# 3. what the live site already claims on the same subject
#    one site: query per positioning topic
search_serp(query=topic, allowed_domains=ctx['domain'])
```

FAIL when a draft claim narrows or widens what a live page asserts. Do **not**
resolve it by editing either side — a service-boundary claim is the client's
call, and guessing puts a public contradiction on their domain. Surface both
strings side by side and stop.

The failure that created this check: a draft placed the brand in a
"preparatory layer alongside whichever accredited firm signs" while a live page
advertised "RERA, KHDA, and DED-compliant audits".

Note what closer checking showed, because it is the general lesson. A second
live page claiming "approved auditors in DMCC, JAFZA, DAFZA..." looked like the
same contradiction and was not — free-zone panel approval is a *different
register* from the emirate-level accreditation the article was about. So C14
must report the two strings and the register each one refers to, and let a human
judge. An automated verdict here produces false alarms that cost more review
time than the defect. Only one of those two pages was actually wrong.

**C16 — cluster siblings.** Count what already ranks for the same intent:

```python
existing = search_serp(query=primary_intent, allowed_domains=ctx['domain'])
linked   = set(re.findall(rf"{ctx['domain']}/([a-z0-9-]+)/", current_body))
unlinked = [u for u in existing if slug(u) not in linked]
```

WARN, do not fail. Adding a page to a cluster is legitimate; adding it *blind*
is not. If ≥3 siblings exist, say so plainly in the report: "this is page N of
an existing cluster, M siblings unlinked". Then the choice to consolidate or add
is made deliberately rather than discovered in a GSC cannibalization report a
quarter later.

Also run `check_urls_liveness` over every internal link before delivery,
including sibling links to articles in the same unpublished batch — those 404
until the batch goes live, so they are only valid if the batch publishes
together. Flag them as batch-dependent rather than dead.

### STEP 4: Auto-restore (if not in strict mode)

For each restorable item:

**C1 — missing keyword:** find the most relevant section (use H2/H3 keyword matching), then inject a short natural sentence containing the missing keyword phrase. Use the same surgical-injection pattern from this session's recovery pass:

> Before: "Bridal-look jewellery under ₹15,000 is a real category."
> After: "Bridal-look jewellery under ₹15,000 is a real category. Affordable bridal jewellery that looks like real gold sits squarely in this band."

**C4 / C7 — missing internal link:** find the sentence in the backup that contained the link, find the closest matching sentence in the humanized version, restore the link with the original anchor text.

**C5 — em-dash:** simple `s/—/-/g` on body only (never frontmatter or citations).

**C6 — banned word:** swap-table replacement:
- `crucial` → `key` / `essential`
- `comprehensive` → `full` / `complete`
- `delve into` → `look at` / `cover`
- `leverage` → `use` / `tap into`
- `robust` → `strong` / `solid`
- `seamless` → `smooth` / `clean`
- `moreover` / `furthermore` / `additionally` → delete or `and` / `also`
- `exquisite` / `mesmerising` / `enchanting` / `captivating` → `striking` / `well-made` (jewellery context)

**C10 — brand spec phrase missing:** restore the exact phrase from the backup into the same section. Brand specs are NEVER paraphrased — they are Nuyug's published positioning.

### STEP 5: Hard fails (any of these → stop and ask user)

- C2 — primary keyword stripped from H1
- C3 — H2 question-ratio dropped below 50%
- C8 — frontmatter modified
- C9 — schema/FAQ_JSON modified
- C11 — number/amount/section-reference changed
- C12 — any figure in the body with no traceable source
- C13 — any draft artifact or hedge marker left in the body
- C14 — brand positioning contradicts a live client page
- C15 — body prose or a table duplicated across a batch

Each hard fail surfaces with the exact diff line so the user can decide: revert humanize, accept the change, or fix manually.

### STEP 6: Report

```
════════════════════════════════════════════════════════════
POST-HUMANIZE GATE B: <article slug>
════════════════════════════════════════════════════════════

C1  Keyword presence              [N missing → M restored, 0 remaining]
C2  Primary KW in H1              ✅
C3  H2 question ratio             ✅ (75%, was 75%)
C4  Internal links present        [N missing → M restored]
C5  Em-dashes                     [3 found → 3 fixed]
C6  Banned words                  [2 found → 2 fixed]
C7  Link count delta              -2 → restored to 0
C8  Frontmatter integrity         ✅
C9  Schema/FAQ_JSON integrity     ✅
C10 Brand specs                   ✅
C11 Numbers/amounts integrity     ✅
C12 Figures traceable             [0 orphan figures]
C13 Draft artifacts               [0 found]
C14 Positioning vs live site      ✅ (3 brand claims checked)
C15 Batch duplication             [0 duplicate paragraphs across 4 articles]
C16 Cluster siblings              ⚠️ page 5 of 5, 2 siblings unlinked
C17 Delta re-score                ✅ 84/100 (D2 84→82, frozen dims carried from Gate A)
────────────────────────────────────────────────────────────
VERDICT: ✅ PASS — auto-restored 5 items, 0 hard fails
       OR ⛔ FAIL — N hard fails, see diff below
════════════════════════════════════════════════════════════
```

### STEP 6b: C17 — the delta re-score (replaces the standalone full re-score)

**Why this exists.** Journey A used to run a second full `/aeo-score` after Gate B. That
re-ran all twelve dimensions, including the network-bound D8 liveness sweep, on an article
whose frozen regions Gate B had *just byte-verified*. 8-12 min per article to re-measure
things that provably cannot have changed.

Humanization rewrites body prose only. The freeze list is enforced by C8 (frontmatter),
C9 (schema + FAQ), C11 (every figure), C4/C7 (every link). So a dimension is worth
re-scoring **only if prose can move it**:

| Dim | Prose-mutable? | Action | Guaranteed by |
|---|---|---|---|
| D1 Heading Format & Answer Structure | **Partly** | Re-score the answer layer only: answer-first ≤60 words, standalone first sentence <29 words, definition inside first 100 words, and the CLIP CHECK. Heading text itself is frozen. | C3 (≥50% question H2s), structural footprint |
| D2 Section & Paragraph Structure | **Fully** | **Re-score in full.** Highest-risk dimension — the humanizer targets sentence length directly, which is exactly what ≤4 sentences / ≤80 words / ≤300-word sections measure. | nothing — must be measured |
| D3 FAQ Quality | No | **Skip.** Carry Gate A score. | C9 byte-verifies FAQ + schema |
| D4 Structured Formats | No | **Skip.** Carry Gate A score. | C9 + structural footprint (tables frozen) |
| D5 Data Density & Citations | **Proper-noun density only** | Re-score entity/proper-noun density (local, no network). Figures, stats and citation count are frozen. | C11 (figures), C12 (traceability), C4/C7 (citations) |
| D6 Multi-Intent & Completeness | **Word count only** | Re-score word count against the client band. Sub-intents are frozen with the headings. | structural footprint |
| D7 E-E-A-T | No | **Skip.** Carry Gate A score. | C8 frontmatter unchanged |
| D8 Internal Linking + liveness | No | **Skip the liveness sweep.** Links are frozen and C4/C7 verify presence. Liveness could only change if the external web moved in the ~20 min since Gate A — and `/final-check-*` re-verifies every URL with `--no-cache` before delivery anyway. | C4, C7, and G5/G6 at final-check |

**Compute it as:**

```
delta_total = (Gate A score for D3, D4, D7, D8 — carried verbatim)
            + (freshly measured D1-answer-layer, D2, D5-entity, D6-wordcount, D9)
⛔ GATE: delta_total ≥ 80   (identical threshold to the old full re-score)
```

Given C8/C9/C11/C4/C7 all passed, this is **arithmetically equivalent** to a full re-score.
It is not a relaxed gate — it is the same gate without the duplicated measurements.

**If it drops below 80:** restore `.original`, fix at Journey A step 4, re-humanize. Never
add new content after humanization. In practice a C17 drop is almost always D2 — see the
prose-constraint block now carried in the humanizer system prompt, which prevents it.

**Run the deterministic scorers, do not hand-measure the delta:**

```bash
python3 ~/.claude/scripts/pre_score.py  <article.md> --client <c> --json   # D2, D6 word count, META
python3 ~/.claude/scripts/clip_check.py <article.md>                       # D1 answer layer + clip
```

Between them these cover every prose-mutable dimension except D5 entity density, which is the
only one needing a reading pass. Compare each against the Gate A run on the same article — a
drop in a countable dimension is a C17 failure regardless of how the prose reads.

**Cost:** ~1-2 min with the scorers (was 8-12 min for the full re-score, 3-4 min hand-measured).

---

### STEP 7: Regenerate downstream deliverables

If anything was restored, regenerate the `.docx`:
1. Re-run pandoc on the body-only slice
2. Apply table borders
3. Insert banner-at-top if `featured_image_path` is set in frontmatter

So Gate B is end-to-end: humanize → check → restore → re-export.

---

## Pipeline integration

Every humanize-* skill MUST invoke this gate at the end:

```
Stage 3 (humanize) finishes successfully
  ↓
Stage 4: /post-humanize-check <slug>  ← automatic
  ↓
- If PASS: proceed to /embed-keywords-prompts (Stage 5)
- If hard FAIL: stop, surface diff, ask user before proceeding
```

The humanize skills now end with:
```
After API success and post-API auto-fix, run:
  /post-humanize-check <slug>
This is NOT optional. Do not proceed to embed-keywords-prompts until Gate B passes.
```

---

## Important rules

1. **Backup is mandatory.** Never run this gate without a pre-humanize backup. Fail loud if missing.
2. **Hyphen-insensitive matching everywhere.** Same rule as `/keywords-prompts-report`, `/seo-optimize`, `/embed-keywords-prompts`.
3. **Body-only scope.** Exclude frontmatter, ---CITATIONS---, ---SCHEMA---, ---FAQ_JSON---, and any KEYWORDS_PROMPTS_BLOCK markers. Humanize should never touch these regions; if it did, that's already a hard fail (C8 or C9).
4. **Auto-restore is surgical, not creative.** Inject one short sentence per missing keyword. Restore one link per missing link. Swap one banned word per occurrence. No paragraph rewrites, no creative wordsmithing — that re-introduces AI patterns.
5. **Number fidelity is non-negotiable.** ₹ amounts, gram weights, micron specs, refractive indices, Mohs values, karat numbers, section references, years — all must match the backup exactly. If they don't, FAIL HARD.
6. **Brand spec phrases are canonical.** "1-year warranty", "hypoallergenic, nickel-free", "anti-tarnish-treated", "AAA-grade" — these are Nuyug's published positioning. Never let humanize downgrade ("good warranty") or embellish ("lifetime guarantee"). Restore exactly from backup if missing.
7. **Don't regenerate DOCX unless something changed.** If C1–C17 all pass without restoration, skip Step 7 — the existing DOCX is still valid.
8. **A long citations list is not coverage.** C12 asks whether *each figure* is traceable, never whether the article has sources. Twelve regulator citations and one uncited price is still a failing article, and the price is the number a reader will check.
9. **Never auto-strip a hedge.** Deleting `(industry estimate)` converts a flagged guess into an asserted fact. C13 fails so a human sources the number or cuts the claim.
10. **Positioning conflicts are escalated, never resolved.** C14 stops the gate and shows both strings. Editing the draft to match the live page, or the reverse, is a commercial decision that belongs to the client.
11. **C12–C16 are not humanization regressions.** They catch defects that pass through humanization untouched, which is why they need their own gate. Every one of them shipped to a founder review before this section existed.

---

## Examples

### Example 1 — invoked automatically by humanize-nuyug

```
[humanize-nuyug runs, succeeds]
[humanize-nuyug calls: /post-humanize-check imitation-jewellery-looks-like-real-gold]

Output:
  POST-HUMANIZE GATE B: imitation-jewellery-looks-like-real-gold
  C1  Keyword presence    [3 missing → 3 restored]
  C5  Em-dashes           [2 found → 2 fixed]
  C6  Banned words        [0]
  ...
  VERDICT: ✅ PASS — 5 auto-restored, 0 hard fails
  DOCX regenerated.
```

### Example 2 — manual strict-mode audit

```
/post-humanize-check imitation-jewellery-looks-like-real-gold strict=true
```

In strict mode, ANY regression (even an em-dash) fails the gate. Use this when you want a clean baseline audit before client delivery.
