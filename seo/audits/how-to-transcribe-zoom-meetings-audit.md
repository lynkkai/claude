# Rule audit: articles/how-to-transcribe-zoom-meetings.md

Checked with `scripts/audit_article.py` (rules from `seo-article`, `seo-score`, `aeo-score`, `humanize-verify` and the Lynkk rules in `CLAUDE.md`).

**Result:** 65 checks passed, 0 failed. Body length 1345 words. Primary keyword: transcribe zoom (2,400 / SD 31).

## Mechanical rules checked (all pass)
H1 13-15 words; meta title ≤60 with primary near the start; meta description 150-160 with primary; evergreen slug; word count at or above the template minimum; primary in first 100 words and in an H2; density 0.5-1.5%; every secondary keyword present; ≥6 question H2s; no dead headings; every section's first 200 characters contain a number; sections ≤300 words without H3s; paragraphs ≤80 words and ≤4 sentences; 5-10 FAQs at 40-60 words; FAQ schema matches body word for word; tables ≤4 columns; 8-14 links; ≥3 lynkk.ai links incl. a feature or use-case page; ≥2 external links, all official government or standards sites; no links to unpublished posts; zero competitor links; no em or en dashes; no placeholders; no empty image links; no AI-tell words; brand spelled Lynkk; Article, FAQPage and BreadcrumbList schema.

## External authority links (2)
- https://www.section508.gov/create/captions-transcripts/
- https://www.ada.gov/resources/effective-communication/

## Open items before publishing (not shown in the article)
- 1. Add or confirm before publishing: author, bio, step screenshots, exact Zoom setting and button names, transcript file format, featured image, canonical URL.
- 2. Click-test all links. lynkk.ai pages returned HTTP 200 in Ubersuggest's crawl; section508.gov and ada.gov were confirmed in search indexes on 2026-09-30.
- 3. Re-check Zoom steps on Zoom's help center and Otter pricing (search by name; no links kept).
- 4. Add the 2 inbound links in `inbound_links_planned`.
- 5. Link from post #3 (Zoom meeting recorders) once both are live.
