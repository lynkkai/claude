# Skill compliance + fact-check brief (Lynkk blog)

Work only inside /home/user/claude/blog and run every command from there. Touch ONLY the articles on your list. Other helpers are editing other articles at the same time. Do NOT commit or push. Do NOT run build_schema.py or build_index.py (the lead runs them at the end).

Read first: /home/user/claude/CLAUDE.md, /home/user/claude/memory/lynkk-brand.md (the "Verified on lynkk.ai" section is the only source of Lynkk facts), and in /tmp/claude-0/-home-user-claude/9093d0b9-e5c3-5da1-af5a-38878f510e39/scratchpad/skillzip/skills-md/: seo-article.md (whole file) and aeo-article.md ("HARD RULE" sections, "PHASE 5: Article Writing" and the 3 verification rounds, roughly lines 340-560).

## Part 1: accurate data (3-round fact check, per the aeo-article skill)
For EVERY factual claim in each article (prices, plan limits, feature claims about any product including Lynkk, platform support, dates, statistics, percentages, legal or standards references, how-to steps in third-party apps):
- Round 1: fetch the PRIMARY source now (WebFetch, or `curl -sL`) and compare. Vendor claims: the vendor's own pricing/help/feature page. Lynkk claims: lynkk.ai pages (pricing, features, integrations, security) or memory/lynkk-brand.md's verified section. Never mark VERIFIED from memory or training data. If you cannot fetch a source, mark COULD NOT VERIFY.
- Round 2: is anything misleading by omission (missing exception, plan caveat, region limit)? Fix it briefly.
- Round 3: internal contradictions (body vs table vs FAQ vs Quick answer vs tldr frontmatter). Fix them.
- Fix every ERROR in the article. A claim you cannot verify: remove it, or reword so it no longer asserts the unverified detail. Unsourced numbers that are genuinely estimates get "(industry estimate)" or are removed.
- Each time you change a number because it was wrong, append one line to review/corrections.tsv (tab-separated, one shell `printf '...\t...\t...\t...\n' >> review/corrections.tsv` per line): article slug, old text, new text, source URL.
- Write review/fact-check/<slug>.md: a short header (article, date checked 2026-10-18) then a table `| # | Claim (short) | Source URL fetched | Status | Fix |` with Status one of VERIFIED, FIXED, REMOVED, COULD NOT VERIFY. Every price, number and product claim gets a row.

## Part 2: skill rules
Run `python3 tools/skill_audit.py articles/<slug>.md -v` and fix until it prints PASS:
- A1 H1: one natural sentence of 13-15 words containing every word of the primary keyword, the year and the market (US or India) as now, never "Official". Also set frontmatter `title:` to the same text. Do not change meta_title, slug, or any H2/H3 heading.
- A2/A3 8-14 unique internal lynkk.ai links, ONLY to URLs listed in research/live_pages.txt (features, use-cases, compare, integrations, pricing, security, live /blog/ posts). Weave them into existing sentences with descriptive anchors; do not bolt on link lists. Never link to a /blog/ slug not in live_pages.txt.
- A4 no anchor text containing "Lynkk" (CTA links to the homepage, /pricing and /sign-up are exempt). Reword anchors, e.g. "Lynkk vs Fathom" -> "a side-by-side with Fathom".
- A5 at least 2 external authority links, each returning HTTP 200 (check with curl).
- A6 every secondary keyword in frontmatter appears at least once, in a natural sentence. A7 primary keyword density 0.5-1.5%.
- A8 at least 50% of sections open (first ~200 characters) with a number or concrete figure that is true and sourced.
- A9 a definition sentence ("X is a/an ...") in the first 100 words after the disclosure line.
- Also apply the skill's judgment rules: no dead headings, answer-first sections, FAQ answers that add something the body does not already say (if a FAQ answer only repeats the body, rewrite the answer to add a sourced edge case; keep the FAQ question heading unchanged).
- Keep the house style: Lynkk listed first and tagged "(our product)" in roundups, the Quick answer, disclosure, byline, "Pricing checked" line, CTAs. (The skill's "brand 1-2 times" rule is overridden by the live lynkk.ai blog house style; do not strip Lynkk mentions.)

## Gates that must still pass on each article when you finish
`python3 tools/check_articles.py articles/<slug>.md` (0 failures), `aeo_score.py` (>=80, no CRITICAL), `seo_score.py` (SEO-READY), `humanize_verify.py` (WORKING, >=85%), `post_humanize_check.py` (PASS), `skill_audit.py` (PASS). New or edited sentences must keep the humanized style: varied sentence lengths, no sentence over 40 words, varied openers, none of the AI-tell words listed in tools/humanize_verify.py.

## Hard rules
Never use em dashes or en dashes (plain hyphen only for ranges/compounds). Brand is always "Lynkk". Lynkk facts only from the verified section (Free 5 notes a month, 2 hours per note; Pro $15/month; bot for Zoom, Google Meet, Teams; Mac app and Chrome extension record without a bot; 17 languages plus Hinglish, Tamil/Telugu/Marathi/Bengali beta; no live CRM; no SOC 2; no Windows/mobile app; data regions US, EU, UK, India, Singapore, Australia). Do not change H2/H3 headings, tables' structure or list structure except to fix a factual error. FAQ answers stay 40-60 words.

## Report back (short)
Per article: gate results, number of claims checked and how many FIXED / REMOVED / COULD NOT VERIFY, and the most important corrections (old -> new, source). List anything you could not resolve.

## Added 2026-10-19 (read this, it changed)
- After you change a number because it was wrong, or rewrite the H1/title for rule A1, `post_humanize_check.py` will fail that article on C8 (frontmatter), C11 (numbers) or C16 (tables/lists), because it compares with the pre-humanize baseline in humanize/originals/. Once the article passes everything else, run:
  `python3 tools/rebaseline.py <slug> --reason "sourced fact corrections (corrections.tsv) and A1 H1 rewrite"`
  It keeps the old baseline under humanize/originals/pre-correction/ and logs the move in review/rebaselines.tsv. Run it ONLY after the correction is recorded in review/corrections.tsv and review/fact-check/<slug>.md, and never to silence a failure you cannot explain.
- Then re-run `post_humanize_check.py articles/<slug>.md`: it must PASS.
- A4 covers the "**More on Lynkk:**" line too: the label can stay, but anchor text like "AI meeting notes in Lynkk" must lose the brand name, e.g. "AI meeting notes with tasks and decisions".
- A2 counts unique internal links, so repeating one URL does not help. research/live_pages.txt lists every URL you may link to. Links between wave articles are currently held as plain text in review/sibling-links.tsv (they go back at launch), so do not re-add a /blog/ link that is not in live_pages.txt.
- Do not commit. I commit each batch after re-running every gate.
