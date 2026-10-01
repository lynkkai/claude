# Rule audit: articles/record-facetime-call.md

Checked with `scripts/audit_article.py`, `scripts/truths_check.py` and `scripts/check_competitor_links.py` on 2026-10-01.

**Result:** 60 checks passed, 0 failed. Body length 1367 words (template C minimum 1,200). Keywords: record facetime call (480 / SD 30); how to record facetime call (1,900 / 32) as secondary. truths_check: 0 issues. Competitor links: none.

## Format
Template C how-to, chosen 2026-10-01 to replace the generic competitor posts in slots #11-#15. Topic is tied to a specific Lynkk capability from TRUTHS.md. Main internal target: /download. Keywords pulled from Ubersuggest (US, locId 2840) on 2026-10-01.

## External authority links (3)
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=632
- https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section2511
- https://www.nist.gov/privacy-framework/privacy-framework

## Platform facts used
Apple Support: FaceTime audio Call Recording on iPhone and Mac (1-to-1 audio calls, supported regions, both parties hear a notice, saved to Notes > Call Recordings, transcript, Apple Intelligence summary on Mac). Platform vendors are named in plain text only; no vendor URLs appear in the article.

## Open items for content writers (not shown in the article)

**1. Author and images**
- Add a named author and bio, then set `author` and `author_bio_url`.
- Create the featured image at `featured_image_path` (1200x630) with the post kit banner script, using `featured_image_alt`.
- Add our own screenshots of each step (platform UI and the Lynkk card).

**2. Facts to confirm before publishing**
- Confirm the Lynkk Mac app card text for FaceTime reads "FaceTime call detected".
- Third-party claim that iPhone screen recording often misses the other voice: re-test on current iOS before publishing.

**3. Publishing checklist**
1. Click-test all links.
2. Add the 2 inbound links listed in `inbound_links_planned`.
3. Regenerate schema with `python3 scripts/build_schema.py` after any FAQ edit.
