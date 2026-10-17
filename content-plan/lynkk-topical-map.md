# Lynkk Content Plan v2: 35 Blogs + 20 Medium/Substack Posts (Audited)

Updated 2026-10-17. This version replaces v1 after two checks you asked for:

1. **Cannibalization:** I read the live title, H1 and every H2 of all 29 existing lynkk.ai blogs and compared them with each topic. For doubtful pairs I compared Google's top 10 for both queries (if 3 or more URLs are shared, Google treats them as one intent).
2. **Volume accuracy:** I checked the live SERP for every primary keyword to confirm the searcher actually wants what the post offers, and to see how strong the ranking sites really are.

Sources: Ubersuggest (volume, SD, SERP), Google Search Console export (last 3 months), live lynkk.ai pages.

## 1. How to read the volume numbers (important)

- **The volume belongs to one exact query, not to the blog title.** Example: for #3 the title is 'Meeting Summary Template: How to Write a Meeting Summary or Recap', but **480/mo is the volume of the exact query `template for meeting summary`**. Nobody searches the full title.
- **Cluster volume** = the separate volumes of the primary keyword plus the other keywords that post covers, added together. It is a rough ceiling, not a traffic forecast.
- **Ubersuggest volumes are estimates.** They come in Google's rounded buckets (390, 480, 590, 720, 880...), so read 480 as 'roughly 400-600'. They can be wrong in two ways I found in this audit:
  - **Wrong meaning:** 'granola alternative' shows 320/mo, but the SERP is 100% food. Removed.
  - **Shared brand name:** 'fathom pricing' shows 590/mo, but 2 of the top 3 results are other companies called Fathom. Kept, marked Low confidence.
  - **Navigational:** 'jamie ai note taker' (1,300) and 'krisp ai note taker' (1,300) are people trying to reach those tools (the brand site, app store and Reddit hold the top). Not used.
- **Real clicks are much lower than volume.** Position 1 gets roughly a quarter of searches, position 5 only a few percent, and AI Overviews take more.
- **Confidence** column: High = GSC impressions or a clean SERP confirm it; Medium = clean SERP, Ubersuggest volume only; Low = ambiguous meaning.
- **Real difficulty** comes from the live top 10, not just SD. Example: 'how to record google meet' has SD 25 but Google's own help pages hold about 6 of the top 10, so it is really High.

## 2. What changed from v1

| v1 topic | Decision | Why |
|---|---|---|
| Meeting Recap Email (v1 #4) | MERGED into #4 | The 'meeting recap email examples' SERP is full of follow-up email articles. One post covers both. |
| Meeting Minutes vs Meeting Notes (v1 #7) | MERGED into #5 | 'What are meeting minutes' shares 3 of 10 URLs with 'how to take meeting minutes', and /blog/meeting-minutes-to-jira already answers 'What are meeting minutes?'. |
| How to Get a Zoom Transcript (v1 #14) | DROPPED: cannibalizes | /blog/how-to-transcribe-zoom-meetings already has 'How do you get a Zoom transcript after the meeting?' and 'How do you download or save a Zoom transcript?'. |
| Can Copilot Take Meeting Notes (v1 #15) | DROPPED: cannibalizes | /blog/ai-note-taker-microsoft-teams already has 'Does Teams have an AI note taker?' and 'Can Copilot take meeting notes?'. |
| Zoom AI Companion Meeting Summary (v1 #16) | DROPPED: wrong SERP | Top 10 is Zoom support and university help docs; blogs barely rank. AI Companion is also covered in /blog/zoom-ai-companion-alternatives. |
| Google Meet Transcript Not Showing (v1 #17) | DROPPED: cannibalizes | /blog/google-meet-transcript already has 'Why is Google Meet transcription not working?' and 'Where are Google Meet transcripts saved?'. Fix that page's title and meta instead. |
| What Is a Meeting Bot (v1 #18) | DROPPED: cannibalizes | /blog/zoom-bot-join-meeting already has 'What is a meeting bot?' and 'How do you send a meeting bot to a meeting?', and /features/meeting-bot targets the same term. |
| Granola Alternatives (v1 #21) | REPLACED by #17 | 'granola alternative' (320/mo) is the food. Its SERP is all yogurt and recipes. Switched to 'granola ai alternatives' (210/mo). |
| Remove Read AI / Remove Otter (v1 #22, #23) | RESTRUCTURED as #26, #27, #28 | Brand removal queries kept separate per brand. Read AI removal joins 'what is read ai'. |
| Otter vs Fireflies vs Read AI (v1 #26) | REPLACED by #18 | Fathom comparisons have more volume (fathom vs fireflies 110, fathom vs otter 70). |
| AI Note Taker Cost for a 20-Person Team (v1 #27) | DROPPED: cannibalizes | 4 existing posts already have 'How much does ... cost for a 10-person team?' H2s, and the GSC question is likely landing on one of them. |
| Is Otter.ai Safe (v1 #29) | MERGED into #25 | Otter review pages rank in the 'is otter ai safe' SERP, so one post covers both. |
| Interview Transcription (v1 #33) | DROPPED: cannibalizes | /blog/recruiting-interview-transcription already covers 'What is interview transcription?', examples and how-to. |
| Hindi Audio to Text (v1 #34) | MOVED to a landing page | The SERP is 100% upload-a-file tools (ElevenLabs, Notta, HappyScribe) with no blogs. Build a 'Hindi audio to text' tool or landing page instead. |
| Multilingual Meeting Transcription (v1 #35) | DROPPED: cannibalizes | Would compete with the /features/multilingual-transcription service page. Optimize that page instead. |

New topics added after SERP checks: #6 LLC meeting minutes, #9 project kickoff agenda, #11 sprint planning agenda, #19 Granola vs Otter, #22 Read AI pricing, #23 Fathom pricing, #24 Granola pricing, #26 What is Read AI, #28 remove Fireflies, #29 ChatGPT meeting notes, #30 Notion AI meeting notes, #35 Hindi voice typing.

## 3. Fixes to make on existing pages first

1. **/blog/google-meet-transcript**: 1,181 impressions at position 9 with 0 clicks. Rewrite the title tag and meta description. This is the single biggest quick win.
2. **/blog/founders-meeting-notes**: reword the H2s 'What is the best way to take meeting notes?' and 'What should you include in meeting notes?' to founder angles, so new pillar #1 owns the generic query.
3. **/blog/meeting-minutes-to-jira**: shorten 'What are meeting minutes?' and 'Who takes meeting minutes?' to 2 lines each and link to #5.
4. **12 posts with an 'Is it legal to record...' H2**: keep each to 2-3 sentences and link to #31.
5. **Existing posts that may already compete with each other** (same tool lists): zoom-note-taker vs zoom-meeting-recorders vs zoom-ai-companion-alternatives; best-ai-note-takers vs ai-powered-meeting-assistants; transcribe-audio-to-text vs ai-transcription-software vs voice-to-text-apps. In GSC, open Performance > Queries, click a query, then the Pages tab. If two of these URLs show for the same query, differentiate their titles or merge them.
6. **/features/knowledge-graph** gets GSC clicks but is missing from the sitemap. **/articles/zoom-note-taker** should 301 to /blog/zoom-note-taker.
7. **New landing page (not a blog): 'Hindi audio to text'** (590/mo India, SD 17). The SERP is all upload tools, so a tool-style page under /features fits, not a blog.
8. **Optimize /features/multilingual-transcription** (GSC position 61) instead of writing a competing blog.

Full audit of all 29 existing posts: `existing-blog-audit.csv`.

## 4. The 35 website blogs

### C1. Meeting Notes & Follow-Up (4 posts)

**Who is searching:** Managers, team leads, EAs and PMs who get asked to take notes or send the recap.  
**Hub service pages:** /features/meeting-notes, /features/action-items

| # | Blog title | Primary keyword (exact query) | Vol/mo of that query | SD | Cluster vol (sum) | Real difficulty (SERP) | Time to page 1 | Overlap risk | Wave |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **How to Take Good Meeting Notes: 9 Steps, Examples & Free Template** (pillar) | `how to take good meeting notes` | 880 | 16 | 2,100 | Low-Med | 2-4 months | MEDIUM | 1 |
| 2 | Free Meeting Notes Template (Word, Google Docs & Notion) + How to Use It | `meeting notes template free` | 880 | 14 | 2,300 | Low | 1-3 months | LOW vs existing | 1 |
| 3 | Meeting Summary Template: How to Write a Meeting Summary or Recap (With Examples) | `template for meeting summary` | 480 | 9 | 1,080 | Low | 1-3 months | NONE vs existing | 1 |
| 4 | How to Write a Follow-Up Email After a Meeting (12 Examples + Recap Email Template) | `follow up email after meeting` | 210 | 26 | 950 | Low-Med | 2-3 months | LOW | 2 |

<details><summary>Keywords covered, SERP evidence, confidence, overlap and links</summary>

**#1 How to Take Good Meeting Notes: 9 Steps, Examples & Free Template**  
URL: `/blog/how-to-take-meeting-notes` | Intent: Informational | Volume confidence: Medium  
Other keywords covered: how to write meeting notes (880); how to type meeting notes (170); how to write meeting notes template (170)  
Live SERP: Weakest in top 10: mercedes-benz.io DA 35 (#10), karbonhq DA 42 (#9), meetgeek DA 44 (#6)  
Overlap: MEDIUM: /blog/founders-meeting-notes has H2s 'What is the best way to take meeting notes?' and 'What should you include in meeting notes?'. SERP for that phrase shares 2 of 10 URLs. Fix: reword those 2 H2s to founder-specific angles and link them to this post.  
Links: existing blogs founders-meeting-notes, meeting-preparation, action-items-examples-template; service pages /features/meeting-notes, /features/action-items, /how-it-works; new blogs #2, #3, #4, #5

**#2 Free Meeting Notes Template (Word, Google Docs & Notion) + How to Use It**  
URL: `/blog/meeting-notes-template` | Intent: Transactional (template download) | Volume confidence: Medium  
Other keywords covered: best meeting notes template (390); meeting notes template for word (390); meeting notes format template (320); notion meeting notes template (320)  
Live SERP: documentero DA 15 (#6), meetingnotes.com DA 38 (#3), fellow DA 46 (#7)  
Overlap: LOW vs existing. MEDIUM vs new #3: their SERPs share 3 of 10 URLs. Keep #2 = blank template to fill DURING the meeting; #3 = summary written AFTER.  
Links: existing blogs meeting-minutes-sample, one-on-one-meeting, daily-standup-meeting; service pages /features/meeting-notes, /features/workspaces; new blogs #1, #3, #8

**#3 Meeting Summary Template: How to Write a Meeting Summary or Recap (With Examples)**  
URL: `/blog/meeting-summary-template` | Intent: Informational / Transactional | Volume confidence: Medium  
Other keywords covered: template for meeting recap (390); how to write a meeting summary template (140); meeting summary example (70)  
Live SERP: booworkspace DA 10 (recap SERP), claap DA 37 (#2), virtuallatinos DA 37  
Overlap: NONE vs existing. Merged v1 'meeting recap template' in here: 'summary template' and 'recap template' SERPs share 3 URLs, so Google treats them as one intent.  
Links: existing blogs ai-powered-meeting-assistants, action-items-examples-template; service pages /features/meeting-notes, /features/ask-your-meetings; new blogs #1, #2, #4

**#4 How to Write a Follow-Up Email After a Meeting (12 Examples + Recap Email Template)**  
URL: `/blog/follow-up-email-after-meeting` | Intent: Informational | Volume confidence: Medium  
Other keywords covered: example of follow up email after meeting (210); follow up email after meeting example (170); how to write follow up email after meeting (110); meeting recap email examples (140); meeting recap email example (110)  
Live SERP: biscred DA 20 (#7), flownote DA 15 (recap SERP #6), fellow DA 46 (#3)  
Overlap: LOW: /blog/sales-conversation-intelligence has a 'sales call follow-up checklist' H2 only. Merged v1 'recap email' here: the recap-email SERP is full of follow-up-email articles.  
Links: existing blogs sales-conversation-intelligence, action-items-examples-template; service pages /features/action-items, /use-cases/sales-calls, /integrations; new blogs #3, #33, #34

</details>

### C2. Minutes, Agendas & Meeting Types (7 posts)

**Who is searching:** Company secretaries, small-business owners, board admins, founders, scrum masters, project managers.  
**Hub service pages:** /features/meeting-notes, /use-cases/team-standups

| # | Blog title | Primary keyword (exact query) | Vol/mo of that query | SD | Cluster vol (sum) | Real difficulty (SERP) | Time to page 1 | Overlap risk | Wave |
|---|---|---|---|---|---|---|---|---|---|
| 5 | **How to Take Meeting Minutes: Step-by-Step Guide (+ Minutes vs Notes)** (pillar) | `how to take meeting minutes` | 1,000 | 30 | 8,700 | Low-Med | 3-5 months | LOW vs /blog/meeting-minutes-sample | 2 |
| 6 | LLC Meeting Minutes Template: Annual and First Meeting (Free) | `llc meeting minutes template` | 480 | 22 | 480 | Low-Med | 2-4 months | LOW | 2 |
| 7 | Board Meeting Agenda: Free Template, Format and Sample | `board meeting agenda` | 1,300 | 14 | 5,500 | Low | 2-3 months | LOW | 1 |
| 8 | How to Write a Meeting Agenda: Free Template + Examples | `meeting agenda free template` | 1,300 | 15 | 3,650 | Medium (SD understates it) | 4-6 months | LOW | 3 |
| 9 | Project Kickoff Meeting Agenda: Template, Checklist and Example | `project kickoff meeting agenda` | 390 | 35 | 770 | Low-Med (SD overstates it) | 2-4 months | NONE | 2 |
| 10 | Sprint Retrospective: Template, Questions and Examples (+ Review vs Retro) | `sprint retrospective samples` | 480 | 20 | 1,030 | Low-Med | 2-4 months | NONE | 2 |
| 11 | Sprint Planning Meeting Agenda: Template and Checklist | `sprint planning meeting agenda` | 170 | 26 | 200 | Low | 1-3 months | NONE | 2 |

<details><summary>Keywords covered, SERP evidence, confidence, overlap and links</summary>

**#5 How to Take Meeting Minutes: Step-by-Step Guide (+ Minutes vs Notes)**  
URL: `/blog/how-to-take-meeting-minutes` | Intent: Informational | Volume confidence: Medium  
Other keywords covered: how to do meeting minutes (1,600); what are meeting minutes (2,400); meeting minutes meaning (1,300); meeting notes minutes (2,400)  
Live SERP: ibabs DA 38 (#5), polly DA 48 (#8), boardbook DA 51 (#4), trint DA 53 (#7)  
Overlap: LOW vs /blog/meeting-minutes-sample: its SERP shares 0 of 10 URLs. MEDIUM vs /blog/meeting-minutes-to-jira, which has H2s 'What are meeting minutes?' and 'Who takes meeting minutes?'. Fix: cut those to 2 lines and link here. Merged v1 'minutes vs notes' in here (3 shared URLs).  
Links: existing blogs meeting-minutes-sample, meeting-minutes-to-jira, meeting-knowledge-management; service pages /features/meeting-notes, /features/action-items; new blogs #1, #6, #7

**#6 LLC Meeting Minutes Template: Annual and First Meeting (Free)**  
URL: `/blog/llc-meeting-minutes-template` | Intent: Transactional (template) | Volume confidence: Medium  
Other keywords covered: none with measurable volume  
Live SERP: speaknotes DA 24 (#8), eforms DA 51 (#10), northwestregisteredagent DA 72 (#2)  
Overlap: LOW: shares 1 URL with the 'meeting minutes sample' SERP. Existing sample covers team and board minutes, not LLC.  
Links: existing blogs meeting-minutes-sample, founders-meeting-notes; service pages /features/meeting-notes; new blogs #5, #7

**#7 Board Meeting Agenda: Free Template, Format and Sample**  
URL: `/blog/board-meeting-agenda` | Intent: Informational / Transactional | Volume confidence: Medium  
Other keywords covered: format of board meeting agenda (1,300); board meeting agenda format (1,600); sample board meeting agenda (1,300)  
Live SERP: boardcloud DA 17 (#8), boardable DA 37 (#5), ibabs DA 38 (#9), nhnonprofits DA 40 (#4)  
Overlap: LOW: /blog/meeting-minutes-sample covers board MINUTES. Keep this post strictly about the AGENDA and link to the sample for minutes.  
Links: existing blogs meeting-minutes-sample, founders-meeting-notes; service pages /features/meeting-notes, /security; new blogs #5, #6, #8

**#8 How to Write a Meeting Agenda: Free Template + Examples**  
URL: `/blog/how-to-write-meeting-agenda` | Intent: Informational / Transactional | Volume confidence: Medium  
Other keywords covered: how to write meeting agenda (590); meeting agenda creator (880); team meeting agenda sample (880)  
Live SERP: Top spots held by zoom.com DA 87, MIT DA 93, Microsoft DA 90, Asana DA 82. Weaker: parkscommunity DA 24 (#7), notejoy DA 37, prialto DA 45  
Overlap: LOW: /blog/meeting-preparation is a prep brief; /blog/one-on-one-meeting has a 1:1 agenda only.  
Links: existing blogs meeting-preparation, one-on-one-meeting, daily-standup-meeting; service pages /features/ask-your-meetings, /integrations; new blogs #2, #7, #9

**#9 Project Kickoff Meeting Agenda: Template, Checklist and Example**  
URL: `/blog/project-kickoff-meeting-agenda` | Intent: Informational / Transactional | Volume confidence: Medium  
Other keywords covered: project kickoff meeting agenda template (210); project kickoff meeting agenda example (170)  
Live SERP: agendalink DA 13 (#9), plane.so DA 29 (#6), outbackteambuilding DA 43 (#8)  
Overlap: NONE: different SERP from the generic agenda query.  
Links: existing blogs meeting-preparation, meeting-minutes-to-jira; service pages /integrations, /features/action-items; new blogs #8, #10

**#10 Sprint Retrospective: Template, Questions and Examples (+ Review vs Retro)**  
URL: `/blog/sprint-retrospective` | Intent: Informational | Volume confidence: High (GSC: 'ai notetakers for team retrospectives' at position 1)  
Other keywords covered: sprint review vs sprint retrospective (390); sprint retrospective questions (70); sprint retrospective agenda (50); how to run sprint retrospective (40)  
Live SERP: resolution.de DA 35 (#5), innovationtraining DA 37 (#7), parabol DA 42 (#4)  
Overlap: NONE: /blog/daily-standup-meeting covers standups only.  
Links: existing blogs daily-standup-meeting, meeting-minutes-to-jira; service pages /use-cases/team-standups, /integrations; new blogs #9, #11

**#11 Sprint Planning Meeting Agenda: Template and Checklist**  
URL: `/blog/sprint-planning-meeting-agenda` | Intent: Informational | Volume confidence: Medium  
Other keywords covered: sprint planning meeting agenda template (30)  
Live SERP: agileseekers DA 12 (#5), agile-academy DA 29 (#7), range DA 42 (#8)  
Overlap: NONE.  
Links: existing blogs daily-standup-meeting, meeting-minutes-to-jira; service pages /use-cases/team-standups, /integrations; new blogs #10, #9

</details>

### C3. Recording & Transcripts by Platform (3 posts)

**Who is searching:** Employees on Google Meet and Teams, often not the host or on a free plan, who need a record of the call.  
**Hub service pages:** /features/meeting-bot, /features/chrome-extension, /download

| # | Blog title | Primary keyword (exact query) | Vol/mo of that query | SD | Cluster vol (sum) | Real difficulty (SERP) | Time to page 1 | Overlap risk | Wave |
|---|---|---|---|---|---|---|---|---|---|
| 12 | **How to Record a Google Meet (Free, as a Participant & on Phone)** (pillar) | `how to record google meet` | 2,400 | 25 | 3,780 | High (SD 25 understates it) | 5-8 months; needs backlinks for page 1 | NONE | 3 |
| 13 | How to Record a Teams Meeting (Even If You're Not the Host) | `how to record teams meeting` | 1,300 | 29 | 1,490 | Medium | 3-5 months | LOW | 3 |
| 14 | How to Download a Teams Transcript (and Turn It Into Meeting Notes) | `how to download teams transcript` | 70 | 30 | 290 | Medium | 3-4 months | MEDIUM | 3 |

<details><summary>Keywords covered, SERP evidence, confidence, overlap and links</summary>

**#12 How to Record a Google Meet (Free, as a Participant & on Phone)**  
URL: `/blog/how-to-record-google-meet` | Intent: Informational | Volume confidence: High (demand is real)  
Other keywords covered: can you record google meet (720); how to record google meet call (260); can you record google meet calls (260); how to record google meet on phone (140)  
Live SERP: About 6 of the top 10 are Google's own pages (DA 93-98). Best blogs: descript DA 69 (#10), otter DA 66 (#13), read.ai DA 47 (#14)  
Overlap: NONE: /blog/google-meet-transcript covers transcripts, not recording.  
Links: existing blogs google-meet-transcript, zoom-meeting-recorders, ai-voice-recorders; service pages /features/chrome-extension, /features/meeting-bot, /download; new blogs #13, #31

**#13 How to Record a Teams Meeting (Even If You're Not the Host)**  
URL: `/blog/how-to-record-teams-meeting` | Intent: Informational | Volume confidence: High  
Other keywords covered: as a participant (70); on iphone (40); outside of teams (40); with copilot (40)  
Live SERP: oneminuteofficemagic DA 24 (#11), circleback DA 32 (#8), msudenver DA 57 (#7); Microsoft Q&A holds #2  
Overlap: LOW: /blog/ai-note-taker-microsoft-teams is a tool comparison with one H2 on where recordings go.  
Links: existing blogs ai-note-taker-microsoft-teams, zoom-meeting-recorders; service pages /features/meeting-bot, /download; new blogs #12, #14

**#14 How to Download a Teams Transcript (and Turn It Into Meeting Notes)**  
URL: `/blog/download-teams-transcript` | Intent: Informational | Volume confidence: Medium  
Other keywords covered: download teams transcript (40); teams transcript download (40); how to get teams transcript after meeting (40); without permission (40); where to find teams transcript (30); how to download ms teams transcript (30)  
Live SERP: tactiq DA 41 (#9), macomb.edu DA 52 (#6); Microsoft pages DA 98 on top  
Overlap: MEDIUM: /blog/ai-note-taker-microsoft-teams has H2 'Where do Teams recordings and transcripts go?'. Fix: keep that H2 to 2 lines and link here.  
Links: existing blogs ai-note-taker-microsoft-teams, meeting-minutes-sample; service pages /features/meeting-notes; new blogs #13, #5

</details>

### C4. AI Note Taker Alternatives, Pricing & Reviews (16 posts)

**Who is searching:** Current Otter, Fireflies, Granola, Read AI, Fathom and Notion users hitting price or plan limits, people who want a bot out of their calls, buyers comparing tools. Bottom of funnel.  
**Hub service pages:** /compare/*, /pricing

| # | Blog title | Primary keyword (exact query) | Vol/mo of that query | SD | Cluster vol (sum) | Real difficulty (SERP) | Time to page 1 | Overlap risk | Wave |
|---|---|---|---|---|---|---|---|---|---|
| 15 | 9 Best Otter.ai Alternatives in 2026 (Free & Paid, Tested) | `otter ai alternatives` | 390 | 15 | 910 | Low | 1-3 months | NONE | 1 |
| 16 | Best Fireflies.ai Alternatives in 2026 (Compared by Price & Features) | `fireflies ai alternatives` | 90 | 15 | 230 | Low | 1-2 months | NONE | 1 |
| 17 | Best Granola AI Alternatives for Windows, Teams and In-Person Meetings | `granola ai alternatives` | 210 | 14 | 250 | Low | 1-2 months | NONE | 1 |
| 18 | Otter vs Fireflies vs Fathom: Which AI Note Taker Is Best in 2026? | `fathom vs fireflies` | 110 | 32 | 360 | Low | 1-3 months | NONE | 1 |
| 19 | Granola vs Otter AI: Which Note Taker Fits Your Meetings? | `granola vs otter ai` | 110 | 11 | 200 | Low | 1-2 months | NONE | 1 |
| 20 | Otter.ai Pricing 2026: Plans, Free Limits and Is Pro Worth It? | `otter ai pricing` | 1,900 | 40 | 4,170 | Medium (SD overstates it) | 2-4 months | LOW | 2 |
| 21 | Fireflies.ai Pricing 2026: Plans, Hidden Limits and Cheaper Options | `fireflies ai price` | 880 | 26 | 1,740 | Low-Med | 2-4 months | NONE | 2 |
| 22 | Read AI Pricing 2026: Plans, Free Tier and What You Actually Get | `read ai pricing` | 260 | 20 | 490 | Low | 1-3 months | NONE | 1 |
| 23 | Fathom Pricing 2026: Is the Free AI Note Taker Really Free? | `fathom pricing` | 590 | 37 | 620 | Low-Med | 2-4 months | NONE (/compare/fathom is Lynkk vs Fathom) | 3 |
| 24 | Granola Pricing 2026: Free Plan Limits and Paid Plans Explained | `granola pricing` | 880 | 16 | 880 | Low | 1-3 months | NONE | 1 |
| 25 | Otter.ai Review 2026: Accuracy, Privacy Concerns and the Lawsuit | `otter ai review` | 880 | 30 | 2,480 | Low-Med | 2-4 months | NONE | 2 |
| 26 | What Is Read AI, Why Is It in Your Meetings, and How to Remove It | `what is read ai` | 1,300 | 36 | 3,020 | Medium-High | 3-6 months | LOW | 3 |
| 27 | How to Remove Otter.ai From Zoom, Teams and Google Meet (and Delete Your Account) | `how to delete otter ai account` | 390 | 36 | 2,280 | Medium-High | 3-6 months | LOW | 3 |
| 28 | How to Remove Fireflies.ai From Teams, Zoom and Google Meet | `how to remove fireflies ai` | 140 | 28 | 670 | Medium | 3-5 months | LOW | 3 |
| 29 | ChatGPT Meeting Notes: How to Use Record Mode, Best Prompts and Limits | `chatgpt meeting notes` | 210 | 28 | 220 | Low-Med | 2-3 months | NONE | 2 |
| 30 | Notion AI Meeting Notes Review: Features, Limits, Pricing and Alternatives | `notion ai meeting notes` | 1,000 | 37 | 1,130 | Medium | 3-5 months (realistic target: positions 5-10) | NONE | 3 |

<details><summary>Keywords covered, SERP evidence, confidence, overlap and links</summary>

**#15 9 Best Otter.ai Alternatives in 2026 (Free & Paid, Tested)**  
URL: `/blog/otter-ai-alternatives` | Intent: Commercial | Volume confidence: High (GSC: /compare/otter already at position 5.5)  
Other keywords covered: otter ai alternative (480); otter ai alternative free (40)  
Live SERP: voicescriber DA 13 (#7), voicedash DA 15 (#8), intermind DA 40 (#6)  
Overlap: NONE: shares 0 of 10 URLs with the 'best ai note takers' SERP. /compare/otter is 'Lynkk vs Otter', a different intent.  
Links: existing blogs best-ai-note-takers, best-free-ai-note-takers; service pages /compare/otter, /pricing; new blogs #18, #20, #25

**#16 Best Fireflies.ai Alternatives in 2026 (Compared by Price & Features)**  
URL: `/blog/fireflies-ai-alternatives` | Intent: Commercial | Volume confidence: High (GSC: /compare/fireflies at position 4.2)  
Other keywords covered: fireflies ai alternative (70); fireflies alternative (70)  
Live SERP: meetingjuice DA 9 (#10), openwhispr DA 29 (#3), meetjamie DA 38 (#5)  
Overlap: NONE.  
Links: existing blogs best-ai-note-takers; service pages /compare/fireflies, /pricing; new blogs #15, #21, #18

**#17 Best Granola AI Alternatives for Windows, Teams and In-Person Meetings**  
URL: `/blog/granola-ai-alternatives` | Intent: Commercial | Volume confidence: High  
Other keywords covered: open source granola alternative (40)  
Live SERP: zackproser DA 22 (#2), usecarly DA 28 (#5), openwhispr DA 29 (#7)  
Overlap: NONE. v1 used 'granola alternative' (320): its SERP is 100% food (yogurt, recipes), so that volume was not ours.  
Links: existing blogs best-ai-note-takers, ai-voice-recorders; service pages /compare/granola, /download; new blogs #19, #24

**#18 Otter vs Fireflies vs Fathom: Which AI Note Taker Is Best in 2026?**  
URL: `/blog/otter-vs-fireflies-vs-fathom` | Intent: Commercial | Volume confidence: Medium  
Other keywords covered: fathom vs otter (70); fathom vs otter ai (40); fireflies ai vs otter ai (70); otter ai vs fireflies ai (70)  
Live SERP: cotera DA 27 (#2), sybill DA 36 (#7), efficient.app DA 37 (#10)  
Overlap: NONE.  
Links: existing blogs best-ai-note-takers; service pages /compare/otter, /compare/fireflies, /compare/fathom; new blogs #15, #16, #23

**#19 Granola vs Otter AI: Which Note Taker Fits Your Meetings?**  
URL: `/blog/granola-vs-otter` | Intent: Commercial | Volume confidence: Medium  
Other keywords covered: granola vs otter (90)  
Live SERP: mrktcorrect DA 9 (#8), zackproser DA 22 (#3), itsconvo DA 23 (#6), get-alfred DA 24 (#10)  
Overlap: NONE.  
Links: existing blogs best-ai-note-takers; service pages /compare/granola, /compare/otter; new blogs #17, #24

**#20 Otter.ai Pricing 2026: Plans, Free Limits and Is Pro Worth It?**  
URL: `/blog/otter-ai-pricing` | Intent: Commercial | Volume confidence: High  
Other keywords covered: otter ai pro plan (1,300); otter ai cost (390); otter ai free plan (320); how much is otter ai (260)  
Live SERP: tinrec DA 10 (#14), fonzi DA 27 (#10), meetergo DA 35 (#8), affine DA 39 (#7)  
Overlap: LOW: /blog/best-free-ai-note-takers has H2 'Is Otter AI free?'. Keep it short and link here.  
Links: existing blogs best-free-ai-note-takers; service pages /pricing, /compare/otter; new blogs #15, #25

**#21 Fireflies.ai Pricing 2026: Plans, Hidden Limits and Cheaper Options**  
URL: `/blog/fireflies-ai-pricing` | Intent: Commercial | Volume confidence: High  
Other keywords covered: fireflies ai pricing (480); is fireflies ai free (170); fireflies ai cost (140); fireflies ai free plan (70)  
Live SERP: cloudeagle DA 38 (#8), lindy DA 40 (#5), meetgeek DA 44 (#9); fireflies.ai's own pages on top  
Overlap: NONE.  
Links: existing blogs best-free-ai-note-takers; service pages /pricing, /compare/fireflies; new blogs #16, #28

**#22 Read AI Pricing 2026: Plans, Free Tier and What You Actually Get**  
URL: `/blog/read-ai-pricing` | Intent: Commercial | Volume confidence: High  
Other keywords covered: is read ai free (140); read ai cost (90)  
Live SERP: checkthat DA 33 (#8), meetjamie DA 38 (#9), meetgeek DA 44 (#6)  
Overlap: NONE.  
Links: existing blogs best-free-ai-note-takers, best-ai-note-takers; service pages /pricing; new blogs #26, #20

**#23 Fathom Pricing 2026: Is the Free AI Note Taker Really Free?**  
URL: `/blog/fathom-pricing` | Intent: Commercial | Volume confidence: LOW: 2 of the top 3 results are other brands named Fathom (usefathom.com analytics, fathomhq.com accounting), so part of the 590 is not about the note taker  
Other keywords covered: fathom pricing plans (30)  
Live SERP: usecarly DA 28 (#10), tomba DA 36 (#6), tldv DA 44 (#8)  
Overlap: NONE (/compare/fathom is Lynkk vs Fathom).  
Links: existing blogs best-free-ai-note-takers; service pages /pricing, /compare/fathom; new blogs #18

**#24 Granola Pricing 2026: Free Plan Limits and Paid Plans Explained**  
URL: `/blog/granola-pricing` | Intent: Commercial | Volume confidence: Medium: the SERP is the app, but a food 'popular products' box also shows, so some volume is grocery shoppers  
Other keywords covered: none with measurable volume  
Live SERP: layer3labs DA 21 (#11), get-alfred DA 24 (#5), usecarly DA 28 (#10), efficient.app DA 37 (#7)  
Overlap: NONE.  
Links: existing blogs best-free-ai-note-takers; service pages /pricing, /compare/granola; new blogs #17, #19

**#25 Otter.ai Review 2026: Accuracy, Privacy Concerns and the Lawsuit**  
URL: `/blog/otter-ai-review` | Intent: Commercial investigation | Volume confidence: High (GSC: 'which llm providers see call transcripts' at position 4.3)  
Other keywords covered: otter ai reviews (720); otter ai lawsuit (390); is otter ai safe (320); is otter ai hipaa compliant (170)  
Live SERP: craftnote DA 11 (#13), anarlog DA 17 (#6), seriousinsights DA 33 (#2), eesel DA 35  
Overlap: NONE. Merged v1 'Is Otter.ai safe?' here: review pages already rank in the 'is otter ai safe' SERP.  
Links: existing blogs best-ai-note-takers; service pages /compare/otter, /security; new blogs #20, #27, #15

**#26 What Is Read AI, Why Is It in Your Meetings, and How to Remove It**  
URL: `/blog/what-is-read-ai` | Intent: Informational (switching intent) | Volume confidence: High  
Other keywords covered: how to remove read ai from teams (480); from zoom (320); how to turn off read ai in teams (320); remove read ai from teams (320); is read ai safe (210); how to stop read ai from joining meetings (70)  
Live SERP: meetgeek DA 44 (#7). Removal SERPs are Microsoft Q&A (DA 98), read.ai help and university IT pages, with no blogs  
Overlap: LOW: /blog/zoom-bot-join-meeting has H2 'How do you stop a bot from joining your Zoom meeting?'. Link it here.  
Links: existing blogs zoom-bot-join-meeting, best-ai-note-takers; service pages /features/meeting-bot, /security; new blogs #22, #27, #28

**#27 How to Remove Otter.ai From Zoom, Teams and Google Meet (and Delete Your Account)**  
URL: `/blog/remove-otter-ai` | Intent: Informational (switching intent) | Volume confidence: High  
Other keywords covered: how to remove otter ai (320); how to turn off otter ai (320); from zoom (260); from teams (260); how to get rid of otter ai (260); how to cancel otter ai subscription (260); how to disable otter ai (210)  
Live SERP: Otter's own pages, Reddit and YouTube only; no blogs in the top 10  
Overlap: LOW: same note as #26 for /blog/zoom-bot-join-meeting.  
Links: existing blogs zoom-bot-join-meeting, best-ai-note-takers; service pages /compare/otter, /features/meeting-bot; new blogs #25, #26, #28

**#28 How to Remove Fireflies.ai From Teams, Zoom and Google Meet**  
URL: `/blog/remove-fireflies-ai` | Intent: Informational (switching intent) | Volume confidence: Medium (SERP not checked)  
Other keywords covered: from teams (140); from zoom (110); remove fireflies ai from teams (90); how to get rid of fireflies ai (70); how to disable fireflies ai (70); how to cancel fireflies ai (50)  
Live SERP: Not SERP-checked; expect support pages like #27  
Overlap: LOW.  
Links: existing blogs zoom-bot-join-meeting; service pages /compare/fireflies, /features/meeting-bot; new blogs #21, #26, #27

**#29 ChatGPT Meeting Notes: How to Use Record Mode, Best Prompts and Limits**  
URL: `/blog/chatgpt-meeting-notes` | Intent: Informational | Volume confidence: Medium  
Other keywords covered: chatgpt meeting notes prompt (10)  
Live SERP: tactiq DA 41 (#7), meetgeek DA 44 (#4), fellow DA 46 (#5), screenapp DA 50 (#9)  
Overlap: NONE.  
Links: existing blogs ai-powered-meeting-assistants, best-ai-note-takers; service pages /features/meeting-notes, /features/ask-your-meetings; new blogs #30, #3

**#30 Notion AI Meeting Notes Review: Features, Limits, Pricing and Alternatives**  
URL: `/blog/notion-ai-meeting-notes` | Intent: Commercial investigation | Volume confidence: Medium  
Other keywords covered: notion ai meeting notes free limit (40); notion ai meeting notes vs granola (30); is notion ai meeting notes free (30); notion ai meeting notes pricing (30)  
Live SERP: Notion holds #1, #2 and #8. Blogs: kurashi DA 18 (#15), noota DA 34 (#10), tldv DA 44 (#9)  
Overlap: NONE.  
Links: existing blogs meeting-knowledge-management, best-ai-note-takers; service pages /features/ask-your-meetings, /features/workspaces; new blogs #29, #2

</details>

### C5. Trust, Security & Compliance (2 posts)

**Who is searching:** IT and security admins, legal and compliance, managers rolling out a tool, and individuals checking recording laws.  
**Hub service pages:** /security, /features/workspaces, /privacy

| # | Blog title | Primary keyword (exact query) | Vol/mo of that query | SD | Cluster vol (sum) | Real difficulty (SERP) | Time to page 1 | Overlap risk | Wave |
|---|---|---|---|---|---|---|---|---|---|
| 31 | **Is It Legal to Record a Conversation? One-Party vs Two-Party Consent by State** (pillar) | `is it legal to record a conversation without permission` | 480 | 30 | 2,290 | Medium (legal topic, Google favors expert sources) | 4-6 months | LOW-MEDIUM | 3 |
| 32 | AI Note Taker Security Checklist: SSO, SCIM, Retention and Admin Controls | `(GSC questions; no Ubersuggest volume)` | GSC only | n/a | n/a | Low | 1-3 months | CHECK FIRST | 2 |

<details><summary>Keywords covered, SERP evidence, confidence, overlap and links</summary>

**#31 Is It Legal to Record a Conversation? One-Party vs Two-Party Consent by State**  
URL: `/blog/is-it-legal-to-record-a-conversation` | Intent: Informational | Volume confidence: High  
Other keywords covered: in california (590); in texas (480); in new york (390); in florida (320); is it legal to record meetings at work (30)  
Live SERP: jnylaw DA 38 (#6), hornwright DA 39 (#10), mwl-law DA 50 (#4); Texas State Law Library DA 89 (#2)  
Overlap: LOW-MEDIUM: 12 existing posts each have a short 'Is it legal to record...' H2. Fix: keep each to 2-3 sentences and link here as the full answer.  
Links: existing blogs legal-transcription-service, ai-voice-recorders, zoom-meeting-recorders; service pages /security, /features/meeting-bot; new blogs #32, #12, #13

**#32 AI Note Taker Security Checklist: SSO, SCIM, Retention and Admin Controls**  
URL: `/blog/ai-note-taker-security-checklist` | Intent: Commercial | Volume confidence: Demand proven by GSC, but small (about 50 impressions in 3 months)  
Other keywords covered: GSC, last 3 months: 'rolling out an ai notetaker to 300 reps: sso, scim, admin dashboard' 28 impressions at 4.6; 'saml sso with okta or entra id plus scim' 6 at 9.0; 'regulated teams ... retention and audit trail' 5 at 3.2; 'admins enforce a recording notice' 6 at 7.0; 'does a 40-person sales team need sso' 4 at 8.5  
Live SERP: Not applicable: long conversational queries  
Overlap: CHECK FIRST: these queries may already land on /blog/ai-note-taker-microsoft-teams (H2s 'What should you check before rolling out...' and 'Is a Teams AI note taker secure enough...'). Do not target 'hipaa compliant ai note taker': /blog/medical-transcription-software owns it.  
Links: existing blogs ai-note-taker-microsoft-teams, medical-transcription-software, legal-transcription-service; service pages /security, /features/workspaces, /demo; new blogs #31, #25

</details>

### C6. Sales Use Cases (2 posts)

**Who is searching:** SDRs, AEs, sales managers and RevOps who run many calls and need notes in their CRM.  
**Hub service pages:** /use-cases/sales-calls, /integrations

| # | Blog title | Primary keyword (exact query) | Vol/mo of that query | SD | Cluster vol (sum) | Real difficulty (SERP) | Time to page 1 | Overlap risk | Wave |
|---|---|---|---|---|---|---|---|---|---|
| 33 | What Is a Discovery Call? Questions, Script and Template | `what is a discovery call` | 390 | 24 | 820 | Medium | 3-5 months | NONE | 3 |
| 34 | How to Get Call Notes Into Your CRM Automatically (Zoom, Meet and Teams) | `(GSC questions; Ubersuggest: 'sales call notes template' 20)` | 20 | 30 | 20 | Low | 1-3 months | CHECK FIRST | 1 |

<details><summary>Keywords covered, SERP evidence, confidence, overlap and links</summary>

**#33 What Is a Discovery Call? Questions, Script and Template**  
URL: `/blog/discovery-call` | Intent: Informational | Volume confidence: Medium  
Other keywords covered: discovery call meaning (210); discovery call questions (70); discovery call template (50); discovery call script (50); sales discovery call (50)  
Live SERP: samsalesconsulting DA 23 (#10), acquire.io DA 45 (#9); Salesforce DA 92, Vidyard DA 75, Highspot DA 69 above  
Overlap: NONE.  
Links: existing blogs sales-conversation-intelligence, meeting-preparation; service pages /use-cases/sales-calls; new blogs #34, #4

**#34 How to Get Call Notes Into Your CRM Automatically (Zoom, Meet and Teams)**  
URL: `/blog/call-notes-to-crm` | Intent: Commercial | Volume confidence: Demand proven by GSC, but small  
Other keywords covered: GSC, last 3 months: 'zoom ai companion gives us summaries but nothing in our crm' 35 impressions at 2.3; 'record sales calls offline' 9 at 43; 'ai call notes for crm' 7 at 66  
Live SERP: Not applicable: long conversational queries  
Overlap: CHECK FIRST: the CRM question may already land on /blog/zoom-ai-companion-alternatives (position 6.9) or /blog/sales-conversation-intelligence.  
Links: existing blogs sales-conversation-intelligence, zoom-ai-companion-alternatives; service pages /use-cases/sales-calls, /integrations, /use-cases/financial-advisors; new blogs #33, #4

</details>

### C7. India (1 posts)

**Who is searching:** Indian professionals, students and teams typing in Hindi. India sends most of Lynkk's clicks today.  
**Hub service pages:** /features/dictation, /features/hinglish-transcription

| # | Blog title | Primary keyword (exact query) | Vol/mo of that query | SD | Cluster vol (sum) | Real difficulty (SERP) | Time to page 1 | Overlap risk | Wave |
|---|---|---|---|---|---|---|---|---|---|
| 35 | Hindi Voice Typing: Best Free Tools for PC, Mac and Phone | `hindi voice typing` | 6,600 (IN) | 27 | 7,740 | Low | 1-3 months | LOW | 2 |

<details><summary>Keywords covered, SERP evidence, confidence, overlap and links</summary>

**#35 Hindi Voice Typing: Best Free Tools for PC, Mac and Phone**  
URL: `/blog/hindi-voice-typing` | Intent: Commercial investigation | Volume confidence: High  
Other keywords covered: hindi voice typing software (590); hindi voice typing online (390); english to hindi voice typing (110); hindi voice typing online free (50)  
Live SERP: hindicheck.in DA 4 ranks #5 with a 'Best Tools 2026' blog; alllanguagetranslator DA 16, speechtyping DA 19 (#1), speech-typing DA 20  
Overlap: LOW: /blog/voice-to-text-apps and /blog/dictation-on-mac are English-focused. CONDITION: publish only if Lynkk dictation supports Hindi.  
Links: existing blogs voice-to-text-apps, dictation-on-mac, dictate-in-microsoft-word; service pages /features/dictation, /features/hinglish-transcription

</details>

## 5. The 20 Medium and Substack posts

These sit outside lynkk.ai and point into it. Because they live on another domain, they can cover angles I removed from the website for cannibalization (meeting bots, Copilot, interview transcription) and send readers to the existing page that owns that topic. Medium marks outbound links nofollow, so treat them as traffic and discovery, not link equity. Write each with a unique angle, never a copy of a website post, and publish it 1-2 weeks after its target page is live.

| # | Platform | Title | Target keyword | Keyword data | Intent | Links back to | Est. time to rank |
|---|---|---|---|---|---|---|---|
| 1 | Medium | I Tested 7 AI Note Takers on Hinglish Meetings. Here's What Broke | hinglish transcription | 110/mo India, SD 28 | Commercial investigation | /features/hinglish-transcription, #35 | 2-6 weeks |
| 2 | Medium | Read AI Kept Joining My Meetings. Here's How I Removed It for Good | how to stop read ai from joining meetings | 70/mo, SD 39 | Informational | #26, /features/meeting-bot | 2-6 weeks |
| 3 | Medium | Otter vs Fireflies vs Fathom After 30 Days of Real Meetings | fathom vs fireflies | 110/mo, SD 32 | Commercial | #18, #15, /compare/fireflies | 2-4 weeks |
| 4 | Medium | The Meeting Notes Template I Use for Every Meeting (Free Copy) | best meeting notes template | 390/mo, SD 19 | Transactional | #2, #1, /features/meeting-notes | 2-4 weeks |
| 5 | Medium | From Sprint Retro to Jira Tickets in 30 Seconds: My Team's Workflow | sprint retrospective jira | 50/mo, SD 24 | Informational | #10, /blog/meeting-minutes-to-jira, /integrations | 2-4 weeks |
| 6 | Medium | What Is Speaker Diarization? A Plain-English Guide for Non-Engineers | what is speaker diarization | 90/mo, SD 34 | Informational | /blog/ai-transcription-software, /features/multilingual-transcription | 3-8 weeks |
| 7 | Medium | Before You Hit Record: One-Party vs Two-Party Consent for Remote Teams | is it legal to record meetings at work | 30/mo, SD 35 | Informational | #31, /security | 3-8 weeks |
| 8 | Medium | The 3-Line Follow-Up Email I Send After Every Sales Call | follow up email after meeting | 210/mo, SD 26 | Informational | #4, #34, /use-cases/sales-calls | 2-4 weeks |
| 9 | Medium | 12 Discovery Call Questions Great AEs Never Skip | discovery call questions | 70/mo, SD 23 | Informational | #33, /use-cases/sales-calls | 2-4 weeks |
| 10 | Medium | How a Meeting Bot Actually Joins Zoom, Meet and Teams (Engineering Notes) | meeting bot / how to make a meeting bot | GSC: 'meeting bot' 102 impr at 21.7; 'how to make a meeting bot' at 29 | Informational (developers) | /blog/zoom-bot-join-meeting, /features/meeting-bot | 2-6 weeks |
| 11 | Medium | How to Record a Google Meet Without Google Workspace Premium | how to record google meet for free | 70/mo, SD 33 | Informational | #12, /features/chrome-extension | 3-8 weeks |
| 12 | Medium | Interview Transcription for UX Researchers: My 5-Step Workflow | user interview transcription | GSC: 93 impr at 40 | Informational | /blog/recruiting-interview-transcription, /use-cases/user-interviews | 3-8 weeks |
| 13 | Substack | Copilot in Teams vs a Dedicated AI Note Taker: Which One Should You Pay For? | copilot vs ai note taker | GSC question at 5.7 | Commercial | /blog/ai-note-taker-microsoft-teams, /compare | 1-3 months |
| 14 | Substack | Zoom AI Companion Is Free. Here's What It Still Can't Do | zoom ai companion meeting summary | 390/mo, SD 26 | Commercial | /blog/zoom-ai-companion-alternatives, #34 | 1-3 months |
| 15 | Substack | The 10 Security Questions IT Will Ask Before Approving an AI Note Taker | ai note taker sso scim | GSC questions at 3.2-9.0 | Commercial | #32, /security | 1-3 months |
| 16 | Substack | Meeting Minutes Are Not Enough: Why Teams Need a Meeting Memory | meeting knowledge management | Thought leadership | Brand / awareness | #5, /blog/meeting-knowledge-management, /features/ask-your-meetings | Distribution, not ranking |
| 17 | Substack | Why Action Items Die After the Meeting (and a System That Keeps Them Alive) | meeting notes with action items | 210/mo, SD 12 | Informational | /blog/action-items-examples-template, #3, /features/action-items | 1-3 months |
| 18 | Substack | Free vs Paid AI Note Takers: What You Actually Get at $0 | best free ai note taker | 260/mo, SD 32 | Commercial | /blog/best-free-ai-note-takers, #20, #24, /pricing | 1-3 months |
| 19 | Substack | Board Meetings at an Early-Stage Startup: Agenda, Minutes and What Investors Expect | sample board meeting agenda | 1,300/mo, SD 31 | Informational | #7, #6, /blog/founders-meeting-notes | 1-3 months |
| 20 | Substack | Running Meetings in Two Languages: What Global and Indian Teams Get Wrong | multilingual meeting transcription | GSC: 20 impr at 20.8 | Thought leadership | /features/multilingual-transcription, #35 | Distribution, not ranking |

## 6. 12-week calendar (about 3 posts a week)

- **Wave 1 (Weeks 1-4: weakest SERPs and lowest SD), 12 posts:** #3, #2, #1, #7, #15, #16, #17, #19, #22, #24, #18, #34
- **Wave 2 (Weeks 5-8), 12 posts:** #5, #6, #4, #9, #10, #11, #20, #21, #25, #29, #32, #35
- **Wave 3 (Weeks 9-12: strongest SERPs, need the most authority), 11 posts:** #8, #12, #13, #14, #23, #26, #27, #28, #30, #31, #33

## 7. Before you publish

- **#32 and #34** are based on GSC questions. First check in GSC which page those queries already land on (Performance > Queries > click the query > Pages). If an existing post gets them, expand that post instead and use the slot for a backup topic: 'Fireflies.ai Review' (`what is fireflies ai`, 720/mo, SD 47).
- **#35** only if Lynkk dictation supports Hindi.
- **Pricing and review posts (#20-#25, #30):** check competitors' current prices on the day you publish.
- **#31** is general information, not legal advice. Say so and cite official state sources.
- After 4-6 weeks, compare GSC impressions with these Ubersuggest numbers. GSC is the real source of truth once a page ranks.
