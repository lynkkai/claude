# Audit: action-items-examples-template

Date: 2026-10-12. Source of topic: Search Console query group (content/gsc-query-topics-2026-10.md).

## Mechanical audit (scripts/audit_article.py)

```
== articles/action-items-examples-template.md (1900 words, primary 'action items') ==
74 checks passed, 0 failed
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
- Replaces the superseded draft `blog/action-items-examples-and-template.md` on branch claude/eager-tesla-cvuh6f (that draft used claims TRUTHS.md forbids). Do not publish the old one.
- Cannibalization guard: /features/action-items owns "meeting action items" and "action item tracker ai"; this post targets "action items" and its template and example terms.
