# Humanize brief (Lynkk blog)

Work only inside /home/user/claude/blog and run every command from there. Do NOT commit, push, or touch any article that is not on your list. Other helpers are editing other articles at the same time.

## Goal
Each of your articles must reach WORKING (85% or more) in `python3 tools/humanize_verify.py articles/<slug>.md -v`.
Pass thresholds: burstiness (CV of sentence length) >= 0.50, sentence-length stdev >= 8, zero AI-tell words (list in tools/humanize_verify.py), top-3 sentence openers <= 25% of sentences, zero em dashes, paragraph-length stdev >= 12, type-token ratio >= 0.40.

## Loop per article
1. `python3 tools/paras.py articles/<slug>.md` prints each prose paragraph with its index, sentence word counts and sentence first words.
2. Write `humanize/rw_<slug>.json` as `{"<slug>": {"<index>": "full new paragraph text", ...}}`. Rewrite only the paragraphs you need (usually 10-20).
3. `python3 tools/apply_rewrites.py humanize/rw_<slug>.json`. It applies each paragraph and prints SKIP lines when a rewrite would drop a number or link, when a FAQ answer would leave 40-62 words, or when the paragraph is not unique. Fix skipped ones and re-apply. Indexes shift only if paragraph count changes, so never split or merge paragraphs; always re-run paras.py before a second round.
4. `python3 tools/humanize_verify.py articles/<slug>.md -v` and iterate.
5. When WORKING, also confirm nothing else broke:
   `python3 tools/check_articles.py articles/<slug>.md`, `python3 tools/aeo_score.py articles/<slug>.md`, `python3 tools/seo_score.py articles/<slug>.md`. All must still pass (0 failures, AEO >= 80 with no CRITICAL, SEO-READY). If a run takes no file argument, run it bare and read your rows.

## How to raise the numbers (what worked on the first 6 articles)
- Mix sentence lengths hard inside paragraphs: a few 2-6 word sentences ("Not quite." "That adds up." "Check the bill.") next to long 28-38 word sentences that join two related clauses. Never exceed 40 words in one sentence (an SEO check fails above 40).
- Vary sentence openers. Do not start most sentences with the product name, "The", "It", "You", "This" or "Lynkk". Lead with the number, the condition ("On the free plan, ..."), a question, or the object.
- Keep the first ~200 characters of each section's first paragraph carrying a number or a concrete claim (clip rule).
- Paragraph stdev: let some paragraphs be one short sentence and others 60-90 words (never over 100 words).

## Hard rules (do not break any)
- Never use em dashes or en dashes. Plain hyphen only for ranges and compound words. Avoid the AI-tell words listed in tools/humanize_verify.py.
- Brand is always "Lynkk".
- Keep every number, price, date, link and markdown formatting (bold, links) in each paragraph. Keep the primary keyword and secondary keywords (see frontmatter) present wherever they were, especially in the first paragraph.
- Add NO new facts, statistics, claims, features, prices or opinions about competitors. Only reorder, split, join, and rephrase what is already there. A short fragment like "Worth checking." is fine; a new claim like "most teams switch within a week" is not.
- Lynkk facts must stay within: Free plan 5 notes a month (2 hours each); Pro $15 a month; bot for Zoom, Google Meet and Microsoft Teams; Mac app and Chrome extension record without a bot; 17 languages plus Hinglish; no live CRM; no SOC 2; no Windows or mobile app.
- Do not edit frontmatter, headings, tables, lists, code blocks, the Quick answer blockquote, the disclosure line, the byline, or the HANDOFF comment. paras.py only shows prose paragraphs; only rewrite those.
- FAQ answers must stay 40-60 words and still answer the question directly in the first sentence.
- For legal posts (board-minutes-of-meeting, board-meeting-agenda, hoa-meeting-minutes-template, llc-meeting-minutes-template, minutes-of-meeting-format): do not change the legal meaning of any sentence. Keep section numbers, day counts, "must"/"should"/"may" exactly as strong or weak as they were, and keep hedges like "generally" or "most states".

## Report back
For each article: final verdict line from humanize_verify, and whether check_articles / aeo_score / seo_score still pass. List any rule you could not satisfy and why. Keep the report short.
