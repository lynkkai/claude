# Rule audit: articles/fathom-ai-review.md

Checked with `scripts/audit_article.py`, `scripts/truths_check.py` and `scripts/check_competitor_links.py` on 2026-10-01.

**Result:** 70 checks passed, 0 failed. Body length 1876 words (template B minimum 1,800). Primary keyword: fathom ai (9,900 / SD 49). truths_check: 0 issues. Competitor links: none.

## Why this angle
Posts #11-#15 were on hold because lynkk.ai already has /compare pages. To avoid competing with them, this post targets the competitor's own review, pricing and "alternatives" searches (keyword-map-v2 primaries) instead of "Lynkk vs X", and links to /compare/fathom as its main internal target. H2s come from Google autocomplete questions pulled through Ubersuggest `google_suggestions` (US) on 2026-10-01.

## External authority links (3)
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=632
- https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section2511
- https://www.nist.gov/privacy-framework/privacy-framework

## Competitor facts used
Fathom pricing page per memory/competitor-facts.md (checked 2026-09-30). CRM sync, call scoring and clips are from Fathom's sales pages as reported in reviews. No competitor URLs appear anywhere in the article.

## Open items for content writers (not shown in the article)

**1. Author and images**
- Add a named author and bio, then set `author` and `author_bio_url`.
- Create the featured image at `featured_image_path` (1200x630) with the post kit banner script, using `featured_image_alt`.
- "How did we compare" describes a documented-feature comparison, not a hands-on test. Add side-by-side test notes and screenshots of the same meeting in both tools if we run one.

**2. Facts to confirm before publishing**
- Paid tier names and prices beyond "from $15 per user per month": add if confirmed.
- Whether Fathom records Zoom through a bot or a desktop app: re-check current behavior; the article says its notetaker joins the call.
- Re-check every competitor price and plan detail on the vendor's own page (search by name; do not keep links).

**3. Publishing checklist**
1. Click-test all links (lynkk.ai pages returned HTTP 200 in the 2026-09-30 crawl; the gov links are the same ones verified for earlier articles).
2. Add the 2 inbound links listed in `inbound_links_planned`.
3. Regenerate schema with `python3 scripts/build_schema.py` after any FAQ edit.
