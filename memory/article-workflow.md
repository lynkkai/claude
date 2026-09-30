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
Batch 1 (2026-09-30): 11 drafts written, all pass `scripts/audit_article.py`. Summary: `seo/audits/batch-1-summary.md`.
- [x] #1 best-ai-note-takers
- [x] #2 best-free-ai-note-takers
- [x] #3 zoom-meeting-recorders
- [x] #4 ai-note-taker-microsoft-teams
- [x] #5 transcribe-audio-to-text
- [x] #6 ai-voice-recorders
- [x] #7 ai-transcription-software
- [x] #8 voice-to-text-apps
- [x] #9 ai-powered-meeting-assistants
- [x] #10 zoom-ai-companion-alternatives
- [x] #16 how-to-transcribe-zoom-meetings
- [ ] #11-#15 Lynkk vs posts: on hold, they overlap existing lynkk.ai/compare pages (decide: update compare pages instead?)
- [ ] Next batch: #17 dictation on Mac, #18 Word dictation, #19 voice memos, #20 Google Meet, #21-#30 use cases

## Tools for every article
- `python3 scripts/build_schema.py articles/<slug>.md` builds Article/ItemList/FAQPage/Breadcrumb schema from the article (keeps FAQ schema in sync).
- `python3 scripts/audit_article.py articles/<slug>.md` runs every mechanical rule (must end with 0 failed).
- Draft long: first drafts have run ~400 words short; aim for 2,800+ on listicles.

## Audit step (required for every article)
After drafting, run the mechanical audit (H1 13-15 words, meta 150-160, density 0.5-1.5%, 200-char clip has a number, sections ≤300 words, paragraphs ≤80 words, FAQ 40-60 words and schema synced, tables ≤4 columns, 8-14 links, zero competitor links (run `python3 scripts/check_competitor_links.py articles/<slug>.md`), at least 2 external links to verified government or standards sites, no links to unpublished pages, schema present, no dashes, no AI-tell words) and save the report to `seo/audits/<slug>-audit.md`.
