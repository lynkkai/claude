# Lynkk.ai: Low Hanging Fruit

Prepared 2026-11-03. Companion to `lynkk-content-plan-2026-11.md`. That document answered "what
should we write". This one answers "what can we win this month without writing much".

Sources: the GSC query export (top 1,000 queries, last 3 months) cross-referenced against Ubersuggest
volume and SD, and against the 54 live blog posts on lynkk.ai.

---

## The one number that matters

| Position band (non-brand) | Queries | Impressions | Clicks |
|---|---|---|---|
| 1 to 3 | 21 | 195 | **0** |
| 4 to 10 | 242 | 1,601 | **1** |
| 11 to 20 | 138 | 1,505 | 2 |
| 21 to 30 | 105 | 1,408 | 2 |
| 31 to 50 | 164 | 2,394 | 2 |
| 51 and worse | 272 | 3,131 | 2 |

**270 non-brand queries rank in the top 10 and return zero clicks. That is 1,967 impressions
already sitting on page one, earning nothing.**

Non-brand performance overall in the top-1,000 export: 10,777 impressions, 9 clicks, 0.08% CTR.
Brand: 323 impressions, 53 clicks, 16.4% CTR.

A normal CTR for position 7 is roughly 3 to 5%. Lynkk is at 0.06% in the 4 to 10 band. This is not
a ranking problem and it is not a content-volume problem. **The rankings already exist and are not
being clicked.** That makes the cheapest wins on this site title, meta description and snippet work
on pages that are already there, not new posts.

A note on scope: the export's top 1,000 queries total 11,100 impressions. Site-wide across all
queries it is 28,051 impressions and 152 clicks, so there is a long tail below this export that
behaves the same way.

---

## Tier 1: Already on page one, zero clicks. Fix the snippet, not the content.

These are ranked by cluster size. Each one is a CTR fix on a page that already exists.

### F1. Google Meet transcript: 583 impressions in the top 14, zero clicks

The biggest single opportunity on the site. 109 query variants, 1,261 impressions total, **451 of
those impressions in the top 10, and zero clicks across all of them.** The page is
`/blog/google-meet-transcript`, which has 6,277 impressions at position 10.03 and 8 clicks (0.13%).

The queries, with position:

| Impressions | Position | Query |
|---|---|---|
| 154 | 11.9 | google meet transcript |
| 33 | 9.7 | meet transcript |
| 28 | 6.9 | where to find google meet transcript |
| 26 | 7.8 | where do i find google meet transcripts |
| 24 | 8.3 | where can i find google meet transcripts |
| 23 | 8.8 | how to get transcript from google meet recording |
| 22 | 8.1 | how to get google meet transcript |
| 18 | 7.9 | where do i find my google meet transcript |
| 17 | 7.4 | how to get meeting transcript in google meet |
| 17 | 7.8 | where is my google meet transcript |
| 15 | 6.9 | where can i find the transcript of a google meet meeting |
| 15 | 11.9 | how to download transcript from google meet recording |
| 14 | 7.1 | how to access google meet transcript |
| 12 | 8.3 | how to find google meet transcript |
| 10 | 8.2 | google meet how to get transcript |
| 10 | 9.0 | where are google meet transcripts saved |
| 8 | 8.6 | google meet transcription location |
| 8 | 8.5 | where do google meet transcripts go |
| 6 | 9.3 | gemini google meet transcript |

Plus roughly 20 more variants at 4 to 8 impressions each, all between positions 7 and 10.

**Read the pattern:** the dominant intent is **"where is it"**, not "how do I enable it". The
queries say *where to find*, *where do i find*, *where is my*, *where are they saved*, *where do
they go*, *transcription location*. Thirteen separate "where" variants. Ubersuggest confirms these
are easy: `where to find google meet transcript` SD 7, `where is my google meet transcript` SD 6,
`how to access google meet transcript` SD 6, `how to find google meet transcript` SD 8. The head
term `google meet transcript` is 1,000/mo at SD 53, and Lynkk is already at 11.9 on it.

**What to do, in order:**
1. Rewrite the title to lead with location. Something like "Where to Find Your Google Meet Transcript
   (and How to Download It)". The current page is almost certainly titled around "how to get", which
   is not what most of these people are typing.
2. Put the literal answer in the first 40 words: the Drive folder path, named exactly. These
   searchers want a file path, and a snippet that contains it will get the click.
3. Add an H2 for each distinct sub-intent that currently has its own query: where it is saved, how
   to download from a recording, why it is missing, how to access it as a non-organiser, the Gemini
   variant.
4. Add FAQ schema using the exact query strings above as the questions.

**Realistic prize:** 451 top-10 impressions at a normal 3% CTR is roughly 13 clicks per quarter from
the export's visible slice alone. Applied to the full page (6,277 impressions at position 10),
moving from 0.13% to a normal 2.5% is roughly **150 clicks per quarter from one title rewrite.**

### F2. Zoom note taker: 868 cluster impressions, position 16 to 18, zero clicks

`zoom note taker` is **880/mo at SD 31** and Lynkk sits at position 16.8. `ai zoom note taker` is
210/mo at SD 25. `zoom note taker ai` 70/mo SD 29. `zoom note taker app` 40/mo SD 24.

| Impressions | Position | Query | Ubersuggest |
|---|---|---|---|
| 84 | 16.8 | zoom note taker | 880/mo, SD 31 |
| 44 | 17.8 | zoom notes taker | same cluster |
| 57 | 54.7 | zoom ai notetaker | needs more than a snippet fix |
| 46 | 49.4 | zoom ai note taker | 390/mo, SD 33 |

Two pages compete here: `/blog/zoom-note-taker` (1,134 impressions, position 28.2) and
`/articles/zoom-note-taker` (469 impressions, position 27.1). **That is a live duplicate.** Having
two URLs on the same slug for the same intent is the most likely reason neither breaks page one.

**What to do:** pick one, 301 the other to it, consolidate the content, then target `ai zoom note
taker` (SD 25) in an H2 since it is the easier variant. This is a medium-competition term at 880/mo
where you are already on page two. Fixing the duplicate is a one-hour job with a real chance of
page one.

### F3. iPhone voice memo transcription: 144 impressions in the top 14, zero clicks

21 variants, all positions 7.8 to 13.8, zero clicks. The page is `/blog/voice-memo-transcription`
(2,179 impressions, position 10.9, 3 clicks, 0.14% CTR). `voice memo transcription iphone` is
170/mo at SD 41.

| Impressions | Position | Query |
|---|---|---|
| 26 | 9.3 | voice memo transcription iphone |
| 20 | 11.6 | iphone voice memo transcription |
| 11 | 10.4 | does voice memos transcribe |
| 6 | 9.7 | can iphone voice memos be transcribed |
| 6 | 10.0 | apple voice memos transcription |
| 6 | 10.8 | how to get transcript from apple voice memo |
| 5 | 7.8 | can you get a transcript from voice memos on iphone |
| 5 | 8.4 | ios voice memo transcription |
| 5 | 10.8 | how to transcribe a voice memo on iphone |

**Read the pattern:** a large share are **yes/no questions**: *does voice memos transcribe*, *can
iphone voice memos be transcribed*, *can you get a transcript*, *can voice memo transcribe*. Five
separate yes/no variants. The page is almost certainly written as a how-to and never answers the
yes/no question in the first line, so the snippet does not match the query.

**What to do:** open with a direct one-line answer ("Yes, since iOS 18 Voice Memos transcribes
automatically. Here is where to find the text."), add "iPhone" and "Apple" to the title, and add a
yes/no FAQ block.

### F4. Action items: 78 impressions in the top 20, zero clicks, and a much larger problem behind it

The cluster is 57 queries and 1,051 impressions, but the weighted position is 44. Only four queries
are inside the top 20:

| Impressions | Position | Query | Ubersuggest |
|---|---|---|---|
| 35 | 10.1 | action items example | 110/mo, SD 37 |
| 24 | 8.2 | recent messages notes action items | n/a |
| 11 | 7.0 | action list examples | n/a |
| 8 | 7.2 | open action items | n/a |

The rest of the cluster (`action items template` 96 impressions at position 32.6, `action items` 87
at 41.8, `meeting action items` 80 at 45.1, `action item lists` 55 at 51.3) sits too deep to be a
snippet fix. The page is `/blog/action-items-examples-template` at 1,717 impressions and position
29.9.

**What to do:** the snippet fix is only worth it for `action items example` at position 10. The
bigger issue is that a 1,717-impression page averages position 30, which means a content upgrade,
not a title tweak. Treat it as a Tier 2 job, below F1 and F2.

### F5. Hinglish and Hindi: 49 of 57 cluster impressions are already in the top 10

Smallest cluster here but the best average position on the whole site: weighted position **9.5**.
`hinglish transcribe` is 18 impressions at position 8.6 with zero clicks. `/blog/hindi-transcription`
is at position 8.15 with 371 impressions and zero clicks, and `/features/hinglish-transcription` is
at position 37 with 297 impressions and 5 clicks.

This is the cluster where Lynkk ranks best and the market (India, 2.97% CTR, 65 of your clicks) is
strongest. It earns nothing because the snippets are not being clicked. A title and meta rewrite
here is low effort against your best-converting geography.

### F6. The "ai agenda templates for board meetings" outlier

28 impressions at **position 5.8**, zero clicks. Also `standup agenda` at 8.8, `action list examples`
at 7.0, `open action items` at 7.2, `meeting preparation` at 8.7 (19 impressions). These are single
queries sitting in the top 10 on pages that rank badly overall, so they are pure snippet wins. Group
them into one batch of meta rewrites across `/blog/board-meeting-agenda`, `/blog/daily-standup-meeting`
and `/blog/meeting-preparation`.

---

## Tier 2: Page two, real volume, worth a content push

Position 11 to 20 with zero clicks: 137 queries, 1,308 impressions. The ones backed by Ubersuggest
volume:

| Impressions | Position | Query | Volume | SD | Existing page |
|---|---|---|---|---|---|
| 84 | 16.8 | zoom note taker | 880 | 31 | duplicate, see F2 |
| 53 | 13.8 | fathom pricing | 53 | 14 | `/blog/fathom-ai-pricing` |
| 43 | 12.9 | granola pricing | n/a | n/a | `/blog/granola-ai-pricing` |
| 53 | 15.5 | zoom bot start meeting | n/a | n/a | `/blog/zoom-bot-join-meeting` |
| 53 | 18.5 | how to send a meeting bot to a meeting | n/a | n/a | `/features/meeting-bot` |
| 40 | 18.2 | medical transcribing software | n/a | n/a | `/blog/medical-transcription-software` |
| 29 | 16.2 | stand up meeting agenda | n/a | n/a | `/blog/daily-standup-meeting` |
| 26 | 19.1 | join google meet call bot | n/a | n/a | `/features/meeting-bot` |
| 25 | 17.7 | zoom bot | n/a | n/a | `/blog/zoom-bot-join-meeting` |
| 23 | 19.9 | best meeting bot api | 40 | 27 | none |
| 18 | 13.6 | daily standup meeting agenda | n/a | n/a | `/blog/daily-standup-meeting` |
| 17 | 13.0 | zoom bot sign in required | n/a | n/a | none |
| 16 | 16.8 | zoom bot for teams | n/a | n/a | none |

Three groupings worth acting on:

**T1. The competitor pricing pages are the closest thing to free traffic.** `fathom pricing` is
SD 14 at position 13.8, `granola pricing` at 12.9, `gong pricing` 54 impressions at 22.4, `otter ai
pricing` at 27.4, `fireflies pricing` at 11.0. These are low-difficulty, high-intent, and you
already have a page for every one of them. Refresh the pricing tables with current 2026 numbers and
a "last updated" date. Pricing pages live or die on freshness signals, and a dated page loses to a
fresher one at identical authority.

**T2. The "zoom bot" cluster is fragmented across three URLs.** 507 cluster impressions at weighted
position 19.6 with one click. `zoom bot start meeting` (53), `zoom bot` (25), `zoom bot sign in
required` (17), `zoom bot for teams` (16), `join zoom call bot` (150 at position 22.7), `zoom
connector bot` (70 at 24.3), `how to send a meeting bot to a meeting` (53 at 18.5), `how to build a
zoom bot` (13 at 18.9), `how to build a zoom notetaker` (11 at 17.7). Right now
`/blog/zoom-bot-join-meeting` and `/features/meeting-bot` split this. Note the developer intent in
`how to build a zoom bot`, `best meeting bot api` (40/mo, SD 27) and `how to make a meeting bot`
(42 impressions at 23.6). That is a distinct audience with no page at all, and `meeting bot api`
carries a $30.60 CPC.

**T3. The standup agenda cluster is one page away from page one.** `stand up meeting agenda` (29 at
16.2), `daily standup meeting agenda` (18 at 13.6), `standup agenda` (8 at 8.8), `stand up meeting
format` (54 at 29.0), `what to say in stand up meeting examples` (4 at 26.3, and it took a click).
All point at `/blog/daily-standup-meeting` at position 26.6. Add an agenda template section with a
copyable block, because every query in this group wants a template.

---

## Tier 3: Low competition queries with no page at all

New content, but the smallest and easiest kind. All verified in Ubersuggest at SD under 30.

| Keyword | Volume | SD | CPC | Note |
|---|---|---|---|---|
| does zoom have an ai note taker | 140 | **16** | $5.64 | yes/no explainer, no page |
| does microsoft teams have an ai note taker | 170 | 29 | $17.23 | no page |
| does teams have ai note taker | 50 | 30 | $6.95 | same cluster |
| does google meet have an ai note taker | 140 | 42 | $22.86 | same cluster |
| how to turn on zoom note taker | 30 | **26** | n/a | no page |
| how to use zoom note taker | 30 | 43 | $12.83 | no page |
| how to add ai note taker to teams | 70 | 30 | $18.36 | no page |
| how to remove ai note taker from teams | 30 | 35 | n/a | no page, and nobody competes for it |
| google meet transcript api | 30 | **24** | n/a | matches GSC "google meet api get transcript", 44 impressions at 22.8 |
| meeting bot api | 40 | 27 | **$30.60** | matches GSC developer queries above |
| best meeting transcription software (question form) | 70 | n/a | n/a | `what is the best meeting transcription software` SD 46 |
| teams meeting transcript without recording | 40 | **25** | $4.91 | no page |
| how to get teams meeting transcript | 30 | 30 | n/a | no page |
| how to summarize teams meeting transcript | 30 | 30 | $5.59 | no page |
| open source ai note taker | 40 | 26 | $4.96 | no page |
| webex ai note taker | 40 | 24 | $8.14 | no page |
| grain ai note taker | 50 | 21 | $4.61 | no page |
| ai note taker for students | 70 | 20 | $7.36 | no page |
| lecture ai note taker | 140 | 23 | $10.27 | use-case page only |
| ai note taker for lectures | 110 | 25 | $9.71 | use-case page only |
| notion meeting transcription | 50 | 20 | $7.99 | no page |
| meeting transcription tool | 50 | 23 | $18.53 | no page |
| teams meeting transcription | 390 | **22** | $16.73 | no page |
| best ai note taker for microsoft teams | 50 | 21 | $29.32 | existing page not optimised for it |
| copilot meeting transcription | 50 | 26 | $3.47 | no page |

**The single best Tier 3 move:** bundle the five "does X have an AI note taker" queries (zoom 140 at
SD 16, teams 170 at SD 29, teams variant 50, meet 140, plus `is there an ai note taker for teams`
30 at SD 25) into **one** comparison post of native tools vs standalone, roughly 530/mo combined at
SD 16 to 42. One page, five query clusters, and it sets up the Copilot and Zoom AI Companion
arguments from the main plan.

**Cannibalization check on Tier 3:** `does zoom have an ai note taker` and the Zoom how-tos must not
reuse "zoom note taker" phrasing, which belongs to F2's consolidated page. Keep the native-feature
post on "does X have" and "how to turn on" phrasing only. The Teams transcript items (SD 22 to 30)
are the same cluster as A3 in the main plan, so build them as one post, not several.

---

## What I would actually do, in order

Ranked by return per hour, not by cluster size.

1. **Rewrite the title and opening paragraph of `/blog/google-meet-transcript`** to lead with
   *where* the transcript is saved. One page, 6,277 impressions, position 10, 0.13% CTR. Largest
   single prize on the site and it needs no new content. (F1)
2. **Resolve the `/blog/zoom-note-taker` vs `/articles/zoom-note-taker` duplicate.** 880/mo at
   SD 31, currently page two with two competing URLs. (F2)
3. **Batch-rewrite titles and metas for the top-10, zero-click pages**: voice memo transcription,
   hindi transcription, board meeting agenda, meeting preparation, action items example. Five
   rewrites, roughly 900 impressions of already-earned page-one visibility. (F3, F5, F6)
4. **Refresh the five competitor pricing pages** with 2026 numbers and visible update dates.
   Lowest-difficulty, highest-intent terms you already rank for. (T1)
5. **Consolidate the zoom bot cluster** and add the developer-intent section (`meeting bot api`,
   $30.60 CPC, SD 27). (T2)
6. **Add an agenda template block** to `/blog/daily-standup-meeting`. (T3)
7. **Then** publish the one new Tier 3 post: "Does Zoom, Teams or Google Meet have a built-in AI
   note taker?" (about 530/mo combined, SD 16 to 42)

Steps 1 through 6 are edits to pages that already exist. On this account, where 270 top-10 queries
return zero clicks, those are worth more than the next ten blog posts.
