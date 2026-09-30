# Keyword Data Verification

**Date:** 2026-09-30 · **Method:** every keyword metric cited in the four SEO reports was re-pulled from Ubersuggest
`keyword_overview` (US locId 2840; India locId 2356 where marked; Global for "lynkk"). The original figures mostly came
from other endpoints (`match_keywords`, `keyword_suggestions`, `page_keywords`), so this is a cross-endpoint check.
Each keyword's monthly history (up to 13 months) was used to compute the median and spot spikes and stale data.

## Result

- **38 of 38 keywords match exactly** on search volume and SEO difficulty. No transcription errors were found in the reports.
- **The headline volume is simply the latest month.** For most keywords that is representative. For 8 it is not (flags below).
- **Two pairs of keywords are the same pool of searches,** so their volumes must not be added together.

## Full table

Flags: **spiky** = the highest month is 8x or more the lowest; **headline>=2x median** = the number shown in the report is
at least double a typical month; **stale** = Ubersuggest's latest month is before June 2026.

| Keyword | Reported | Re-check | SD rep | SD re | Match | 13-mo median | Min | Max | Flags |
|---|---|---|---|---|---|---|---|---|---|
| ai note taker | 27100 | 27100 | 48 | 48 | yes | 27100 | 18100 | 40500 | ok |
| ai notes taker | 27100 | 27100 | 34 | 34 | yes | 27100 | 18100 | 40500 | ok |
| ai powered meeting assistant | 40500 | 40500 | 50 | 50 | yes | 40500 | 5400 | 90500 | spiky |
| ai meeting assistant | 4400 | 4400 | 60 | 60 | yes | 4400 | 1600 | 8100 | ok |
| meeting assistant | 4400 | 4400 | 59 | 59 | yes | 2400 | 90 | 33100 | spiky |
| ai notetaker | 2900 | 2900 | 42 | 42 | yes | 2900 | 1900 | 4400 | ok |
| conversation intelligence | 1900 | 1900 | 60 | 60 | yes | 1600 | 590 | 3600 | stale (last 2026-03) |
| meeting ai | 1900 | 1900 | 48 | 48 | yes | 1600 | 720 | 2900 | ok |
| ai meeting notes | 1000 | 1000 | 41 | 41 | yes | 1000 | 720 | 1600 | ok |
| meeting notes ai | 590 | 590 | 39 | 39 | yes | 480 | 390 | 880 | ok |
| ai note taker for in person meetings | 480 | 480 | 40 | 40 | yes | 480 | 260 | 720 | ok |
| live ai meeting assistant | 170 | 170 | 51 | 51 | yes | 20 | 10 | 1600 | spiky, headline>=2x median |
| real time ai meeting assistant | 110 | 110 | 59 | 59 | yes | 30 | 10 | 880 | spiky, headline>=2x median |
| ai meeting recorder | 480 | 480 | 37 | 37 | yes | 480 | 390 | 720 | ok |
| meeting notetaker | 880 | 880 | 46 | 46 | yes | 880 | 590 | 1000 | ok |
| speech to text mac | 1600 | 1600 | 25 | 25 | yes | 1600 | 1300 | 1900 | ok |
| ai dictation | 480 | 480 | 31 | 31 | yes | 480 | 390 | 720 | ok |
| google meet ai note taker | 590 | 590 | 40 | 40 | yes | 590 | 480 | 880 | ok |
| teams ai note taker | 590 | 590 | 28 | 28 | yes | 590 | 480 | 720 | ok |
| ai note taker for zoom | 480 | 480 | 33 | 33 | yes | 390 | 210 | 1900 | spiky |
| bot free ai note taker | 110 | 110 | 59 | 59 | yes | 90 | 40 | 260 | ok |
| team ai meeting notes | 720 | 720 | 25 | 25 | yes | 720 | 390 | 880 | stale (last 2025-12) |
| team ai note taker | 720 | 720 | 27 | 27 | yes | 590 | 480 | 880 | stale (last 2025-12) |
| action item tracker | 320 | 320 | 31 | 31 | yes | 260 | 210 | 1000 | ok |
| wispr flow alternative | 480 | 480 | 11 | 11 | yes | 480 | 210 | 880 | ok |
| slack ai notes | 170 | 170 | 34 | 34 | yes | 30 | 20 | 1600 | spiky, headline>=2x median |
| team meeting notes | 390 | 390 | 43 | 43 | yes | 390 | 260 | 480 | stale (last 2026-05) |
| meeting bot | 70 | 70 | 37 | 37 | yes | 70 | 40 | 140 | ok |
| ai note taker app | 880 | 880 | 32 | 32 | yes | 880 | 590 | 1300 | ok |
| how to record google meet | 2400 | 2400 | 25 | 25 | yes | 2400 | 1600 | 2900 | ok |
| record google meet chrome extension | 140 | 140 | 36 | 36 | yes | 10 | 10 | 880 | spiky, headline>=2x median |
| speech to text mac app | 320 | 320 | 28 | 28 | yes | 260 | 140 | 1300 | spiky |
| ai meeting summary | 170 | 170 | 37 | 37 | yes | 170 | 110 | 260 | ok |
| hindi transcription (IN) | 1900 | 1900 | 15 | 15 | yes | 1900 | 1300 | 2400 | ok |
| hinglish transcription (IN) | 110 | 110 | 28 | 28 | yes | 110 | 90 | 140 | ok |
| lynkk (Global) | 170 | 170 | None | None | yes | 170 | 70 | 260 | ok |
| ai notes | 5400 | 5400 | 55 | 55 | yes | 5400 | 2400 | 8100 | ok |
| record meeting notes | 390 | 390 | 57 | 57 | yes | 390 | 320 | 480 | ok |

## Issues found and what was corrected

| Keyword | Reported | Typical month (median) | Problem | Correction made |
|---|---|---|---|---|
| live ai meeting assistant | 170 | 20 | 170 is the latest month; one 1,600 spike; usually 10 to 20 | Homepage report now says "usually 10 to 20/mo" |
| real time ai meeting assistant | 110 | 30 | One 880 spike (Apr 2026); usually 10 to 70 | Homepage report updated |
| slack ai notes | 170 | 30 | Spikes of 1,600 (Sep 2025) and 170 (Aug 2026); usually about 30 | Product-pages and feature audits updated |
| record google meet chrome extension | 140 | 10 | Was 10 to 30 for most of the year; spiked to 590 to 880 in May to Jun 2026 | Product-pages and feature audits updated |
| meeting assistant | 4,400 | 2,400 | Swings from 90 to 33,100 a month | Homepage report updated |
| ai powered meeting assistant | 40,500 | 40,500 | Rose from about 5,400 to 90,500 within a year; unusually low CPC ($2.49) | Already flagged in homepage report; no change |
| ai note taker for zoom | 480 | 390 | One 1,900 spike (Feb 2026); otherwise steady | Minor; no change needed |
| speech to text mac app | 320 | 260 | One 1,300 spike (Mar 2026); otherwise 140 to 480 | Minor; no change needed |
| **ai note taker / ai notes taker** | 27,100 each | 27,100 | **Identical monthly history and identical SERP click estimates:** Ubersuggest (and Google) treat these as one pool of searches. The report called "ai notes taker" a separate, easier target (SD 34 vs 48); both SERPs share Read AI, Otter and Notta, so the lower SD is not reliable | Homepage report corrected: same target, not additive |
| **team ai meeting notes / team ai note taker** | 720 each | 720 / 590 | Near-identical history, and **data last updated Dec 2025** (9 months old) | Product-pages and feature audits note staleness and overlap |
| conversation intelligence | 1,900 | 1,600 | Data last updated Mar 2026 | Already described as declining; left as is |
| team meeting notes | 390 | 390 | Data last updated May 2026 | Minor; no change |
| lynkk (Global) | 170 | 170 | September 2026 data arrived since the homepage report (170, up from 90). "Falling" was too strong | Homepage report now says "uneven" |

## Impact on recommendations

- **Unchanged:** the main targets are steady and verified: ai note taker (27,100), ai notetaker (2,900), ai meeting notes (1,000),
  speech to text mac (1,600), ai dictation (480), google meet ai note taker (590), teams ai note taker (590),
  ai meeting recorder (480), ai note taker for in person meetings (480), wispr flow alternative (480), hindi transcription IN (1,900).
- **Weaker than stated:** "live/real-time AI meeting assistant" should explain the feature in copy, not be treated as a traffic
  target. The /slack page's search potential is about 30/mo, not 170. "record google meet chrome extension" is a recent spike, not proven demand.
- **Workspaces:** "team ai meeting notes" is still the best-fit term, but re-check it once Ubersuggest updates past Dec 2025.

## Limits of this check

This confirms the reports faithfully reflect Ubersuggest. It does **not** prove Ubersuggest's estimates match Google's real
numbers; no second keyword tool (Google Keyword Planner, Search Console) is connected in this session. Google Search Console
impressions for lynkk.ai would be the best ground truth once pages start ranking.
