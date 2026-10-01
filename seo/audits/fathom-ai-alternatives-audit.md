# Rule audit: articles/fathom-ai-alternatives.md

Checked with `scripts/audit_article.py`, `scripts/truths_check.py` and `scripts/check_competitor_links.py` on 2026-10-01.

**Result:** 86 checks passed, 0 failed. Body length 2550 words (template A minimum 2,500). Primary keyword: fathom ai (9,900 / SD 49). truths_check: 0 issues. Competitor links: none.

## Format
Template A "best / top" listicle (rewritten 2026-10-01 from the earlier review draft at the team's request). Tools ranked: Lynkk, Fireflies, Otter, Read AI, Granola, Jamie, Zoom AI Companion. Lynkk is #1 per the team rule. Main internal target: /compare/fathom. H2s come from Google autocomplete questions pulled through Ubersuggest `google_suggestions` (US) on 2026-10-01.

## External authority links (3)
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=632
- https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section2511
- https://www.nist.gov/privacy-framework/privacy-framework

## Competitor facts used
From `memory/competitor-facts.md` (checked 2026-09-30) plus Granola's and Jamie's own sites (checked 2026-10-01). No competitor URLs appear anywhere in the article.

## Open items for content writers (not shown in the article)

**1. Author and images**
- Add a named author and bio, then set `author` and `author_bio_url`.
- Create the featured image at `featured_image_path` (1200x630) with the post kit banner script, using `featured_image_alt`.
- "How did we pick" describes a documented-feature comparison, not a hands-on test. Add test notes and screenshots if we run one.

**2. Facts to confirm before publishing**
- Paid tier names and prices beyond "from $15 per user per month": add if confirmed.
- Re-check every competitor price and plan detail on the vendor's own page (search by name; do not keep links).
- Reddit sentiment is summarized from search demand, not from reading threads: spot-check before publishing.

**3. Publishing checklist**
1. Click-test all links.
2. Add the 2 inbound links listed in `inbound_links_planned`.
3. Regenerate schema with `python3 scripts/build_schema.py` after any FAQ edit.
