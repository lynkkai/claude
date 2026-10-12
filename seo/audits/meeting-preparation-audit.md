# Audit: meeting-preparation

Date: 2026-10-12. Checked against `.claude/skills/seo-article/SKILL.md`, `memory/unveilr-skills/seo-score.md` and `humanize-verify.md`.
Topic source: Search Console query group (content/gsc-query-topics-2026-10.md).

## Mechanical audit (scripts/audit_article.py)

```
== articles/meeting-preparation.md (1754 words, primary 'meeting preparation') ==
66 checks passed, 0 failed
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

- **G1 Intent and SERP format:** PASS. Top 10 for "meeting preparation" are guides and checklists (BCcampus textbook chapter, formeret, weekdone, ksl-training checklist, flowtrace); this is a guide with a checklist and template.
- **G2 Cannibalization:** PASS. Primary is not targeted by any of the 38 live lynkk.ai pages or the 13 unpublished drafts (content/blog-inventory-2026-10-12.md), and no lynkk.ai page ranks in the top 20 for it in the Search Console export.
- **G3 Depth vs SERP median:** PASS. Ranking pages: 480 to 2,308 words, median about 1,320. This draft: about 1,780 (135%).
- **G4 Fan-out integrity:** PASS. 6 or more question H2s, no dead headings, every H2 traced to a source below.

## Inherited AEO structure

PASS: H1 13-15 words, no "Official", evergreen slug, Quick answer callout and Last updated line, question headings, answer-first sections, every section's first 200 characters contain a number.

## Humanize-verify proxies

Burstiness (sentence-length variation) is 0.50 or higher, the human floor. No AI-tell words, no em or en dashes.

## Query fan-out sources (H2 to source)

| H2 | Source |
|---|---|
| What is meeting preparation? | Ubersuggest: what is meeting preparation; meeting preparation (390) |
| What should a meeting brief include? | Ubersuggest: meeting brief (110) |
| Free meeting brief template | Ubersuggest: meeting brief template (40) |
| What is a good checklist for meeting preparation? | Ubersuggest: checklist for meeting preparation (50); SERP: ksl-training checklist (pos 7) |
| How do you prepare for a meeting using past meeting notes? | GSC: automated meeting briefs that pull in decisions from prior standups (pos 1); which ai connects dots between different conversations (pos 3) |
| How can AI prepare you for your next meeting? | Ubersuggest: ai meeting preparation, meeting preparation ai; GSC: ai tools that generate automated attendee briefings (pos 7) |
| How do engineering leads prepare standups with past decisions? | GSC: our engineering leads want automated meeting briefs ... prior standups (pos 1) |
| How do you prepare for a client or sales meeting? | Ubersuggest: client meeting preparation, sales meeting preparation template |
| How long should meeting preparation take? | Ubersuggest: meeting preparation time |
| Can you record a meeting without consent? | Web SERP: "Can You Record a Meeting Without Consent?" ranks as its own page |

## Handoff note

GSC conversational queries answered: automated meeting briefs from prior standups (pos 1), attendee briefings and research dossiers before meetings (pos 7), enterprise chatbots that summarize meetings into leadership emails (pos 7).


## Open items for content writers (before publishing)

- Add an author name and author bio URL in the frontmatter (currently empty; schema falls back to "Lynkk").
- Create the featured image at the `featured_image_path` in the frontmatter, plus step screenshots where the article describes UI.
- Add the 2 planned inbound links (see `inbound_links_planned`) on the live source pages at publish, and confirm they are live.
- Click-test every link at publish. The California Penal Code 632 page returns 403 to automated checks (bot blocking); it was verified in earlier drafts, so confirm it in a browser.
- The article is a draft and is not published. Publishing needs explicit approval.
- Answers the Search Console queries that already rank 1 to 10: automated meeting briefs from prior standups (pos 1), attendee briefings before meetings (pos 7), meeting summaries as emails (pos 7).
- Links to /blog/founders-meeting-notes, whose "Can AI prepare me for my next meeting?" section is related; it does not target "meeting notes".
