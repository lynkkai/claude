---
name: seo-optimize
description: Run a full SEO optimization audit + automatic fixes on one or more articles. Complements AEO. Checks meta tags, slug, H1 keyword presence, keyword density, internal/external linking, schema completeness, image alt text, heading hierarchy, mobile readability, Open Graph fields, and canonical URLs. Produces a scored report and applies the safe fixes inline.
---

<!-- Provenance: Unveilr platform registry · category=content · version=2 · scope=global · synced 2026-08-25 -->
<!-- AVIAAN: default client below is nuyug — pass client=aviaan-equivalent settings explicitly.
     Aviaan link band 8-14, no /collections/ rule, AED currency, UAE/British spelling. -->

## ⛔ HARD RULE (GATE) — INBOUND internal links required

Treat inbound internal links as a HARD scoring gate. Every article MUST earn **at least 1–2 INBOUND internal links** — existing, live, topically-relevant pages on the SAME domain that link **TO** this article — separate from and in addition to the article's own OUTBOUND links. An article with **0** planned/placed inbound links **FAILS this gate** (it launches as an internal-link orphan with ~0 internal PageRank; diagnosed on the VS CIN cannibalization case, 2026-07-22: our page 0 GSC impressions vs the in-house page ~602, decided by inbound links 1 vs 4 — schema was identical). To PASS: name 1–2 live sibling source pages + the exact anchor text that will link to this article, and verify them live. If no relevant sibling exists to link from, FLAG it — do not pass silently.


# SEO Optimization Pass

AEO scoring targets AI engines (ChatGPT, Perplexity, Gemini, Google AI Overviews). **SEO scoring targets classic Google search ranking signals** — these overlap but are not the same. Run this skill AFTER `/aeo-score` passes (≥80) and BEFORE humanization, so SEO fixes don't get re-broken by humanization.

## Input

$ARGUMENTS

Parse for:
- **articles**: One or more article slugs OR paths to `.md` files. Required. Accepts `all` to scan everything in `articles/`.
- **client**: Brand context. Default and primary target: `nuyug`. Loads client-specific anchor text rules, internal-link patterns, and meta conventions.
- **fix**: `report` (default — audit only), `safe` (auto-apply the non-destructive fixes), or `aggressive` (apply all suggested fixes including rewording for keyword density). Use `safe` for client-bound articles.

---

## What SEO Optimization Covers (the 12 dimensions, 100 pts total)

### S1 — Meta tags & SERP snippet (15 pts)

- **(4)** `meta_title` is ≤ 60 chars, includes primary keyword **in the first 50 chars**, and ends with brand or year if space allows
- **(4)** `meta_description` is 150-160 chars, leads with the primary value/answer, includes the primary keyword once, has a soft call-to-action
- **(3)** `suggested_url` slug is ≤ 7 words, hyphenated lowercase, contains primary keyword, no stop words ("the", "a", "and", "of", "in") unless natural
- **(2)** Open Graph fields (`og:title`, `og:description`, `og:image`) are present in frontmatter or schema. For Shopify, these auto-populate from meta — confirm.
- **(2)** Canonical URL is set (defaults to article slug on brand domain)

### S2 — Heading hierarchy & keyword placement (10 pts)

- **(3)** H1 contains the primary keyword **verbatim or as close paraphrase**. Only one H1 per page.
- **(3)** Primary keyword appears in at least one H2
- **(2)** Strict H1 → H2 → H3 hierarchy, no skipped levels
- **(2)** Average heading every 150-250 words

### S3 — Primary & secondary keyword usage in body (15 pts)

- **(5)** Primary keyword in the first 100 words of the body
- **(4)** Primary keyword density 0.5%–1.5% (not stuffed, not under-used). Calculate: primary_count × 100 / body_word_count
- **(3)** Each secondary keyword appears at least once in body, hyphen-insensitive
- **(3)** LSI / related-term coverage — at least 5 semantically related terms (synonyms, sub-topics) appear naturally

### S4 — Internal linking (10 pts)

- **(3)** 8-14 internal links total for a 1500–2500 word article
- **(3)** At least 1 link to the brand's pillar/parent page or collection page (e.g., for Nuyug, at least 1 `/collections/*` link per cluster)
- **(2)** At least 2 cross-links to sibling articles in the same content cluster
- **(2)** All internal anchor text is descriptive topic phrase (not "click here", "this", or the brand name)

### S5 — External linking & authority (5 pts)

- **(3)** At least 2 external links to authoritative sources (.gov, .edu, well-known industry/news sites). 0 external links = lose all 3 pts.
- **(2)** All external links use `rel="noopener"` and either `rel="nofollow"` for promotional or default follow for editorial. Default editorial follow is fine for citations.

### S6 — Image SEO (10 pts)

- **(3)** Featured image is present (`featured_image_path` in frontmatter)
- **(3)** Featured image alt text is descriptive (8-15 words), includes a topic keyword, mentions brand naturally
- **(2)** Inline images (if any) have alt text. If no inline images, give 2/2 by default.
- **(2)** Image file names are descriptive (slugified topic terms, not `IMG_1234.png`)

### S7 — Schema markup (10 pts)

- **(3)** `Article` schema with `headline`, `datePublished`, `dateModified`, `author`, `publisher`
- **(3)** `FAQPage` schema present if FAQs exist; questions and answers match the visible FAQ body word-for-word
- **(2)** `BreadcrumbList` schema (Home → Section → Article)
- **(2)** `inLanguage` set (e.g., `en-IN` for India-targeted content)
- **HARD FAIL (-10)** No `@type: Product` node nested inside Article schema's `about` / `mentions` / `isPartOf` arrays. Google parses every nested Product independently and the Product Snippets report demands `offers`/`review`/`aggregateRating` — which an Article page does not have. Real incident: Care Dale `postpartum-hair-fall-hard-water-cities-india` flagged in GSC, May 2026. Rewrite to `@type: Thing` (preferred) or `@type: Brand` with the same `name`. Reserve `@type: Product` for actual PDP URLs.

### S8 — Content depth & engagement signals (10 pts)

- **(3)** Word count appropriate: 1500–2500 for cluster articles, 2500–4000 for pillar pages
- **(3)** Average sentence length ≤ 22 words (mobile readability)
- **(2)** Paragraphs average ≤ 4 sentences (mobile readability)
- **(2)** Bullets/numbered lists used for any 3+ comparable points (skim-readability)

### S9 — Mobile-friendly markup (5 pts)

- **(2)** No table wider than 4 columns (mobile horizontal scroll breaks)
- **(2)** No paragraph longer than 100 words
- **(1)** No sentence longer than 40 words

### S10 — E-E-A-T signals (5 pts)

- **(2)** Author name present (`author` field), linked to author bio URL if available
- **(2)** "Last Updated" / `dateModified` visible in body (not just schema)
- **(1)** At least one verified source citation in body

### S11 — URL & link health (5 pts)

- **(3)** All internal links return HTTP 200 (run live-check on every link)
- **(2)** All external links return HTTP 200 OR 301-302 (with the redirect resolving)

### S12 — Non-scored binary checklist

- [ ] No duplicate content (article is unique vs every existing post on the brand's blog)
- [ ] Cannibalization audit clean (no two articles target the same primary keyword)
- [ ] Featured image dimensions match the Nuyug CMS template (1500×940)
- [ ] Article is in draft state, not auto-published
- [ ] `noindex` is NOT set (unless intentionally)

---

## Workflow

### STEP 1: Resolve files

Resolve slugs to `articles/<slug>.md` paths. Fail loudly on missing files.

### STEP 2: Audit each dimension

Run S1–S11 checks programmatically:

```python
# Skeleton — extract these into a script /Users/pranjalrai/Documents/articles/scripts/seo_audit.py
import re, frontmatter
from pathlib import Path

def audit_article(path, client=None):
    fm = frontmatter.load(path)
    body = extract_body(fm.content)
    body_lower_no_hyphen = body.lower().replace('-', ' ')

    scores = {}
    # S1
    mt = fm.get('meta_title', '')
    md = fm.get('meta_description', '')
    pk = (fm.get('selected_keywords') or fm.get('keywords') or [''])[0].lower()
    scores['S1_meta_title_len']     = 4 if 0 < len(mt) <= 60 and pk.replace('-',' ') in mt.lower().replace('-',' ')[:50] else 2
    scores['S1_meta_desc_len']      = 4 if 150 <= len(md) <= 160 else 2
    # ... etc for each row
    return scores

# Run S11 live-check via check_urls_liveness or curl HEAD
```

For S11, use the brand's MCP `check_urls_liveness` if available (e.g., `mcp__unveilr-nuyug__check_urls_liveness`). Otherwise `curl -I -L -o /dev/null -w '%{http_code}'` per link in parallel batches of 10.

### STEP 3: Report + (optional) fix

Render this per article:

```
══════════════════════════════════════════════════════════════
SEO SCORE: <X>/100  Article: <title>
══════════════════════════════════════════════════════════════

DIMENSION                                  SCORE   STATUS
──────────────────────────────────────────────────────────────
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
TOTAL                                      XX/100

GATE: [✅ PUBLISH-READY ≥85 | ⚠️ MINOR FIXES 70–84 | ❌ FIX REQUIRED <70]
══════════════════════════════════════════════════════════════

PRIORITY FIXES (ordered by score impact)
1. [highest impact — dimension, issue, action]
2. ...
```

If `fix=safe` or `fix=aggressive`:

| Fix | Mode | Action |
|---|---|---|
| Meta title >60 chars | safe | Truncate at last word break before 60 |
| Meta description outside 150-160 | safe | Pad with a value-prop phrase OR truncate |
| Missing canonical / OG fields | safe | Inject into frontmatter |
| Missing alt text on featured image | safe | Generate descriptive alt with primary keyword + brand |
| H1 missing primary keyword | aggressive | Suggest rewrite (do NOT auto-apply without confirmation) |
| Primary keyword density <0.5% | aggressive | Inject 1-2 more natural mentions in body |
| Primary keyword density >2.5% | aggressive | Replace some occurrences with synonyms |
| Missing schema fields | safe | Inject `inLanguage`, `dateModified`, `BreadcrumbList`, `Organization.publisher` |
| `@type: Product` nested in Article `about`/`mentions`/`isPartOf` without `offers`/`review`/`aggregateRating` | safe | Rewrite the offending node to `@type: Thing` (or `Brand`) preserving the `name` field. Prevents GSC Product Snippets "Either offers, review, or aggregateRating should be specified" error |
| Broken internal link | safe | Replace with closest live alternative from the Nuyug `/collections/<slug>` map |
| Anchor text contains brand name | safe | Rewrite to topic phrase |
| Missing "Last Updated" line in body | safe | Inject `*Last updated: <today>*` italic line right under H1 |
| Sibling article cross-links <2 | aggressive | Suggest 2 sibling article links to insert (require user confirmation) |
| Table >4 columns | aggressive | Suggest column merge or split (require user confirmation) |
| External link returns 404 | safe | Remove the link and replace with `(source no longer available)` OR find a replacement |

### STEP 4: Re-run S1–S11 after fixes

To confirm fixes held. Report delta.

### STEP 5: Output

- Chat: scorecard + priority-fix punch list + delta after fixes
- Optional DOCX deliverable: pass `format=docx` for a client-facing scorecard report

---

## Important rules

1. **AEO and SEO are separate.** Don't combine the scores. An article can be 88/100 AEO and 65/100 SEO — both need to pass independently before publish.
2. **Run AFTER `/aeo-score` passes, BEFORE humanization.** Otherwise humanization can re-break SEO (especially keyword density and exact-match headings).
3. **Hyphen-insensitive matching for all keyword presence checks.** Same rule as `/keywords-prompts-report` — never strip hyphens, normalize to spaces.
4. **Don't auto-apply aggressive fixes** without showing the diff and asking for confirmation. The user controls invasive edits.
5. **Run live link checks every time.** Stale link audits cached from a previous session are not trustworthy — links rot fast.
6. **Nuyug-specific rule:** every Nuyug article must internal-link to `/collections/<slug>` pages (per `feedback_nuyug_link_collection_pages.md`). Penalize S4 hard if missing.
7. **The publish gate is 85, not 80.** SEO is more sensitive to thin coverage than AEO — 70-84 is "minor fixes", <70 is "do not publish".

---

## Examples

```
/seo-optimize imitation-jewellery-looks-like-real-gold
```
→ Report only.

```
/seo-optimize all client=nuyug fix=safe
```
→ Audit every article in `articles/`, apply safe fixes (meta truncation, alt text injection, broken-link replacement, schema field injection, last-updated line).

```
/seo-optimize a b c fix=aggressive format=docx
```
→ Audit + apply aggressive fixes (keyword density rebalancing, sibling cross-link injection) on 3 articles, then export a DOCX scorecard.
