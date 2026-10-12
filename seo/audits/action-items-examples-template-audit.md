# Audit: action-items-examples-template

Date: 2026-10-12. Checked against `.claude/skills/seo-article/SKILL.md`, `memory/unveilr-skills/seo-score.md` and `humanize-verify.md`.
Topic source: Search Console query group (content/gsc-query-topics-2026-10.md).

## Mechanical audit (scripts/audit_article.py)

```
== articles/action-items-examples-template.md (1902 words, primary 'action items') ==
74 checks passed, 0 failed
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
| S11 Link health | 4/5 | All links 200 except California Penal Code 632 (403 bot block) and EUR-Lex (202 challenge); click-test both |
| **Total** | **90/100** | Gate is 85. Adding the author and images raises this by up to 9 points |

## Ranking gates (seo-score.md, Part 2)

- **G1 Intent and SERP format:** PASS. Top 10 for "action items" (US, 2026-10-12) are definition and how-to guides (profit.co, meetingnotes.com, timetrackapp, plaky); this is a guide plus template.
- **G2 Cannibalization:** PASS. Primary is not targeted by any of the 38 live lynkk.ai pages or the 13 unpublished drafts (content/blog-inventory-2026-10-12.md), and no lynkk.ai page ranks in the top 20 for it in the Search Console export.
- **G3 Depth vs SERP median:** PASS. Ranking pages: 1,546 to 2,477 words, median about 1,770. This draft: about 1,920 (108%).
- **G4 Fan-out integrity:** PASS. 6 or more question H2s, no dead headings, every H2 traced to a source below.

## Inherited AEO structure

PASS: H1 13-15 words, no "Official", evergreen slug, Quick answer callout and Last updated line, question headings, answer-first sections, every section's first 200 characters contain a number.

## Humanize-verify proxies

Burstiness (sentence-length variation) is 0.50 or higher, the human floor. No AI-tell words, no em or en dashes.

## Query fan-out sources (H2 to source)

| H2 | Source |
|---|---|
| What are action items in a meeting? | Ubersuggest: what are action items in a meeting (70), action items meaning (880) |
| How do you write a good action item? | Ubersuggest: how to write action items (30); SERP: timetrackapp "smart action items" |
| What is an example of action items? | Ubersuggest: example of action items (110) |
| How do you write meeting notes with action items? | Ubersuggest: meeting notes with action items (210) |
| What does a meeting minutes format with action items look like? | Ubersuggest: meeting minutes format with action items (260) |
| Free action items template you can copy | Ubersuggest: action items template (480), template action items (590) |
| How do you go about tracking action items after a meeting? | Ubersuggest: tracking action items (320), how to track action items from a meeting |
| Why do action items often get missed? | Ubersuggest: why do action items often get missed |
| How does AI find action items in a meeting? | GSC: action item detection (pos 57), ai solutions for action item detection in meetings (pos 89); Ubersuggest: how to identify action items in a meeting |
| Is it legal to record a meeting? | Web SERP: "is it legal to record a meeting" and "Can you record a meeting without consent?" both have dedicated ranking pages |

## Handoff note

GSC conversational queries answered: "which ai board tools compare decisions and action items across meetings?" (pos 9) and the action-item detection queries.


## Open items for content writers (before publishing)

- Add an author name and author bio URL in the frontmatter (currently empty; schema falls back to "Lynkk").
- Create the featured image at the `featured_image_path` in the frontmatter, plus step screenshots where the article describes UI.
- Add the 2 planned inbound links (see `inbound_links_planned`) on the live source pages at publish, and confirm they are live.
- Click-test every link at publish. The California Penal Code 632 page returns 403 to automated checks (bot blocking); it was verified in earlier drafts, so confirm it in a browser.
- The article is a draft and is not published. Publishing needs explicit approval.
- Replaces the superseded draft `blog/action-items-examples-and-template.md` on branch claude/eager-tesla-cvuh6f (that draft used claims TRUTHS.md forbids). Do not publish the old one.
- Cannibalization guard: /features/action-items owns "meeting action items" and "action item tracker ai"; this post targets "action items" and its template and example terms.
