# Audit: zoom-note-taker

Date: 2026-10-12. Source of topic: Search Console query group (content/gsc-query-topics-2026-10.md).

## Mechanical audit (scripts/audit_article.py)

```
== articles/zoom-note-taker.md (2583 words, primary 'zoom note taker') ==
85 checks passed, 0 failed
```

## TRUTHS.md check (scripts/truths_check.py)

0 issue(s)

## Competitor links (scripts/check_competitor_links.py)

0 competitor links. Competitor facts are cited in plain text only.

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
