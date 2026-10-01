# Batch 4: posts for slots #11-#15, audit summary (2026-10-01)

Slots #11-#15 of the 30-post plan were never written (they were "Lynkk vs X" posts on hold because
lynkk.ai already has /compare pages). After two rounds (competitor reviews, then "best alternatives"
listicles) the team asked for less generic topics, so these slots now hold 5 specific how-tos, each tied
to something Lynkk does that most note takers do not: recording FaceTime, WhatsApp, Webex and Slack
huddle calls from the Mac with no bot, and recording Google Meet from your own side with the Chrome
extension. None of these topics has a dedicated article among the other 25. None are published.

| # | Article | Primary keyword (vol / SD) | Words | Audit |
|---|---|---|---|---|
| 11 | [How to Record FaceTime Calls on iPhone and Mac, With Audio From Both Sides](../../articles/record-facetime-call.md) | record facetime call (480 / SD 30) | 1367 | 60 checks passed |
| 12 | [How to Record WhatsApp Calls on iPhone, Android and Mac, and Get Notes Afterward](../../articles/record-whatsapp-call.md) | record whatsapp call (1,300 / SD 35) | 1390 | 58 checks passed |
| 13 | [How to Record Google Meet Calls, Even When the Record Button Is Missing](../../articles/how-to-record-google-meet.md) | how to record google meet (2,400 / SD 25) | 1394 | 59 checks passed |
| 14 | [How to Record Webex Meetings and Get a Webex Transcript on Any Plan](../../articles/how-to-record-webex-meeting.md) | how to record webex meeting (590 / SD 23) | 1342 | 59 checks passed |
| 15 | [Slack Huddle Notes: How to Record, Transcribe and Summarize a Huddle on Your Mac](../../articles/slack-huddle-notes.md) | slack huddle (1,000 / SD 46) | 1333 | 60 checks passed |

Combined primary plus secondary search volume: about 12,000 US searches a month, all at SD 46 or lower.

All 5 pass `scripts/audit_article.py` (0 failed), `scripts/truths_check.py` (0 issues) and
`scripts/check_competitor_links.py`. Lynkk claims come only from `lynkk-post-kit/docs/TRUTHS.md`.
Platform steps come from Apple Support, Google Meet Help, the Webex Help Center and the Slack Help Center.

## Needs your decision
- The /compare pages still cover the "Lynkk vs" intent; the plan's #11-#15 comparison titles are retired.
- Each post needs our own step screenshots (platform UI plus the Lynkk call card) before publishing.
- Banners: not generated yet. Run `lynkk-post-kit/posts/blog-banners/build.py` for the 5 new slugs.
