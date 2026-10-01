# Rule audit: articles/follow-up-email-after-meeting.md

Checked with `scripts/audit_article.py`, `scripts/truths_check.py` and `scripts/check_competitor_links.py` on 2026-10-01.

**Result:** 68 checks passed, 0 failed. Body length 1941 words (template C minimum 1,200). Primary keyword: follow up email after meeting (210 / SD 26). truths_check: 0 issues. Competitor links: none.

## Why this topic
Chosen from `seo/feature-keyword-map-2026-10-01.md`: the topic maps to a Lynkk feature with search demand and no existing article. Main internal target: /features/meeting-notes. H2s come from Google autocomplete questions pulled through Ubersuggest `google_suggestions` (US) on 2026-10-01.

## External authority links (2)
- https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section2511
- https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business

## Facts used
TRUTHS.md: summary emailed after every meeting (attendees if opted in), revocable share link, action items with owner/due date/priority. FTC CAN-SPAM compliance guide for the commercial email section.

## Open items for content writers (not shown in the article)

**1. Author and images**
- Add a named author and bio, then set `author` and `author_bio_url`.
- Create the featured image at `featured_image_path` (1200x630) with the post kit banner script, using `featured_image_alt`.
- Add a screenshot of a real Lynkk Meeting Brief (anonymized).

**2. Facts and decisions before publishing**
- The article states Lynkk writes the recap, not the email. Do not add claims that Lynkk drafts or sends follow-up emails unless the product team confirms it.
- Example company name "Acme" is generic; keep or replace.

**3. Publishing checklist**
1. Click-test all links.
2. Add the 2 inbound links listed in `inbound_links_planned`.
3. Regenerate schema with `python3 scripts/build_schema.py` after any FAQ edit.
