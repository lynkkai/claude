# Rule audit: articles/voice-to-text-apps.md

Checked with `scripts/audit_article.py` (rules from `seo-article`, `seo-score`, `aeo-score`, `humanize-verify` and the Lynkk rules in `CLAUDE.md`).

**Result:** 87 checks passed, 0 failed. Body length 2508 words. Primary keyword: voice to text app (4,400 / SD 47).

## Mechanical rules checked (all pass)
H1 13-15 words; meta title ≤60 with primary near the start; meta description 150-160 with primary; evergreen slug; word count at or above the template minimum; primary in first 100 words and in an H2; density 0.5-1.5%; every secondary keyword present; ≥6 question H2s; no dead headings; every section's first 200 characters contain a number; sections ≤300 words without H3s; paragraphs ≤80 words and ≤4 sentences; 5-10 FAQs at 40-60 words; FAQ schema matches body word for word; tables ≤4 columns; 8-14 links; ≥3 lynkk.ai links incl. a feature or use-case page; ≥2 external links, all official government or standards sites; no links to unpublished posts; zero competitor links; no em or en dashes; no placeholders; no empty image links; no AI-tell words; brand spelled Lynkk; Article, FAQPage and BreadcrumbList schema.

## External authority links (3)
- https://www.ada.gov/resources/effective-communication/
- https://www.section508.gov/create/captions-transcripts/
- https://www.nist.gov/privacy-framework/privacy-framework

## Open items before publishing (not shown in the article)
- 1. Add or confirm before publishing: author, bio, dictation test results, featured image, Lynkk free-plan dictation limits, Windows and iPhone availability, Dragon price, canonical URL.
- 2. Click-test all links. lynkk.ai pages returned HTTP 200 in Ubersuggest's crawl; ada.gov, section508.gov and nist.gov were confirmed in search indexes on 2026-09-30.
- 3. Re-check Apple, Microsoft, Google and vendor details (search by name; no links kept).
- 4. Add the 2 inbound links in `inbound_links_planned`.
- 5. When post #18 (dictate in Word) is live, link it from the Word Dictate section.

## Open items for content writers (moved out of the article)

**1. Author and images**
- Add a named author and a short bio (E-E-A-T requirement), then set `author` and `author_bio_url` in the frontmatter.
- Add the featured image at the path in `featured_image_path` (1200x630) with the alt text in `featured_image_alt`, and add screenshots from our own accounts.

**2. Facts to confirm before publishing (these were left out of the article until confirmed)**
- *Our quick picks:* Price
- *How did we compare these voice to text apps?:* Add test notes: dictate the same 500-word passage in each tool and record errors and time.
- *What else does Lynkk do beyond dictation?:* Free-plan dictation limits; Windows availability
- *6. Dragon Professional: best dictation software for heavy Windows users:* Current price
- *How much does dictation software cost?:* Price
- *What is the best free voice to text app?:* Lynkk free plan dictation limit for the free-options table
- *Which dictation software is best for Windows?:* Lynkk Windows availability
- *What is the best speech to text app for iPhone?:* Lynkk iPhone app availability

**3. Publishing checklist**
**Keyword note:** "good voice to text app" and "voice dictation software for mac" are secondaries of posts #18 and #17, so they are not targeted here.
1. Add or confirm before publishing: author, bio, dictation test results, featured image, Lynkk free-plan dictation limits, Windows and iPhone availability, Dragon price, canonical URL.
2. Click-test all links. lynkk.ai pages returned HTTP 200 in Ubersuggest's crawl; ada.gov, section508.gov and nist.gov were confirmed in search indexes on 2026-09-30.
3. Re-check Apple, Microsoft, Google and vendor details (search by name; no links kept).
4. Add the 2 inbound links in `inbound_links_planned`.
5. When post #18 (dictate in Word) is live, link it from the Word Dictate section.
