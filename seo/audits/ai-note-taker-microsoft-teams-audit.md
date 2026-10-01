# Rule audit: articles/ai-note-taker-microsoft-teams.md

Checked with `scripts/audit_article.py` (rules from `seo-article`, `seo-score`, `aeo-score`, `humanize-verify` and the Lynkk rules in `CLAUDE.md`).

**Result:** 87 checks passed, 0 failed. Body length 2509 words. Primary keyword: teams ai (880 / SD 40).

## Mechanical rules checked (all pass)
H1 13-15 words; meta title ≤60 with primary near the start; meta description 150-160 with primary; evergreen slug; word count at or above the template minimum; primary in first 100 words and in an H2; density 0.5-1.5%; every secondary keyword present; ≥6 question H2s; no dead headings; every section's first 200 characters contain a number; sections ≤300 words without H3s; paragraphs ≤80 words and ≤4 sentences; 5-10 FAQs at 40-60 words; FAQ schema matches body word for word; tables ≤4 columns; 8-14 links; ≥3 lynkk.ai links incl. a feature or use-case page; ≥2 external links, all official government or standards sites; no links to unpublished posts; zero competitor links; no em or en dashes; no placeholders; no empty image links; no AI-tell words; brand spelled Lynkk; Article, FAQPage and BreadcrumbList schema.

## External authority links (3)
- https://csrc.nist.gov/pubs/fips/197/final
- https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section2511

## Open items before publishing (not shown in the article)
- 1. Add or confirm before publishing: author, bio, tenant test screenshots, featured image, Lynkk free-plan limits, team pricing, admin requirements, Teams Premium price, Reddit links, canonical URL.
- 2. Click-test all links. lynkk.ai pages returned HTTP 200 in Ubersuggest's crawl; csrc.nist.gov, eur-lex.europa.eu and uscode.house.gov were confirmed in search indexes on 2026-09-30.
- 3. Re-check Microsoft facts on Microsoft Support / Learn and competitor prices on each vendor's pricing page (search by name; no links kept).
- 4. Add the 2 inbound links in `inbound_links_planned`.

## Open items for content writers (moved out of the article)

**1. Author and images**
- Add a named author and a short bio (E-E-A-T requirement), then set `author` and `author_bio_url` in the frontmatter.
- Add the featured image at the path in `featured_image_path` (1200x630) with the alt text in `featured_image_alt`, and add screenshots from our own accounts.

**2. Facts to confirm before publishing (these were left out of the article until confirmed)**
- *How did we compare these Teams AI note takers?:* Add hands-on test notes and screenshots from a real Teams tenant before publishing.
- *What does Lynkk do that Microsoft's Teams AI does not?:* Free-plan limits and team pricing
- *3. Teams Premium intelligent recap: AI recap without full Copilot:* Current Teams Premium price
- *How much does Teams AI cost for a 10-person team?:* Team pricing and Workspaces
- *What do Reddit users say about Teams AI note takers?:* Add 2-3 thread links reviewed
- *Can I use an AI note taker in Teams without admin approval?:* Lynkk admin requirements

**3. Publishing checklist**
1. Add or confirm before publishing: author, bio, tenant test screenshots, featured image, Lynkk free-plan limits, team pricing, admin requirements, Teams Premium price, Reddit links, canonical URL.
2. Click-test all links. lynkk.ai pages returned HTTP 200 in Ubersuggest's crawl; csrc.nist.gov, eur-lex.europa.eu and uscode.house.gov were confirmed in search indexes on 2026-09-30.
3. Re-check Microsoft facts on Microsoft Support / Learn and competitor prices on each vendor's pricing page (search by name; no links kept).
4. Add the 2 inbound links in `inbound_links_planned`.
