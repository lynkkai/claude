# Rule audit: articles/zoom-meeting-recorders.md

Checked with `scripts/audit_article.py` (rules from `seo-article`, `seo-score`, `aeo-score`, `humanize-verify` and the Lynkk rules in `CLAUDE.md`).

**Result:** 85 checks passed, 0 failed. Body length 2513 words. Primary keyword: zoom meeting recorder (2,900 / SD 17).

## Mechanical rules checked (all pass)
H1 13-15 words; meta title ≤60 with primary near the start; meta description 150-160 with primary; evergreen slug; word count at or above the template minimum; primary in first 100 words and in an H2; density 0.5-1.5%; every secondary keyword present; ≥6 question H2s; no dead headings; every section's first 200 characters contain a number; sections ≤300 words without H3s; paragraphs ≤80 words and ≤4 sentences; 5-10 FAQs at 40-60 words; FAQ schema matches body word for word; tables ≤4 columns; 8-14 links; ≥3 lynkk.ai links incl. a feature or use-case page; ≥2 external links, all official government or standards sites; no links to unpublished posts; zero competitor links; no em or en dashes; no placeholders; no empty image links; no AI-tell words; brand spelled Lynkk; Article, FAQPage and BreadcrumbList schema.

## External authority links (2)
- https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section2511
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=632

## Open items before publishing (not shown in the article)
- 1. Add or confirm before publishing: author, bio, test screenshots, featured image, Lynkk free-plan limits, canonical URL.
- 2. Click-test all links. lynkk.ai pages returned HTTP 200 in Ubersuggest's crawl; uscode.house.gov and leginfo.legislature.ca.gov were confirmed in search indexes on 2026-09-30.
- 3. Re-check Zoom facts on Zoom's help center and competitor prices on each vendor's pricing page (search by name; no links kept).
- 4. Add the 2 inbound links in `inbound_links_planned`.
- 5. Update `seo/keyword-map-v2.md` row #3 with the primary keyword change.
