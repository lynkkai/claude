# Lynkk.ai: Keyword Research, Blog Plan and AI Visibility Plan

Prepared 2026-11-03. Sources: Google Search Console export (last 3 months, web, text), Ubersuggest
(keyword metrics, US locId 2840; AI Search Visibility for project `lynkk.ai`), and a crawl of the
lynkk.ai sitemap (54 live blog posts, 11 feature pages, 12 compare pages, 10 use-case pages,
7 integration pages).

Note on scope: the brief asked for "15 blog topics" and "10 blog topics". I have read that as two
separate sets, because they serve two different engines. Set A (15) is built from Ubersuggest
volume and difficulty for classic Google rankings. Set B (10) is built from answer-engine demand,
where Google volume is near zero but the buying intent is highest. All 25 are deduplicated against
the existing 54 posts and against each other.

---

## 1. Where lynkk.ai stands today

### GSC, last 3 months

| Metric | Value |
|---|---|
| Clicks | 152 |
| Impressions | 28,051 |
| CTR | 0.54% |
| Average position | 22.3 |

The shape of the account matters more than the totals:

- **Brand is converting, non-brand is not.** `lynkk` alone is 52 of 152 clicks (34%) at position 2.2.
  Strip brand and the whole site earned roughly 100 non-brand clicks in 90 days.
- **India drives clicks, the US drives impressions.** India: 65 clicks from 2,192 impressions
  (2.97% CTR, avg position 13.2). United States: 11 clicks from 13,966 impressions (0.08% CTR,
  avg position 30.2). Half the site's impressions come from a market where it ranks on page 3.
- **Two pages carry the impression load but convert at near zero.**
  `/blog/google-meet-transcript` has 6,277 impressions at position 10.03 and 8 clicks (0.13% CTR).
  `/blog/voice-memo-transcription` has 2,179 impressions at position 10.9 and 3 clicks.
  `/blog/voice-to-text-apps` has 2,001 impressions at position 35.5 and 2 clicks. Position 10 with
  a 0.13% CTR is a title and snippet problem, not a ranking problem, and it is the single cheapest
  fix on the site.
- **Desktop and mobile are split.** Desktop: 22,403 impressions at position 23.8. Mobile: 5,506
  impressions at position 16.0. Mobile ranks better and converts better (0.62% vs 0.52%).
- **AI-style conversational queries are already working.** 165 of the top 1,000 queries are eight
  words or longer, and Lynkk ranks in the top 10 for most of them. Examples below. This is the most
  valuable signal in the whole export and section 3 is built on it.

### Ubersuggest AI Search Visibility, project `lynkk.ai`

| Metric | Value |
|---|---|
| Lynkk visibility | **0%** |
| Lynkk total mentions | **0** across 10 tracked prompts |
| Lynkk share of voice | **0%** |
| Competing brands detected | 30 |

Leaders on the same 10 prompts: Fireflies.ai 50% visibility (avg rank 1.8), Otter.ai 30% (2.67),
Notta 30% (4.0), Fathom 20% (2.5), Avoma 20% (2.5).

So there are two different problems, and they need different fixes:

1. **Google already finds Lynkk credible on long conversational queries** (positions 2 to 6 on
   prompts about CRM gaps, SSO rollouts, transcript retention, source-linked answers).
2. **ChatGPT does not mention Lynkk at all**, because ChatGPT answers these questions by citing
   third-party listicles, and Lynkk is on none of them. The 14 cited pages Ubersuggest found all
   name Fathom, Fireflies, Otter or Avoma and none name Lynkk. Highest-value targets by domain
   rating: notta.ai (DR 51, 33% of missed answers), help.fathom.video (DR 47), spotsaas.com (DR 41),
   dupple.com (DR 32, 2 pages), cleverly.co (DR 30), knowledgesense.in (DR 15, the India listicle).

---

## 2. Medium and low competition keyword pool

Ubersuggest SD (search difficulty, 0 to 100) is the competition measure. I treated SD 0 to 29 as
low and SD 30 to 45 as medium, and discarded anything above 45 unless Lynkk already ranks for it.
Volumes are US monthly.

### Low competition (SD under 30)

| Keyword | Volume | SD | CPC | Note |
|---|---|---|---|---|
| teams meeting transcription | 390 | 22 | $16.73 | no page |
| microsoft teams meeting transcription | 390 | 30 | $16.32 | no page |
| teams meeting transcript without recording | 40 | 25 | $4.91 | no page |
| best ai note taker for microsoft teams | 50 | 21 | $29.32 | existing post, not optimised for this |
| ai note taker for microsoft teams | 110 | 26 | $17.02 | existing post |
| ms teams ai note taker | 90 | 26 | $19.70 | existing post |
| microsoft teams ai note taker | 590 | 26 | $13.73 | existing post, pos 23.4 in GSC |
| open source ai note taker | 40 | 26 | $4.96 | no page |
| copilot meeting transcription | 50 | 26 | $3.47 | no page |
| notion meeting transcription | 50 | 20 | $7.99 | no page |
| notion meeting notes ai | 50 | 31 | $21.17 | no page |
| webex ai note taker | 40 | 24 | $8.14 | no page |
| ai note taker for lectures | 110 | 25 | $9.71 | use-case page only |
| lecture ai note taker | 140 | 23 | $10.27 | use-case page only |
| ai note taker for students | 70 | 20 | $7.36 | no page |
| grain ai note taker | 50 | 21 | $4.61 | no page |
| read ai note taker | 50 | 22 | $4.10 | compare page exists |
| meeting transcription tool | 50 | 23 | $18.53 | no page |
| teams meeting transcription without recording | 90 | 30 | $2.96 | no page |
| does zoom have an ai note taker | 140 | 16 | $5.64 | no page |
| best ai note taker for google meet | 40 | 16 | $25.32 | existing post ranks pos 5.7 |
| best ai note taker for zoom | 40 | 12 | $31.27 | existing post |
| does microsoft teams have an ai note taker | 170 | 29 | $17.23 | no page |
| how to summarize teams meeting transcript with copilot | 40 | 29 | n/a | no page |
| microsoft copilot meeting notes | 50 | 30 | $6.33 | no page |

### Medium competition (SD 30 to 45)

| Keyword | Volume | SD | CPC | Note |
|---|---|---|---|---|
| ai note taker for in person meetings | 480 | 40 | $14.62 | **no page, core differentiator** |
| best ai note taker for in person meetings | 110 | 65 | $9.06 | same cluster, harder head term |
| in person meeting ai note taker | 90 | 44 | $22.39 | same cluster |
| in person ai note taker | 50 | 52 | $14.75 | same cluster |
| ai note taker that doesn't join meetings | 90 | 30 | $21.61 | **no page, core differentiator** |
| wearable ai note taker | 720 | 34 | $6.59 | adjacent to existing ai-voice-recorders post |
| ai note taker device | 590 | 30 | $7.60 | adjacent to existing ai-voice-recorders post |
| hipaa compliant ai note taker | 260 | 31 | $31.04 | **no page, highest CPC cluster** |
| ai note taker for therapists | 90 | 35 | $50.63 | same cluster |
| hipaa compliant ai note taker for therapists | 40 | 40 | $56.87 | same cluster |
| therapy ai note taker | 30 | 52 | $40.10 | same cluster |
| ai note taker for phone calls | 140 | 65 | $19.58 | head term is hard |
| best ai note taker for phone calls | 70 | 34 | $10.34 | **use this as the entry point** |
| notion ai note taker | 140 | 41 | $12.36 | no page |
| microsoft teams meeting transcript | 320 | 41 | $6.84 | no page |
| teams meeting transcript | 390 | 38 | $5.30 | no page |
| best wearable ai note taker | 70 | 31 | $9.48 | adjacent to existing post |
| slack ai note taker | 30 | 44 | $17.77 | /slack page only, no blog |
| meeting bot api | 40 | 27 | $30.60 | feature page only |
| google meet ai note taker free | 90 | 30 | $16.09 | existing post |
| zoom ai note taker free | 40 | 26 | $22.14 | existing post |
| local ai note taker | 20 | 34 | $4.26 | no page |

### What the pool rules out

These look attractive but are head terms where Lynkk cannot win yet on a domain with 152 clicks per
quarter. Do not build new posts for them: `ai note taker` (27,100, SD 48), `ai meeting assistant`
(4,400, SD 60), `meeting transcription` (480, SD 62), `best meeting transcription software` (70,
SD 50), `ai note taker online` (50, SD 75), `best meeting notes ai` (30, SD 81).

---

## 3. Set A: 15 blog topics from keyword research

Every row names the existing pages it sits next to and how the overlap is handled, because the
brief was explicit about not creating cannibalization. Cluster volume is the sum of the keyword
variants the post would target.

### A1. AI note taker for in-person meetings: what actually works without a laptop in the room

- **Primary:** ai note taker for in person meetings (480, SD 40)
- **Supporting:** in person meeting ai note taker (90), in person ai note taker (50), free ai note
  taker for in person meetings (50), in person meeting notes ai (30), best free ai note taker for
  in person meetings (20)
- **Cluster volume:** about 760/mo. **Competition:** medium.
- **Why it is first:** this is the largest unclaimed cluster on the entire map and it is Lynkk's own
  positioning ("record any conversation, online or in person"). There is no page on lynkk.ai that
  targets it. Competitors answer it with hardware.
- **Cannibalization:** none. `/blog/ai-voice-recorders` answers "which device should I buy", this
  answers "how do I get structured notes from a room". Link A1 to it and to `/use-cases/field-interviews`.

### A2. AI note takers that do not join your meeting: bot-free capture compared

- **Primary:** ai note taker that doesn't join meetings (90, SD 30)
- **Supporting:** bot free ai note taker (110, SD 59), ai note taker without joining meeting (30),
  bot free ai meeting assistant (40), teams meeting transcription without recording (90, SD 30),
  ai notetaker no meeting bot
- **Cluster volume:** about 360/mo. **Competition:** low to medium.
- **Why:** "a bot joined our call" is the single most common objection in this category, and the
  desktop-capture answer is Lynkk's. Also feeds the AI prompt "which ai notetakers let admins
  enforce a recording notice for everyone on the call without a bot joining" (GSC position 5).
- **Cannibalization:** watch `/features/meeting-bot` (812 impressions, position 22.7). That page
  sells the bot. This post must be framed as "when you want a bot and when you do not", linking
  to the feature page for the bot path. Do not let both chase "meeting bot".

### A3. Microsoft Teams meeting transcript: how to find it, download it and summarize it

- **Primary:** teams meeting transcript (390, SD 38), microsoft teams meeting transcript (320, SD 41)
- **Supporting:** teams meeting transcription (390, SD 22), microsoft teams meeting transcription
  (390, SD 30), how to get teams meeting transcript without recording (40), download teams meeting
  transcript (30), how to summarize teams meeting transcript (30), where to find teams meeting
  transcription, teams meeting transcript location
- **Cluster volume:** about 1,250/mo. **Competition:** low to medium.
- **Why:** `/blog/google-meet-transcript` proves the model works: 6,277 impressions at position 10
  from exactly this intent on the other platform. Teams is the missing leg, and the Teams variants
  carry lower SD than the Google Meet ones did.
- **Cannibalization:** none on transcripts. `/blog/ai-note-taker-microsoft-teams` targets "note
  taker" (tool choice), this targets "transcript" (task completion). Keep the Teams note-taker post
  off transcript phrasing and cross-link.
- **Also fix while you are here:** `/blog/google-meet-transcript` has 6,277 impressions and a 0.13%
  CTR at position 10. Rewrite the title and meta before publishing A3 and apply what works to both.

### A4. HIPAA-compliant AI note takers for therapists and clinicians

- **Primary:** hipaa compliant ai note taker (260, SD 31, CPC $31.04)
- **Supporting:** ai note taker for therapists (90, SD 35, CPC $50.63), hipaa compliant ai note
  taker for therapists (40, SD 40, CPC $56.87), therapy ai note taker (30), simple practice ai note
  taker (390, SD 15)
- **Cluster volume:** about 810/mo. **Competition:** medium. **Highest commercial value on the map**
  at $31 to $57 CPC.
- **Why:** data residency is a Lynkk feature and this is the audience that pays for it. Also feeds
  the GSC query "what is the best ai tool for healthcare transcription?" (position 53 today).
- **Cannibalization:** `/blog/medical-transcription-software` exists at position 34.4 with 576
  impressions and 0 clicks. That post is about transcription services and software. A4 is about
  compliance and clinical note-taking for a solo or small practice. The split is real, but the two
  must be edited together: push medical-transcription-software toward "transcription services" and
  keep every HIPAA and therapist phrase in A4 only.

### A5. Microsoft Copilot in Teams vs a standalone AI notetaker

- **Primary:** microsoft copilot meeting notes (50, SD 30), copilot meeting transcription (50, SD 26)
- **Supporting:** how to summarize teams meeting transcript with copilot (40, SD 29), copilot ai
  note taker (40, SD 43), teams meeting transcription copilot, meeting transcription with copilot
- **Cluster volume:** about 180/mo in Google, but see below. **Competition:** low.
- **Why the Google volume understates it:** GSC already shows this exact question driving real
  impressions at strong positions: "does microsoft copilot in teams give us enough retention,
  consent and audit control for meeting notes, or do regulated teams look at other notetakers?"
  (38 impressions, position 6.0) and "my team uses copilot in teams for meeting recaps but i also
  meet on zoom, google meet and in person. is it worth switching from copilot in teams to a separate
  notetaker?" (20 impressions, position 5.9). Lynkk has 12 compare pages and not one of them is
  Copilot, which is the largest default competitor in the category.
- **Cannibalization:** none. Recommend a `/compare/copilot` page as well, with A5 as the long-form
  version.

### A6. What an AI note taker actually costs per seat in 2026

- **Primary:** how much is ai note taker (20, SD 29), summary ai note taker cost (90, SD 30)
- **Supporting:** ai note taker comparison (20), what's the best value ai notetaker, cheap ai note
  taker (Lynkk already ranks position 81 and took a click)
- **Cluster volume:** low in Google, high in AI surfaces: "how much do ai notetakers typically cost
  for a 20-person product team?" (position 5.78), "how much does an ai meeting assistant cost for a
  10-person team" (position 10), "which ai notetaker is best for a growing company that will double
  headcount this year?" (position 4.25), "is gong worth renewing at $100 per user per month for a
  small team?" (position 8.0).
- **Why:** Lynkk has five single-vendor pricing posts (gong, fathom, otter, fireflies, granola) and
  no page that compares them. That is a missing hub, and hubs are what AI engines quote.
- **Cannibalization:** zero if built as a hub. It must link out to all five existing pricing posts
  and must not re-rank for "gong pricing" or "fathom pricing" style queries. Keep vendor names in
  table cells, not in H2s.

### A7. Meeting transcription without recording: transcript-only and privacy-first setups

- **Primary:** teams meeting transcription without recording (90, SD 30)
- **Supporting:** teams meeting transcript without recording (40, SD 25), how to get teams meeting
  transcript without recording (40, SD 32), meeting transcription without recording, teams meeting
  transcription privacy, teams meeting transcription retention
- **Cluster volume:** about 180/mo plus a long zero-volume tail. **Competition:** low.
- **Why:** pairs with the retention and audit-trail prompts where Lynkk already ranks position 4.05.
- **Cannibalization:** `/blog/is-it-legal-to-record-a-meeting` covers consent law. A7 covers the
  technical setup. Keep "legal", "consent" and "two-party" phrasing in the existing post.

### A8. Best AI note taker for phone and sales calls

- **Primary:** best ai note taker for phone calls (70, SD 34)
- **Supporting:** ai note taker for phone calls (140, SD 65), ai note taker for calls (30, SD 13),
  phone call ai note taker (30), ai note taker phone calls (20)
- **Cluster volume:** about 290/mo. **Competition:** medium on the entry term, high on the head term,
  so target the "best ... for" variant first.
- **Cannibalization:** `/use-cases/sales-calls` (204 impressions, position 50) is a product page.
  A8 is a comparison. Link down to the use case.

### A9. Meeting notes in Notion: transcripts, dictation and automatic syncing

- **Primary:** notion ai note taker (140, SD 41)
- **Supporting:** notion meeting notes ai (50, SD 31), notion meeting transcription (50, SD 20),
  notion ai meeting transcription, is notion meeting transcription free
- **Cluster volume:** about 240/mo. **Competition:** low to medium.
- **Why:** GSC already shows "what's the best dictation tool for someone who drafts documents and
  notes in notion every day?" at position 8.8, and Notion AI appears as a competing brand in the
  Ubersuggest knowledge-management prompt. Lynkk's Mac dictation (text at your cursor in any app)
  is the direct answer.
- **Cannibalization:** `/features/dictation` and `/blog/dictate-in-microsoft-word` exist. Keep A9 on
  Notion-specific phrasing only.

### A10. Open-source, local and on-device AI note takers

- **Primary:** open source ai note taker (40, SD 26)
- **Supporting:** local ai note taker (20, SD 34), on device meeting transcription, local meeting
  transcription mac, local llm meeting transcription, meeting transcription no wifi
- **Cluster volume:** about 70/mo in Google, large zero-volume tail. **Competition:** low.
- **Why:** small cluster, but it is the only cluster where "offline-first" is the literal search
  term, and the audience it attracts (privacy-driven, technical) is the one that writes the Reddit
  and GitHub mentions that AI engines cite.
- **Cannibalization:** none.

### A11. AI note taker for lectures, classes and students

- **Primary:** lecture ai note taker (140, SD 23)
- **Supporting:** ai note taker for lectures (110, SD 25), ai note taker for lecture (110, SD 28),
  ai note taker for students (70, SD 20), ai note taker lectures (70, SD 31), best ai note taker for
  lectures (30), ai note taker for class (40, SD 30), ai note taker for video lectures (20)
- **Cluster volume:** about 600/mo. **Competition:** low, the lowest SD per unit of volume on the map.
- **Honest caveat:** this is not Lynkk's buying audience. Include it as a traffic and link-earning
  play, not a conversion play, and do not put it ahead of A1 through A5.
- **Cannibalization:** `/use-cases/lectures` (47 impressions, position 25) is a product page, no blog
  exists. Fine.

### A12. AI note takers beyond Zoom, Meet and Teams: Webex, Slack, Discord and phone bridges

- **Primary:** webex ai note taker (40, SD 24)
- **Supporting:** slack ai note taker (30, SD 44), discord ai note taker (50, SD 30), ai note taker
  for discord (20, SD 27), webex meeting bot
- **Cluster volume:** about 140/mo. **Competition:** low.
- **Why:** cheap coverage of the platforms every competitor's comparison grid leaves blank, and it
  is a natural home for the "records any conversation" claim.
- **Cannibalization:** none. `/slack` is a product page, link to it.

### A13. AI note taker devices vs software: do you need the hardware?

- **Primary:** wearable ai note taker (720, SD 34), ai note taker device (590, SD 30)
- **Supporting:** ai note taker devices (320), best wearable ai note taker (70, SD 31), best ai note
  taker device (170), portable ai note taker (50), ai note taker necklace (30), ai note taker pen (110)
- **Cluster volume:** about 2,000/mo. **Competition:** medium. Largest raw volume in the pool.
- **Cannibalization warning, read this one:** `/blog/ai-voice-recorders` already exists and
  `/compare/plaud` already exists. This cluster will cannibalize them unless A13 is strictly a
  "device or app" decision post: the buying criteria, the battery and consent trade-offs, when a
  recorder genuinely wins. Every "best wearable recorder" style listicle phrase stays in
  ai-voice-recorders. If the team is not willing to police that split, drop A13 and instead expand
  ai-voice-recorders with a device-vs-app section. That is the lower-risk option and I would take it.

### A14. SSO, SCIM and admin controls: rolling out an AI notetaker to hundreds of seats

- **Google volume:** effectively zero. Ubersuggest returns no measurable volume for `ai notetaker sso`.
- **Real demand, from GSC:** "rolling out an ai notetaker to 300 reps: which plans include sso, scim
  and an admin dashboard?" (78 impressions, position 6.88), "which ai notetakers support saml sso
  with okta or microsoft entra id plus scim deprovisioning for leavers?" (6 impressions, position 9),
  "does a 40-person sales team really need sso for an ai notetaker, or is google login fine?"
  (6 impressions, position 7.5), "which ai notetakers let admins enforce a recording notice for
  everyone on the call ... roughly 300 employees" (9 impressions, position 5).
- **Competition:** none. No page on lynkk.ai mentions SSO or SCIM, and no competitor owns the topic.
- **Why include a zero-volume topic:** these are 300-seat buyers asking a procurement question in an
  AI assistant. One of these converts for more than a thousand lecture-note visitors. Treat the
  volume number as irrelevant and the position data as the proof of demand.

### A15. Who can see your meeting transcripts: subprocessors, LLM providers and data residency

- **Google volume:** effectively zero for `ai notetaker data residency`.
- **Real demand, from GSC:** "which third-party llm providers get to see prospect call transcripts
  that an ai notetaker processes?" (69 impressions, position 3.64), "looking for options besides zoom
  ai companion for regulated teams that need configurable transcript retention and an audit trail"
  (65 impressions, position 4.05), "does microsoft copilot in teams give us enough retention, consent
  and audit control" (38 impressions, position 6.0).
- **Competition:** none, and this is the hardest page for a competitor to copy, because answering it
  honestly requires naming your own subprocessors and regions.
- **Why:** region-pinned processing is Lynkk's stated differentiator and the site currently has only
  a `/security` page (22 impressions) to carry it. Publish the subprocessor and region table, because
  AI engines quote tables.

### Set A priority order

Publish in this order, which is impact over effort rather than cluster size:

1. A1 in-person (largest unclaimed on-brand cluster)
2. A3 Teams transcript (proven model from Google Meet, lowest SD per unit volume)
3. A2 bot-free (strongest objection handler)
4. A5 Copilot (largest unaddressed competitor)
5. A4 HIPAA and therapists (highest CPC)
6. A15 data residency, 7. A6 cost per seat, 8. A14 SSO and SCIM, 9. A7 no-recording,
10. A9 Notion, 11. A8 phone calls, 12. A12 other platforms, 13. A10 open source,
14. A11 lectures, 15. A13 devices (only with the split policed, otherwise drop)

---

## 4. Set B: 10 blog topics built for AI visibility

These exist because Lynkk is at 0% visibility and 0 mentions in ChatGPT answers while sitting at
positions 2 to 6 for the same questions in Google. The 14 pages ChatGPT cited all name Fathom,
Fireflies, Otter or Avoma. Set B is written in the shape those answers quote from: a direct answer
in the first 60 words, a comparison table with named tools and real numbers, explicit criteria, a
dated "last updated", and FAQ schema. Google volume is low or zero for most of them, which is the
point.

| # | Topic | Demand evidence | Competition | Overlap handling |
|---|---|---|---|---|
| B1 | Best AI meeting notetakers for Indian startups, with INR pricing | Ubersuggest prompt where Lynkk scores 0 and knowledgesense.in (DR 15) is cited instead; India is 43% of Lynkk clicks | Low. The cited page has DR 15 and is beatable | New. No India page exists on lynkk.ai |
| B2 | AI notetakers with Hindi and regional language support, including code-switched Hinglish | Ubersuggest Hindi prompt (Otter and Stenoji cited, Lynkk absent); GSC "which ai service converts spoken hindi into written text" position 9.8, "best voice to text app for multilingual ... english and spanish" position 9.25 | Low | **Risk.** `/blog/hindi-transcription` (371 impressions, position 8.15) and `/features/hinglish-transcription` exist. B2 must be a multi-tool comparison listicle, never a how-to. Keep all "how to transcribe Hindi" phrasing in the existing post |
| B3 | Enterprise-grade vs individual AI notetakers: SSO, SCIM, audit logs and admin controls compared | GSC "which popular ai notetakers are genuinely enterprise-grade, and which are really built for individuals?" position 2.6; "which ai notetakers can individual employees start using without a company-wide it rollout?" position 1 | None | Pairs with A14. A14 is the how-to for a buyer, B3 is the tool-by-tool grid. Different H1s, cross-link |
| B4 | Which AI notetakers give source-linked answers across every past meeting | GSC "which notetakers offer searchable meeting history with source-linked answers?" 60 impressions at position 3.32; "which ai meeting tools let me ask questions across all my past calls and show where each answer came from?" position 9.21 | None | `/features/knowledge-graph` and `/features/ask-your-meetings` are product pages. B4 compares tools |
| B5 | AI notetakers that work with MCP-compatible assistants | GSC "which ai notetakers work with mcp-compatible assistants so i can ask questions about my past customer calls? we're a 20-person startup" position 2.5 | Essentially none. Almost nobody has written this | New. MCP is in Lynkk's integration list and on no page's title |
| B6 | AI notetakers that cover online calls and in-person conversations in one tool | GSC "which zoom ai companion alternatives also cover google meet calls and in-person interviews?" 40 impressions at position 8.68; "alternatives to zoom ai companion for sales reps who also take customer calls on teams and google meet" position 8.57 | Low | **Risk.** `/blog/zoom-ai-companion-alternatives` (364 impressions, position 6.26) is close. Safer alternative: expand that existing post with an in-person column rather than publish B6. Decide before writing |
| B7 | Alternatives to the OpenAI and ChatGPT note taker | GSC "which alternatives to the openai note-taker work best for zoom, google meet and teams meetings where i want notes organized by project?" 26 impressions at position 4.38; "best alternatives to the openai note-taker for a founder who wants searchable notes across all of their meetings" position 1 | Low, and the query is new enough that few have covered it | New. Lynkk has 12 compare pages, none for OpenAI |
| B8 | Closing the CRM gap: notetakers that write back to your CRM, not just summarize | GSC "zoom ai companion gives us summaries but nothing in our crm. what other tools could close that gap for reps?" **102 impressions at position 3, the single highest-impression prompt query in the export** | Low | `/blog/sales-conversation-intelligence` and `/integrations/salesforce` exist. B8 is specifically "summary vs CRM write-back", a narrower claim |
| B9 | Rollout and volume pricing: starting with the leadership team, then the whole company | GSC "do ai notetakers offer volume discounts if we start with just the leadership team and roll it out company-wide later?" 44 impressions at position 5.16; "what's the best value ai notetaker for a company watching software spend?" position 4 | None | Pairs with A6. A6 is list price per seat, B9 is discounting and expansion mechanics |
| B10 | AI notetakers that can summarize an all-hands or town hall for people who missed it | GSC "which ai notetakers can summarize a company all-hands or town hall for people who couldn't attend?" position 3.5; "which ai notetakers work well for team retrospectives when i'm also the one facilitating?" position 1 | None. Ubersuggest returns no measurable volume for "all hands meeting summary", so this is AI-surface only | New. `/use-cases/team-standups` and `/blog/daily-standup-meeting` cover standups, not all-hands |

Two things to do alongside Set B, because content alone will not move a 0% ChatGPT visibility score:

1. **Get Lynkk onto the listicles that are already being cited.** Priority order by domain rating and
   citation share: notta.ai (DR 51, cited in 33% of missed answers), help.fathom.video (DR 47),
   spotsaas.com (DR 41), dupple.com (DR 32, two cited pages), cleverly.co (DR 30),
   knowledgesense.in (DR 15, the India listicle, easiest win). Eleven of the fourteen cited pages
   have DR under 35, so most are reachable with a straightforward outreach or submission.
2. **Add Lynkk as a tracked brand in Ubersuggest.** It currently shows `is_user_brand: true` but
   `is_tracked: false`, which is why there is no rank history to improve against.

---

## 5. Five prompts to target for AI visibility

All 10 prompt slots in the Ubersuggest brand are used, and all 10 currently return 0 Lynkk mentions,
mostly because they ask generic "best/cheapest in India" questions that incumbents own on authority
alone. These five replace the weakest of those. Each one is chosen on three tests: proven demand in
GSC, a differentiator a competitor cannot claim back quickly, and an answer that only Lynkk's own
page can satisfy fully.

**P1. "Which AI notetakers can answer questions across all my past meetings and show which meeting
each answer came from?"**
- Demand: 60 impressions at position 3.32, plus a second variant at position 9.21.
- Why Lynkk wins it: knowledge graph plus source-linked answers across every meeting. Fireflies and
  Otter return search results, not cited answers.
- Supporting page: B4, then `/features/knowledge-graph` and `/features/ask-your-meetings`.

**P2. "Which AI notetakers record in-person conversations as well as online calls, in one tool?"**
- Demand: 40 impressions at position 8.68 and 21 at position 8.57 on the Zoom AI Companion variants.
- Why Lynkk wins it: records online meetings and in-person conversations, offline-first, Mac app.
  The incumbents are all meeting-bot-only, so the honest answer excludes them.
- Supporting page: A1, then B6 or the expanded Zoom AI Companion post.

**P3. "Which AI notetaker lets me choose the region where meeting transcripts are processed, and who
are its subprocessors?"**
- Demand: 69 impressions at position 3.64 on the LLM-provider variant, 65 at position 4.05 on the
  retention and audit-trail variant.
- Why Lynkk wins it: region-pinned processing, where every model behind Lynkk answers from the chosen
  region. Almost no competitor publishes this, so a page that does becomes the citable source.
- Supporting page: A15, then `/security`.

**P4. "Which AI notetaker writes action items straight into Jira and updates CRM fields, instead of
just producing a summary?"**
- Demand: the CRM-gap prompt is the highest-impression query in the whole export at 102 impressions,
  position 3. Plus "which tools integrate with jira to keep meeting notes and decisions searchable
  across teams?" at position 11 and "ai notetaker that sends action items after a call" at position 6.
- Why Lynkk wins it: Jira tickets, CRM field updates and assigned action items within about 30
  seconds of the call ending, which is a do-this-not-summarize-this claim.
- Supporting page: B8, then `/integrations/jira` and `/blog/meeting-minutes-to-jira`.

**P5. "Which AI notetakers work with MCP-compatible assistants like Claude so I can query my past
customer calls?"**
- Demand: position 2.5 already, on a query almost nobody has written for.
- Why Lynkk wins it: "connect anything via MCP" is in the product and in nothing a competitor
  markets. This is the cheapest first-mover prompt on the list, and it is the one most likely to be
  asked inside an AI assistant rather than in Google.
- Supporting page: B5.

Replace these five Ubersuggest prompts, which Lynkk cannot win on authority and which return
incumbents or unrelated project-management tools:
`Which automated action item tracking tool is best for project teams in India?` and
`What is the most cost-effective automated action item tracking software for Indian SMEs?` (both
return ClickUp, Zoho, Asana, Jira and Trello, a different category entirely),
`Which AI knowledge management tool is best suited for IT companies in India?` and
`What is the most affordable AI knowledge management platform for Indian mid-sized businesses?`
(both return Confluence, Glean, Notion and Guru), and
`Which conversation intelligence platform offers the best pricing for small businesses in India?`
(pure price query against Fireflies and Gong, unwinnable and low value).

Keep the three India-specific notetaker and transcription prompts. They map to Lynkk's strongest
market, and B1 and B2 are written to win them.

---

## 6. Cannibalization register

Four proposed topics sit close to something that already ranks. These are the only four that need a
decision before anyone writes:

| New topic | Existing page | Current GSC | Decision |
|---|---|---|---|
| A13 devices vs software | `/blog/ai-voice-recorders`, `/compare/plaud` | ai-voice-recorders not in top pages, so low traffic to protect | **Recommend dropping A13** and adding a device-vs-app section to ai-voice-recorders instead. The cluster is 2,000/mo but the overlap is near total |
| A4 HIPAA and therapists | `/blog/medical-transcription-software` | 576 impressions, position 34.4, 0 clicks | **Proceed.** Re-scope the existing post to transcription services and move every HIPAA, therapist and clinical phrase into A4 |
| B2 Hindi and regional language comparison | `/blog/hindi-transcription`, `/features/hinglish-transcription` | 371 impressions, position 8.15 | **Proceed with a hard split.** B2 is a tool comparison only. All how-to phrasing stays in hindi-transcription, which is already ranking well and must not be disturbed |
| B6 online plus in-person coverage | `/blog/zoom-ai-companion-alternatives` | 364 impressions, position 6.26 | **Recommend expanding the existing post** rather than publishing B6. It already ranks at position 6 for the parent intent. Adding an in-person column is lower risk and faster |

Everything else in Set A and Set B targets phrasing that no existing lynkk.ai page ranks for.

---

## 7. Three fixes worth more than any new post

Listing these because the data makes them hard to ignore, and they do not need a writer.

1. **Fix the titles on the three high-impression, no-click pages.** `/blog/google-meet-transcript`
   (6,277 impressions, position 10.03, 0.13% CTR), `/blog/voice-memo-transcription` (2,179,
   position 10.9, 0.14%), `/blog/voice-to-text-apps` (2,001, position 35.5, 0.10%). At position 10
   a normal CTR is roughly 2 to 3%. Google Meet transcript alone is leaving several hundred clicks a
   quarter on the table with no new content required.
2. **Decide what to do about the US.** 13,966 US impressions, 11 clicks, average position 30.2.
   Either commit to improving those rankings or accept that India is the market and weight the
   content calendar there. Right now the site is half-serving both.
3. **Track Lynkk as a brand in Ubersuggest.** `is_tracked` is false today, so there is no history to
   measure Set B against. Do this before publishing anything in Set B, so the before-and-after is
   real.
