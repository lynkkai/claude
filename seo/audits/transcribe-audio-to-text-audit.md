# Rule audit: articles/transcribe-audio-to-text.md

Checked with `scripts/audit_article.py` (rules from `seo-article`, `seo-score`, `aeo-score`, `humanize-verify` and the Lynkk rules in `CLAUDE.md`).

**Result:** 84 checks passed, 0 failed. Body length 2511 words. Primary keyword: transcribe audio to text (22,200 / SD 46).

## Mechanical rules checked (all pass)
H1 13-15 words; meta title ≤60 with primary near the start; meta description 150-160 with primary; evergreen slug; word count at or above the template minimum; primary in first 100 words and in an H2; density 0.5-1.5%; every secondary keyword present; ≥6 question H2s; no dead headings; every section's first 200 characters contain a number; sections ≤300 words without H3s; paragraphs ≤80 words and ≤4 sentences; 5-10 FAQs at 40-60 words; FAQ schema matches body word for word; tables ≤4 columns; 8-14 links; ≥3 lynkk.ai links incl. a feature or use-case page; ≥2 external links, all official government or standards sites; no links to unpublished posts; zero competitor links; no em or en dashes; no placeholders; no empty image links; no AI-tell words; brand spelled Lynkk; Article, FAQPage and BreadcrumbList schema.

## External authority links (3)
- https://www.section508.gov/create/captions-transcripts/
- https://www.ada.gov/resources/effective-communication/
- https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section2511

## Open items before publishing (not shown in the article)
- 1. Add or confirm before publishing: author, bio, featured image, Lynkk free-plan limits, whether Lynkk accepts uploaded audio files, Dragon price, canonical URL.
- 2. Click-test all links. lynkk.ai pages returned HTTP 200 in Ubersuggest's crawl; section508.gov, ada.gov and uscode.house.gov were confirmed in search indexes on 2026-09-30.
- 3. Re-check competitor prices and Microsoft/Apple steps on the vendor pages (search by name; no links kept).
- 4. Add the 2 inbound links in `inbound_links_planned`.
