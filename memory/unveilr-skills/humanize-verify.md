---
name: humanize-verify
description: Offline check of whether text is ACTUALLY humanized after humanization completes — works with any humanizer (external tool OR your internal model). No API. Computes the proxy signals AI-detectors use (burstiness, sentence-length variance, AI-tell words, repeated openers, em-dashes) and compares the humanized article against its pre-humanize .original backup. Answers 'is my humanizer working?' — which /post-humanize-check does NOT.
---

<!-- Provenance: Unveilr platform registry · category=content · version=1 · scope=global · synced 2026-08-25 -->
<!-- NOTE: the script path below is the author's machine (pranjalrai). Repoint before use on this host. -->

# Humanize-Verify — "Is the text actually humanized?" (offline)

`/post-humanize-check` (Gate B) only proves humanization did not BREAK the article
(keywords/links/numbers preserved). It says nothing about whether the prose now
reads human. This skill answers the other question: **did the humanizer actually
make the text less machine-like?** It is humanizer-agnostic — use it whether the
rewrite came from aihumanize.io or your own internal humanizer model.

No external detector API is used. It computes the same proxy signals AI-detectors
score under the hood, so it runs fully offline and free.

## Input

$ARGUMENTS

Parse for:
- **article**: path or slug of the freshly humanized `.md` (required)
- **original**: optional explicit path to the pre-humanize backup. Default: `<article>.md.original`
- **brand**: optional override; otherwise read from the article's `brand:` frontmatter
- **batch**: if `true` (or a directory/glob is given), run across many articles and print a summary table

## ⛔ Vakilsearch STRICT brand gate (auto-on)

When the article's `brand` is **Vakilsearch** (frontmatter `brand:` or `--brand vakilsearch`),
the script runs an extra **hard-fail** gate BEFORE the proxy scoring. The humanizer
(aihumanize.io under UK English) is the #1 cause of these exact regressions, so a
Vakilsearch article that reads perfectly human still **fails** if any of these are present:

| Violation | Rule | Why the humanizer causes it |
|---|---|---|
| `VakilSearch` (capital S) | brand is **Vakilsearch**, lowercase 's' | rewriter title-cases brand names |
| `per cent` / `percent` / `percentage` | always the **`%`** symbol, no space | UK-English locale expands `%`→"per cent" |
| Contractions (`you'll`, `there's`, `don't`…) | formal legal register — **none allowed** | humanizer adds casual contractions |

Any hit → verdict `❌ BRAND-STRICT FAIL`, which **overrides** the proxy score (an
on-brand-broken article is not shippable no matter how human it reads). Source of
truth: `memory/strict_vakilsearch_brand_name_and_percent.md` +
`strict_aeo_pipeline_order.md`. This gate is Vakilsearch-only — Care Dale and Nuyug
articles skip it and are judged on proxy signals alone.

## What it measures (proxy signals)

| Signal | Human prose | AI prose | Why it matters |
|---|---|---|---|
| **Burstiness** (CV of sentence length) | high (≥0.5) | low (uniform) | the #1 thing detectors key on |
| Repeated sentence-opener rate | low | high | AI reuses the same sentence starts |
| AI-tell words | ~0 | many | delve, crucial, seamless, robust, moreover… |
| Em-dashes | 0 | frequent | classic AI punctuation |
| Sentence-length stdev | high | low | varied rhythm = human |
| Paragraph-length stdev | high | uniform | AI writes even blocks |
| Lexical diversity (TTR) | higher | lower | repetition tell |

## Workflow

1. **Locate the backup.** The humanize step MUST write `<article>.md.original`
   BEFORE running (your internal-model pipeline has to do: copy → humanize → verify).
   If no backup exists, the script still runs in single-file mode (absolute metrics
   only, no before→after delta) — but warn the user a delta is far more informative.

2. **Run the analyzer:**
   ```bash
   python3 /Users/pranjalrai/Documents/articles/scripts/humanize_verify.py <article.md>
   # or with an explicit backup:
   python3 .../humanize_verify.py <article.md> --original <backup.md>
   ```

3. **Read the verdict.** The script scores absolute floors + before→after deltas:
   - `✅ HUMANIZER WORKING` — reads human on proxy signals (score ≥ 85%)
   - `⚠️ MARGINAL` — some signals still read AI; tune the humanizer (60–85%)
   - `❌ NOT WORKING` — still machine-written (< 60%)

4. **For a batch run**, loop the script over every humanized `.md` that has an
   `.original`, collect each verdict, and present a table:

   ```
   | Article slug | Burstiness Δ | AI-tells Δ | Verdict |
   |---|---|---|---|
   | benefits-washing-face-filtered-water | 0.63→0.66 | 0→0 | ✅ WORKING |
   | ...                                  | ...        | ...  | ...        |
   ```

   A humanizer that is "working right" should produce ✅ on the large majority of a
   10–20 article sample — one good doc is not proof.

## How to read it for "is my tool working right?"

- **Consistent ✅ across a batch** → your internal humanizer is doing its job.
- **Burstiness barely moves (Δ < 0.02)** → the model is paraphrasing word-for-word
  without varying rhythm; detectors will still flag it. Tune toward mixing short and
  long sentences.
- **AI-tell words not dropping** → add a post-pass swap table (reuse the C6 list).
- **Em-dashes reappear** → add `—`→`-` cleanup.

## Relationship to the other gates (run all three)

```
your internal humanizer runs
  ↓
/post-humanize-check <slug>   → did it BREAK content? (keywords/links/numbers)
  ↓
/humanize-verify <slug>       → is it ACTUALLY humanized? (this skill)
  ↓
/aeo-score <slug>             → did overall AEO quality hold ≥ 80?
```

`/post-humanize-check` + `/humanize-verify` + `/aeo-score` together fully answer
"is my humanizer working right" — fidelity, human-ness, and quality.

## Important rules

1. **Proxy ≠ ground truth.** These metrics correlate with detector output but are not
   a detector. For a hard client guarantee, spot-check the ✅ articles through a real
   detector (Originality.ai / GPTZero) occasionally to calibrate the floors.
2. **Always prefer the before→after delta.** Single-file absolute metrics can pass a
   doc that was already human-ish; the delta proves the humanizer caused the change.
3. **Batch, don't cherry-pick.** Judge the tool on a sample, not one article.
4. **Tune the floors in the script** (`FLOORS` dict) if your brand voice runs
   naturally short/long — recalibrate against a few known-good human articles.
