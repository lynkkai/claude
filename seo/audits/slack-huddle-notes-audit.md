# Rule audit: articles/slack-huddle-notes.md

Checked with `scripts/audit_article.py`, `scripts/truths_check.py` and `scripts/check_competitor_links.py` on 2026-10-01.

**Result:** 60 checks passed, 0 failed. Body length 1333 words (template C minimum 1,200). Keywords: slack huddle (1,000 / SD 46). truths_check: 0 issues. Competitor links: none.

## Format
Template C how-to, chosen 2026-10-01 to replace the generic competitor posts in slots #11-#15. Topic is tied to a specific Lynkk capability from TRUTHS.md. Main internal target: /slack. Keywords pulled from Ubersuggest (US, locId 2840) on 2026-10-01.

## External authority links (3)
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=632
- https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title18-section2511
- https://www.nist.gov/privacy-framework/privacy-framework

## Platform facts used
Slack Help Center (via search, slack.com blocked here): huddle limits (2 on free, 50 on paid, 25 video), AI huddle notes on paid plans, not with external people or guests, steps to turn on, canvas with attendees, topics, action items and transcript, everyone notified. Platform vendors are named in plain text only; no vendor URLs appear in the article.

## Open items for content writers (not shown in the article)

**1. Author and images**
- Add a named author and bio, then set `author` and `author_bio_url`.
- Create the featured image at `featured_image_path` (1200x630) with the post kit banner script, using `featured_image_alt`.
- Add our own screenshots of each step (platform UI and the Lynkk card).

**2. Facts to confirm before publishing**
- Confirm the Lynkk card text for Slack huddles (the article says "Slack call detected").
- Re-check Slack's AI notes plan availability; Slack changed plan features in 2025-2026.

**3. Publishing checklist**
1. Click-test all links.
2. Add the 2 inbound links listed in `inbound_links_planned`.
3. Regenerate schema with `python3 scripts/build_schema.py` after any FAQ edit.
