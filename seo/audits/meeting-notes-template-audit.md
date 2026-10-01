# Rule audit: articles/meeting-notes-template.md

Checked with `scripts/audit_article.py`, `scripts/truths_check.py` and `scripts/check_competitor_links.py` on 2026-10-01.

**Result:** 71 checks passed, 0 failed. Body length 1944 words (template C minimum 1,200). Primary keyword: meeting notes template (22,200 / SD 49). truths_check: 0 issues. Competitor links: none.

## Why this topic
Chosen from `seo/feature-keyword-map-2026-10-01.md`: the topic maps to a Lynkk feature with search demand and no existing article. Main internal target: /features/meeting-notes. H2s come from Google autocomplete questions pulled through Ubersuggest `google_suggestions` (US) on 2026-10-01.

## External authority links (2)
- https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section2511
- https://www.irs.gov/instructions/i990

## Facts used
Meeting Brief (7 parts) and the 9 Summary Shapes from TRUTHS.md; IRS Form 990 documentation question for board meetings.

## Open items for content writers (not shown in the article)

**1. Author and images**
- Add a named author and bio, then set `author` and `author_bio_url`.
- Create the featured image at `featured_image_path` (1200x630) with the post kit banner script, using `featured_image_alt`.
- Add a screenshot of a real Lynkk Meeting Brief (anonymized).

**2. Facts and decisions before publishing**
- The sample uses illustrative numbers (40% drop-off at step 3); keep them clearly as a sample or replace with a real anonymized example.
- Confirm the 9 Summary Shape names still match the product.
- Consider a downloadable .docx / Google Docs copy of the template as a lead magnet.
- Overlaps lightly with #30 (meeting-minutes-sample, formal minutes) and #27 (one-on-one template): link to both at publish.

**3. Publishing checklist**
1. Click-test all links.
2. Add the 2 inbound links listed in `inbound_links_planned`.
3. Regenerate schema with `python3 scripts/build_schema.py` after any FAQ edit.
