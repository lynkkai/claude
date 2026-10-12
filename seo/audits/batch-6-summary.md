# Batch 6: Search Console query topics 1 to 4 (2026-10-12)

Topics come from real lynkk.ai Search Console queries (content/gsc-query-topics-2026-10.md), sized with Ubersuggest (US).
All 4 drafts pass scripts/audit_article.py (0 failed), scripts/truths_check.py (0 issues) and scripts/check_competitor_links.py.

| # | Article | Primary keyword (vol / SD) | Template | Words |
|---|---|---|---|---|
| 1 | [Action Items: What They Are, Examples, a Free Template, and How to Track Them](../../articles/action-items-examples-template.md) | action items (2,900 / 40) | D | 1,900 |
| 2 | [The Best Zoom Note Taker in 2026: 7 AI Tools Compared for Zoom Meetings](../../articles/zoom-note-taker.md) | zoom note taker (880 / 31) | A | 2,583 |
| 3 | [How to Add a Meeting Bot to Zoom, Google Meet or Teams, Step by Step](../../articles/zoom-bot-join-meeting.md) | zoom bot (210 / 27) | C | 1,631 |
| 4 | [Meeting Preparation: How to Walk Into Every Meeting With Context From the Last One](../../articles/meeting-preparation.md) | meeting preparation (390 / 24) | D | 1,740 |

Change to tooling: scripts/audit_article.py now allows links to the 19 blog posts live on lynkk.ai (sitemap checked 2026-10-12); links to unpublished posts still fail.

Open items common to all 4: author, featured images and screenshots, inbound links on live pages, link click-test, publishing approval. See each audit file.

## Skill review (2026-10-12, second pass)

Checked against the full seo-article skill, seo-score.md and humanize-verify.md, not only the mechanical audit.

| Article | SEO score | G1 intent | G2 cannibal | G3 depth | G4 fan-out | Burstiness |
|---|---|---|---|---|---|---|
| action-items-examples-template | 90 | Pass | Pass | Pass (108% of SERP median) | Pass | 0.52 |
| zoom-note-taker | 90 | Pass with risk (Zoom's own pages lead) | Pass | Pass (89%) | Pass | 0.53 |
| zoom-bot-join-meeting | 88 | Partial (SERP is developer-heavy) | Pass | Pass | Pass | 0.50 |
| meeting-preparation | 90 | Pass | Pass | Pass (135%) | Pass | 0.53 |

Fixes made in this pass: second live blog cross-link on 2 posts, keyword added to 2 image alt texts, 4 headings renamed to sourced queries, a "stop bots joining your Zoom meeting" section and a developer-scope note on the zoom bot post, shorter sentences for rhythm. Every H2 is now mapped to its source in each audit file.

Points still missing (all 4): author and bio (S10), featured image and screenshots (S6). These are writer tasks, listed in each audit.
