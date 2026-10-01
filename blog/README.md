# Lynkk blog: catch-up batch (October 2026)

Five draft articles to cover the missed blog slots. All are `status: draft` and need a
human review before publishing (see checklist below).

## How the topics were chosen

lynkk.ai has no blog yet. The September 2026 site crawl (Ubersuggest project `lynkk.ai`) found
only product, feature, compare and use-case pages, and the site ranks in the top 100 for
**none** of its 34 tracked keywords (US, UK, India). Every post below targets a tracked keyword
cluster that Ubersuggest flags as a "new content" opportunity or that has the best
volume to difficulty ratio, does not duplicate an existing page, and links to a relevant product page.

| # | Article | Primary keyword | Market | Volume / mo | SEO difficulty | Main product link |
|---|---|---|---|---|---|---|
| 1 | [How to Record a Teams Meeting (and Find, Download and Transcribe It)](how-to-record-a-teams-meeting.md) | how to record a teams meeting | UK | 1,300 (cluster of 9 keywords: ~4,900) | 30 | /features/meeting-bot |
| 2 | [How to Transcribe a Zoom Meeting: 5 Ways, Free and Paid](how-to-transcribe-zoom-meetings.md) | transcribe zoom | US | 2,400 | 31 | /features/chrome-extension |
| 3 | [Action Items: What They Are, How to Write Them, and a Free Template](action-items-examples-and-template.md) | actions items / action items template | US | 2,900 + 480 | 38 / 32 | /features/action-items |
| 4 | [AI Note Taking: How It Works, Where It Helps, and How to Choose a Tool](ai-note-taking.md) | ai note taking | UK | 3,600 | 34 | /features/meeting-notes |
| 5 | [What Is a Conversation Intelligence Platform?](conversation-intelligence-platform.md) | conversation intelligence platform | US | 880 | 37 | /features/knowledge-graph |

Suggested publishing order: 1, 2, 3 (easiest wins, clear search intent), then 4 and 5 (broader, more competitive).

Next in line (not written yet): "teams transcription" (UK, 480, SD 21), "personal knowledge
management system" (US, 590, SD 36), "google meet note taker" (India, 260, SD 26).

## Product facts used

Product claims come from `memory/lynkk-brand.md` plus the September 2026 Ubersuggest crawl of
lynkk.ai (meeting bot, botless Chrome extension, Mac app, Slack, Jira, GDPR and encryption,
multilingual and code-switching support). No accuracy percentages, language counts or prices are
quoted in the articles.

Third-party facts (Microsoft Teams and Zoom behavior) were checked against public sources on
2026-10-01. Both products change their UI often.

## Before publishing

- [ ] Re-check the Teams and Zoom steps against the current apps (button labels, plan requirements, Zoom's May 2026 caption change)
- [ ] Confirm every Lynkk claim with the product team, especially: Mac app records Zoom desktop calls; in-person recording; action items carry due dates; data region choice is live
- [ ] Confirm internal link URLs still resolve
- [ ] Add a hero image and alt text per post
- [ ] Add FAQ schema (each post ends with a "Quick answers" section written for it)
- [ ] Add the published URLs to the Ubersuggest project so rankings get tracked
- [ ] Run the no-dash check: `LC_ALL=C.UTF-8 grep -nP '[\x{2013}\x{2014}]' blog/*.md` should print nothing
