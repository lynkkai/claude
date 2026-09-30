# Rule audit: articles/sales-conversation-intelligence.md (#21)

Checked with `scripts/audit_article.py` (rules from `seo-article`, `seo-score`, `aeo-score`, `humanize-verify` and the Lynkk rules in `CLAUDE.md`).

**Result:** 62 checks passed, 0 failed. Body length 1512 words. Primary keyword: conversation intelligence (1,900 / SD 60).

## Mechanical rules checked (all pass)
H1 13-15 words; meta title ≤60 with primary near the start; meta description 150-160 with primary; evergreen slug; word count at or above the template minimum; primary in first 100 words and in an H2; density 0.5-1.5%; every secondary keyword present; ≥6 question H2s; no dead headings; every section's first 200 characters contain a number; sections ≤300 words without H3s; paragraphs ≤80 words and ≤4 sentences; 5-10 FAQs at 40-60 words; FAQ schema matches body word for word; tables ≤4 columns; 8-14 links; ≥3 lynkk.ai links incl. a feature or use-case page; ≥2 external links, all official government or standards sites; no links to unpublished posts; zero competitor links; no em or en dashes; no placeholders; no internal notes in the article; no AI-tell words; brand spelled Lynkk; Article, FAQPage and BreadcrumbList schema.

## Research and sources
- Heading sources: autocomplete for 'conversation intelligence' (what is / software) plus brief keywords (gong alternatives, sales call recording software). Competitor prices from memory/competitor-facts.md (vendor pricing pages, checked 2026-09-30). The example call output is illustrative and labeled as such.
- Competitor and vendor facts are cited in plain text only (no links), checked 2026-09-30.
- Keyword volumes: Ubersuggest US (locId 2840), pulled 2026-09-30. The daily report limit was reached before new keyword lookups, so `keywords_added` uses brief keywords already measured that day.

## External authority links (2)
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=632
- https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section2511

## Open items for content writers (not shown in the article)

**1. Author and images**
- Add a named author and a short bio (E-E-A-T requirement), then set `author` and `author_bio_url` in the frontmatter.
- Add the featured image at the path in `featured_image_path` (1200x630) with the alt text in `featured_image_alt`, and add screenshots from our own accounts.

**2. Facts and evidence to add before publishing**
- Which CRMs Lynkk updates (HubSpot, Salesforce?); a real anonymized call walkthrough with permission; a quote from a sales leader with permission.
- Examples in the article are labeled illustrative; replace with real, permissioned examples where available.

**3. Publishing checklist**
1. Click-test all links. lynkk.ai pages returned HTTP 200 in Ubersuggest's crawl; the external pages above were confirmed in search results restricted to their official domains on 2026-09-30.
2. Re-check vendor steps and prices on each vendor's own help or pricing page (search by name; no links kept).
3. Add the 2 inbound links in `inbound_links_planned`.
4. Set the final blog URL path and canonical.
