# Rule audit: articles/best-ai-note-takers.md

Checked on 2026-09-30 against the uploaded skill files: `seo-article`, `seo-score` (S1-S11, G1-G4), `aeo-score` (D1-D9) and `humanize-verify`, plus the Lynkk rules in `CLAUDE.md` and `memory/lynkk-brand.md`.

**Before this audit (draft v2), 11 rules failed.** Draft v3 fixes every rule that can be fixed in the text. What is left needs your team's input or a tool this environment cannot reach.

## Rules that now pass

| Rule (source file) | Requirement | v2 result | v3 result |
|---|---|---|---|
| H1 length (seo-article, aeo-score D9) | 13-15 words, one natural sentence | 17 words | **15 words** |
| No "Official" in title (aeo-score D9) | Word never used | Pass | Pass |
| meta_title (seo-score S1) | ≤60 chars, keyword in first 50, year | 53 chars, pos 5, 2026 | Pass |
| meta_description (seo-score S1, aeo D9) | 150-160 chars | 148 | **152** |
| Slug (seo-score S1) | Keyword, ≤7 words, no year | Pass | Pass |
| Keyword in first 100 words (seo-article #2) | Required | Pass | Pass |
| Keyword density (seo-score S3) | 0.5-1.5% | 1.2% | **1.3%** |
| Secondary keywords (seo-score S3) | Each used ≥1 time | Pass | Pass (all 4) |
| Quick Answer + Last updated (seo-article #3) | After H1 | Pass | Pass |
| "X is Y" definition in first 100 words (aeo D1) | Required | Pass | Pass |
| Question-format H2s (seo-score G4) | ≥6 | 6 | **8** |
| No dead headings (seo-article hard rule) | 0 | Pass | Pass |
| 200-character clip (seo-article hard rule) | Each section opens with a number + concrete claim | 5 sections failed | **0 fail** |
| Section length (aeo D2) | ≤300 words per H2 without H3s | Lynkk section 418 words | **Split into 3 question H3s** |
| Paragraphs (aeo D2) | ≤80 words, ≤4 sentences | 1 over | **0 over** |
| FAQ answers (aeo D3) | 40-60 words, 5-10 questions | 4 of 6 under 40 | **All 6 at 47-53** |
| FAQ schema sync (aeo D3) | Body = JSON-LD word for word | No schema | **Synced** |
| Tables on mobile (seo-score S9) | ≤4 columns | 7 columns | **4 and 2 columns** |
| Link count (aeo D8) | 8-14 total | 22 | **14** |
| External authority links (seo-score S5) | ≥2 | 0 | **8 vendor sources** |
| Dead links (seo-score S11, aeo D8) | 0 links to pages that do not exist | 5 links to unpublished /blog/ posts | **0** |
| Link to service page (seo-article #6) | Required | Pass | Pass (/features/meeting-bot) |
| Schema (seo-score S7) | Article, FAQPage, BreadcrumbList, inLanguage | None | **Article, ItemList, FAQPage, BreadcrumbList, en-US** |
| Image SEO (seo-score S6) | Featured image + alt text 8-15 words | None | **Alt text written (13 words); image file pending** |
| OG + canonical (seo-score S1) | Present | None | **Added** |
| Inbound links plan (seo-article + seo-score hard gate) | Name 1-2 source pages + anchors | Not named | **2 named in frontmatter** |
| Keyword expansion log (Lynkk rule) | Added keywords recorded | Pass | Pass (7 added) |
| No em or en dashes (CLAUDE.md) | 0 | 0 | 0 |
| AI-tell words (humanize-verify) | ~0 | 0 | 0 |
| Lynkk ranked #1, positive (team rule) | Required | Pass | Pass |
| Brand spelling "Lynkk" (CLAUDE.md) | Always | Pass | Pass |

## Rules still open (need your team or tools not available here)

| Rule | Why it is open | What is needed |
|---|---|---|
| Named author + bio URL (seo-score S10, aeo D7) | No author given | Author name, role, bio page |
| E-E-A-T testing ("How we evaluated") | Tests not run | Test log, meeting count, dates, screenshots |
| Featured image (seo-score S6) | No image file | 1200x630 image at the path in frontmatter |
| Link liveness (seo-score S11, hard rule) | Vendor sites blocked from this environment | Check the 8 vendor links; the 6 lynkk.ai links returned 200 in Ubersuggest's crawl |
| Inbound links live (hard gate) | Article not published | Add the 2 planned links at publish and verify |
| G2 cannibalization via GSC | GSC not connected | Connect GSC, or accept: lynkk.ai ranks for no competing keyword today |
| G3 depth vs SERP median | Could not fetch competitor articles | Spot-check top listicles; this draft is ~2,600 body words |
| Expert quote (aeo D5) | None available | A quote from a Lynkk founder or customer (real, with permission) |
| Named statistic every 200 words (aeo D5) | 8 sourced vendor facts; target ~13 | Add original test data once tests run |
| External humanizer + humanize-verify script | Script path is on the original author's machine | Self-edited for plain wording; run your humanizer if you use one |
| Lynkk free-plan limits and Pro billing terms | Not on crawled page titles | Confirm from /pricing |
| Legal source on consent laws, Reddit links, Gemini plan eligibility | Not fetched | Add links |

## Verdict

On-page rules: **pass**. Publish readiness: **not yet**, until the open items above are filled.
