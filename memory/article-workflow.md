# Article creation workflow (Lynkk)

Source: Unveilr skills archive (uploaded 2026-09-30). All 16 skill files are kept in `memory/unveilr-skills/`.
The writer skill is installed as a project skill at `.claude/skills/seo-article/SKILL.md` (invoke with `/seo-article`).

## Pipeline for each blog post
1. Take the post's primary + secondary keywords from `seo/keyword-map-v2.md` and the E-E-A-T rules/template from `seo/content-briefs.md`.
2. Research: Ubersuggest `serp_analysis` (top-10 format and depth), `google_suggestions` (questions / fan-out), web search for facts. At least 6 sourced questions become the H2/H3s. No invented headings.
3. **Keyword expansion bypass:** if a sub-topic suggests extra keywords, check them in Ubersuggest (US, locId 2840) and add the relevant ones that are not another post's primary. Log them in `keywords_added`.
4. Draft answer-first: Quick Answer, definition in first 100 words, every section opens with ~2 sentences that include a number and a concrete claim.
5. Self-check against `memory/unveilr-skills/seo-score.md` gates and humanize-verify signals. No em or en dashes.
6. Save to `articles/<slug>.md`. Do not publish; publishing needs explicit approval.

## Lynkk-specific rules
- Unconfirmed product facts are written as `[CONFIRM: ...]`.
- Disclosure box + "How we tested" on listicles and comparisons.
- Competitor prices: dated, linked to the vendor page, and marked for re-check before publish.
- Each article needs 1-2 inbound internal links from existing lynkk.ai pages at publish time.

## Progress
- [x] #1 Best AI Note Takers in the USA (2026) (primary: ai note taker): draft at `articles/best-ai-note-takers.md`, needs [CONFIRM] items filled
- [ ] #2 Best Free AI Note Takers in the USA for 2026 (primary: free ai note taker)
