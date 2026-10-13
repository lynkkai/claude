# Audit: how-to-record-a-teams-meeting

Date: 2026-10-13. Checked against `.claude/skills/seo-article/SKILL.md`, `memory/unveilr-skills/seo-score.md` and `humanize-verify.md`.
Primary keyword: how to record a teams meeting (US 2,400 / SD 29).
Topic source: Ubersuggest high-volume cluster (teams recording 1,300, how to download teams recording 1,300, download teams recording 880, record team meeting 880). Rewrites the superseded eager-tesla draft blog/how-to-record-a-teams-meeting.md, which made forbidden claims (knowledge graph, "30 seconds").

## Mechanical audit (scripts/audit_article.py)

```
== articles/how-to-record-a-teams-meeting.md (1726 words, primary 'how to record a teams meeting') ==
62 checks passed, 0 failed
```

TRUTHS.md check: 0 issues. Competitor links: 0. Em or en dashes: 0.

## SEO score (seo-score.md, Part 1)

| Dim | Score | Note |
|---|---|---|
| S1 Meta tags and snippet | 15/15 | Title, meta, slug, OG, canonical all in range |
| S2 Headings and keyword placement | 10/10 | Primary in H1 and an H2 |
| S3 Keyword usage | 15/15 | First 100 words, density 0.5-1.5%, every secondary present |
| S4 Internal linking | 10/10 | Feature page link plus 2 or more live blog cross-links |
| S5 External authority | 5/5 | 2 or more official gov or EU links |
| S6 Image SEO | 4/10 | Alt text 8-15 words with keyword; featured image and screenshots not created yet |
| S7 Schema | 10/10 | Article, FAQPage (synced), BreadcrumbList, inLanguage |
| S8 Depth and readability | 10/10 | Template band met, mean sentence under 22 words, lists for 3+ points |
| S9 Mobile markup | 5/5 | Tables 4 columns max, no sentence over 40 words |
| S10 E-E-A-T | 2/5 | Last updated and sources present; author and bio missing |
| S11 Link health | 5/5 | uscode.house.gov returns 200; EUR-Lex returns 202 (bot challenge), click-test once |
| **Total** | **91/100** | Gate is 85. Adding the author and images raises this by up to 9 points |

## Ranking gates (seo-score.md, Part 2)

- **G1 Intent and SERP format:** PASS. Top 10 are how-to answers (Reddit, a University of Michigan KB article, YouTube, Microsoft Q&A, 2 small note-taker blogs). This is a numbered how-to with troubleshooting.
- **G2 Cannibalization:** PASS WITH NOTE. The live post /blog/ai-note-taker-microsoft-teams targets "where do teams recording go" in its meta keywords. This draft does not list it or "teams recording location", uses the heading "Where are Teams recordings saved?", keeps that section short and links to the live post. Google may still swap which page ranks for that query; watch it in Search Console for 4 weeks after publishing. The chrome-extension feature page owns "record microsoft teams in browser" (different intent).
- **G3 Depth vs SERP median:** PASS. Ranking pages: median about 1,050 words. This draft: 1,726 (164%).
- **G4 Fan-out integrity:** PASS. 6 or more question or fan-out H2s, no dead headings, every H2 traced to a source below.

## Inherited AEO structure

PASS: H1 13-15 words, no "Official", evergreen slug, Quick answer callout and Last updated line, answer-first sections, every section's first 200 characters contain a number.

## Humanize-verify proxies

Burstiness (sentence-length variation): 0.51 (human floor 0.50). No AI-tell words, no em or en dashes.

## Query fan-out sources (H2 to source)

| H2 | Source |
|---|---|
| How to record a Teams meeting in 3 clicks | Ubersuggest: how to record a teams meeting (2,400), how to record microsoft team meeting (260), record team meeting (880) |
| Who can record a Teams meeting? | SERP: Microsoft Q&A and University of Michigan KB both cover permissions |
| Why is the Teams Record button greyed out? | SERP: Reddit thread and Microsoft Q&A threads on a missing Record button |
| Where are Teams recordings saved? | Ubersuggest: teams recording (1,300); kept short to avoid the live Teams post's "where do teams recording go" |
| How do you download a Teams recording? | Ubersuggest: how to download teams recording (1,300), how to download a teams recording (880), download teams recording (880) |
| How long do Teams recordings last? | Microsoft Learn: Teams recording expiration policy (120-day default) |
| Can you record a Teams meeting without being the organizer? | SERP: Microsoft Q&A question on recording as an attendee |
| How do you get notes and action items from a Teams recording? | GSC: Teams and meeting notes queries for lynkk.ai |
| Is it legal to record a Teams meeting? | Web SERP: consent pages rank for recording queries |

## Handoff note

Draft only, not published. Product claims follow lynkk-post-kit/docs/TRUTHS.md (no prices, "Start free", no CRM, no automatic Jira, no regions, no Windows or phones). Platform steps from Microsoft or Apple are cited in plain text, with no links.

## Open items before publishing

- Add author name and bio URL (S10).
- Create the featured image and 2 or 3 screenshots (S6).
- Add the planned inbound links from the pages in the frontmatter.
- Click-test every external link in a browser.
- Microsoft changes Teams menu names often. Check "More > Record and transcribe > Start recording", the Recap tab and the 120-day default against Microsoft Learn before publishing.
- Get publishing approval.
