# Rule audit: articles/medical-transcription-software.md (#29)

Checked with `scripts/audit_article.py` (rules from `seo-article`, `seo-score`, `aeo-score`, `humanize-verify` and the Lynkk rules in `CLAUDE.md`).

**Result:** 63 checks passed, 0 failed. Body length 1504 words. Primary keyword: medical transcription software (1,000 / SD 33).

## Mechanical rules checked (all pass)
H1 13-15 words; meta title ≤60 with primary near the start; meta description 150-160 with primary; evergreen slug; word count at or above the template minimum; primary in first 100 words and in an H2; density 0.5-1.5%; every secondary keyword present; ≥6 question H2s; no dead headings; every section's first 200 characters contain a number; sections ≤300 words without H3s; paragraphs ≤80 words and ≤4 sentences; 5-10 FAQs at 40-60 words; FAQ schema matches body word for word; tables ≤4 columns; 8-14 links; ≥3 lynkk.ai links incl. a feature or use-case page; ≥2 external links, all official government or standards sites; no links to unpublished posts; zero competitor links; no em or en dashes; no placeholders; no internal notes in the article; no AI-tell words; brand spelled Lynkk; Article, FAQPage and BreadcrumbList schema.

## Research and sources
- Heading sources: Autocomplete for 'medical transcription software' (what is / what does it do / best / what software transcriptionists use / how to transcribe medical dictation). Dragon Medical One facts from the vendor's product pages (plain text). HIPAA facts from hhs.gov (BAA provisions, Security Rule summary).
- Competitor and vendor facts are cited in plain text only (no links), checked 2026-09-30.
- Keyword volumes: Ubersuggest US (locId 2840), pulled 2026-09-30; daily report limit reached before new keyword lookups.

## External authority links (2)
- https://www.hhs.gov/hipaa/for-professionals/covered-entities/sample-business-associate-agreement-provisions/index.html
- https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html

## Open items for content writers (not shown in the article)

**1. Author and images**
- Add a named author and a short bio (E-E-A-T requirement), then set `author` and `author_bio_url` in the frontmatter.
- Add the featured image at the path in `featured_image_path` (1200x630) with the alt text in `featured_image_alt`, and add screenshots from our own accounts.

**2. Facts and evidence to add before publishing**
- IMPORTANT: confirm whether Lynkk signs a HIPAA business associate agreement. The article does not claim HIPAA compliance and tells readers to get a BAA from any vendor, Lynkk included. Also a clinician reviewer for E-E-A-T.
- Examples in the article are labeled illustrative or fictional; replace with real, permissioned examples where available.

**3. Publishing checklist**
1. Click-test all links. lynkk.ai pages returned HTTP 200 in Ubersuggest's crawl; the external pages above were confirmed in search results restricted to their official domains on 2026-09-30.
2. Re-check vendor facts and prices on each vendor's own pages (search by name; no links kept).
3. Add the 2 inbound links in `inbound_links_planned`.
4. Set the final blog URL path and canonical.
