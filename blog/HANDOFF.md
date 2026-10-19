# Handoff: Lynkk blog wave 1 (35 articles)

Written 19 October 2026 so another session, or another person, can pick this up cold.
Read this file, then `README.md` (index, tools and gates), then `docs/audit-brief.md`.

## Where things live

| | |
|---|---|
| Repo and branch | `lynkkai/claude`, branch **`claude/lucid-clarke-pe75fi`** (all work is here; nothing merged, no PR open) |
| Articles | `blog/articles/<slug>.md`, 35 of them |
| Rules you must follow | `/CLAUDE.md` (brand is always **Lynkk**; **never use em or en dashes**; run the checker and schema builder before committing) |
| Lynkk product facts | `/memory/lynkk-brand.md`, **only** the "Verified on lynkk.ai (2026-10-17)" section. Everything above it is older and partly wrong |
| The skill pack this was written from | `blog/docs/skills/` (seo-article, aeo-article, seo-score, aeo-score, humanize-verify, post-humanize-check and others) |
| Working briefs given to helper agents | `blog/docs/humanize-brief.md`, `blog/docs/audit-brief.md` |

Commit messages in this repo end with the two attribution lines used by the earlier commits; copy the
format from `git log`.

## The pipeline

`research -> write -> aeo_score + seo_score -> humanize -> post_humanize_check -> skill_audit -> publish`

Six gates. Run every one from the repo root. All must pass before an article is published.

```
python3 blog/tools/check_articles.py        # 0 failures (meta, keywords, question H2s, FAQ, links, dashes, brand)
python3 blog/tools/aeo_score.py             # >= 80, no CRITICAL
python3 blog/tools/seo_score.py             # >= 85 and gates G1-G4
python3 blog/tools/humanize_verify.py       # WORKING (>= 85% of weighted signals)
python3 blog/tools/post_humanize_check.py   # C1-C17 pass
python3 blog/tools/skill_audit.py           # A1-A13 pass (the skill rules the scorers do not cover)
```

Each takes article paths and `-v` for row detail. After any FAQ edit run `build_schema.py`; after any
article edit run `build_index.py` to refresh the README table.

## Status on 19 October 2026

- **check_articles, aeo_score, seo_score, humanize_verify: 35 of 35 pass.**
- **post_humanize_check: 3 articles fail** (C12 a sentence over 40 words, C16 a corrected table). Both are
  articles a helper was still mid-edit on. Run it, read the rows, fix or re-baseline (below).
- **skill_audit: 21 of 35 pass. 14 still fail**, listed under "What is left" below.
- **Fact check: 13 of 35 have a sheet** in `blog/review/fact-check/`. Every number changed so far is logged
  in `blog/review/corrections.tsv` with the source URL.

## What is left

**1. Finish the fact check and skill audit on these 14 articles.** Follow `docs/audit-brief.md` exactly: a
3-round check of every claim against the primary source (fetch the page, never answer from memory), then
`skill_audit.py` to PASS, then all six gates.

```
app-for-meeting-minutes  avoma-alternatives  board-minutes-of-meeting  granola-vs-otter-ai
hoa-meeting-minutes-template  how-to-take-good-meeting-notes  llc-meeting-minutes-template
minutes-of-meeting-format  notta-pricing  otter-ai-vs-fireflies-ai
project-kickoff-meeting-agenda-template  record-google-meet-call  remove-fireflies-ai-from-teams
tactiq-alternative
```

The audit failures are almost always the same four: **A1** H1 not 13-15 words, **A2** fewer than 8 unique
internal links, **A4** anchor text containing "Lynkk", **A6** a secondary keyword missing from the body.

**2. The legal sheet.** `blog/review/legal-review.md` lists every legal claim in the 4 India/US governance
posts with its source and a tick box. A helper was part-way through upgrading each row by fetching the
primary statute text (India Code, Companies Act s.118/173/174, ICSI SS-1 2024, Cal. Civ. Code 4950/4935,
Fla. Stat. 720.303, state LLC acts) and answering the reviewer questions. That is unfinished. **A human
company secretary or attorney must still sign it off either way**; the tick boxes are theirs, not yours.

**3. Publish-day mechanics** (nothing to do until a post goes live):
- `python3 blog/tools/skill_audit.py --refresh` re-reads lynkk.ai/sitemap.xml into `research/live_pages.txt`.
- `python3 blog/tools/sibling_links.py --restore` re-links the 94 links between wave posts that are
  currently held as plain text in `review/sibling-links.tsv` (the skill forbids shipping dead links).
- `python3 blog/tools/inbound_verify.py` then `--mark`: tells you which inbound links in
  `review/inbound-links.md` to paste on which live page, and ticks each one once it is really there.
- Upload the three Word files in `blog/downloads/` and add the download link to posts #22, #25 and #27.

**4. Prices.** `python3 blog/tools/price_check.py` confirms every competitor figure still appears on the
vendor page. All 11 vendors were unchanged on 18 October 2026. A scheduled task runs this weekly
(Mondays 08:48 UTC) and pushes any needed updates to a `price-check/<date>` branch.

## Things that will bite you

- **The baseline.** `blog/humanize/originals/<slug>.md` is each article as it was before the humanize
  rewrite; `post_humanize_check.py` compares against it, so a *later* sourced fact correction or an H1
  rewrite shows up for ever as a C8/C11/C16 failure. The fix is **not** to edit the baseline by hand:
  record the change in `review/corrections.tsv` and a `review/fact-check/<slug>.md` sheet, then run
  `python3 blog/tools/rebaseline.py <slug> --reason "..."`. It keeps the old baseline under
  `humanize/originals/pre-correction/` and logs the move in `review/rebaselines.tsv`.
- **Rewriting prose breaks the humanize score.** Any new sentence must keep varied sentence lengths (mix
  2-6 word sentences with 28-38 word ones, never over 40), varied openers, and none of the AI-tell words
  listed in `tools/humanize_verify.py`. Re-run `humanize_verify.py` after every edit.
- **`apply_rewrites.py` refuses** a rewrite that drops a number or a link, or pushes a FAQ answer outside
  40-62 words. The SKIP lines are the tool working, not a bug.
- **Soft warnings are not failures.** `check_articles.py` warns about keyword density under 0.5% and about
  "sentences over 40 words" that are really a heading ending in a colon joined to the next paragraph. The
  stricter C12 check in `post_humanize_check.py` is the one to trust.
- **Type-token ratio** (vocabulary variety) sits just under its 0.40 target on several pricing and legal
  posts, because they repeat "minutes", "meeting", "plan" and price wording by design. It carries the
  least weight, so those articles still score WORKING at 91%. Leave it.
- **Legal posts.** Keep every "must", "should", "may", every hedge ("most states", "generally"), every
  section number and day count exactly as strong as it is, unless a primary source shows otherwise.
- **Never claim**: a live CRM integration, SOC 2 or ISO certification, a Windows or mobile app, "speaks
  when needed", "offline-first", or notes "within 30 seconds". None are on the current site.
- Do not commit the raw Search Console export. `research/gsc_cannibalization.md` holds the findings only.

## Known good facts to reuse

Lynkk: Free is 5 notes a month at 2 hours each; Pro is $15 a month; the bot joins Zoom, Google Meet and
Microsoft Teams; the Mac app and Chrome extension record without a bot; 17 languages plus a Hinglish
setting, with Tamil, Telugu, Marathi and Bengali in beta; data regions US, EU, UK, India, Singapore,
Australia; AES-256 in transit and at rest.

Corrections already found and applied (see `corrections.tsv` for all of them): Read AI's 5-license minimum
is on **Enterprise+**, not Enterprise; Teams intelligent recap needs **Teams Premium or** a Microsoft 365
Copilot license; Zoom retired the "AI Companion" name on 24 June 2026; Jamie's Android app is a beta;
Granola bills annually on Enterprise only.
