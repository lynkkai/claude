# Audit: zoom-bot-join-meeting

Date: 2026-10-12. Checked against `.claude/skills/seo-article/SKILL.md`, `memory/unveilr-skills/seo-score.md` and `humanize-verify.md`.
Topic source: Search Console query group (content/gsc-query-topics-2026-10.md).

## Mechanical audit (scripts/audit_article.py)

```
== articles/zoom-bot-join-meeting.md (1786 words, primary 'zoom bot') ==
66 checks passed, 0 failed
```

TRUTHS.md check: 0 issues. Competitor links: 0. Em or en dashes: 0.

## SEO score (seo-score.md, Part 1)

| Dim | Score | Note |
|---|---|---|
| S1 Meta tags and snippet | 15/15 | Title, meta, slug, OG, canonical all in range |
| S2 Headings and keyword placement | 8/10 | Primary not in H1 (allowed by the 13-15 word rule) |
| S3 Keyword usage | 15/15 | First 100 words, density 0.5-1.5%, every secondary present |
| S4 Internal linking | 10/10 | Feature page link plus 2 or more live blog cross-links |
| S5 External authority | 5/5 | 2 or more official gov or EU links |
| S6 Image SEO | 4/10 | Alt text 8-15 words with keyword; featured image and screenshots not created yet |
| S7 Schema | 10/10 | Article, FAQPage (synced), BreadcrumbList, inLanguage |
| S8 Depth and readability | 10/10 | Template band met, mean sentence under 22 words, lists for 3+ points |
| S9 Mobile markup | 5/5 | Tables 4 columns max, no sentence over 40 words |
| S10 E-E-A-T | 2/5 | Last updated and sources present; author and bio missing |
| S11 Link health | 4/5 | All links 200 except California Penal Code 632 (403 bot block) and EUR-Lex (202 challenge); click-test both |
| **Total** | **88/100** | Gate is 85. Adding the author and images raises this by up to 9 points |

## Ranking gates (seo-score.md, Part 2)

- **G1 Intent and SERP format:** PARTIAL (risk). SERP for "zoom bot" is split: developer pages about building a bot (Recall.ai, Zoom devforum, GitHub, Zoom chatbot docs, 5 of 10) and university IT pages about AI bots joining uninvited (OU, UMich, Cornell, 3 of 10). This draft serves the how-to and IT intent (new section on stopping bots, and an explicit note that building a bot is out of scope) but not the developer intent. Expect it to rank for the Search Console how-to queries (join zoom call bot, how to send a meeting bot to a meeting) rather than the head term "zoom bot".
- **G2 Cannibalization:** PASS. Primary is not targeted by any of the 38 live lynkk.ai pages or the 13 unpublished drafts (content/blog-inventory-2026-10-12.md), and no lynkk.ai page ranks in the top 20 for it in the Search Console export.
- **G3 Depth vs SERP median:** PASS. Ranking pages: about 1,015 to 1,020 words. This draft: about 1,800.
- **G4 Fan-out integrity:** PASS. 6 or more question H2s, no dead headings, every H2 traced to a source below.

## Inherited AEO structure

PASS: H1 13-15 words, no "Official", evergreen slug, Quick answer callout and Last updated line, question headings, answer-first sections, every section's first 200 characters contain a number.

## Humanize-verify proxies

Burstiness (sentence-length variation) is 0.50 or higher, the human floor. No AI-tell words, no em or en dashes.

## Query fan-out sources (H2 to source)

| H2 | Source |
|---|---|
| What is a meeting bot? | Ubersuggest: what is meeting bot; GSC: meeting bot (62 impressions, pos 14) |
| How do you send a meeting bot to a meeting? | GSC: how to send a meeting bot to a meeting (pos 24) |
| How do you add a Zoom bot to a Zoom meeting? | GSC: join zoom call bot (35 impressions, pos 27); Ubersuggest: zoom bot to join meeting (10), zoom bot join (10) |
| How does a Google Meet bot join a call? | Ubersuggest: google meet bot (50), google meet bot joiner (40) |
| Can you add a meeting bot to Microsoft Teams? | GSC: zoom bot for teams (pos 17); Ubersuggest: meeting bot for teams |
| What does the meeting bot record? | Ubersuggest: zoom bot recording |
| Why can't my meeting bot join the call? | Ubersuggest: zoom bot sign in required, zoom bot skip waiting room |
| Can you record a meeting without a bot? | Ubersuggest: meeting bot vs local recording |
| How do you stop a bot from joining your Zoom meeting? | SERP: OU, UMich and Cornell IT pages on bots joining without an invite (positions 9, 10, 13) |
| Is it legal to use a meeting bot? | Web SERP: "is that bot in your meeting breaking the law" and consent pages |

## Handoff note

GSC queries answered: meeting bot, join zoom call bot, zoom connector bot, meetingbot, how to send a meeting bot to a meeting, zoom bot for teams, conference bot. Not answered on purpose: how to make / build a meeting bot (developer intent, Lynkk is not an API).
H1 does not contain the primary keyword "zoom bot". The skill allows this when the 13-15 word natural sentence wins; the keyword is in meta_title, slug and the first 100 words. Decision for the team: keep "zoom bot" as primary, or switch to "google meet bot" (50 / SD 13) if the developer-heavy SERP is a concern.

## Open items for content writers (before publishing)

- Add an author name and author bio URL in the frontmatter (currently empty; schema falls back to "Lynkk").
- Create the featured image at the `featured_image_path` in the frontmatter, plus step screenshots where the article describes UI.
- Add the 2 planned inbound links (see `inbound_links_planned`) on the live source pages at publish, and confirm they are live.
- Click-test every link at publish. The California Penal Code 632 page returns 403 to automated checks (bot blocking); it was verified in earlier drafts, so confirm it in a browser.
- The article is a draft and is not published. Publishing needs explicit approval.
- Primary keyword is "zoom bot" (210 / SD 27). /features/meeting-bot keeps "meeting bot", "zoom meeting bot" and "meeting notetaker bot"; do not add those to this post's keywords.
- Confirm the waiting room, Google Meet admit and Teams lobby descriptions against each platform's current help pages.
