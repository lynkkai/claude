# Audit: zoom-note-taker

Date: 2026-10-12. Checked against `.claude/skills/seo-article/SKILL.md`, `memory/unveilr-skills/seo-score.md` and `humanize-verify.md`.
Topic source: Search Console query group (content/gsc-query-topics-2026-10.md).

## Mechanical audit (scripts/audit_article.py)

```
== articles/zoom-note-taker.md (2592 words, primary 'zoom note taker') ==
85 checks passed, 0 failed
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

- **G1 Intent and SERP format:** PASS WITH RISK. SERP for "zoom note taker" mixes Zoom's own product and help pages (positions 2, 5, 11), a Reddit best-of thread (4), a marketplace app (6) and listicles (8 to 10). The listicle format is present, but Zoom's own pages hold the top spots.
- **G2 Cannibalization:** PASS. Primary is not targeted by any of the 38 live lynkk.ai pages or the 13 unpublished drafts (content/blog-inventory-2026-10-12.md), and no lynkk.ai page ranks in the top 20 for it in the Search Console export.
- **G3 Depth vs SERP median:** PASS. Ranking listicles: 1,050 to 4,046 words, median about 2,930. This draft: about 2,600 (89%).
- **G4 Fan-out integrity:** PASS. 6 or more question H2s, no dead headings, every H2 traced to a source below.

## Inherited AEO structure

PASS: H1 13-15 words, no "Official", evergreen slug, Quick answer callout and Last updated line, question headings, answer-first sections, every section's first 200 characters contain a number.

## Humanize-verify proxies

Burstiness (sentence-length variation) is 0.50 or higher, the human floor. No AI-tell words, no em or en dashes.

## Query fan-out sources (H2 to source)

| H2 | Source |
|---|---|
| What is a Zoom note taker? | GSC: zoom note taker (pos 52); SERP #2 is Zoom's "AI note taker" page |
| How did we compare these Zoom note takers? | Template A requirement (How we tested) |
| Does Zoom have a built-in AI note taker? | SERP: Zoom product page and "Getting started with Zoom Notes" (positions 2 and 5) |
| Is there a free AI note taker for Zoom? | GSC: free ai note taker for zoom (pos 83); Ubersuggest: free zoom note taker (30), zoom note taker free (30) |
| How do you turn on a Zoom note taker? | Ubersuggest: how to turn on zoom note taker (30) |
| Can a Zoom note taker work without a bot joining? | Ubersuggest: meeting bot vs local recording; earlier map: ai note taker that doesn't join meetings |
| Which AI note taker for Zoom meetings fits your team? | Ubersuggest: ai note taker for zoom meetings (140) |
| How do you use a Zoom note taker after the call? | Ubersuggest: how to use zoom note taker (30) |
| Is it legal to use a Zoom note taker? | Web SERP: "is it legal to use an AI note taker in meetings" has law-firm and vendor pages ranking |

## Handoff note

GSC queries answered: best zoom ai notetaker, best ai note taker for zoom, free ai note taker for zoom, ai zoom note taker, zoom note taker (all pos 52 to 90 today).
Routing note (skill: is an on-domain article the right asset?): "best Zoom note taker" is unbranded discovery intent, where independent roundups get cited more than a vendor's own list. Getting Lynkk named in third-party Zoom note taker roundups is worth pursuing alongside this post.

## Open items for content writers (before publishing)

- Add an author name and author bio URL in the frontmatter (currently empty; schema falls back to "Lynkk").
- Create the featured image at the `featured_image_path` in the frontmatter, plus step screenshots where the article describes UI.
- Add the 2 planned inbound links (see `inbound_links_planned`) on the live source pages at publish, and confirm they are live.
- Click-test every link at publish. The California Penal Code 632 page returns 403 to automated checks (bot blocking); it was verified in earlier drafts, so confirm it in a browser.
- The article is a draft and is not published. Publishing needs explicit approval.
- Re-check every competitor price and free-plan limit on the vendor's own pricing page before publishing. All figures come from `memory/competitor-facts.md` (checked 2026-09-30) and are dated in the article.
- Confirm the Zoom AI Companion "turn on" steps (web settings, admin permission, AI Companion button) against Zoom's help center.
- TRUTHS.md says posts should not name competitors unless the team supplies sourced facts. The live listicles on lynkk.ai already name competitors; confirm the team is happy for this listicle to do the same.
- Cannibalization guard: remove "ai note taker for zoom" from the meta keywords of the live /blog/best-ai-note-takers page so this post owns the Zoom note taker queries.
