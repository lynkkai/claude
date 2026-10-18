# Lynkk blog wave 1 (35 articles)

Drafts for lynkk.ai/blog, written 17-18 October 2026 from the topic plan, Ubersuggest data and the
`seo-article` skill pack. Every article is a draft for editorial review: nothing here has been published.

## What is in this folder

| Path | What it is |
|---|---|
| `articles/<slug>.md` | One article per topic, with frontmatter (meta title, meta description, slug, keywords, inbound-link plan, author) and an HTML-comment handoff note at the end |
| `schema/<slug>.json` | JSON-LD (Article + BreadcrumbList + FAQPage), generated from each article's own FAQ |
| `research/briefs.md` | Ubersuggest volumes, SERPs and autocomplete fan-out per topic, plus checked competitor prices |
| `tools/check_articles.py` | Pre-score checker: meta lengths, keyword placement, question H2s, FAQ, links, no em/en dashes, brand spelling |
| `tools/build_schema.py` | Rebuilds `schema/` after any FAQ edit |

Run both before publishing:

```
python3 blog/tools/check_articles.py
python3 blog/tools/build_schema.py
```

## Article index

PASS = no warnings. WARN = soft guidance only (density, long sentences, clip numbers). No article has a FAIL.

| # | Title | Slug | Primary keyword | Market | Words | Check |
|---|---|---|---|---|---|---|
| 1 | [Best Otter.ai Alternatives in the US for 2026](articles/otter-ai-alternatives.md) | `otter-ai-alternatives` | otter ai alternatives | US | 2096 | PASS |
| 2 | [Granola vs Fathom in 2026: Which Fits US Teams Better?](articles/granola-vs-fathom.md) | `granola-vs-fathom` | granola vs fathom | US | 1679 | PASS |
| 3 | [Read AI Alternatives US Teams Are Switching To in 2026](articles/read-ai-alternative.md) | `read-ai-alternative` | read ai alternative | US | 1588 | WARN |
| 4 | [Granola AI Alternatives That Work for US Teams in 2026](articles/granola-ai-alternatives.md) | `granola-ai-alternatives` | granola ai alternatives | US | 1581 | PASS |
| 5 | [Granola AI Pricing in 2026: What US Users Actually Pay](articles/granola-pricing.md) | `granola-pricing` | granola pricing | US | 1654 | WARN |
| 6 | [Granola vs Otter AI in 2026: Which Suits US Teams?](articles/granola-vs-otter-ai.md) | `granola-vs-otter-ai` | granola vs otter ai | US | 1551 | PASS |
| 7 | [Otter vs Fireflies vs Fathom: A 2026 Guide for US Teams](articles/otter-ai-vs-fireflies-ai.md) | `otter-ai-vs-fireflies-ai` | otter ai vs fireflies ai | US | 1512 | PASS |
| 8 | [Read AI Pricing in 2026: Plans and Costs for US Teams](articles/read-ai-pricing.md) | `read-ai-pricing` | read ai pricing | US | 1524 | WARN |
| 9 | [Read AI vs Otter AI in 2026: Which Should US Teams Pick?](articles/read-ai-vs-otter-ai.md) | `read-ai-vs-otter-ai` | read ai vs otter ai | US | 1596 | PASS |
| 10 | [Notion AI Note Taker Review for US Teams in 2026](articles/notion-note-taker.md) | `notion-note-taker` | notion note taker | US | 1717 | WARN |
| 11 | [Jamie AI Note Taker Review: A 2026 Look for US Teams](articles/jamie-ai-note-taker.md) | `jamie-ai-note-taker` | jamie ai note taker | US | 1551 | PASS |
| 12 | [Tactiq Alternatives for US Teams in 2026](articles/tactiq-alternative.md) | `tactiq-alternative` | tactiq alternative | US | 1586 | WARN |
| 13 | [Best App for Meeting Minutes: 8 Tools US Teams Use in 2026](articles/app-for-meeting-minutes.md) | `app-for-meeting-minutes` | app for meeting minutes | US | 1546 | PASS |
| 14 | [Notta Pricing in 2026: What Each Plan Costs in the US](articles/notta-pricing.md) | `notta-pricing` | notta pricing | US | 1389 | WARN |
| 15 | [Best AI Meeting Summarizer Tools in the US for 2026](articles/team-meeting-summary-ai.md) | `team-meeting-summary-ai` | team meeting summary ai | US | 1480 | PASS |
| 16 | [Google Meet AI Note Takers Worth Using in India in 2026](articles/google-meet-ai-note-taker.md) | `google-meet-ai-note-taker` | google meet ai note taker | India | 1495 | WARN |
| 17 | [Hindi Transcription in India: Free Audio to Text in 2026](articles/hindi-transcription.md) | `hindi-transcription` | hindi transcription | India | 1541 | WARN |
| 18 | [Hindi Speech to Text in India: Free Voice Typing for 2026](articles/hindi-speech-to-text.md) | `hindi-speech-to-text` | hindi speech to text | India | 1383 | WARN |
| 19 | [Avoma Alternatives for US Sales Teams in 2026](articles/avoma-alternatives.md) | `avoma-alternatives` | avoma alternatives | US | 1523 | PASS |
| 20 | [How to Remove Fireflies.ai From Teams, Zoom and Meet in 2026](articles/remove-fireflies-ai-from-teams.md) | `remove-fireflies-ai-from-teams` | how to remove fireflies ai from teams | US | 1393 | WARN |
| 21 | [How to Record a Google Meet Call for Free in 2026](articles/record-google-meet-call.md) | `record-google-meet-call` | how to record google meet call | US | 1469 | PASS |
| 22 | [Minutes of Meeting Format in India: Free Templates for 2026](articles/minutes-of-meeting-format.md) | `minutes-of-meeting-format` | minutes of meeting format | India | 1760 | WARN |
| 23 | [Meeting Notes vs Minutes: How to Write Minutes in 2026](articles/meeting-notes-vs-minutes.md) | `meeting-notes-vs-minutes` | meeting notes minutes | US | 1445 | PASS |
| 24 | [Board Minutes of Meeting in India: 2026 Format and Sample](articles/board-minutes-of-meeting.md) | `board-minutes-of-meeting` | board minutes of meeting | India | 1564 | WARN |
| 25 | [Meeting Agenda Template in Word: Free 2026 Download](articles/meeting-agenda-template-word.md) | `meeting-agenda-template-word` | meeting agenda template in word | US | 1417 | WARN |
| 26 | [Board Meeting Agenda Template for US Boards in 2026](articles/board-meeting-agenda.md) | `board-meeting-agenda` | board meeting agenda | US | 1407 | WARN |
| 27 | [Free Meeting Notes Template for 2026 (Word, Docs, Notion)](articles/meeting-notes-template.md) | `meeting-notes-template` | free meeting notes template | US | 1264 | WARN |
| 28 | [How to Take Good Meeting Notes in 2026 (+ Free Template)](articles/how-to-take-good-meeting-notes.md) | `how-to-take-good-meeting-notes` | how to take good meeting notes | US | 1391 | WARN |
| 29 | [Meeting Summary Template for 2026, With Real Examples](articles/meeting-summary-template.md) | `meeting-summary-template` | template for meeting summary | US | 1372 | PASS |
| 30 | [Follow-Up Email After a Meeting: 12 Examples for 2026](articles/follow-up-email-after-meeting.md) | `follow-up-email-after-meeting` | example of follow up email after meeting | US | 1676 | WARN |
| 31 | [Sprint Retrospective Template for 2026: 40 Questions](articles/sprint-retrospective-template-samples.md) | `sprint-retrospective-template-samples` | sprint retrospective samples | US | 1512 | WARN |
| 32 | [What Is a Discovery Call? A 2026 Guide for US Sales Teams](articles/what-is-a-discovery-call.md) | `what-is-a-discovery-call` | what is a discovery call | US | 1437 | WARN |
| 33 | [Project Kickoff Meeting Agenda Template for 2026 (Free)](articles/project-kickoff-meeting-agenda-template.md) | `project-kickoff-meeting-agenda-template` | project kickoff meeting agenda template | US | 1319 | PASS |
| 34 | [HOA Meeting Minutes Template for US Boards in 2026](articles/hoa-meeting-minutes-template.md) | `hoa-meeting-minutes-template` | homeowners association meeting minutes template | US | 1353 | WARN |
| 35 | [LLC Meeting Minutes Template for US Owners in 2026](articles/llc-meeting-minutes-template.md) | `llc-meeting-minutes-template` | llc meeting minutes template | US | 1355 | WARN |

## Editorial notes before publishing

1. **Facts were checked on 17-18 October 2026.** Competitor prices come from vendor pricing pages (Fireflies from its
   help center; Notta monthly prices from a third-party review). Re-check prices the week each post goes live.
2. **Lynkk claims** use only what lynkk.ai showed on 17 October 2026 (see `memory/lynkk-brand.md`). No CRM sync,
   no SOC 2, no "speaks in the meeting", no Windows or mobile apps are claimed.
3. **Byline** follows the live blog: Samarth Wagh, Co-founder, Lynkk.ai. Change it if a different author should own a post.
4. **Legal-adjacent posts** (#24 board minutes India, #34 HOA minutes, #35 LLC minutes) state rules generally and
   should get a quick review by a company secretary or attorney.
5. **Inbound links:** each article's frontmatter names 1-2 live lynkk.ai posts and the anchor text to add there,
   per the skill's inbound-link gate. Add them when the article goes live.
6. **Each handoff note** (the HTML comment at the end of every article) lists the prompts the article answers,
   prompt gaps to register, the fan-out sources and any item the editor should verify.
7. **Pipeline steps not run here:** `/aeo-score`, `/seo-score` (with live GSC), the humanizer and
   `/post-humanize-check` are not installed in this environment. The checker covers the mechanical parts of
   `/seo-score`; run the full pipeline before publishing.
8. **Templates posts** (#22, #25, #27) rank against downloadable files; attaching a real .docx or .pdf would match intent.
