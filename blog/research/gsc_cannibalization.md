# G2 cannibalization check (Google Search Console)

Source: Search Console export for `https://lynkk.ai/`, "Performance on Search", web search, last 3 months
(supplied 2026-10-18). 773 queries and 53 pages. The raw export is not committed; only the findings below.

## Result

**G2a passes for all 35 articles.** No existing lynkk.ai page ranks in the top 20 for any article's primary
keyword or a close variant. The export does not join queries to pages, so overlaps were judged by topic
against the page list.

| Article topic | Related GSC queries (position) | Existing page | Verdict |
|---|---|---|---|
| Read AI alternative | "read ai alternative" (83.5), "read ai alternatives" (84) | not identified | Pass: no page near top 20; new post can take the query |
| Otter alternatives / comparisons | "otter ai" (1.5), "otter.ai" (4.5) | `/compare/otter` (pos 5.5) | Pass: brand navigational queries, not "alternatives" or "vs" |
| Fireflies | "fireflies ai" (3.0) | `/compare/fireflies` (pos 4.2) | Pass: brand queries only |
| Granola | "granola chrome extension" (15.5) | `/compare/granola` (pos 5.6) | Pass: different intent from pricing, alternatives and vs posts |
| Hindi transcription / speech to text | "hinglish transcription" (8.9), "transcribe hinglish" (10) | `/features/hinglish-transcription` (pos 41.6 avg) | Pass, with care: posts target "hindi", not "hinglish", and link to the feature page as their support-lane target |
| Google Meet (record, AI note taker) | "how to get a transcript of a google meet recording" (9-10) | `/blog/google-meet-transcript` (pos 9.0, 1,181 impr.) | Pass: transcript intent stays with the existing post; new posts target recording and note takers, and link to it |
| Team meeting summary AI | "ai meeting summary for teams" (68) | `/blog/ai-note-taker-microsoft-teams` (pos 24.9) | Pass: not top 20 |
| Daily standup agenda | "daily standup meeting agenda" (18) | `/blog/daily-standup-meeting` | Not one of the 35 targets; noted so kickoff and retro posts do not drift into standup terms |

No queries were found for: tactiq, notta, jamie, avoma, notion note taker, discovery call, kickoff, HOA, LLC,
minutes of meeting format, board minutes, follow-up email.

## Changes made from this data

1. Each article's `internal_link_target` now points at its support-lane page (`/compare/*`, `/features/*`,
   `/use-cases/*`), so new posts feed existing pages instead of competing with them.
2. Each article has a "More on Lynkk" line linking 2 to 3 of those pages, and the most relevant page is
   listed as an extra inbound-link source in frontmatter.
3. Bylines link to the live author page `/blog/authors/samarth-wagh` (`author_url` in frontmatter).

## Watch after publishing

- `/blog/google-meet-transcript` already earns 1,181 impressions at position 9. If the Google Meet posts start
  ranking for "transcript" queries, re-check whether one of them should be merged into it.
- `/features/hinglish-transcription` ranks 8.9 for "hinglish transcription". The Hindi posts use "Hinglish"
  only as a feature name; do not retitle them around Hinglish.
