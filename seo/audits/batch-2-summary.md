# Batch 2: 10 articles (#17-#26), audit summary (2026-09-30)

All 10 articles pass every mechanical rule in `scripts/audit_article.py` and the competitor-link check. None are published. Article files contain article content only; open items for writers are in each `seo/audits/<slug>-audit.md`.

| # | Article | Primary keyword (vol / SD) | Words | Audit |
|---|---|---|---|---|
| 17 | [How to Use Dictation on Mac, Fix It When It Stops Working, and Go Further](../../articles/dictation-on-mac.md) | dictation on mac (1,600 / SD 29) | 1445 | 64 checks passed |
| 18 | [How to Dictate in Microsoft Word and When You Need Microsoft Word Dictation Software](../../articles/dictate-in-microsoft-word.md) | microsoft word dictation software (1,300 / SD 30) | 1411 | 63 checks passed |
| 19 | [How Voice Memo Transcription Works on iPhone and How to Turn Memos Into Notes](../../articles/voice-memo-transcription.md) | voice memo transcription (1,600 / SD 36) | 1299 | 61 checks passed |
| 20 | [How to Get a Google Meet Transcript and What Gemini AI Notes Can Do](../../articles/google-meet-transcript.md) | google meet transcript (1,000 / SD 53) | 1403 | 63 checks passed |
| 21 | [How Sales Teams Use Conversation Intelligence to Prepare, Follow Up and Close More Deals](../../articles/sales-conversation-intelligence.md) | conversation intelligence (1,900 / SD 60) | 1512 | 62 checks passed |
| 22 | [How Recruiters and Hiring Teams Use Interview Transcription to Run Better Debriefs and Hire Faster](../../articles/recruiting-interview-transcription.md) | interview transcription (1,300 / SD 25) | 1517 | 62 checks passed |
| 23 | [How Product Teams Turn Meeting Minutes Into Jira Tickets Automatically With AI Meeting Minutes](../../articles/meeting-minutes-to-jira.md) | meeting minutes (9,900 / SD 36) | 1506 | 65 checks passed |
| 24 | [How Founders Keep Up With Back-to-Back Meetings Using AI Meeting Notes and One AI Teammate](../../articles/founders-meeting-notes.md) | meeting notes (3,600 / SD 29) | 1515 | 63 checks passed |
| 25 | [Your Meetings Are Your Knowledge Base: How Knowledge Management Tools Build Searchable Team Memory](../../articles/meeting-knowledge-management.md) | knowledge management tools (4,400 / SD 46) | 1513 | 62 checks passed |
| 26 | [How Engineering Teams Run a Faster Daily Standup Meeting in Scrum With AI Notes](../../articles/daily-standup-meeting.md) | standup meeting (2,400 / SD 19) | 1503 | 62 checks passed |

## How they were built
- **Headings:** from Ubersuggest Google autocomplete questions for each primary keyword (pulled 2026-09-30) plus the brief's questions in `seo/content-briefs.md`.
- **Facts:** Apple Support, Microsoft Support and Google Meet Help (cited in plain text, never linked), the 2020 Scrum Guide, and `memory/lynkk-brand.md` / `memory/competitor-facts.md`.
- **Authority links (all confirmed in search restricted to the official domain):** uscode.house.gov (18 U.S.C. 2511), leginfo.legislature.ca.gov (Penal Code 632), ecfr.gov (29 CFR 1602.14), w3.org (WCAG Label in Name), iso.org (ISO 30401), nist.gov (Privacy Framework), csrc.nist.gov (FIPS 197).
- **Lynkk plan facts used:** start free with 5 hours of recording in total; Pro $15 a month; the meeting bot is described as a Pro feature. Nothing claims audio upload, Windows or iOS apps, or which CRMs are supported.
- **Examples** (transcripts, minutes, standup notes, a founder's week) are labeled illustrative. No quotes or results were invented.

## Changes for your review
- **#26:** primary switched from "standup meeting scrum" to "standup meeting" (same 2,400 volume); the exact phrase is kept as a secondary.
- **Keyword expansion:** Ubersuggest's daily limit (150 reports) was reached before new lookups, so `keywords_added` uses brief keywords already measured on 2026-09-30. A paid Ubersuggest plan raises the limit.
- **Cannibalization watch:** #21, #22 and #26 support the existing lynkk.ai pages /use-cases/sales-calls, /use-cases/user-interviews and /use-cases/team-standups and link to them; they target blog intent, not the service pages' head terms.

## Common open items
Author name and bio; featured images and screenshots; permissioned quotes and real examples (#21, #22, #24, #26); which CRMs Lynkk updates; whether the knowledge graph is Pro-only; whether Lynkk dictation and the Chrome extension are on the free plan; final blog URL paths.
