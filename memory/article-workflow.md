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
- **Never link to competitors** (no hyperlinks or bare URLs to competitor sites). Competitor facts are cited in plain text with the date checked. No competitor URLs anywhere in the repo, including audit and handoff notes. Chat replies to the team must not include competitor links either.
- External authority links: every article needs at least 2, and they must go to official government, legislative or standards sites (for example .gov, uscode.house.gov, state legislature sites, nist.gov, eur-lex.europa.eu). Confirm each page exists (search restricted to the official domain) before adding it, and click-test at publish.
- Unconfirmed product facts are written as `[CONFIRM: ...]`.
- Disclosure box + "How we tested" on listicles and comparisons.
- Competitor prices: dated, cited in plain text (never linked), and marked for re-check before publish.
- Each article needs 1-2 inbound internal links from existing lynkk.ai pages at publish time.

## Progress
- [x] #1 Best AI Note Takers (primary: ai note taker): draft v3 at `articles/best-ai-note-takers.md`, passed rule audit `seo/audits/best-ai-note-takers-audit.md`; needs [CONFIRM] items filled
- [ ] #2 Best Free AI Note Takers in the USA for 2026 (primary: free ai note taker)

## Audit step (required for every article)
After drafting, run the mechanical audit (H1 13-15 words, meta 150-160, density 0.5-1.5%, 200-char clip has a number, sections ≤300 words, paragraphs ≤80 words, FAQ 40-60 words and schema synced, tables ≤4 columns, 8-14 links, zero competitor links (run `python3 scripts/check_competitor_links.py articles/<slug>.md`), at least 2 external links to verified government or standards sites, no links to unpublished pages, schema present, no dashes, no AI-tell words) and save the report to `seo/audits/<slug>-audit.md`.
