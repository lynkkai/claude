# Lynkk website changes

Every recommended change to lynkk.ai in one place: what to change, why, and the new copy.
Compiled 15 November 2026, updated 16 November 2026, from the Search Console export (14 Aug to 13 Nov), a crawl of all 126 sitemap URLs, Ubersuggest data and the live plan table.
**Nothing here has been applied to the site yet.** The pricing page and the legal pages (terms, refund) are left out on purpose: they will be handled separately.

Pricing used throughout: **Pro** $4 a month (₹250 in India), **Enterprise** custom. Users must pay before they can use Lynkk: there is no free plan, free tier or free trial.

## Contents

1. [Remove free-plan claims](#1-remove-free-plan-claims)
2. [Homepage and product pages](#2-homepage-and-product-pages)
3. [Blog rewrites: high impressions, low clicks](#3-blog-rewrites-high-impressions-low-clicks)
4. [New pages to create](#4-new-pages-to-create)
5. [Every blog post: diagnosis and action](#5-every-blog-post-diagnosis-and-action)
6. [Site structure and internal links](#6-site-structure-and-internal-links)
7. [Technical fixes](#7-technical-fixes)
8. [Free to paid: service pages, find and replace](#8-free-to-paid-service-pages-find-and-replace)
9. [Free to paid: blog posts, find and replace](#9-free-to-paid-blog-posts-find-and-replace)
10. [Full blog rewrites](#10-full-blog-rewrites)

## 1. Remove free-plan claims

The live site still sells a free plan. Every line to change is in sections 8 to 10, with the final text to paste:

- **Service pages:** 52 pages, 308 changes (section 8), plus 5 site-wide template fixes.
- **Blog posts:** 41 pages, 110 changes (section 9).
- **Full rewrites:** `/blog/best-free-ai-note-takers` and `/blog/ai-note-taker-microsoft-teams` (section 10).
- **Not included:** the pricing page and the terms and refund pages.

The most common changes:

| Now | Where | Change to |
|---|---|---|
| Start for free (button) | Header and footer, all 126 pages (477 times) | **Get Lynkk Pro** |
| Free (plan table column) | Homepage plan table | **Remove the column. Show Pro and Enterprise only.** |
| Free plan card: Free · $0 · ₹0 / forever · For your first conversations. | Homepage | **Remove the card. Show Pro ($4 / ₹250 a month) and Enterprise only.** |
| Lynkk · Free · $0 (row in "Pricing, side by side") | 12 compare pages | **Remove Lynkk's Free row. Keep Pro and Enterprise.** |
| Free to start, on your Mac or in the browser ... Free includes the first 5 hours of AI notes. | 12 compare pages (sign-up block) | **Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes.** |
| 5 hours of AI notes on the free plan · | Strip under the footer button, 25 pages | **Lynkk Pro from $4 a month ·** |
| Start free with Lynkk | 18 blog posts | **Get Lynkk Pro, $4 a month** |
| Sign up free. | 15 pages | **Get Lynkk Pro for $4 (₹250) a month.** |
| There is no trial to run out: the free plan has no end date. | 12 compare pages | **Lynkk Pro is $4 a month (₹250 in India).** |
| ... Start free. (end of meta description) | Homepage, meeting notes, 9 use-case pages | **... From $4 a month.** |
| Free stays free for everyone. / No credit card required. | Homepage | **Remove both (payment is required to use Lynkk).** |

| ... It's free to start. | 10 use-case pages | **... Lynkk Pro is $4 a month.** |
| Is it free? Yes, there's a free plan. | Use-case FAQs | **How much does it cost? Lynkk Pro is $4 a month (₹250 in India).** |

**Keep "free" where it is true:** free templates, competitors' free plans, Zoom's free plan, a free Gmail account.

**Wording rules from now on:** use "Get Lynkk Pro", "Get Lynkk Pro, $4/mo" or "From $4 a month". Never "Start free", "free plan", "free forever" or "free AI note taker" about Lynkk.

## 2. Homepage and product pages

### Homepage

`/`

**Why:** Brand traffic converts well (78 clicks, 10% CTR), but Lynkk averages #44 in GSC for its own target, "ai meeting assistant" (4,400/mo, SD 11). Headings carry the price instead of searched phrases, and the page links to no blog hub.

| Element | Now | Change to |
|---|---|---|
| Title | Lynkk: AI Meeting Assistant & Note Taker for Sales Teams | **Lynkk: AI Meeting Assistant & AI Note Taker, From $4/mo** |
| Meta description | Lynkk is the AI meeting assistant that takes notes on Zoom, Meet, Teams and in person, then drafts your follow-ups. 17 languages. Start free. | **The AI meeting assistant for Zoom, Google Meet, Teams and in-person meetings. Notes, action items and follow-up emails after every call. From $4/mo.** |
| H1 | The AI meeting assistant that remembers every sales conversation | **Keep (it contains the keyword)** |
| H2 (price) | Lynkk Pro for $4₹250 a month. | **Lynkk Pro: $4 a month. Show the regional price in body text, not in the heading.** |
| H2 (notes) | AI meeting notes, action items and follow-ups | **AI note taker: notes, action items and follow-ups after every call** |
| H2 (integrations) | Integrations: your CRM, Zoom, Google Meet, Microsoft Teams and Slack | **Meeting assistant software that works with Zoom, Meet, Teams, Slack and Jira** |
| H2 (pricing) | Pricing: a free AI note taker, Pro at $4₹250 a month | **Lynkk Pro: $4 a month** |
| Plan table | Free, Pro and Enterprise columns | **Pro and Enterprise only (remove the Free column)** |

- Add a "Works on every meeting" section: Zoom, Google Meet, Microsoft Teams and In person, each linking to its page.
- Add a "Free meeting templates and guides" block linking to the 6 blog hub pages (section 6). This passes homepage authority to the blog.
- FAQ: "Is it Lynkk or Lynk?" Answer: "Lynkk, with two k's (lynkk.ai)." GSC shows misspellings such as linnnk, linnkk and liknkk.
- FAQ: "What is the best AI meeting assistant for sales teams?" Two sentences and a link to /compare.
- The homepage title drops "for Sales Teams" to reach wider searches. Keep it if sales positioning matters more.

### Features hub

`/features`

**Why:** Ranks #2.4 with 130 impressions and 0 clicks. Ubersuggest's audit counted 87 words of body copy, and no blog post links to it.

| Element | Now | Change to |
|---|---|---|
| Title | Lynkk Features: Meeting Notes, Ask, Dictation, Slack \| Lynkk | **AI Meeting Assistant Features: Notes, Bot, Dictation \| Lynkk** |
| Structure | One short block per feature | **Three groups: Before the meeting (Ask your meetings, prep), During (meeting bot, Chrome extension, Mac app, Spotter live help in early access), After (notes, action items, Jira, Slack). 100-150 words and a screenshot each.** |

- Link to /features from the nav, the homepage and every blog hub page.

### AI meeting notes feature

`/features/meeting-notes`

**Why:** Ubersuggest: "ai powered meeting notes app" 170/mo at SD 5, and "minutes of meeting recorder" 260/mo in India at SD 10. Both match this page.

| Element | Now | Change to |
|---|---|---|
| Title | AI Note Taker & Meeting Minutes Generator \| Lynkk | **AI Meeting Notes App & Minutes of Meeting Recorder \| Lynkk** |
| Meta description | ... online or in person. Start free. | **... online or in person. From $4 a month.** |
| New H2s | (new) | **"AI meeting summarizer: one summary for every call" · "Minutes of meeting (MoM) recorder for online and in-person meetings"** |

- Link to it from every template post, with the anchor "AI meeting notes app" under the template.

### Chrome extension

`/features/chrome-extension`

**Why:** No-bot recording is a real differentiator, and people search for it. Chrome Web Store listings rank on page 1 for "google meet transcript" and "ai note taker for teams".

| Element | Now | Change to |
|---|---|---|
| Title | AI Note Taker Chrome Extension, No Bot \| Lynkk | **AI Note Taker Without a Bot: Chrome Extension \| Lynkk** |
| New H2 | (new) | **An AI note taker that doesn't join your meetings** |

- Publish or optimize the Chrome Web Store and Edge Add-ons listings as "Lynkk: AI Note Taker for Google Meet, Zoom & Teams".

### Meeting bot

`/features/meeting-bot`

**Why:** 17 clicks at 1.6% CTR, and "meeting bot" sits at #17. The word "Free" in the title is now inaccurate.

| Element | Now | Change to |
|---|---|---|
| Title | Free AI Meeting Bot for Zoom, Google Meet & Teams \| Lynkk | **AI Meeting Bot for Zoom, Google Meet & Teams \| Lynkk** |
| New H2 | (new) | **Meeting bot vs no bot: which should you send?** |

- Link from zoom-bot-join-meeting with the anchor "AI meeting bot".

### Sales calls use case

`/use-cases/sales-calls`

**Why:** The page Lynkk's main buyer should land on. It ranks #42 at about 1,200 words, and its title promises CRM sync, which the plan table lists as "Not yet".

| Element | Now | Change to |
|---|---|---|
| Title | AI Sales Call Notes That Sync to Your CRM \| Lynkk | **AI Note Taker for Sales Calls: Notes and Follow-Up Emails** |
| Meta description | ... writes the next steps for you. Start free. | **... writes the next steps for you. From $4 a month.** |
| H1 | AI for sales calls: you talk, Lynkk writes the notes. | **Keep** |
| New H2s | (new) | **"The follow-up email, drafted from the call" · "Lynkk vs Gong and Fireflies for sales teams" · "From call to follow-up email, in one example"** |

- Add a real example: call summary, next steps and the follow-up email it drafts.
- Link to it from all 15 sales blog posts and the new sales follow-up email page.
- The /use-cases hub gets 0 blog links: link to it from the homepage and the blog hubs.

### Compare pages

`/compare/otter, /compare/fireflies`

**Why:** Otter ranks #4.7 (206 impressions) and Fireflies #4.2 (163) with 0 clicks, while the Circleback compare page converts at 13%. The snippets lead with Lynkk, but searchers want the competitor's alternative.

| Element | Now | Change to |
|---|---|---|
| Otter title | Otter.ai Alternative: Lynkk vs Otter Compared \| Lynkk | **Otter.ai Alternative With No-Bot Recording, From $4/mo** |
| Otter meta | Looking for an Otter.ai alternative? Compare Lynkk and Otter on bot-free recording, languages, Jira and Slack... | **Switching from Otter.ai? Lynkk records with or without a bot, works in person and in 17 languages, and costs $4/mo. Side-by-side table inside.** |
| Fireflies title | Fireflies Alternative: Lynkk vs Fireflies.ai \| Lynkk | **Fireflies.ai Alternative for In-Person Meetings, $4/mo** |
| Avoma H1 | Lynkk vs Avoma: an Avoma alternative with a free plan that keeps recording | **Lynkk vs Avoma: an Avoma alternative from $4 a month, with in-person recording** |
| All compare pages | There is no trial to run out: the free plan has no end date. | **Lynkk Pro is $4 a month (₹250 in India).** |

### How it works and Demo

`/how-it-works, /demo`

**Why:** /how-it-works ranks #2.6 (307 impressions) with 0 clicks. /demo has 148 words.

| Element | Now | Change to |
|---|---|---|
| How it works meta | How an AI note taker works, start to finish: record a meeting with the Mac app, a bot, Chrome or a browser... | **Record with a bot, the Chrome extension or the Mac app, then get notes, action items and a follow-up email. See one meeting, start to finish.** |
| Demo | Booking form | **Add a 2-minute product video with its transcript, and 3 FAQs (security, rollout, team pricing).** |

### Integration titles for Zoom and Google Meet

`/integrations/zoom, /integrations/google-meet`

**Why:** Both titles call Lynkk free.

| Element | Now | Change to |
|---|---|---|
| Zoom title | Free AI Note Taker for Zoom Meetings (Bot or No Bot) \| Lynkk | **AI Note Taker for Zoom, Even on Free Zoom (Bot or No Bot)** |
| Zoom meta | Free AI note taker for Zoom, even on free Zoom plans... | **An AI note taker that works on free Zoom plans. Send a bot or record from your Mac, and get the summary and action items. From $4/mo.** |
| Google Meet title | Free AI Note Taker for Google Meet (Bot or Chrome Extension) | **AI Note Taker for Google Meet, No Workspace Plan Needed** |
| Google Meet meta | Free AI note taker for Google Meet, no Workspace plan needed... | **An AI note taker for Google Meet with no Workspace plan needed. A notetaker joins from your calendar, or the Chrome extension records your tab. From $4/mo.** |

## 3. Blog rewrites: high impressions, low clicks

These pages already show on page 1-3 but win few clicks. Ordered by expected gain. Numbers are GSC, 14 Aug to 13 Nov.

### 3.1 `/blog/google-meet-transcript`

10,422 impr · 33 clicks · 0.32% CTR · #8.8

**Why:** The biggest page on the site (17% of all impressions). At #8.8 a 2-3% CTR is typical. Searchers type short phrases ("google meet transcript" 160 impr #13, "where to find google meet transcript" #7).

- **Current title:** Where Is My Google Meet Transcript? Find It in 3 Steps
- **New title (59 chars):** Google Meet Transcript: Where to Find It and How to Get One
- **New meta (153 chars):** Google Meet saves the transcript to the organizer's Google Drive. Find it in 3 steps, fix a missing transcript, or get one on any Google plan with Lynkk.
- **On the page:**
  - 3-step answer box with screenshots under the H1.
  - H2 "How to download a Google Meet transcript" and H2 "Google Meet transcript not showing? 6 fixes".
  - Table: Workspace plan vs transcript available.
  - CTA after step 3: "No Workspace plan? Lynkk transcribes Google Meet on any account, from $4 a month."
  - Move the Zoom AI Companion questions to that post and link to it.

### 3.2 `/blog/zoom-ai-companion-alternatives`

953 impr · 0 clicks · #6.4

**Why:** Almost all impressions are long AI-search questions (CRM gap, regulated teams, Google Meet plus in-person). You win when the AI answer names Lynkk.

- **Current title:** 7 Zoom AI Companion Alternatives (Free Zoom, CRM Sync)
- **New title (55 chars):** Zoom AI Companion Alternatives: 7 Tools Compared (2026)
- **New meta (156 chars):** Zoom AI Companion only works in Zoom. Compare 7 alternatives that also cover Google Meet, Teams and in-person meetings, on retention, CRM support and price.
- **On the page:**
  - One H2 per real question: "Which alternatives sync notes to the CRM?", "Which also cover Google Meet and in-person interviews?", "Which offer retention controls and an audit trail?"
  - Start each answer with a one-sentence verdict that names Lynkk where it fits. On the CRM question, name the tools that sync to a CRM today; Lynkk's plan table lists CRM sync as "Not yet".
  - Comparison table with a row per question.
  - Link to /blog/ai-notetaker-security and /compare.

### 3.3 `/blog/ai-note-taker-microsoft-teams`

2,309 impr · 1 click · #20.4

**Why:** "ai note taker for teams" (590/mo, SD 29) sits at #51. A DA 13 site ranks #2 for it, so it is winnable.

**Done: full rewrite in section 10.2.** It removes the free-plan claims and applies the SEO fixes:

- **New title (55 chars):** AI Note Taker for Microsoft Teams: 7 Picks, No Copilot
- **New meta (147 chars):** Copilot costs $30 a user. Compare Teams Premium recap, free Teams transcription, Otter, Fireflies, Fathom and Lynkk ($4/mo) for a 10-person team.
- Answer to "Does Teams have an AI note taker?" first, comparison table above the fold, and a new H2 "How to add an AI note taker to Microsoft Teams".
- Still to do: link to it from /integrations/microsoft-teams.

### 3.4 `/blog/granola-ai-pricing`

1,628 impr · 0 clicks · #9.8

**Why:** Buyer intent: "granola pricing" alone has 313 impressions at #11. A snippet showing the numbers and "is it free" wins #2-4.

- **Current title:** Granola AI Pricing 2026: Free, Business, Enterprise
- **New title (51 chars):** Granola Pricing (Nov 2026): Free, $14 and $35 Plans
- **New meta (140 chars):** Granola is free with 30 days of history. Business is $14 and Enterprise $35 per user a month. Every limit, team costs, and a $4 alternative.
- **On the page:**
  - "Is Granola free?" as the 2nd H2 (81 impressions for that query).
  - "Last checked: November 2026" next to the price table.
  - Team cost table for 5 and 10 users, with Lynkk Pro at $4 as the last row.
  - Same pattern on the Fathom, Fireflies, Otter and Gong pricing posts. Fathom title: "Fathom Pricing (Nov 2026): Free vs $16, $15 and $25 Plans".

### 3.5 `/blog/voice-memo-transcription`

2,506 impr · 8 clicks · #11.7

**Why:** Queries sit at #9-34. Searchers write "voice memo transcription" (1,600/mo, SD 27).

- **Current title:** How to Transcribe Voice Memos on iPhone (Free, 2026)
- **New title (57 chars):** Voice Memo Transcription on iPhone: Free in 3 Taps (2026)
- **New meta (143 chars):** Turn on voice memo transcription on iPhone in 3 taps, view or copy the transcript, and transcribe older voice memos on Mac. Free, step by step.
- **On the page:**
  - H2 "Voice memo to transcript: copy or export it".
  - H2 "Apple voice memo transcription accuracy".
  - CTA: "Recording a meeting, not a memo? Lynkk adds speakers and action items." ("Free" here refers to Apple's feature.)

### 3.6 `/blog/action-items-examples-template`

3,082 impr · 4 clicks · #24.6

**Why:** People want a file ("action items template" 206 impr #25, "action item list" 120 impr #31).

- **Current title:** Action Item Template (Free, Copy Into Sheets) + 12 Examples
- **New title (58 chars):** Action Item Template: Free for Sheets, Excel + 12 Examples
- **New meta (139 chars):** Copy a free action item template for Google Sheets, Excel or Word, see 12 action item examples, and track owners and due dates in one list.
- **On the page:**
  - "Make a copy" buttons for Google Sheets, Excel and Notion.
  - Exact-match H2 "Action item list example".
  - Under the template: "Lynkk fills this in for you after every meeting."

### 3.7 `/blog/meeting-minutes-sample`

1,620 impr · 4 clicks · #22.6

**Why:** India sends the most clicks (96 at 2.25% CTR vs 59 at 0.21% for the US). India: "template for meeting minutes" 14,800/mo at SD 10, "meeting minutes format pdf" 1,000 at SD 6.

- **Current title:** Meeting Minutes Sample: Copy-Ready Team & Board Templates
- **New title (52 chars):** Meeting Minutes Format (MoM): Templates and Examples
- **New meta (145 chars):** Copy-ready minutes of meeting (MoM) formats for team, board and client meetings, with Word and PDF examples, plus how to write MoM in 10 minutes.
- **On the page:**
  - H2s "MoM format" and "Minutes of meeting example (PDF and Word)".
  - H2 "Board of directors meeting minutes example" (590/mo, SD 14).
  - Downloadable Word and PDF versions.
  - Hinglish note linking to /features/hinglish-transcription.

### 3.8 `/blog/daily-standup-meeting`

1,884 impr · 3 clicks · #25.7

**Why:** Searchers lead with "template", and "scrum stand up meeting" is 2,400/mo at SD 6 (a DA 2 site ranks #5).

- **Current title:** Daily Standup Meeting Agenda & Format (Free Template)
- **New title (52 chars):** Daily Standup Meeting Template + Agenda (Free, 2026)
- **New meta (144 chars):** Copy a free daily standup meeting template with a 15-minute agenda, plus Scrum and async standup formats you can paste into Slack, Docs or Jira.
- **On the page:**
  - Template block first, as a downloadable file.
  - H2s "Scrum stand up meeting" and "Async standup template".
  - Link to /use-cases/team-standups.

### 3.9 `/blog/follow-up-email-after-meeting`

2,304 impr · 12 clicks · #15.9

**Why:** Its main queries sit at #33-76. The sales angle is the best keyword found ("follow up email to sales call" 8,100/mo, SD 7).

- **Current title:** Follow-Up Email After a Meeting: 12 Examples to Copy
- **New title (53 chars):** Follow-Up Email After a Meeting: 15 Templates to Copy
- **New meta (152 chars):** Send it within 24 hours with thanks, decisions, owners and dates. Copy 15 follow-up email templates for clients, sales calls, teams and no-reply nudges.
- **On the page:**
  - "Sales call follow-up email" section with 3 templates, linking to the new sales follow-up page.
  - H2 "How to write a follow-up email after a meeting".
  - CTA: "Lynkk drafts this email from your meeting notes."

### 3.10 `/blog/hindi-transcription`

914 impr · 8 clicks · #8.3

**Why:** The queries are about Hinglish ("hinglish transcribe", "hinglish transcription"), but the title leads with Hindi.

- **Current title:** Hindi Audio to Text Converter: 6 Free Ways (Hinglish Too)
- **New title (56 chars):** Hindi & Hinglish Audio to Text: 6 Free Converters (2026)
- **New meta (150 chars):** Convert Hindi or Hinglish audio to text free with Google Docs, Gboard, YouTube captions or Whisper, or try Lynkk for mixed Hindi and English meetings.
- **On the page:**
  - H2 "Hinglish transcription: why most tools split the sentence".
  - Link to /features/hinglish-transcription.

Smaller title changes from the per-post table (section 5): ai-powered-meeting-assistants → "What Is an AI Meeting Assistant? Before, During and After"; transcribe-audio-to-text → "Best Software to Transcribe Audio to Text (2026): 5 Picks"; one-on-one-meeting → "1:1 Meeting Agenda Template"; meeting-notes-vs-minutes → "What Are Meeting Minutes? Meaning, Format, vs Notes"; is-it-legal-to-record-a-meeting → "Is It Legal to Record a Meeting? One-Party vs Two-Party States"; zoom-note-taker → "AI Note Taker for Zoom: 7 Best Tools, Free and Paid".

## 4. New pages to create

From the keyword plan, highest priority first. Projected clicks use Ubersuggest's click model at the target position, so treat them as a ranking of the work, not a forecast.

| Priority | New page | Hub | Target keywords (volume/mo, SD) | Clicks/mo at target |
|---|---|---|---|---|
| P1 | `/blog/sales-follow-up-email` | Sales meetings | follow up email to sales call (8,100, SD 7); follow up email sales sample (2,400, SD 22); sales call follow up email (9,900, SD 26) | 639 |
| P1 | `/blog/meeting-notes-template` | Meeting templates | meeting notes template free (880, SD 14); project management meeting notes template (260, SD 14); how to write meeting notes template (170, SD 9) | 102 |
| P1 | `/blog/how-to-record-teams-meeting` | Meeting platform guides | how to recording teams meeting (590 UK, SD 6); how to record teams meeting (1,300, SD 34) | 71 |
| P1 | `/blog/jamie-ai-review` | Compare tools | jamie ai note taker (1,300, SD 17) | 56 |
| P1 | `/blog/granola-vs-otter` | Compare tools | granola vs otter ai (110, SD 11); otter ai vs granola (90, SD 12) | 16 |
| P1 | `/blog/granola-vs-fathom` | Compare tools | granola vs fathom (110, SD 14); fathom vs granola (110, SD 17) | 14 |
| P2 | `/blog/how-to-record-google-meet` | Meeting platform guides | how to record a google meet (1,600, SD 28); how to record a google meet call (320, SD 24) | 45 |
| P2 | `/blog/teams-transcript` | Meeting platform guides | teams meeting transcription (390, SD 22); how to download teams meeting transcript (30, SD 6) | 20 |
| P2 | `/blog/read-ai-pricing` | Compare tools | read ai pricing (260, SD 20) | 11 |
| P2 | `/blog/fireflies-vs-otter` | Compare tools | fireflies vs otter (110, SD 21); otter ai vs fireflies (90, SD 17) | 9 |
| P2 | `/blog/ai-note-taker-in-person-meetings` | AI note takers | is there an ai note taker for in person meetings (20, SD 11); ai note taker for in person meetings (480, SD 40) | 8 |
| P2 | `/blog/granola-alternatives` | Compare tools | granola alternative (320, SD 28) | 6 |
| P2 | `/blog/fathom-vs-otter` | Compare tools | otter ai vs fathom (70, SD 24); fathom vs otter ai (40, SD 7) | 6 |
| P2 | `/blog/gong-alternatives` | Sales meetings | gong alternative (210, SD 28) | 4 |

Also rewrite `/blog/how-to-transcribe-zoom-meetings` into the Zoom transcript guide ("transcribe zoom" 2,400/mo, SD 21) instead of creating a new URL.

**Outline for every "Tool A vs Tool B" page:** quick verdict · side-by-side table (capture, bots, languages, price) · where A wins · where B wins · price for a team of 10 · a third option: Lynkk (our product, from $4/mo) · FAQ.

**Outline for the sales follow-up email page:** when to send · template after a discovery call · after a demo · no reply after a proposal · after a pricing call · subject lines · write it in 2 minutes from your call notes (Lynkk drafts it).

## 5. Every blog post: diagnosis and action

Diagnosis key: **Working** (good CTR) · **Snippet problem** (ranks #1-12, low CTR: fix title and meta) · **Page 2 push** (#13-30: improve content and links) · **Wrong target** (#30+: retarget to the long tail or stop) · **Low impressions** · **Not indexed** · **New** (under 3 weeks).

### Platform how-tos (4 posts, 58 clicks, 12,745 impressions)

| Post | Impr. | Clicks | CTR | Pos | Diagnosis | Action |
|---|---|---|---|---|---|---|
| google-meet-transcript | 10,422 | 33 | 0.32% | 8.8 | Snippet problem | **Optimize:** Rewrite title and meta (see section 3.1). Add a 3-step answer box with screenshots, a "download the transcript" H2, a plan table and a free-transcript CTA. |
| zoom-bot-join-meeting | 1,788 | 23 | 1.29% | 11.6 | Snippet problem | **Optimize:** Retitle around "meeting bot" (238 impr, #17). Add a comparison of which note takers send a bot vs record without one, linking to /features/meeting-bot. |
| how-to-transcribe-zoom-meetings | 535 | 2 | 0.37% | 49.3 | Wrong target | **Optimize:** Rewrite this URL into the Zoom transcript guide (find, download, save, without recording). Ubersuggest: "transcribe zoom" 2,400/mo at SD 21, Lynkk #67. |
| zoom-meeting-recorders | 0 | 0 | 0.00% |  | Not indexed | **Optimize:** Not indexed. Request indexing in GSC, link to it from google-meet-transcript and zoom-note-taker. India: "zoom meeting recorder" 880/mo at SD 32. |

### Templates (8 posts, 33 clicks, 12,276 impressions)

| Post | Impr. | Clicks | CTR | Pos | Diagnosis | Action |
|---|---|---|---|---|---|---|
| action-items-examples-template | 3,082 | 4 | 0.13% | 24.6 | Page 2 push | **Optimize:** 3,082 impr at #25. Downloadable Sheets/Excel/Notion files plus an "action item list" H2 (section 3.6). |
| follow-up-email-after-meeting | 2,304 | 12 | 0.52% | 15.9 | Page 2 push | **Optimize:** 12 clicks, #15.9. Add a sales follow-up section, or link to a new sales follow-up page (8,100/mo, SD 7). |
| daily-standup-meeting | 1,884 | 3 | 0.16% | 25.7 | Page 2 push | **Optimize:** 1,884 impr at #25.7. Lead the title with "Template" (that is what people type). Add Scrum and async templates as files. |
| meeting-summary-template | 1,819 | 7 | 0.38% | 23.5 | Page 2 push | **Optimize:** 1,819 impr at #23.5. Retitle "Meeting Summary Template + Examples", put the template first, and add "meeting recap template" and "synopsis" as H3s. |
| meeting-minutes-sample | 1,620 | 4 | 0.25% | 22.6 | Page 2 push | **Optimize:** 1,620 impr at #22.6. Add a MoM format section for India and a board minutes example (section 3.7). |
| board-meeting-agenda | 1,353 | 2 | 0.15% | 21.3 | Page 2 push | **Optimize:** "ai agenda templates for board meetings" is at #5 (156 impr). Add an "AI board agenda template" H2 and a nonprofit first-meeting sample. |
| meeting-notes-vs-minutes | 154 | 0 | 0.00% | 30.3 | Wrong target | **Optimize:** Retitle to "What Are Meeting Minutes? Meaning, Format, vs Notes". In India, "meeting minutes means" is 4,400/mo at SD 14. |
| one-on-one-meeting | 60 | 1 | 1.67% | 25.9 | Low impressions | **Optimize:** Retitle to "1:1 Meeting Agenda Template". "121 meeting agenda template" gets 2,400/mo at SD 19. |

### AI note takers (8 posts, 26 clicks, 8,753 impressions)

| Post | Impr. | Clicks | CTR | Pos | Diagnosis | Action |
|---|---|---|---|---|---|---|
| zoom-note-taker | 2,457 | 4 | 0.16% | 25.2 | Page 2 push | **Optimize:** Retitle to "AI Note Taker for Zoom" (480/mo, SD 33). Add "best AI note taker for Zoom" (40/mo, SD 12) as an H2 with a ranked table. |
| ai-note-taker-microsoft-teams | 2,309 | 1 | 0.04% | 20.4 | Page 2 push | **Optimize:** Rewrite title and meta (section 3.3). Put a comparison table in the first screen. Add "how to add an AI note taker to Teams". |
| ai-powered-meeting-assistants | 2,009 | 7 | 0.35% | 29.6 | Page 2 push | **Optimize:** Retitle to "What Is an AI Meeting Assistant?" and let the homepage own the commercial term. In India it ranks #8 for "meeting ai assistant" (590/mo). |
| best-ai-note-takers | 1,697 | 3 | 0.18% | 33.5 | Wrong target | **Optimize:** Head terms are long-term (#34). Add H2s "best AI note taker for Zoom" (you rank #7 for this) and "what is the best AI note taker for meetings" (70/mo, SD 18). |
| google-meet-ai-note-taker | 280 | 11 | 3.93% | 5.9 | Working | **Optimize:** Working (3.9% CTR). Expand toward "ai note taker for google meets" (170/mo, SD 24) and "best ai note taker for google meet" (SD 16). |
| best-ai-meeting-notes-for-teams | 1 | 0 | 0.00% | 1.0 | New (<3 weeks) | **Hold:** 1 impression and not in the sitemap. Check it is meant to be live. If yes, add it to the sitemap; if not, 301 it to best-ai-note-takers. |
| ai-voice-recorders | 0 | 0 | 0.00% |  | Not indexed | **Optimize:** Not indexed. Low priority: hardware-device intent (Plaud) does not suit Lynkk. Request indexing once, then leave. |
| best-free-ai-note-takers | 0 | 0 | 0.00% |  | Not indexed | **Optimize:** Not indexed despite 24 internal links. Request indexing. Keep it as an honest comparison of other tools' free plans; Lynkk has no free plan and is shown at $4 a month. Not a target keyword in the plan. |

### Transcription (8 posts, 47 clicks, 7,833 impressions)

| Post | Impr. | Clicks | CTR | Pos | Diagnosis | Action |
|---|---|---|---|---|---|---|
| voice-memo-transcription | 2,506 | 8 | 0.32% | 11.7 | Snippet problem | **Optimize:** 2,506 impr at #11.7. Small title fix and a "voice memo to transcript" H2 (section 3.5). |
| medical-transcription-software | 1,876 | 1 | 0.05% | 31.6 | Wrong target | **Hold:** 1,876 impr at #31.6 but no HIPAA proof. Do not expand until compliance is confirmed. |
| recruiting-interview-transcription | 1,302 | 3 | 0.23% | 23.0 | Page 2 push | **Optimize:** 1,302 impr at #23. Queries are generic ("interview transcript" #6.5). Broaden the title beyond recruiters. |
| transcribe-audio-to-text | 1,019 | 26 | 2.55% | 37.7 | Working | **Optimize:** Working on long tail (26 clicks). Retitle to "Best Software to Transcribe Audio to Text". India: "audio to text transcription software" 390/mo at SD 20. |
| hindi-transcription | 914 | 8 | 0.88% | 8.3 | Snippet problem | **Optimize:** 914 impr at #8.3. Put Hinglish in the title, since the queries are "hinglish transcribe" and "hinglish transcription". |
| ai-transcription-software | 216 | 1 | 0.46% | 8.2 | Page 2 push | **Optimize:** 216 impr at #8.2. Retitle to "AI Transcription Software" for India ("transcription software" 320/mo at SD 17, "automatic transcription software" 170 at SD 19). |
| real-time-ai-interview-assistant | 0 | 0 | 0.00% |  | New (<3 weeks) | **Hold:** New. India: "real time ai meeting assistant" 70/mo at SD 6. Add that phrase to an H2. |
| legal-transcription-service | 0 | 0 | 0.00% |  | Not indexed | **Optimize:** Not indexed. Request indexing once. Low priority unless lawyers are a target segment. |

### Competitors (8 posts, 8 clicks, 4,703 impressions)

| Post | Impr. | Clicks | CTR | Pos | Diagnosis | Action |
|---|---|---|---|---|---|---|
| granola-ai-pricing | 1,628 | 0 | 0.00% | 9.8 | Snippet problem | **Optimize:** 1,628 impr at #9.8, 0 clicks. New title with prices, and "Is Granola free?" as the 2nd H2 (section 3.4). |
| zoom-ai-companion-alternatives | 953 | 0 | 0.00% | 6.4 | Snippet problem | **Optimize:** 953 impr at #6.4 and 0 clicks, almost all from long AI-search questions. Answer each question as its own H2 (section 3.2). |
| fathom-ai-pricing | 805 | 2 | 0.25% | 11.6 | Snippet problem | **Optimize:** Same pricing fix as Granola. "fathom pricing" 253 impr at #17. |
| gong-pricing | 577 | 3 | 0.52% | 17.6 | Page 2 push | **Optimize:** Page 2. Add a "Gong alternatives for small teams" section ($64 CPC keyword). |
| fireflies-pricing | 265 | 0 | 0.00% | 12.1 | Page 2 push | **Optimize:** Same pricing fix. Target "fireflies ai price" (880/mo, SD 26). |
| otter-ai-alternatives | 219 | 0 | 0.00% | 74.7 | Wrong target | **Optimize:** #75. Rewrite in the format Bluedot uses to rank #2: comparison table first, then Lynkk labelled "our product". |
| read-ai-vs-otter-ai | 148 | 3 | 2.03% | 16.9 | Working | **Optimize:** Working (2% CTR). Use it as the template for new vs pages. |
| otter-ai-pricing | 108 | 0 | 0.00% | 26.8 | Page 2 push | **Optimize:** Same pricing fix. "otter ai pricing" is 1,900/mo at SD 24, and the page sits at #27. |

### Mac & dictation (6 posts, 4 clicks, 3,433 impressions)

| Post | Impr. | Clicks | CTR | Pos | Diagnosis | Action |
|---|---|---|---|---|---|---|
| voice-to-text-apps | 3,028 | 4 | 0.13% | 41.9 | Wrong target | **Optimize:** 3,028 impr at #42: the head terms are too hard. Retarget to the long tail it does reach: "best dictation software for small business", "voice to email software". Lead with Lynkk's Mac dictation. |
| dictate-in-microsoft-word | 365 | 0 | 0.00% | 46.0 | Wrong target | **Stop:** Ranks #46 for Microsoft-owned terms. No further work. Keep as a support page for the dictation feature. |
| dictation-on-mac | 40 | 0 | 0.00% | 27.9 | Low impressions | **Merge:** 40 impressions in 3 months. Merge into speech-to-text-mac with a 301 redirect. |
| best-mac-note-taking-app | 0 | 0 | 0.00% |  | New (<3 weeks) | **Hold:** New. Make sure it links to /download (Mac app). |
| record-audio-on-mac | 0 | 0 | 0.00% |  | New (<3 weeks) | **Hold:** New. Wait 4-6 weeks, then review. Link to /features/dictation and the Mac download. |
| speech-to-text-mac | 0 | 0 | 0.00% |  | New (<3 weeks) | **Hold:** New. Overlaps dictation-on-mac. Once it has data, 301 dictation-on-mac into it. |

### Sales (15 posts, 4 clicks, 2,070 impressions)

| Post | Impr. | Clicks | CTR | Pos | Diagnosis | Action |
|---|---|---|---|---|---|---|
| revenue-operations | 615 | 0 | 0.00% | 56.9 | Wrong target | **Stop:** #57, off-topic. No further work. Do not write more RevOps content. |
| spin-selling | 386 | 3 | 0.78% | 20.8 | Page 2 push | **Optimize:** Re-angle with a "SPIN discovery call notes template" and a CTA to /use-cases/sales-calls. |
| sales-enablement-tools | 365 | 0 | 0.00% | 9.2 | Snippet problem | **Optimize:** #2 for "what does sales enablement software typically cost?" (AI search). Add a cost table near the top. |
| quarterly-business-review-template | 169 | 0 | 0.00% | 55.6 | Wrong target | **Stop:** #56. No further work. |
| sales-forecast-template | 146 | 1 | 0.68% | 10.4 | Page 2 push | **Stop:** 146 impr at #10. Leave as is. |
| mutual-action-plan | 128 | 0 | 0.00% | 35.0 | Wrong target | **Stop:** 128 impr at #35. No further work. |
| lead-qualification | 85 | 0 | 0.00% | 21.1 | Low impressions | **Stop:** 85 impr. No further work. |
| sales-conversation-intelligence | 72 | 0 | 0.00% | 16.2 | Low impressions | **Optimize:** 72 impr. Target "conversation intelligence platform" (880/mo, SD 37), already tracked in Ubersuggest. |
| key-account-planning-process | 34 | 0 | 0.00% | 24.5 | Low impressions | **Stop:** 34 impr. No further work. |
| meddic-sales | 33 | 0 | 0.00% | 67.1 | Low impressions | **Optimize:** #67. Add a MEDDIC call notes template. Otherwise stop. |
| bant-sales-qualification | 29 | 0 | 0.00% | 22.6 | Low impressions | **Optimize:** Add a BANT call notes template. Otherwise stop. |
| call-coaching-software | 5 | 0 | 0.00% | 24.2 | New (<3 weeks) | **Hold:** New. Links to /use-cases/sales-calls. |
| objection-handling | 3 | 0 | 0.00% | 7.7 | New (<3 weeks) | **Hold:** New. Avoma ranks with this topic but gets little traffic, so keep expectations low. |
| sales-call-recording-software | 0 | 0 | 0.00% |  | New (<3 weeks) | **Hold:** New, 4 internal links. "sales call recording software" is 110/mo at SD 31 and a $108 CPC: link to it from every sales post. |
| discovery-call-questions | 0 | 0 | 0.00% |  | New (<3 weeks) | **Hold:** New, 5 internal links. Link to it from spin-selling, bant and use-cases/sales-calls. |

### Meeting prep & knowledge (6 posts, 7 clicks, 1,326 impressions)

| Post | Impr. | Clicks | CTR | Pos | Diagnosis | Action |
|---|---|---|---|---|---|---|
| meeting-preparation | 488 | 7 | 1.43% | 8.7 | Snippet problem | **Optimize:** Working (1.4%). Add an "AI meeting prep tools" H2 ("ai meeting preparation tool" #19) featuring Lynkk's pre-call briefing. |
| founders-meeting-notes | 388 | 0 | 0.00% | 6.7 | Snippet problem | **Optimize:** 388 impr at #6.7, 0 clicks, all from AI-search questions. Answer them word for word in H2s so AI answers name Lynkk. |
| meeting-knowledge-management | 297 | 0 | 0.00% | 8.9 | Page 2 push | **Optimize:** 297 impr at #8.9, 0 clicks, from AI-search questions. Add a direct answer FAQ and a Lynkk knowledge graph demo. |
| meeting-minutes-to-jira | 142 | 0 | 0.00% | 10.2 | Page 2 push | **Optimize:** #10, low volume. Link to /integrations/jira and add "meeting action items jira" as an H2. |
| best-second-brain-apps | 11 | 0 | 0.00% | 4.2 | New (<3 weeks) | **Hold:** New. Ranks #4 already on 11 impressions. |
| personal-knowledge-management | 0 | 0 | 0.00% |  | New (<3 weeks) | **Hold:** New. Ubersuggest: these KM keywords are SD 36-62, so treat them as long-term. |

### Security (2 posts, 0 clicks, 101 impressions)

| Post | Impr. | Clicks | CTR | Pos | Diagnosis | Action |
|---|---|---|---|---|---|---|
| is-it-legal-to-record-a-meeting | 95 | 0 | 0.00% | 14.6 | Low impressions | **Optimize:** Retitle to "Is It Legal to Record a Meeting? One-Party vs Two-Party States". Otter ranks #4 for "is it illegal to record a conversation" (1,600/mo). |
| ai-notetaker-security | 6 | 0 | 0.00% | 4.2 | New (<3 weeks) | **Hold:** New. Matches the regulated-team AI-search questions (SSO, SCIM, retention). Link to it from zoom-ai-companion-alternatives. |

## 6. Site structure and internal links

Create 6 blog hub pages at `/blog/topic/[hub]` (300-500 words plus a list of posts). Every post links up to its hub, across to 2-3 sibling posts, and to one product page.

| Hub | Funnel | Hub page | Posts link down to |
|---|---|---|---|
| Meeting platform guides | TOFU | `/blog/topic/zoom-meet-teams` | /integrations/zoom, /integrations/google-meet, /integrations/microsoft-teams, /features/chrome-extension |
| Meeting templates | TOFU | `/blog/topic/meeting-templates` | /features/meeting-notes, /features/action-items |
| Sales meetings | TOFU/MOFU | `/blog/topic/sales-meetings` | /use-cases/sales-calls, /pricing |
| AI note takers | MOFU | `/blog/best-ai-note-takers (pillar)` | /features/meeting-notes, /features/meeting-bot, /compare, /pricing |
| Compare tools | MOFU/BOFU | `/compare (pillar)` | /compare/[tool], /pricing |
| Transcription and languages | TOFU/MOFU | `/blog/ai-transcription-software (pillar)` | /features/multilingual-transcription, /features/hinglish-transcription, /download |

**Linking rules:**

- TOFU post → one CTA in context after the step or template, e.g. "No Zoom transcript? Lynkk records Zoom on any Zoom plan."
- MOFU post → comparison table with Lynkk as a row, linking to its /compare page.
- Homepage → "Free meeting templates and guides" block linking to all 6 hubs.
- Anchor text = the target keyword of the page you link to ("AI note taker for Teams", not "click here").
- Under-linked today (blog links): /features 0, /use-cases 0, Teams integration 2, team standups 2, Hinglish 5.
- Park (no new posts): sales theory (RevOps, BANT, MEDDIC, QBR), medical (until HIPAA status is confirmed), extra Mac/dictation posts. Merge dictation-on-mac into speech-to-text-mac with a 301.

## 7. Technical fixes

| Fix | Detail |
|---|---|
| Request indexing (GSC URL Inspection) | 6 indexable pages have zero impressions: /blog/best-free-ai-note-takers, /blog/zoom-meeting-recorders, /blog/ai-voice-recorders, /blog/legal-transcription-service, /integrations/pipedrive, /integrations/zoho-crm. If "Crawled, currently not indexed": add a unique section and links from the strongest pages in the hub. |
| Regional price in headings | Two homepage H2s read "$4₹250" to search engines. Keep prices out of headings. |
| Sitemap lastmod | 52 URLs share one lastmod (30 Oct 12:00). Use the real edit date. |
| best-ai-meeting-notes-for-teams | 1 impression and not in the sitemap. Add it to the sitemap or 301 it to best-ai-note-takers. |
| Ubersuggest tracked keywords | Remove the 10 knowledge-management terms. Add: ai note taker for teams, ai note taker for zoom, granola vs otter ai, otter ai vs fireflies, fathom vs otter ai, granola pricing, fathom pricing, google meet transcript, zoom transcript, action items template, daily standup meeting template; India: zoom meeting recorder, meeting assistant software, transcription software, template for meeting minutes, hindi audio to text converter. |
| Ubersuggest "page not allowed" warning | Lists sign-in and sign-up URLs, which are correctly noindexed. Dismiss it. |

## 8. Free to paid: service pages, find and replace

Find the text in the "Find" column and replace it with the "Replace with" column. Some lines are fragments: replace exactly that text and leave the words around it. "…" means the sentence continues unchanged. The pricing page and the legal pages are not included.

### Fix once, site-wide

| Where | Find | Replace with |
|---|---|---|
| Footer CTA strip (template) | 5 hours of AI notes on the free plan · | Lynkk Pro from $4 a month · |
| "Start for free" buttons (header, hero, CTA bands, every page) | Start for free | Get Lynkk Pro |
| "Sign up free" links | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| After "Pro, at $4 a month" on feature and integration pages | , makes summaries unlimited | , includes unlimited AI summaries |
| Plan tables everywhere | The Free column, Free card or "Lynkk · Free · $0" row | Remove. Show Pro and Enterprise only. |

### Confirm before publishing

- **Cancelling Pro:** the FAQ and support pages promise that "going back to Free deletes nothing". With no free plan, the team needs to decide what happens to a user's notes after they cancel. Those lines are marked [Confirm first].
- **Annual price:** compare pages and the FAQ say "$40 a year (₹2,500), two months free" and "2 months free" on the Yearly toggle. Keep only if the annual plan is still sold. ("Two months free" here is a discount, not a free plan, so it is fine if the plan exists.)
- **Meeting video:** Pro included video from the bot, and only Pro is left, so the bot labels now say "audio and video". Check this is right.
- **CRM:** the CRM integration pages and the integrations hub say calls are logged in the CRM, but the plan table lists CRM sync as "Not yet".

### Homepage

#### /

15 changes · https://lynkk.ai

| Where | Find | Replace with |
|---|---|---|
| Plan table | Free (column in "Find the right plan for the way you sell") | Remove the Free column. Show Pro and Enterprise only. |
| Plan card / price table | Free · $0 · ₹0 / forever | Remove the Free plan card. Show Pro ($4 / ₹250 a month) and Enterprise only. |
| Meta | Lynkk is the AI meeting assistant that takes notes on Zoom, Meet, Teams and in person, then drafts your follow-ups. 17 languages. Start free. | The AI meeting assistant for Zoom, Google Meet, Teams and in-person meetings. Notes, action items and follow-up emails after every call. From $4/mo. |
| Body | Free stays free for everyone. | Remove (Lynkk has no free plan). |
| Body | / forever | Remove (part of the Free plan card). |
| Body | For your first conversations. | Remove (part of the Free plan card). |
| Body | Your first 5 hours of AI notes | Remove (part of the Free plan card). |
| Body | Everything in Free | Unlimited notes, up to 2 hours each, the meeting bot, every language, search, tasks and Jira |
| Body | First 5 hours | Remove (Free column of the plan table). |
| Body | Unlimited notes, up to 2 hours each, and your first 5 hours of AI notes. No credit card is required. Pro adds unlimited summaries and Ask Lynkk across every call. | Unlimited notes, up to 2 hours each, unlimited AI notes, Ask Lynkk across every call and answers in Slack, for $4 a month (₹250 in India). Enterprise adds a shared workspace for up to 10 people. |
| Body | Free to start | From $4 a month |
| Body (price card) | Cancel any time. No card for the free plan. | Cancel any time. |
| Body (price card) | No credit card required. | Remove (part of the Free plan card). |
| FAQ question | What’s included in the free plan? | What’s included in Lynkk Pro? |
| FAQ answer | …record from the Chrome extension with no bot, or let the Mac app notice the call. The bot is on the free plan. | …record from the Chrome extension with no bot, or let the Mac app notice the call. The bot is included with Lynkk Pro. |

### Core pages

#### /faq

9 changes · https://lynkk.ai/faq

| Where | Find | Replace with |
|---|---|---|
| Meta | Answers about Lynkk: the meeting bot, the Mac app, languages, what a note holds, Ask Lynkk, privacy, and what Free and Pro include. Search or browse by topic. | Answers about Lynkk: the meeting bot, the Mac app, languages, what a note holds, Ask Lynkk, privacy, and what Pro and Enterprise include. |
| Body | There is no trial, because Free has no time limit. | There is no free plan or trial: Pro is $4 (₹250) a month. |
| Body | or the browser. Your first 5 hours of AI notes are free, in total rather than per month. After that, new notes still get their recording, transcript and search, without the summary and action items. Free also has unlimited dictation on the Mac, every language, Jira send, share links and the full export. No card needed. | or the browser, with unlimited AI notes, unlimited dictation on the Mac, every language, Jira send, share links and the full export. |
| Body | . To cancel, open Settings, Account and press Manage subscription, which opens Paddle's billing page. Pro keeps running until the end of the period you paid for, and going back to Free deletes nothing. If a workspace pays for your Pro, the workspace owner handles billing. | . To cancel, open Settings, Account and press Manage subscription, which opens Paddle's billing page. Pro keeps running until the end of the period you paid for. If an Enterprise workspace pays for your Pro, the workspace admin handles billing. |
| Body | Free to start, on your Mac or in the browser. Record a meeting and see what Lynkk writes. | Lynkk Pro is $4 a month, on your Mac or in the browser. Record a meeting and see what Lynkk writes. |
| Body (sign-up answer) | …confirmed by a code we send you. No card is needed. Then connect Google Calendar… | …confirmed by a code we send you, then choose Lynkk Pro. Then connect Google Calendar… |
| Topic description | Free, Pro, workspaces, cancelling and refunds. | Pro, Enterprise, cancelling and refunds. |
| FAQ question | What can I do on the free plan? | What does Lynkk Pro include? |
| FAQ question | Is there a free trial, and can I get a refund? | Is there a free trial, and can I get a refund? (keep; answer is the line above) |

#### /security

1 change · https://lynkk.ai/security

| Where | Find | Replace with |
|---|---|---|
| Body | Free to start, on your Mac or in the browser. | Lynkk Pro is $4 a month, on your Mac or in the browser. |

#### /support

6 changes · https://lynkk.ai/support

| Where | Find | Replace with |
|---|---|---|
| Body | The agreement for using Lynkk, on Free and on Pro. | The agreement for using Lynkk Pro and Enterprise. |
| Body | Pro keeps running to the end of the period you paid for, and going back to Free deletes nothing. If a workspace pays for your Pro, there is no button: the workspace owner handles billing. | Pro keeps running to the end of the period you paid for. If an Enterprise workspace pays for your Pro, there is no button: the workspace admin handles billing. |
| Body | On Free, the first 5 hours of AI notes are free, in total. After that, new notes still get their recording, transcript and search, without a summary or action items. | AI notes need an active Lynkk Pro subscription. |
| Body | If you're on Pro, or under the 5 hours, and a note still has no summary, write to us with its link. | If you're on Pro and a note still has no summary, write to us with its link. |
| Body | What Free includes and what Pro adds. | What Pro and Enterprise include. |
| Body | Free to start, on your Mac or in the browser. If anything goes wrong, a person reads your email. | Lynkk Pro is $4 a month, on your Mac or in the browser. If anything goes wrong, a person reads your email. |

### Feature and product pages

#### /download

3 changes · https://lynkk.ai/download

| Where | Find | Replace with |
|---|---|---|
| Meta | Lynkk for Mac records Zoom, Meet, Teams and Slack huddle calls with no bot in the call, and types what you say in any app. Free on Apple silicon. | Lynkk for Mac records Zoom, Meet, Teams and Slack huddle calls with no bot in the call, and types what you say in any app. Runs on Apple silicon. |
| Body | free to install | Remove "free to install". The app needs Lynkk Pro to use. |
| FAQ question | Is dictation free? | Which plan includes dictation? |

#### /features

3 changes · https://lynkk.ai/features

| Where | Find | Replace with |
|---|---|---|
| Card: meeting bot | …It shows up as a visible participant, and it is on the free plan. | …It shows up as a visible participant, and it is included with Lynkk Pro. |
| Card: dictation | Hold one key and talk. Your words are typed at the cursor in any app on your Mac. Free, with unlimited words. | Hold one key and talk. Your words are typed at the cursor in any app on your Mac, with unlimited words. |
| Card: Chrome extension | Nothing joins the call, so nobody sees a bot. It works on the free plan, next to the web app and the Mac app. | Nothing joins the call, so nobody sees a bot. It works next to the web app and the Mac app. |

#### /features/action-items

2 changes · https://lynkk.ai/features/action-items

| Where | Find | Replace with |
|---|---|---|
| Body | Free for your first 5 hours of AI notes, then Pro at | Lynkk Pro, |
| Body | Action items, the task board and Send to Jira work on the free plan, for meetings within your 5 hours of AI notes. Pro, at | Action items, the task board and Send to Jira are all included in Lynkk Pro, which, at |

#### /features/ask-your-meetings

1 change · https://lynkk.ai/features/ask-your-meetings

| Where | Find | Replace with |
|---|---|---|
| Body | Ask Lynkk is part of Pro. Workspace members get Pro through their workspace. The free plan records and summarizes your calls, with tasks and Jira send. | Ask Lynkk is part of Pro, at $4 a month. Members of an Enterprise workspace get Pro through their workspace. |

#### /features/chrome-extension

3 changes · https://lynkk.ai/features/chrome-extension

| Where | Find | Replace with |
|---|---|---|
| Body | Is the Lynkk Chrome extension free? | Which plan includes the Lynkk Chrome extension? |
| Body | Meet, Zoom, Teams · Audio only · Works on Free | Meet, Zoom, Teams · Audio only · Included with Pro |
| FAQ answer | Yes. It is included on the Free plan, where recording, transcription and the summary all work. On Pro, the note also gets what Pro adds, such as Ask Lynkk. | It is included with Lynkk Pro ($4 a month): recording, transcription, the summary and Ask Lynkk all work. |

#### /features/dictation

4 changes · https://lynkk.ai/features/dictation

| Where | Find | Replace with |
|---|---|---|
| Meta | Hold fn and speak. Lynkk types your words into any app on your Mac, cleans up the ums, and lets you circle anything on screen. Free on every plan. | Hold fn and speak. Lynkk types your words into any app on your Mac, cleans up the ums, and lets you circle anything on screen. Included with Lynkk Pro. |
| Badge (2 places) | Start free · Set up in minutes · Apple silicon | Lynkk Pro · Set up in minutes · Apple silicon |
| FAQ question | What do I need, and is it free? | What do I need? |
| FAQ answer | A Mac with Apple silicon on macOS 14.2 (Sonoma) or later. Dictation is free on every plan, with everything included: … | A Mac with Apple silicon on macOS 14.2 (Sonoma) or later, and Lynkk Pro. Dictation includes everything: … |

#### /features/hinglish-transcription

4 changes · https://lynkk.ai/features/hinglish-transcription

| Where | Find | Replace with |
|---|---|---|
| Title | Hinglish Transcription Software for Meetings, Free \| Lynkk | Hinglish Transcription Software for Meetings \| Lynkk |
| Body | Hinglish is on every plan, Free included, like every other language. The free plan writes AI notes for your first 5 hours of meetings. Pro, at | Hinglish is included in Lynkk Pro, like every other language. Pro, at |
| Body | Every plan, Free included. Language is never a paid feature. The free plan records and transcribes unlimited notes and writes AI notes for your first 5 hours of meetings; Pro, at | Every plan includes it: language is never an extra. Lynkk Pro records and transcribes unlimited notes in every language, with AI notes for every meeting, and Pro, at |
| Link text | free Hindi audio to text converter options | No change (links to a blog post about free tools). |

#### /features/meeting-bot

6 changes · https://lynkk.ai/features/meeting-bot

| Where | Find | Replace with |
|---|---|---|
| Title | Free AI Meeting Bot for Zoom, Google Meet & Teams \| Lynkk | AI Meeting Bot for Zoom, Google Meet & Teams \| Lynkk |
| H2 | Free, audio only | Audio and video, on Pro |
| Body | Free, audio only | Audio and video, on Pro |
| Body | The bot is on every plan. On the free plan it records audio, and your first 5 hours of meetings get AI notes and action items. After that, meetings are still recorded and transcribed, and you can search them, but no summary is written. Pro, at | The bot is included with Lynkk Pro. Every meeting gets AI notes and action items, and Pro, at |
| Body | The bot is on the free plan and records audio. Recording the meeting video is part of Pro. A live transcript panel shows the words while the meeting runs. | The bot is included with Lynkk Pro and records the audio and the meeting video. A live transcript panel shows the words while the meeting runs. |
| FAQ answer | On Pro it records the meeting video in speaker view as well as the audio. On the free plan it records audio only. Either way you get the transcript, summary and action items. | On Pro it records the meeting video in speaker view as well as the audio, and you get the transcript, summary and action items. |

#### /features/meeting-notes

4 changes · https://lynkk.ai/features/meeting-notes

| Where | Find | Replace with |
|---|---|---|
| Meta | Lynkk's AI note taker writes your meeting notes when the call ends: AI summary, decisions, action items and minutes, online or in person. Start free. | Lynkk's AI note taker writes your meeting notes when the call ends: AI summary, decisions, action items and minutes, online or in person. From $4 a month. |
| Body | Is Lynkk a free AI note taking app? | Is Lynkk free? (new answer below) |
| FAQ answer (Is Lynkk free?) | Yes, you can start free: no limit on notes, 5 lifetime hours of AI notes, the meeting bot with audio, tasks and Send to Jira. Pro adds per-note chat, Summary Shapes, Ask Lynkk and meeting video. | No. Lynkk Pro is $4 a month (₹250 in India): no limit on notes, unlimited AI notes, the meeting bot with video, tasks, Send to Jira, per-note chat, Summary Shapes and Ask Lynkk. |
| Badge | Free plan · No limit on notes · Mac and web | Lynkk Pro · No limit on notes · Mac and web |

#### /features/multilingual-transcription

1 change · https://lynkk.ai/features/multilingual-transcription

| Where | Find | Replace with |
|---|---|---|
| Body | Every language is on every plan, Free included. Every plan records and transcribes unlimited notes in every language, Hinglish included, and the free plan writes AI notes for your first 5 hours of meetings. Pro, at | Every language is included. Lynkk Pro records and transcribes unlimited notes in every language, Hinglish included, and writes AI notes for every meeting. Pro, at |

#### /how-it-works

1 change · https://lynkk.ai/how-it-works

| Where | Find | Replace with |
|---|---|---|
| CTA | Start free | Get Lynkk Pro |

#### /meeting-and-dictation

13 changes · https://lynkk.ai/meeting-and-dictation

| Where | Find | Replace with |
|---|---|---|
| Title | Meeting Notes and Free AI Dictation in One Mac App \| Lynkk | Meeting Notes and AI Dictation in One Mac App \| Lynkk |
| Meta | Lynkk writes up your meetings and types what you say into any app on your Mac. Dictation is free on every plan, with unlimited words. | Lynkk writes up your meetings and types what you say into any app on your Mac. Dictation is included with Lynkk Pro, with unlimited words. |
| H2 | Unlimited words. Free. | Unlimited words, included with Pro. |
| Body | Is Lynkk dictation really free? | Is dictation included in Lynkk Pro? |
| Body | A Mac with Apple silicon on macOS 14.2 (Sonoma) or later. The free plan also includes unlimited meeting notes and your first 5 hours of AI summaries. | A Mac with Apple silicon on macOS 14.2 (Sonoma) or later, and Lynkk Pro ($4 a month), which also includes unlimited meeting notes and AI summaries. |
| Meta/intro | Lynkk writes up your calls and types what you say into any app on your Mac. Dictation is free, with no word limit. | Lynkk writes up your calls and types what you say into any app on your Mac. Dictation has no word limit. |
| Label | Dictation free | Dictation included |
| Label | Words you can dictate on the free plan | Words you can dictate on Pro |
| Label | Free dictation | Unlimited dictation |
| Heading | Free on every plan | Included with Lynkk Pro |
| FAQ answer | Yes. Dictation is free on every plan with no word limit. Instant, Accurate and Polished… | Yes. Dictation is included with Lynkk Pro with no word limit. Instant, Accurate and Polished… |
| Body | Both take meeting notes without a bot and both now dictate for free. Lynkk keeps the recording… | Both take meeting notes without a bot and both dictate. Lynkk keeps the recording… |
| Body | …Lynkk has no word limit on any plan, and its meeting notes keep the audio with the summary. | No change. |

#### /web-app

3 changes · https://lynkk.ai/web-app

| Where | Find | Replace with |
|---|---|---|
| Body | Yes. Recording, transcripts, tasks and sharing are free, and the free plan includes 5 hours of AI notes. Pro, at | It is included with Lynkk Pro: recording, transcripts, tasks, sharing and AI notes. Pro, at |
| Body | Free to start. Read the note here when the meeting ends. | Lynkk Pro is $4 a month. Read the note here when the meeting ends. |
| FAQ question | Is the web app free? | Which plan includes the web app? |

### Use-case pages

#### /use-cases

2 changes · https://lynkk.ai/use-cases

| Where | Find | Replace with |
|---|---|---|
| Body | Yes. The free plan includes 5 hours of AI notes and recordings of up to 2 hours each. Pro adds unlimited AI notes, Ask Lynkk across your notes and Summary Shapes. | No. Lynkk Pro is $4 a month (₹250 in India), with unlimited AI notes, recordings of up to 2 hours each, Ask Lynkk across your notes and Summary Shapes. |
| CTA | Download the Mac app, or start free in the browser | Download the Mac app, or use Lynkk in the browser, from $4 a month |

#### /use-cases/customer-research

4 changes · https://lynkk.ai/use-cases/customer-research

| Where | Find | Replace with |
|---|---|---|
| Meta | Record customer calls and focus groups, then ask Lynkk what customers said across all of them, with their exact words. AI for marketing teams. Start free. | Record customer calls and focus groups, then ask Lynkk what customers said across all of them, with their exact words. AI for marketing teams. From $4 a month. |
| CTA band | Try Lynkk … It's free to start. | Keep the first sentence; replace "It's free to start." with "Lynkk Pro is $4 a month." |
| FAQ question | Is it free? | How much does it cost? |
| FAQ answer | Yes, there's a free plan. Asking Lynkk across all your calls is part of Pro. | Lynkk Pro is $4 a month (₹250 in India), and asking Lynkk across all your calls is included. |

#### /use-cases/field-interviews

2 changes · https://lynkk.ai/use-cases/field-interviews

| Where | Find | Replace with |
|---|---|---|
| Meta | Record field interviews on your Mac with no internet. Lynkk uploads them later and writes the notes, with Hindi transcription, Hinglish and more. Start free. | Record field interviews on your Mac with no internet. Lynkk uploads them later and writes the notes, with Hindi transcription, Hinglish and more. From $4 a month. |
| CTA band | Try Lynkk … It's free to start. | Keep the first sentence; replace "It's free to start." with "Lynkk Pro is $4 a month." |

#### /use-cases/financial-advisors

5 changes · https://lynkk.ai/use-cases/financial-advisors

| Where | Find | Replace with |
|---|---|---|
| Meta | An AI note taker for financial advisors: record client reviews and get goals, life changes and tasks written for you. Your data stays in your region. Start free. | An AI note taker for financial advisors: record client reviews and get goals, life changes and tasks written for you. Your data stays in your region. From $4 a month. |
| Body | If you want simple, private notes from every client meeting, try Lynkk free. | If you want simple, private notes from every client meeting, try Lynkk Pro for $4 a month. |
| CTA band | Try Lynkk … It's free to start. | Keep the first sentence; replace "It's free to start." with "Lynkk Pro is $4 a month." |
| FAQ question | Is it free? | How much does it cost? |
| FAQ answer | Yes, there's a free plan. Asking Lynkk about past reviews is part of Pro. | Lynkk Pro is $4 a month (₹250 in India), and asking Lynkk about past reviews is included. |

#### /use-cases/lawyers

2 changes · https://lynkk.ai/use-cases/lawyers

| Where | Find | Replace with |
|---|---|---|
| Meta | AI for law firms that records client meetings and writes the facts, documents to collect and next steps. Private, and your data stays in your region. Start free. | AI for law firms that records client meetings and writes the facts, documents to collect and next steps. Private, and your data stays in your region. From $4 a month. |
| CTA band | Try Lynkk … It's free to start. | Keep the first sentence; replace "It's free to start." with "Lynkk Pro is $4 a month." |

#### /use-cases/lectures

1 change · https://lynkk.ai/use-cases/lectures

| Where | Find | Replace with |
|---|---|---|
| CTA band | Try Lynkk … It's free to start. | Keep the first sentence; replace "It's free to start." with "Lynkk Pro is $4 a month." |

#### /use-cases/one-on-one-meetings

4 changes · https://lynkk.ai/use-cases/one-on-one-meetings

| Where | Find | Replace with |
|---|---|---|
| Meta | Lynkk records your one on one meeting, writes the wins, problems and tasks, and reminds you what's still open before the next one. Start free. | Lynkk records your one on one meeting, writes the wins, problems and tasks, and reminds you what's still open before the next one. From $4 a month. |
| CTA band | Try Lynkk … It's free to start. | Keep the first sentence; replace "It's free to start." with "Lynkk Pro is $4 a month." |
| FAQ question | Is it free? | How much does it cost? |
| FAQ answer | Yes, there's a free plan. Asking about past 1:1s and the 1:1 note format is part of Pro. | Lynkk Pro is $4 a month (₹250 in India), and asking about past 1:1s and the 1:1 note format is included. |

#### /use-cases/real-estate-agents

4 changes · https://lynkk.ai/use-cases/real-estate-agents

| Where | Find | Replace with |
|---|---|---|
| Meta | One of the real estate AI tools that records client calls and meetings, then writes each buyer's budget, must-haves and next steps. Start free. | One of the real estate AI tools that records client calls and meetings, then writes each buyer's budget, must-haves and next steps. From $4 a month. |
| CTA band | Try Lynkk … It's free to start. | Keep the first sentence; replace "It's free to start." with "Lynkk Pro is $4 a month." |
| FAQ question | Is it free? | How much does it cost? |
| FAQ answer | Yes, there's a free plan. Asking Lynkk about past clients is part of Pro. | Lynkk Pro is $4 a month (₹250 in India), and asking Lynkk about past clients is included. |

#### /use-cases/sales-calls

2 changes · https://lynkk.ai/use-cases/sales-calls

| Where | Find | Replace with |
|---|---|---|
| Meta | Lynkk is the AI sales assistant and conversation intelligence platform that records your sales calls and writes the next steps for you. Start free. | Lynkk is the AI sales assistant and conversation intelligence platform that records your sales calls and writes the next steps for you. From $4 a month. |
| CTA band | Try Lynkk … It's free to start. | Keep the first sentence; replace "It's free to start." with "Lynkk Pro is $4 a month." |

#### /use-cases/team-standups

2 changes · https://lynkk.ai/use-cases/team-standups

| Where | Find | Replace with |
|---|---|---|
| Meta | Lynkk joins your daily standup meeting and writes it down: yesterday, today, blockers, and tasks with owners. AI for project managers. Start free. | Lynkk joins your daily standup meeting and writes it down: yesterday, today, blockers, and tasks with owners. AI for project managers. From $4 a month. |
| CTA band | Try Lynkk … It's free to start. | Keep the first sentence; replace "It's free to start." with "Lynkk Pro is $4 a month." |

#### /use-cases/user-interviews

2 changes · https://lynkk.ai/use-cases/user-interviews

| Where | Find | Replace with |
|---|---|---|
| Meta | Record user and customer interviews on a call or in person. Lynkk writes the transcript with speaker labels, the key points and open questions. Start free. | Record user and customer interviews on a call or in person. Lynkk writes the transcript with speaker labels, the key points and open questions. From $4 a month. |
| CTA band | Try Lynkk … It's free to start. | Keep the first sentence; replace "It's free to start." with "Lynkk Pro is $4 a month." |

### Integration pages

#### /integrations

2 changes · https://lynkk.ai/integrations

| Where | Find | Replace with |
|---|---|---|
| Body | Free to start, on your Mac or in the browser. | Lynkk Pro is $4 a month, on your Mac or in the browser. |
| Body | Google Calendar, Slack and the meeting bot with audio are free. Pro adds video from the bot, Ask Lynkk and answers in Slack. CRM logging is priced with our sales team. | Google Calendar, Slack, the meeting bot (audio and video), Ask Lynkk and answers in Slack are all in Lynkk Pro, $4 a month. [Confirm] CRM logging: the plan table says "Not yet". |

#### /integrations/attio

1 change · https://lynkk.ai/integrations/attio

| Where | Find | Replace with |
|---|---|---|
| CTA button | Start for free | Get Lynkk Pro (covered by the template change). [Confirm] these CRM pages also claim CRM logging, which the plan table lists as "Not yet". |

#### /integrations/google-calendar

3 changes · https://lynkk.ai/integrations/google-calendar

| Where | Find | Replace with |
|---|---|---|
| Body | Free to start. The notetaker joins your next Zoom, Meet or Teams meeting. | Lynkk Pro is $4 a month. The notetaker joins your next Zoom, Meet or Teams meeting. |
| FAQ question | Is the Google Calendar integration free? | Which plan includes the Google Calendar integration? |
| FAQ answer | Yes. Connecting, Home, auto-join and the recap email are free on every plan. Booking a follow-up from Ask Lynkk is part of Pro, at | Lynkk Pro. Connecting, Home, auto-join, the recap email and booking a follow-up from Ask Lynkk are all included, at |

#### /integrations/google-meet

9 changes · https://lynkk.ai/integrations/google-meet

| Where | Find | Replace with |
|---|---|---|
| Title | Free AI Note Taker for Google Meet (Bot or Chrome Extension) | AI Note Taker for Google Meet, No Workspace Plan Needed |
| Meta | Free AI note taker for Google Meet, no Workspace plan needed. A notetaker joins from your calendar, or the Chrome extension records your tab. | An AI note taker for Google Meet with no Workspace plan needed. A notetaker joins from your calendar, or the Chrome extension records your tab. From $4/mo. |
| H2 | Free AI note taker for Google Meet, on any Google account | AI note taker for Google Meet, on any Google account |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | Every Lynkk plan records and transcribes unlimited Meet calls, up to 2 hours each, in 17 languages with speaker labels. Free also writes AI notes for your first 5 hours of meetings: a summary, action items with owners and decisions. | Lynkk Pro records and transcribes unlimited Meet calls, up to 2 hours each, in 17 languages with speaker labels, and writes AI notes for every meeting: a summary, action items with owners and decisions. |
| Body | Yes. Lynkk's free plan includes the notetaker for Meet (audio) and the Chrome extension, with unlimited notes of up to 2 hours each and the first 5 hours of AI notes. Pro, at | A few tools have free plans, but Lynkk is not one of them. Lynkk Pro includes the notetaker for Meet and the Chrome extension, with unlimited notes of up to 2 hours each and unlimited AI notes, at |
| Body | Free to start. Connect Google Calendar and the notetaker joins your next Meet call. | Lynkk Pro is $4 a month. Connect Google Calendar and the notetaker joins your next Meet call. |
| Plan table label | Free plan | Remove the Free plan row or column. |
| Body | It works in Chrome, Edge, Brave and Arc, on the free plan. | It works in Chrome, Edge, Brave and Arc. |

#### /integrations/hubspot

1 change · https://lynkk.ai/integrations/hubspot

| Where | Find | Replace with |
|---|---|---|
| CTA button | Start for free | Get Lynkk Pro (covered by the template change). [Confirm] these CRM pages also claim CRM logging, which the plan table lists as "Not yet". |

#### /integrations/jira

2 changes · https://lynkk.ai/integrations/jira

| Where | Find | Replace with |
|---|---|---|
| Body | Free to start. Send the action items from your next call. | Lynkk Pro is $4 a month. Send the action items from your next call. |
| FAQ question | Is the Jira integration free? | Which plan includes the Jira integration? (check the answer below it; it is likely "Yes, on every plan": change to "It is included with Lynkk Pro.") |

#### /integrations/microsoft-teams

8 changes · https://lynkk.ai/integrations/microsoft-teams

| Where | Find | Replace with |
|---|---|---|
| H2 | Free Teams note taker (no Copilot license) | Teams note taker without a Copilot license |
| Body | Lynkk Free | Lynkk Pro ($4 a month) |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | Every plan records and transcribes unlimited Teams calls, up to 2 hours each, in 17 languages. Free also writes AI notes for your first 5 hours of meetings, with no Microsoft license and no admin setup. | Lynkk Pro records and transcribes unlimited Teams calls, up to 2 hours each, in 17 languages, and writes AI notes for every meeting, with no Microsoft license and no admin setup. |
| Body | Yes. Lynkk's free plan includes the notetaker for Teams (audio), unlimited notes of up to 2 hours each and the first 5 hours of AI notes. Pro, at | A few tools have free plans, but Lynkk is not one of them. Lynkk Pro includes the notetaker for Teams, unlimited notes of up to 2 hours each and unlimited AI notes, at |
| Body | Free to start, with no Microsoft license needed. | Lynkk Pro is $4 a month, with no Microsoft license needed. |
| Plan table label | Free plan | Remove the Free plan row or column. |
| Heading | What you get for free | What you get with Lynkk Pro |

#### /integrations/pipedrive

1 change · https://lynkk.ai/integrations/pipedrive

| Where | Find | Replace with |
|---|---|---|
| CTA button | Start for free | Get Lynkk Pro (covered by the template change). [Confirm] these CRM pages also claim CRM logging, which the plan table lists as "Not yet". |

#### /integrations/salesforce

1 change · https://lynkk.ai/integrations/salesforce

| Where | Find | Replace with |
|---|---|---|
| CTA button | Start for free | Get Lynkk Pro (covered by the template change). [Confirm] these CRM pages also claim CRM logging, which the plan table lists as "Not yet". |

#### /integrations/zoho-crm

1 change · https://lynkk.ai/integrations/zoho-crm

| Where | Find | Replace with |
|---|---|---|
| CTA button | Start for free | Get Lynkk Pro (covered by the template change). [Confirm] these CRM pages also claim CRM logging, which the plan table lists as "Not yet". |

#### /integrations/zoom

14 changes · https://lynkk.ai/integrations/zoom

| Where | Find | Replace with |
|---|---|---|
| Title | Free AI Note Taker for Zoom Meetings (Bot or No Bot) \| Lynkk | AI Note Taker for Zoom, Even on Free Zoom (Bot or No Bot) |
| Meta | Free AI note taker for Zoom, even on free Zoom plans. Send a bot or record from your Mac, and get the summary and action items after the call. | An AI note taker that works on free Zoom plans. Send a bot or record from your Mac, and get the summary and action items. From $4/mo. |
| H2 | Free AI note taker for Zoom: what you get | AI note taker for Zoom: what you get |
| Body | Lynkk is a free AI note taker for Zoom. | Lynkk is an AI note taker for Zoom, from $4 a month. |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | Every plan records and transcribes unlimited Zoom calls, up to 2 hours each, in 17 languages. Free also writes AI notes for your first 5 hours of meetings, with no card needed. | Lynkk Pro records and transcribes unlimited Zoom calls, up to 2 hours each, in 17 languages, and writes AI notes for every meeting. |
| Body | After the first 5 hours, calls are still recorded, transcribed and searchable. Pro, at | Every call is recorded, transcribed and searchable. Pro, at |
| Body | No card needed. | Remove. |
| Body | Yes. Lynkk's free plan has unlimited notes of up to 2 hours each and the first 5 hours of AI notes, with no card needed, and it works on a free Zoom account. After that you keep the transcript and search. Pro, at | A few tools have free plans, but Lynkk is not one of them. Lynkk Pro has unlimited notes of up to 2 hours each and unlimited AI notes, and it works on a free Zoom account. Pro, at |
| Body | Free to start. Record with no bot from your Mac, or let the notetaker join. | Lynkk Pro is $4 a month. Record with no bot from your Mac, or let the notetaker join. |
| Body | Paste the link or let your calendar send it. Audio is free, video is on Pro. | Paste the link or let your calendar send it. The bot records audio and video. |
| Plan table label | Free plan | Remove the Free plan row or column. |
| Intro | What the free plan covers on Zoom, and what to do when the notetaker can't get in. | What Lynkk Pro covers on Zoom, and what to do when the notetaker can't get in. |
| Heading | Everything you need for a Zoom call, free | Everything you need for a Zoom call, from $4 a month |

### Compare pages

#### /compare

11 changes · https://lynkk.ai/compare

| Where | Find | Replace with |
|---|---|---|
| Body | Is Lynkk free? | Is Lynkk free? (keep the question; new answer below) |
| Body | Lynkk has a free plan that keeps recording, and puts asking across meetings in its | Lynkk has no free plan, and puts asking across meetings in its |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Notta has phone and Windows apps and file upload, and sells translation as an add-on. Lynkk has every language and Hinglish on every plan, and 2-hour notes on Free. | Notta has phone and Windows apps and file upload, and sells translation as an add-on. Lynkk Pro includes every language and Hinglish, with notes up to 2 hours each. |
| Body | Yes. The free plan has unlimited notes of up to 2 hours each, the meeting bot (audio), the Mac app, the Chrome extension and every language, and AI notes for your first 5 hours of meetings. Pro is | No. Lynkk has no free plan or trial. Lynkk Pro, with unlimited notes and AI notes, is |
| Body | Free and Pro, line by line. | Pro and Enterprise, line by line. |
| Body | Free to start, on your Mac or in the browser. Record a meeting the way you usually would, and read the note. | Lynkk Pro is $4 a month, on your Mac or in the browser. Record a meeting the way you usually would, and read the note. |
| Comparison card (Gong, Avoma, Clari Copilot) | Gong is a full revenue platform with forecasting and deal analytics. Lynkk is a notetaker you can start free today, with a public price and no contract. | Gong is a full revenue platform with forecasting and deal analytics. Lynkk is a notetaker at $4 a month, with a public price and no contract. |
| Comparison card | MeetGeek covers 100+ languages, phone apps and a long CRM list. Lynkk follows Hinglish mid-sentence, gives Free 2-hour notes and answers across calls with sources. | MeetGeek covers 100+ languages, phone apps and a long CRM list. Lynkk follows Hinglish mid-sentence, gives 2-hour notes and answers across calls with sources. |
| Reason heading | You want a free plan that keeps working | You want a low flat price with no trial clock |
| Comparison card | …, with no contract and a free plan. | …, with no contract, from $4 a month. |

#### /compare/avoma

14 changes · https://lynkk.ai/compare/avoma

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Meta | Looking for an Avoma alternative? Compare Lynkk and Avoma on the free plan, add-ons, asking across meetings and in-person recording, as of October 2026. | Looking for an Avoma alternative? Compare Lynkk and Avoma on price, add-ons, asking across meetings and in-person recording, as of October 2026. |
| H1 | Lynkk vs Avoma: an Avoma alternative with a free plan that keeps recording | Lynkk vs Avoma: an Avoma alternative from $4 a month, with in-person recording |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | After Avoma's 14-day trial, accounts drop to a Viewer role that cannot record. Lynkk Free has no end date: unlimited notes of up to 2 hours, with AI notes for the first 5 hours in total. | After Avoma's 14-day trial, accounts drop to a Viewer role that cannot record. Lynkk has no trial clock: Pro is $4 a month with unlimited notes and AI notes. |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |
| Body | …It has no coaching, no forecasting, no scheduling and no CRM sync. It does have a free plan with no end date… | …It has no coaching, no forecasting, no scheduling and no CRM sync. It does have a low flat price of $4 a month… |
| Reason heading | You want a free plan that keeps working | You want a low flat price with no trial clock |
| Price | Free, then Pro at | Pro at |

#### /compare/circleback

11 changes · https://lynkk.ai/compare/circleback

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Circleback's free plan writes notes for unlimited meetings and keeps 30 days of history. Lynkk's free plan has unlimited notes too, but its AI notes stop after the first 5 hours in total. | Circleback's free plan writes notes for unlimited meetings and keeps 30 days of history. Lynkk has no free plan; Lynkk Pro is $4 a month with unlimited AI notes. |
| Body | Circleback offers an API, MCP and a CLI, even on Free. Lynkk has no public API. | No change (this is Circleback's Free plan). |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | Yes: unlimited meetings with 30 days of history on 2 teams. Lynkk's free plan has unlimited notes of up to 2 hours each, with AI notes for the first 5 hours in total. | Yes: unlimited meetings with 30 days of history on 2 teams. Lynkk has no free plan; Lynkk Pro is $4 a month with unlimited notes and AI notes. |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |

#### /compare/clari-copilot

12 changes · https://lynkk.ai/compare/clari-copilot

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Body | Lynkk has a free plan that keeps recording, and puts asking across meetings in its | Lynkk has no free plan, and puts asking across meetings in its |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | Yes. The free plan has unlimited notes of up to 2 hours each and AI notes for the first 5 hours in total, and it has no end date. | Lynkk has no free plan or trial. Pro is $4 a month with no contract, and your first payment has a 7-day money-back guarantee. |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |
| FAQ answer | Yes. Free, Pro at | Yes. Pro at |
| Body | Start free, upgrade when you like and stop when you like. Connect Google Calendar… | Get Lynkk Pro and stop when you like. Connect Google Calendar… |

#### /compare/fathom

12 changes · https://lynkk.ai/compare/fathom

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Body | Does Lynkk have a free plan like Fathom's? | Does Lynkk have a free plan like Fathom's? (Answer: no. Lynkk Pro is $4 a month.) |
| Body | Lynkk has a free plan with unlimited notes of up to 2 hours each and the first 5 hours of AI notes in total. | Lynkk Pro ($4 / ₹250 a month) has unlimited notes and unlimited AI notes. |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Fathom's free plan records, transcribes and stores your calls without a monthly cap and keeps them until you delete them. Lynkk's free plan has no cap on notes either, but its AI notes stop after the first 5 hours in total, while Fathom's advanced summaries come back every month. If cost is the deciding factor and your calls are online, Fathom gives more for nothing. | Fathom's free plan records, transcribes and stores your calls without a monthly cap and keeps them until you delete them. Lynkk has no free plan; Lynkk Pro is $4 a month. If cost is the deciding factor and your calls are online, Fathom gives more for nothing. |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | Lynkk has a free plan with unlimited notes of up to 2 hours each and the first 5 hours of AI notes in total. Past those hours a note still gets its recording, transcript and search, but no summary. Fathom's free plan records and stores calls without a monthly cap and gives advanced summaries on the first 5 calls every month, so over time it gives more summaries for free. | No. Lynkk has no free plan or trial; Lynkk Pro is $4 a month (₹250) with unlimited notes and AI notes. Fathom's free plan records and stores calls without a monthly cap and gives advanced summaries on the first 5 calls every month. |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |

#### /compare/fireflies

10 changes · https://lynkk.ai/compare/fireflies

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Body | Lynkk's bot is on the free plan and records audio; video is Pro. | Lynkk's bot records audio, and on Pro it also records the meeting video. |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |
| Body | …the language picker is open on every plan, Free included. | …the language picker is open on every plan. |

#### /compare/gong

14 changes · https://lynkk.ai/compare/gong

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Body | Lynkk has a free plan that keeps recording, and puts asking across meetings in its | Lynkk has no free plan, and puts asking across meetings in its |
| Body | Sign up free, with no sales call and no trial clock. | Get Lynkk Pro for $4 a month, with no sales call. |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |
| Body | …It has no forecasting, no call scores and no CRM sync. It has a free plan, a public price of | …It has no forecasting, no call scores and no CRM sync. It has a public price of |
| FAQ answer | Yes. Free, Pro at | Yes. Pro at |
| FAQ answer | For recording calls and writing them up, yes, and you can start free. For forecasting… | For recording calls and writing them up, yes, from $4 a month. For forecasting… |
| Body | …If price keeps stalling the decision, starting free on Lynkk for the call notes is a cheap way to learn what you need. | …If price keeps stalling the decision, Lynkk Pro at $4 a month for the call notes is a cheap way to learn what you need. |

#### /compare/granola

8 changes · https://lynkk.ai/compare/granola

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |

#### /compare/meetgeek

15 changes · https://lynkk.ai/compare/meetgeek

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Meta | Looking for a MeetGeek alternative? Compare Lynkk and MeetGeek on languages, bot-free recording, free plans and asking across meetings, as of October 2026. | Looking for a MeetGeek alternative? Compare Lynkk and MeetGeek on languages, bot-free recording, price and asking across meetings, as of October 2026. |
| Body | Lynkk Free has unlimited notes of up to 2 hours each, with AI notes for the first 5 hours in total. | Lynkk Pro ($4 / ₹250 a month) has unlimited notes and unlimited AI notes. |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Lynkk Free has unlimited notes of up to 2 hours each, with AI notes for the first 5 hours in total. MeetGeek Free has 3 hours of transcription a month and keeps the audio for a month. | Lynkk Pro, at $4 a month, has unlimited notes of up to 2 hours each and unlimited AI notes. MeetGeek Free has 3 hours of transcription a month and keeps the audio for a month. |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |
| Comparison table | 2 hours on every plan, Free included | 2 hours per note |
| Comparison table | 2 hours on the free plan | 2 hours per note |
| Reason heading | A free plan you can live on | A low price you can live on |
| FAQ answer | …or you want a free plan with more room. If you need over 100 languages… | …or you want a low flat price. If you need over 100 languages… |

#### /compare/notta

15 changes · https://lynkk.ai/compare/notta

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Meta | Looking for a Notta alternative? Compare Lynkk and Notta on languages, Hinglish, bot-free recording and the free plan, with both price lists as of October 2026. | Looking for a Notta alternative? Compare Lynkk and Notta on languages, Hinglish, bot-free recording and price, with both price lists as of October 2026. |
| Body | Lynkk Free has unlimited notes of up to 2 hours each, with AI notes for the first 5 hours in total. | Lynkk Pro ($4 / ₹250 a month) has unlimited notes and unlimited AI notes. |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Longest note on Free | Longest note |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Lynkk Free has unlimited notes of up to 2 hours each, with AI notes for the first 5 hours in total. Notta's free plan stops each conversation at 3 minutes. | Lynkk Pro has unlimited notes of up to 2 hours each with unlimited AI notes. Notta's free plan stops each conversation at 3 minutes. |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | For short clips. Notta's free plan stops each conversation at 3 minutes. Lynkk's free plan has unlimited notes of up to 2 hours each, and AI notes for the first 5 hours in total. | For short clips. Notta's free plan stops each conversation at 3 minutes. Lynkk has no free plan; Lynkk Pro is $4 a month, with notes up to 2 hours each. |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |
| Reason heading | A free plan that fits a meeting | A note length that fits a meeting |
| Body | Lynkk transcribes 17 languages plus Hinglish, with auto-detect, on every plan, Free included, and charges nothing extra… | Lynkk transcribes 17 languages plus Hinglish, with auto-detect, and charges nothing extra… |

#### /compare/otter

12 changes · https://lynkk.ai/compare/otter

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | a month and Otter Pro is $8.33. The plans limit different things: Otter counts minutes, while Lynkk gives every plan unlimited notes of up to 2 hours each and, on Free, counts the first 5 hours of AI notes in total. | a month and Otter Pro is $8.33. The plans limit different things: Otter counts minutes, while Lynkk Pro has unlimited notes of up to 2 hours each. |
| Body | Lynkk's free plan records unlimited meetings of up to 2 hours each, includes your first 5 hours of AI notes, and works with Zoom, Google Meet, Teams and in-person meetings. Pro is $4 a month ₹250 a month and removes the summary limit. | Fathom's free plan is the most generous free alternative. Lynkk is not free: Lynkk Pro is $4 a month (₹250) and records unlimited meetings of up to 2 hours each, with AI notes, on Zoom, Google Meet, Teams and in person. |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |
| Comparison table | 2 hours on every plan, Free included | 2 hours per note |
| FAQ question | What is the best free Otter.ai alternative? | No change to the question (new answer above). |

#### /compare/plaud

11 changes · https://lynkk.ai/compare/plaud

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | Lynkk counts notes, not minutes. Every plan has unlimited notes of up to 2 hours each, and Free includes AI notes for the first 5 hours in total. Plaud Pro gives 1,200 transcription minutes a month unless you pay for Unlimited. | Lynkk counts notes, not minutes. Lynkk Pro has unlimited notes of up to 2 hours each, with unlimited AI notes. Plaud Pro gives 1,200 transcription minutes a month unless you pay for Unlimited. |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |
| FAQ answer | No. Lynkk runs in the browser, on the Mac and as a Chrome extension. The free plan has unlimited notes and no end date. | No. Lynkk runs in the browser, on the Mac and as a Chrome extension. Lynkk Pro has unlimited notes. |
| Body | Lynkk Free has unlimited notes and costs nothing. Pro is | Lynkk Pro, with unlimited notes, is |

#### /compare/read-ai

11 changes · https://lynkk.ai/compare/read-ai

| Where | Find | Replace with |
|---|---|---|
| Plan card / price table | Lynkk · Free · $0 | Remove Lynkk's Free row from the price table. Keep Pro ($4 a month) and Enterprise. |
| Body | Sign up free. | Get Lynkk Pro for $4 (₹250) a month. |
| Body | There is no trial to run out: the free plan has no end date. | Lynkk Pro is $4 a month (₹250 in India). |
| Body | Unlimited notes, 2 hours per note, the first 5 hours of AI notes | No free plan. Pro: unlimited notes and AI notes, $4 a month |
| Body | Unlimited notes, up to 2 hours each, and the first 5 hours of AI notes in total. The meeting bot (audio), the Mac app, the Chrome extension, the web app and every language. | Remove (text of the Lynkk Free plan card, which is removed). |
| Body | a month and Read AI Pro is $15. Lynkk Free has unlimited notes of up to 2 hours each and AI notes for the first 5 hours in total; Read AI Free has 5 transcripts a month of up to 1 hour. | a month and Read AI Pro is $15. Lynkk Pro has unlimited notes of up to 2 hours each and unlimited AI notes; Read AI Free has 5 transcripts a month of up to 1 hour. |
| Body | Free to start, on your Mac or in the browser. Every plan has unlimited notes of up to 2 hours, and Free includes the first 5 hours of AI notes. | Lynkk Pro is $4 a month, on your Mac or in the browser, with unlimited notes and AI notes. |
| Price row in related-comparison cards | Free with unlimited notes, or Pro at | Pro at |
| Comparison table label | Free plan | Change the row label to "Lynkk plans" (the Lynkk cell is replaced above). |
| Comparison table | 2 hours on every plan, Free included | 2 hours per note |
| Body | …plus 17 languages and auto-detect, on every plan, Free included. | …plus 17 languages and auto-detect, on every plan. |

## 9. Free to paid: blog posts, find and replace

Same method as section 8. The site-wide template fixes in section 8 also cover every blog post. The two posts rewritten in full (section 10) are not repeated here.

### Check before publishing

- **Annual price:** the pricing posts (Fathom, Fireflies, Granola, Otter) say "$40 a year (₹2,500), two months free". Keep it only if the annual plan is still sold.
- **CRM claims:** some posts say Lynkk logs calls on the deal in HubSpot or Salesforce (for example granola-ai-pricing, zoom-meeting-recorders, zoom-ai-companion-alternatives, ai-powered-meeting-assistants, best-ai-note-takers). The plan table lists CRM sync as "Not yet", so the team needs to confirm before these stay. Three lines on zoom-ai-companion-alternatives that mix the free plan with CRM sync are held for the same reason.

### Summary

| # | Blog post | Changes | Impressions |
|---|---|---|---|
| 1 | [/blog/google-meet-transcript](https://lynkk.ai/blog/google-meet-transcript) | 4 | 10,422 |
| 2 | [/blog/action-items-examples-template](https://lynkk.ai/blog/action-items-examples-template) | 1 | 3,082 |
| 3 | [/blog/zoom-note-taker](https://lynkk.ai/blog/zoom-note-taker) | 5 | 2,457 |
| 4 | [/blog/follow-up-email-after-meeting](https://lynkk.ai/blog/follow-up-email-after-meeting) | 1 | 2,304 |
| 5 | [/blog/ai-powered-meeting-assistants](https://lynkk.ai/blog/ai-powered-meeting-assistants) | 4 | 2,009 |
| 6 | [/blog/daily-standup-meeting](https://lynkk.ai/blog/daily-standup-meeting) | 1 | 1,884 |
| 7 | [/blog/medical-transcription-software](https://lynkk.ai/blog/medical-transcription-software) | 1 | 1,876 |
| 8 | [/blog/meeting-summary-template](https://lynkk.ai/blog/meeting-summary-template) | 1 | 1,819 |
| 9 | [/blog/zoom-bot-join-meeting](https://lynkk.ai/blog/zoom-bot-join-meeting) | 5 | 1,788 |
| 10 | [/blog/best-ai-note-takers](https://lynkk.ai/blog/best-ai-note-takers) | 7 | 1,697 |
| 11 | [/blog/granola-ai-pricing](https://lynkk.ai/blog/granola-ai-pricing) | 5 | 1,628 |
| 12 | [/blog/meeting-minutes-sample](https://lynkk.ai/blog/meeting-minutes-sample) | 2 | 1,620 |
| 13 | [/blog/board-meeting-agenda](https://lynkk.ai/blog/board-meeting-agenda) | 1 | 1,353 |
| 14 | [/blog/recruiting-interview-transcription](https://lynkk.ai/blog/recruiting-interview-transcription) | 1 | 1,302 |
| 15 | [/blog/zoom-ai-companion-alternatives](https://lynkk.ai/blog/zoom-ai-companion-alternatives) | 7 | 953 |
| 16 | [/blog/hindi-transcription](https://lynkk.ai/blog/hindi-transcription) | 5 | 914 |
| 17 | [/blog/fathom-ai-pricing](https://lynkk.ai/blog/fathom-ai-pricing) | 4 | 805 |
| 18 | [/blog/gong-pricing](https://lynkk.ai/blog/gong-pricing) | 2 | 577 |
| 19 | [/blog/how-to-transcribe-zoom-meetings](https://lynkk.ai/blog/how-to-transcribe-zoom-meetings) | 6 | 535 |
| 20 | [/blog/meeting-preparation](https://lynkk.ai/blog/meeting-preparation) | 1 | 488 |
| 21 | [/blog/founders-meeting-notes](https://lynkk.ai/blog/founders-meeting-notes) | 3 | 388 |
| 22 | [/blog/sales-enablement-tools](https://lynkk.ai/blog/sales-enablement-tools) | 1 | 365 |
| 23 | [/blog/meeting-knowledge-management](https://lynkk.ai/blog/meeting-knowledge-management) | 1 | 297 |
| 24 | [/blog/google-meet-ai-note-taker](https://lynkk.ai/blog/google-meet-ai-note-taker) | 3 | 280 |
| 25 | [/blog/fireflies-pricing](https://lynkk.ai/blog/fireflies-pricing) | 4 | 265 |
| 26 | [/blog/otter-ai-alternatives](https://lynkk.ai/blog/otter-ai-alternatives) | 4 | 219 |
| 27 | [/blog/ai-transcription-software](https://lynkk.ai/blog/ai-transcription-software) | 4 | 216 |
| 28 | [/blog/meeting-notes-vs-minutes](https://lynkk.ai/blog/meeting-notes-vs-minutes) | 1 | 154 |
| 29 | [/blog/read-ai-vs-otter-ai](https://lynkk.ai/blog/read-ai-vs-otter-ai) | 2 | 148 |
| 30 | [/blog/meeting-minutes-to-jira](https://lynkk.ai/blog/meeting-minutes-to-jira) | 2 | 142 |
| 31 | [/blog/otter-ai-pricing](https://lynkk.ai/blog/otter-ai-pricing) | 4 | 108 |
| 32 | [/blog/sales-conversation-intelligence](https://lynkk.ai/blog/sales-conversation-intelligence) | 1 | 72 |
| 33 | [/blog/one-on-one-meeting](https://lynkk.ai/blog/one-on-one-meeting) | 2 | 60 |
| 34 | [/blog/bant-sales-qualification](https://lynkk.ai/blog/bant-sales-qualification) | 1 | 29 |
| 35 | [/blog/best-second-brain-apps](https://lynkk.ai/blog/best-second-brain-apps) | 1 | 11 |
| 36 | [/blog/call-coaching-software](https://lynkk.ai/blog/call-coaching-software) | 2 | 5 |
| 37 | [/blog/authors/samarth-wagh](https://lynkk.ai/blog/authors/samarth-wagh) | 1 | 0 |
| 38 | [/blog/best-mac-note-taking-app](https://lynkk.ai/blog/best-mac-note-taking-app) | 1 | 0 |
| 39 | [/blog/legal-transcription-service](https://lynkk.ai/blog/legal-transcription-service) | 2 | 0 |
| 40 | [/blog/sales-call-recording-software](https://lynkk.ai/blog/sales-call-recording-software) | 2 | 0 |
| 41 | [/blog/zoom-meeting-recorders](https://lynkk.ai/blog/zoom-meeting-recorders) | 4 | 0 |

### Changes by post

#### 1. /blog/google-meet-transcript

10,422 impressions · 4 changes · https://lynkk.ai/blog/google-meet-transcript

| Where | Find | Replace with |
|---|---|---|
| Body | It works on Lynkk's Free plan and gives you a transcript with speaker labels. | It works on Lynkk Pro ($4 a month) and gives you a transcript with speaker labels. |
| Body | Lynkk records Zoom with a free bot or no bot, even on free Zoom, while AI Companion needs a paid plan. | Lynkk records Zoom with a bot or no bot, even on free Zoom accounts, for $4 a month, while AI Companion needs a paid Zoom plan. |
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | Yes. A third-party note taker can transcribe the call instead. Lynkk's free plan records Google Meet with its meeting bot or Chrome extension and returns a transcript with speaker labels, plus your first 5 hours of AI summaries in total, with no Workspace plan needed. | Yes. A third-party note taker can transcribe the call instead. Lynkk Pro ($4 a month) records Google Meet with its meeting bot or Chrome extension and returns a transcript with speaker labels and AI summaries, with no Workspace plan needed. |

#### 2. /blog/action-items-examples-template

3,082 impressions · 1 change · https://lynkk.ai/blog/action-items-examples-template

| Where | Find | Replace with |
|---|---|---|
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |

#### 3. /blog/zoom-note-taker

2,457 impressions · 5 changes · https://lynkk.ai/blog/zoom-note-taker

| Where | Find | Replace with |
|---|---|---|
| Meta | Lynkk records Zoom with a free bot or no bot, even on free Zoom, while AI Companion needs a paid plan. Seven Zoom note takers with free limits and prices. | Lynkk records Zoom with a bot or no bot, even on free Zoom, from $4 a month, while AI Companion needs a paid plan. Seven Zoom note takers with prices. |
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | Free has unlimited notes of up to 2 hours each, the first 5 hours of AI summaries in total, the meeting bot (audio), tasks and Jira send. Pro is | Lynkk Pro includes unlimited notes of up to 2 hours each, the meeting bot, tasks and Jira send. It is |
| Body | Unlimited notes up to 2 hours each; first 5 hours of AI summaries in total; meeting bot records audio | Remove the Lynkk row from the free-plan table. Add under the table: "Lynkk has no free plan. Lynkk Pro is $4 a month (₹250 in India)." |
| Body (FAQ: What is the best AI note taker for Zoom?) | which records Zoom three ways, with a free bot, the Mac app or the Chrome extension, even on free Zoom accounts. | which records Zoom three ways, with a bot, the Mac app or the Chrome extension, even on free Zoom accounts, for $4 a month. |

#### 4. /blog/follow-up-email-after-meeting

2,304 impressions · 1 change · https://lynkk.ai/blog/follow-up-email-after-meeting

| Where | Find | Replace with |
|---|---|---|
| Body | The free plan records unlimited notes up to 2 hours each and includes your first 5 hours of AI summaries. [Start for free] | Lynkk Pro records unlimited notes up to 2 hours each, with unlimited AI summaries, for $4 a month (₹250). [Get Lynkk Pro] |

#### 5. /blog/ai-powered-meeting-assistants

2,009 impressions · 4 changes · https://lynkk.ai/blog/ai-powered-meeting-assistants

| Where | Find | Replace with |
|---|---|---|
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | Unlimited notes up to 2 hours each; first 5 hours of AI summaries in total | Remove the Lynkk row from the free-options table. Add under the table: "Lynkk has no free plan. Lynkk Pro is $4 a month (₹250 in India)." |
| Body (FAQ: Is there a free AI meeting assistant?) | Yes. Lynkk, Otter, Fireflies, Read AI and Fathom all have free plans, with very different limits. | Yes. Otter, Fireflies, Read AI and Fathom all have free plans, with very different limits. Lynkk is paid, from $4 a month. |
| Cost table, Lynkk Pro row | ; a Workspace puts up to 10 members on Pro with one bill | ; a shared workspace for up to 10 people is on Enterprise, priced on a call |

#### 6. /blog/daily-standup-meeting

1,884 impressions · 1 change · https://lynkk.ai/blog/daily-standup-meeting

| Where | Find | Replace with |
|---|---|---|
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |

#### 7. /blog/medical-transcription-software

1,876 impressions · 1 change · https://lynkk.ai/blog/medical-transcription-software

| Where | Find | Replace with |
|---|---|---|
| Body | join (audio on Free, video on Pro) or record in the room. | join or record in the room. |

#### 8. /blog/meeting-summary-template

1,819 impressions · 1 change · https://lynkk.ai/blog/meeting-summary-template

| Where | Find | Replace with |
|---|---|---|
| Body | The free plan includes your first 5 hours of AI summaries. [Start for free] | Lynkk Pro, at $4 a month (₹250), includes unlimited AI summaries. [Get Lynkk Pro] |

#### 9. /blog/zoom-bot-join-meeting

1,788 impressions · 5 changes · https://lynkk.ai/blog/zoom-bot-join-meeting

| Where | Find | Replace with |
|---|---|---|
| Body | Lynkk records Zoom with a free bot or no bot, even on free Zoom, while AI Companion needs a paid plan. | Lynkk records Zoom with a bot or no bot, even on free Zoom accounts, for $4 a month, while AI Companion needs a paid Zoom plan. |
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | The Lynkk Zoom bot is free and records audio. | The Lynkk Zoom bot records audio. |
| Body | The Lynkk Zoom bot is free on every plan and records audio in Zoom, Google Meet and Teams, with a live transcript during the call and notes afterward. | Not with Lynkk. The Lynkk Zoom bot is included with Lynkk Pro ($4 a month) and records audio in Zoom, Google Meet and Teams, with a live transcript during the call and notes afterward. |
| Body | On Free, your first 5 hours of meetings get AI summaries; after that, meetings are still recorded, transcribed and searchable. Lynkk does not train AI models on your conversations. | Lynkk Pro gives every meeting an AI summary, and every meeting is recorded, transcribed and searchable. Lynkk does not train AI models on your conversations. |

#### 10. /blog/best-ai-note-takers

1,697 impressions · 7 changes · https://lynkk.ai/blog/best-ai-note-takers

| Where | Find | Replace with |
|---|---|---|
| Meta | Fathom for free recording, Otter for live transcripts, Lynkk for bot or no bot and in-person notes. Ten AI note takers with free limits, prices and how we scored them. | Fathom for free recording, Otter for live transcripts, Lynkk for bot or no bot and in-person notes at $4/mo. Ten AI note takers with free limits, prices and scores. |
| Body | Lynkk starts free, Pro is | Lynkk Pro is |
| Body | Try Lynkk free | Get Lynkk Pro |
| Body | or no bot at all, Lynkk (free, Pro | or no bot at all, Lynkk (Pro |
| Body | Free has unlimited notes of up to 2 hours each and the first 5 hours of AI summaries in total. Pro is | Lynkk Pro has unlimited notes of up to 2 hours each and unlimited AI summaries, at |
| Comparison table, Lynkk row, Free plan column | Yes | No |
| Body (Lynkk pricing, after the line above) | Workspaces put up to 10 members on Pro with one bill, | Enterprise (custom price) gives a shared workspace for up to 10 people, |

#### 11. /blog/granola-ai-pricing

1,628 impressions · 5 changes · https://lynkk.ai/blog/granola-ai-pricing

| Where | Find | Replace with |
|---|---|---|
| Body | Granola's free plan limits how long you keep notes; Lynkk's free plan keeps every note and limits AI summaries to the first 5 hours in total, so nothing disappears after 30 days. | Granola's free plan limits how long you keep notes; Lynkk Pro, at $4 a month, keeps every note with unlimited AI summaries, so nothing disappears after 30 days. |
| Body | you keep. Its free plan is $0 with no card: unlimited notes of up to 2 hours each, kept with no 30-day window, and the first 5 hours of AI summaries in total. Pro is | you keep. Pro has unlimited notes of up to 2 hours each, kept with no 30-day window, and unlimited AI summaries. It is |
| Body | They leave your meeting history, so you can no longer look back at them on Basic. Upgrading to Business at $14 per user a month restores unlimited history. Lynkk's free plan keeps every note with no time window and limits only AI summaries, to the first 5 hours. | They leave your meeting history, so you can no longer look back at them on Basic. Upgrading to Business at $14 per user a month restores unlimited history. Lynkk Pro, at $4 a month, keeps every note with no time window. |
| Body (after the Lynkk price) | After the first 5 hours on Free, notes still record and transcribe, without summaries. | Delete this sentence. |
| Body (Lynkk section) | Workspaces put up to 10 members on Pro with one bill, | Enterprise (custom price) gives a shared workspace for up to 10 people, |

#### 12. /blog/meeting-minutes-sample

1,620 impressions · 2 changes · https://lynkk.ai/blog/meeting-minutes-sample

| Where | Find | Replace with |
|---|---|---|
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | joins online on every plan (audio on Free), and the Mac app records in-person meetings in the room. | joins online meetings, and the Mac app records in-person meetings in the room. |

#### 13. /blog/board-meeting-agenda

1,353 impressions · 1 change · https://lynkk.ai/blog/board-meeting-agenda

| Where | Find | Replace with |
|---|---|---|
| Body | . When the meeting ends you get a note with a summary, decisions, action items with owners and due dates, and a transcript with speaker labels. The free plan includes your first 5 hours of AI summaries; Pro at $4 a month ₹250 a month makes them unlimited. [Start for free] | . When the meeting ends you get a note with a summary, decisions, action items with owners and due dates, and a transcript with speaker labels. Lynkk Pro, at $4 a month (₹250), includes unlimited AI summaries. [Get Lynkk Pro] |

#### 14. /blog/recruiting-interview-transcription

1,302 impressions · 1 change · https://lynkk.ai/blog/recruiting-interview-transcription

| Where | Find | Replace with |
|---|---|---|
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |

#### 15. /blog/zoom-ai-companion-alternatives

953 impressions · 7 changes · https://lynkk.ai/blog/zoom-ai-companion-alternatives

| Where | Find | Replace with |
|---|---|---|
| Body | Lynkk records Zoom with a free bot or no bot, even on free Zoom, while AI Companion needs a paid plan. | Lynkk records Zoom with a bot or no bot, even on free Zoom accounts, for $4 a month, while AI Companion needs a paid Zoom plan. |
| Body | Lynkk starts free and covers Zoom, Teams, Google Meet and in-person meetings. | Lynkk Pro is $4 a month and covers Zoom, Teams, Google Meet and in-person meetings. |
| Body | Sign up free | Get Lynkk Pro |
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | Free is $0 with no card, unlimited notes up to 2 hours each, and the first 5 hours of AI summaries in total. Pro is | Lynkk Pro has unlimited notes up to 2 hours each and unlimited AI summaries, at |
| Body | Lynkk, Otter, Fireflies, Fathom and Read AI all have free plans that work with Zoom. | Otter, Fireflies, Fathom and Read AI all have free plans that work with Zoom, and Lynkk Pro is $4 a month. |
| Body (how-to steps) | Pick the meeting bot (free, audio only) or no-bot recording | Pick the meeting bot or no-bot recording |

#### 16. /blog/hindi-transcription

914 impressions · 5 changes · https://lynkk.ai/blog/hindi-transcription

| Where | Find | Replace with |
|---|---|---|
| Body | For meetings that mix Hindi and English, Lynkk's free plan has a | For meetings that mix Hindi and English, Lynkk Pro ($4 a month) has a |
| Body | try Lynkk free | get Lynkk Pro |
| Body | Unlimited transcripts, first 5 hours of AI summaries | No. Lynkk Pro is $4 a month (₹250) |
| Body | Lynkk covers 17 languages plus auto-detect, with Tamil, Telugu, Marathi and Bengali in beta. Every plan transcribes unlimited notes in every language; Free includes the first 5 hours of AI summaries, and Pro is | Lynkk covers 17 languages plus auto-detect, with Tamil, Telugu, Marathi and Bengali in beta. Lynkk Pro transcribes unlimited notes in every language, with unlimited AI summaries, and is |
| Body (link text) | the free plan of an AI meeting tool | an AI meeting tool |

#### 17. /blog/fathom-ai-pricing

805 impressions · 4 changes · https://lynkk.ai/blog/fathom-ai-pricing

| Where | Find | Replace with |
|---|---|---|
| Body | Fathom's free plan is the more generous of the two on summaries, since Lynkk Free stops summarizing after the first 5 hours. | Fathom's free plan costs nothing to start, but Lynkk Pro, at $4 a month, gives unlimited summaries for less than any paid Fathom plan. |
| Body | app with one flat Pro price. Free is $0 with no card: unlimited notes of up to 2 hours each and the first 5 hours of AI summaries in total. Pro is | app with one flat Pro price. Pro is |
| Body (after the Lynkk price) | After the first 5 hours on Free, notes still record and transcribe, without summaries. | Delete this sentence. |
| Body (Lynkk section) | Workspaces put up to 10 members on Pro with one bill, | Enterprise (custom price) gives a shared workspace for up to 10 people, |

#### 18. /blog/gong-pricing

577 impressions · 2 changes · https://lynkk.ai/blog/gong-pricing

| Where | Find | Replace with |
|---|---|---|
| Body | Lynkk's free plan is $0 with no card: unlimited notes (up to 2 hours each) and the first 5 hours of AI summaries in total, with action items and a summary emailed after each call. | Lynkk Pro is $4 a month (₹250 in India): unlimited notes (up to 2 hours each) and unlimited AI summaries, with action items and a summary emailed after each call. |
| Body (Lynkk section) | Workspaces put up to 10 members on Pro with one bill, | Enterprise (custom price) gives a shared workspace for up to 10 people, |

#### 19. /blog/how-to-transcribe-zoom-meetings

535 impressions · 6 changes · https://lynkk.ai/blog/how-to-transcribe-zoom-meetings

| Where | Find | Replace with |
|---|---|---|
| Body | Lynkk records Zoom with a free bot or no bot, even on free Zoom, while AI Companion needs a paid plan. | Lynkk records Zoom with a bot or no bot, even on free Zoom accounts, for $4 a month, while AI Companion needs a paid Zoom plan. |
| Body | Sign up free, with no card, and connect Google Calendar. | Get Lynkk Pro ($4 a month) and connect Google Calendar. |
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | To transcribe Zoom meetings with Lynkk, sign up free, then connect Google Calendar or paste a Zoom link so the meeting bot joins. | To transcribe Zoom meetings with Lynkk, get Lynkk Pro ($4 a month), then connect Google Calendar or paste a Zoom link so the meeting bot joins. |
| Body | joins as a visible participant named after you, on every plan (audio on Free, video on Pro). With no bot, the | joins as a visible participant named after you and records audio and video. With no bot, the |
| Body | handles speakers who switch languages mid-sentence. Free covers unlimited notes of up to 2 hours each and the first 5 hours of AI summaries in total; Pro, at | handles speakers who switch languages mid-sentence. Lynkk Pro, at |

#### 20. /blog/meeting-preparation

488 impressions · 1 change · https://lynkk.ai/blog/meeting-preparation

| Where | Find | Replace with |
|---|---|---|
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |

#### 21. /blog/founders-meeting-notes

388 impressions · 3 changes · https://lynkk.ai/blog/founders-meeting-notes

| Where | Find | Replace with |
|---|---|---|
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | joins online calls on every plan (audio on Free), and the | joins online calls, and the |
| Body | You can start on the free plan, which records and transcribes unlimited notes and includes the first 5 hours of AI summaries; Pro is | Lynkk Pro records and transcribes unlimited notes with unlimited AI summaries, and is |

#### 22. /blog/sales-enablement-tools

365 impressions · 1 change · https://lynkk.ai/blog/sales-enablement-tools

| Where | Find | Replace with |
|---|---|---|
| Body | answers questions across all your notes with numbered sources. Lynkk does not sync with a CRM today, so you copy summaries into your CRM yourself. Free is $0 with unlimited notes and the first 5 hours of AI summaries; Pro is | answers questions across all your notes with numbered sources. Lynkk does not sync with a CRM today, so you copy summaries into your CRM yourself. Lynkk Pro has unlimited notes and AI summaries and is |

#### 23. /blog/meeting-knowledge-management

297 impressions · 1 change · https://lynkk.ai/blog/meeting-knowledge-management

| Where | Find | Replace with |
|---|---|---|
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |

#### 24. /blog/google-meet-ai-note-taker

280 impressions · 3 changes · https://lynkk.ai/blog/google-meet-ai-note-taker

| Where | Find | Replace with |
|---|---|---|
| Body | Lynkk records Zoom with a free bot or no bot, even on free Zoom, while AI Companion needs a paid plan. | Lynkk records Zoom with a bot or no bot, even on free Zoom accounts, for $4 a month, while AI Companion needs a paid Zoom plan. |
| Body | you can send to Jira. On Pro, Ask Lynkk answers across all your meetings. Free covers unlimited notes of up to 2 hours each and your first 5 hours of AI summaries; Pro is | you can send to Jira. On Pro, Ask Lynkk answers across all your meetings, with unlimited notes and AI summaries. Pro is |
| Free Google Meet AI note taker table, Lynkk row | Lynkk (our product) \| Unlimited notes up to 2 h each, first 5 h of AI summaries \| Yes | Remove the Lynkk row. Add under the table: "Lynkk has no free plan. Lynkk Pro is $4 a month (₹250 in India)." |

#### 25. /blog/fireflies-pricing

265 impressions · 4 changes · https://lynkk.ai/blog/fireflies-pricing

| Where | Find | Replace with |
|---|---|---|
| Body | with no storage pool and no credits. Its free plan is $0 with no card: unlimited notes of up to 2 hours each and the first 5 hours of AI summaries in total. Pro is | with no storage pool and no credits. Pro is |
| Body | and the one limit on Free is the first 5 hours of AI summaries, which Pro removes. | and Lynkk Pro has unlimited AI summaries. |
| Body (after the Lynkk price) | After the first 5 hours on Free, notes still record and transcribe, without summaries. | Delete this sentence. |
| Body (Lynkk section) | Workspaces put up to 10 members on Pro with one bill, | Enterprise (custom price) gives a shared workspace for up to 10 people, |

#### 26. /blog/otter-ai-alternatives

219 impressions · 4 changes · https://lynkk.ai/blog/otter-ai-alternatives

| Where | Find | Replace with |
|---|---|---|
| Body | Start for free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | Try Lynkk free | Get Lynkk Pro |
| Body | Free gives unlimited notes of up to 2 hours each, the meeting bot (audio) and your first 5 hours of AI summaries in total. Pro is | Lynkk Pro has unlimited notes of up to 2 hours each and the meeting bot, at |
| Body | Hunting for Otter AI alternatives that are free instead? Fathom gives unlimited recordings, and Lynkk gives unlimited notes with the task board and Jira send included, plus your first 5 hours of AI summaries. | Hunting for Otter AI alternatives that are free instead? Fathom gives unlimited recordings on its free plan. Lynkk is paid, but at $4 a month it costs less than Otter Pro and includes the task board and Jira send. |

#### 27. /blog/ai-transcription-software

216 impressions · 4 changes · https://lynkk.ai/blog/ai-transcription-software

| Where | Find | Replace with |
|---|---|---|
| Body | Five tools in this guide have free transcription, each with a limit: Lynkk's Free plan, Otter's 300 minutes a month, Fireflies' free plan, Descript's hour a month, and Word Transcribe if you already pay for Microsoft 365. | Four tools in this guide have free transcription, each with a limit: Otter's 300 minutes a month, Fireflies' free plan, Descript's hour a month, and Word Transcribe if you already pay for Microsoft 365. Lynkk is paid, from $4 a month. |
| Body | every plan records and transcribes unlimited notes, up to 2 hours each; Free includes your first 5 hours of AI summaries, and Pro is | Lynkk Pro records and transcribes unlimited notes, up to 2 hours each, with unlimited AI summaries, and is |
| Body | For meetings on Zoom, Teams, Google Meet and in person, Lynkk's Free plan records and transcribes unlimited notes and includes the meeting bot (audio) and your first 5 hours of AI summaries. For files, Word Transcribe and Otter are the most generous. | For meetings on Zoom, Teams, Google Meet and in person, Lynkk Pro records and transcribes unlimited notes, with the meeting bot and unlimited AI summaries, for $4 a month. For free file transcription, Word Transcribe and Otter are the most generous. |
| Comparison table, Lynkk row, Free option column | Yes | No |

#### 28. /blog/meeting-notes-vs-minutes

154 impressions · 1 change · https://lynkk.ai/blog/meeting-notes-vs-minutes

| Where | Find | Replace with |
|---|---|---|
| Body | , then gives you a summary, decisions, and action items with owners and due dates, plus a transcript with speaker labels. Turning them into approved minutes takes a quick review instead of an hour of typing. The free plan includes your first 5 hours of AI summaries; Pro at $4 a month ₹250 a month makes them unlimited. [Start for free] | , then gives you a summary, decisions, and action items with owners and due dates, plus a transcript with speaker labels. Turning them into approved minutes takes a quick review instead of an hour of typing. Lynkk Pro, at $4 a month (₹250), includes unlimited AI summaries. [Get Lynkk Pro] |

#### 29. /blog/read-ai-vs-otter-ai

148 impressions · 2 changes · https://lynkk.ai/blog/read-ai-vs-otter-ai

| Where | Find | Replace with |
|---|---|---|
| Body | Try Lynkk free | Get Lynkk Pro |
| Body | , Hinglish included. Free gives unlimited notes of up to 2 hours each and your first 5 hours of AI summaries in total, and | , Hinglish included, with unlimited notes and AI summaries, and Lynkk |

#### 30. /blog/meeting-minutes-to-jira

142 impressions · 2 changes · https://lynkk.ai/blog/meeting-minutes-to-jira

| Where | Find | Replace with |
|---|---|---|
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | joins on every plan (audio on Free), or the Mac app records in the room with no bot. | joins online meetings, or the Mac app records in the room with no bot. |

#### 31. /blog/otter-ai-pricing

108 impressions · 4 changes · https://lynkk.ai/blog/otter-ai-pricing

| Where | Find | Replace with |
|---|---|---|
| Body | If you only want notes without metered minutes, Lynkk's free plan records unlimited notes up to 2 hours each. | If you only want notes without metered minutes, Lynkk Pro records unlimited notes up to 2 hours each for $4 a month. |
| Body | that does not meter minutes. Its free plan is $0 with no card and records unlimited notes of up to 2 hours each, with the first 5 hours of AI summaries in total. Pro is | that does not meter minutes. Pro records unlimited notes of up to 2 hours each and is |
| Body (after the Lynkk price) | After the first 5 hours on Free, notes still record and transcribe, without summaries. | Delete this sentence. |
| Body (Lynkk section) | Workspaces put up to 10 members on Pro with one bill, | Enterprise (custom price) gives a shared workspace for up to 10 people, |

#### 32. /blog/sales-conversation-intelligence

72 impressions · 1 change · https://lynkk.ai/blog/sales-conversation-intelligence

| Where | Find | Replace with |
|---|---|---|
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |

#### 33. /blog/one-on-one-meeting

60 impressions · 2 changes · https://lynkk.ai/blog/one-on-one-meeting

| Where | Find | Replace with |
|---|---|---|
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | joins on every plan (audio on Free), or the | joins online 1:1s, or the |

#### 34. /blog/bant-sales-qualification

29 impressions · 1 change · https://lynkk.ai/blog/bant-sales-qualification

| Where | Find | Replace with |
|---|---|---|
| Body | ), Ask Lynkk searches every call you have recorded, so "what did the buyer say about budget?" comes back with the answer and numbered sources. Lynkk does not sync with a CRM today, so you copy the summary into the deal record yourself. The free plan includes unlimited notes and your first 5 hours of AI summaries ( | ), Ask Lynkk searches every call you have recorded, so "what did the buyer say about budget?" comes back with the answer and numbered sources. Lynkk does not sync with a CRM today, so you copy the summary into the deal record yourself. Lynkk Pro includes unlimited notes and AI summaries ( |

#### 35. /blog/best-second-brain-apps

11 impressions · 1 change · https://lynkk.ai/blog/best-second-brain-apps

| Where | Find | Replace with |
|---|---|---|
| Body | answers questions across every note and shows the note and minute behind each answer. Free includes unlimited recordings with the first 5 hours of AI notes, and Pro is | answers questions across every note and shows the note and minute behind each answer. Lynkk Pro includes unlimited recordings and AI notes, and is |

#### 36. /blog/call-coaching-software

5 impressions · 2 changes · https://lynkk.ai/blog/call-coaching-software

| Where | Find | Replace with |
|---|---|---|
| Body | Few coaching tools are fully free. Fathom has a free-forever plan for recording, with scorecards on its Business plan, and Lynkk's free plan records unlimited meetings with the first 5 hours of AI notes included. Gong and Clari Copilot have no free plan, and Avoma offers a 14-day trial instead. | Few coaching tools are fully free. Fathom has a free-forever plan for recording, with scorecards on its Business plan. Gong and Clari Copilot have no free plan, Avoma offers a 14-day trial instead, and Lynkk is paid, at $4 a month. |
| Comparison table, Lynkk price | Free plan; Pro $4 a month ₹250 a month | Pro $4 a month (₹250) |

#### 37. /blog/authors/samarth-wagh

0 impressions · 1 change · https://lynkk.ai/blog/authors/samarth-wagh

| Where | Find | Replace with |
|---|---|---|
| Body | Lynkk records Zoom with a free bot or no bot, even on free Zoom, while AI Companion needs a paid plan. | Lynkk records Zoom with a bot or no bot, even on free Zoom accounts, for $4 a month, while AI Companion needs a paid Zoom plan. |

#### 38. /blog/best-mac-note-taking-app

0 impressions · 1 change · https://lynkk.ai/blog/best-mac-note-taking-app

| Where | Find | Replace with |
|---|---|---|
| Body | with action items and decisions. On Pro, Ask Lynkk answers questions across every note with the minute behind each answer. Free includes unlimited recordings and the first 5 hours of AI notes, with Pro at | with action items and decisions. On Pro, Ask Lynkk answers questions across every note with the minute behind each answer. Lynkk Pro, with unlimited recordings and AI notes, is |

#### 39. /blog/legal-transcription-service

0 impressions · 2 changes · https://lynkk.ai/blog/legal-transcription-service

| Where | Find | Replace with |
|---|---|---|
| Body | Lynkk is a flat plan instead: free, or | Lynkk is a flat plan instead: |
| Comparison table, Lynkk price | Free plan; Pro $4 a month ₹250 a month | Pro $4 a month (₹250) |

#### 40. /blog/sales-call-recording-software

0 impressions · 2 changes · https://lynkk.ai/blog/sales-call-recording-software

| Where | Find | Replace with |
|---|---|---|
| Body | , or without one from the Mac app, which also records a conversation across a table. Each call becomes a transcript, summary and action items, and on Pro, Ask Lynkk answers questions across every call with the minute behind each answer. Free includes unlimited recordings and the first 5 hours of AI notes, with Pro at | , or without one from the Mac app, which also records a conversation across a table. Each call becomes a transcript, summary and action items, and on Pro, Ask Lynkk answers questions across every call with the minute behind each answer. Lynkk Pro includes unlimited recordings and AI notes, at |
| Body | Fathom is the strongest free option, with a free-forever recording plan. Lynkk's free plan covers unlimited recordings and the first 5 hours of AI notes. Zoom includes local recording on its free tier with limits. Free plans usually restrict AI summaries, CRM sync or scorecards rather than the recording itself. | Fathom is the strongest free option, with a free-forever recording plan. Zoom includes local recording on its free tier with limits. Free plans usually restrict AI summaries, CRM sync or scorecards rather than the recording itself. Lynkk has no free plan; Lynkk Pro is $4 a month with unlimited recordings and AI notes. |

#### 41. /blog/zoom-meeting-recorders

0 impressions · 4 changes · https://lynkk.ai/blog/zoom-meeting-recorders

| Where | Find | Replace with |
|---|---|---|
| Body | Lynkk records Zoom with a free bot or no bot, even on free Zoom, while AI Companion needs a paid plan. | Lynkk records Zoom with a bot or no bot, even on free Zoom accounts, for $4 a month, while AI Companion needs a paid Zoom plan. |
| Body | Start free with Lynkk | Get Lynkk Pro, $4 a month |
| Body | That is the gap an AI Zoom meeting recorder fills, and Fathom and Lynkk both have free plans that work with free Zoom. | That is the gap an AI Zoom meeting recorder fills: Fathom has a free plan, and Lynkk costs $4 a month. Both work with free Zoom. |
| Body | Free is $0 with no card: unlimited notes of up to 2 hours each and the first 5 hours of AI summaries in total. Pro is | Pro has unlimited notes of up to 2 hours each and unlimited AI summaries, at |

## 10. Full blog rewrites

Replace the whole post with the text below. Meta title, description and buttons are listed above each post.

### 10.1 `/blog/best-free-ai-note-takers`

Lynkk has no free plan any more, so this post no longer ranks Lynkk as a free tool. It now compares the seven competitors that do have free plans, and presents Lynkk Pro ($4 a month) as the cheapest upgrade when a free plan runs out. Competitor facts are unchanged from the live post (checked 30 September 2026); recheck them before publishing.

- **URL:** keep `/blog/best-free-ai-note-takers` (it already exists; changing it loses what it has built up)
- **Meta title (55 chars):** Best Free AI Note Takers in 2026: 7 Free Plans Compared
- **Meta description (150 chars):** Free AI note taker plans compared: Fathom's unlimited recording, Otter's 300 minutes, Granola's 30-day history and 4 more, plus the cheapest upgrade.
- **Byline line:** By Samarth Wagh · 3 October 2026 · Updated 16 November 2026 · Competitor pricing checked 30 September 2026
- **CTA buttons on this page:** "Download for Mac" and "Get Lynkk Pro, $4 a month" (replace "Start for free")

#### Best Free AI Note Takers in 2026: What Each Free Plan Includes

**Quick answer:** A free AI note taker records your meetings and writes notes and action items at no cost, within limits on minutes, meetings or history. Fathom offers unlimited free recording for video calls, Otter gives 300 minutes a month, and Granola keeps 30 days of history. When those limits start to bite, Lynkk Pro is the lowest-priced upgrade in this guide at $4 a month (₹250 in India), with unlimited notes and AI summaries.

**Disclosure:** This guide is published by Lynkk. Lynkk is a paid tool and is not ranked in the free list below; we cover it separately as an upgrade option. Competitor plan details come from each vendor's own pricing page, checked on the date above.

##### Our quick picks

We compared the free plans of seven AI note takers. Every one has a limit: minutes per month, meetings per month, length per meeting, or how long notes are kept. The limit matters more than the price tag. For paid plans too, see our full list of the [best AI note takers](/blog/best-ai-note-takers).

| Rank and tool | Free plan includes | Main free limit | First paid plan |
|---|---|---|---|
| 1. Fathom | Unlimited recordings and summaries | Advanced summaries on 5 calls a month | $15/user/month |
| 2. Fireflies | Transcription with limits, limited summaries | 400 minutes of storage, 2 hours per meeting | $10/seat/month |
| 3. Otter | 300 minutes a month | 20 AI chat queries | $8.33/user/month |
| 4. Granola | Unlimited meetings | 30 days of note history | $14/user/month |
| 5. Jamie | 10 meetings a month | 30 minutes per meeting | €25/month |
| 6. Read AI | 5 meetings a month | 5-meeting cap | $15/user/month |
| 7. Descript | 1 hour of transcription a month | 1 hour cap | $16/month |

Not free, but cheaper than every upgrade above: **Lynkk Pro at $4 a month** (₹250 in India), with unlimited notes and AI summaries. [More below](#outgrown-free).

##### 1. Fathom: best free recorder for video calls

Fathom's free plan includes unlimited recordings, transcripts and AI summaries, which makes it the most generous free plan for video calls. Advanced summary templates apply to your first 5 calls each month. Paid plans start at $15 per user per month, and new team plans need a paid seat for every member. See [Lynkk vs Fathom](/compare/fathom).

**Best for:** individuals who record a lot of Zoom, Teams or Google Meet calls and only need notes afterward.

**Good to know:** here is [what Fathom's paid tiers cost](/blog/fathom-ai-pricing), plan by plan.

**Where Lynkk goes further:** Fathom is built for online calls. Lynkk also covers in-person meetings, Slack huddles and WhatsApp calls, for $4 a month.

Source: Fathom pricing page, checked 30 September 2026.

##### 2. Fireflies: free plan for a small call library

Fireflies' free plan includes transcription with limits, limited AI summaries and 400 minutes of storage, with each recording capped at 2 hours and no downloads. Pro costs $10 per seat per month billed yearly, or $18 monthly, and Business adds unlimited storage. See [Lynkk vs Fireflies](/compare/fireflies).

**Best for:** small sales teams that want a searchable library of short calls.

**Good to know:** our [Fireflies pricing guide](/blog/fireflies-pricing) explains what the free plan actually allows.

**Where Lynkk goes further:** Lynkk records in-person meetings and handles mid-sentence language switching.

Source: Fireflies pricing page, checked October 2026.

##### 3. Is Otter AI free?

Yes, Otter AI is free on its Basic plan, which includes 300 transcription minutes a month and 20 AI chat queries. Otter Pro costs $8.33 per user per month billed annually and raises the limit to 1,200 minutes. Heavy users hit the free cap in about two weeks of daily 30-minute calls. See [Lynkk vs Otter](/compare/otter).

**Best for:** people who want to read a live transcript during a few calls a week.

**Where Lynkk goes further:** Lynkk Pro has no monthly minute cap and sends action items from meetings to Jira, for less than half the price of Otter Pro.

Source: Otter pricing page, checked 30 September 2026.

##### 4. Granola: best free AI notepad

Granola's free plan has no meeting limit, but you can only see notes from the last 30 days. It records your device's audio without a bot and runs on Mac, Windows, iPhone and Android. Business costs $14 per user per month and removes the history limit. See [Lynkk vs Granola](/compare/granola).

**Best for:** individuals who type rough notes during calls and want AI to fill in the gaps.

**Good to know:** see [what Granola costs](/blog/granola-ai-pricing) beyond the free plan.

**Where Lynkk goes further:** Lynkk Pro keeps every note with no history limit, at $4 a month against Granola's $14.

Source: Granola pricing page, checked 30 September 2026.

##### 5. Jamie: best free bot-free option

Jamie's free plan covers 10 meetings a month of up to 30 minutes each, with no bot on the call. Paid plans start at €25 per month, and Jamie hosts data in the EU. It suits short internal check-ins where you would rather not have a bot join, but longer meetings get cut off on the free plan.

**Best for:** short, bot-free check-ins under 30 minutes.

**Where Lynkk goes further:** Lynkk also records without a bot, through its Chrome extension and Mac app, and lets you choose the region where your data is processed.

Source: Jamie pricing page, checked 30 September 2026.

##### 6. Read AI: free plan for meeting reports

Read AI's free plan covers 5 meetings a month with summaries, transcription and search. Pro starts at $15 per user per month billed annually. Its strength is reporting on how meetings went, and the Enterprise+ plan adds data retention policies, domain capture and SAML for larger companies. See [Lynkk vs Read AI](/compare/read-ai).

**Best for:** managers who want reports on how meetings went.

**Where Lynkk goes further:** Lynkk focuses on the follow-up: action items with owners, Jira, and answers across your notes with Ask Lynkk.

Source: Read AI plans and pricing page, checked 30 September 2026.

##### 7. Descript: free transcription for recordings

Descript's free plan includes 1 hour of automatic transcription a month, aimed at editing audio and video rather than live meetings. Paid plans start at $16 a month. You edit the recording by editing its transcript, which makes it a creator tool more than a note taker, but the free hour is handy for a short file.

**Best for:** creators who edit recorded audio or video by editing the transcript.

**Where Lynkk goes further:** Lynkk records the meeting itself and writes notes and tasks automatically.

Source: Descript pricing page, checked 30 September 2026.

<a id="outgrown-free"></a>
##### Outgrown your free plan? Lynkk Pro is $4 a month

Lynkk is not free: it is a paid tool from the first meeting. We include it here because it costs less than any paid plan in this guide, so it is often the cheapest step up when a free plan runs out.

Lynkk records Zoom, Google Meet, Microsoft Teams and in-person meetings in one account, plus Slack huddles and WhatsApp calls from the Mac app, then writes notes and action items after each one. Lynkk Pro, at $4 a month (₹250 in India), includes:

- **Unlimited notes and AI summaries,** with a transcript and speaker labels in 17 languages, Hinglish included.
- **Bot or no bot:** the meeting bot for Zoom, Meet and Teams, the Chrome extension that records without a bot, or the Mac app.
- **In-person meetings:** the Mac app records the whole room and keeps recording if your connection drops.
- **Action items with owners** on one task board, sent to Jira when you choose.
- **Ask Lynkk,** which answers questions across every call with sources, plus answers in Slack, meeting video from the bot and a weekly digest.

Teams can move to Enterprise (custom price) for a shared workspace of up to 10 people, where everyone gets Pro and admins can ask across the whole workspace. See the full [Lynkk pricing](/pricing).

##### How many meetings can you record on each free AI note taker?

The number of meetings you can record for free ranges from two a month to unlimited. We converted each free plan into 30-minute meetings, the length of a typical team call. A plan that looks generous can still stop you: some count minutes, some count meetings, and some hide older notes.

| Free plan | Limit | About how many 30-minute meetings |
|---|---|---|
| Fathom | Unlimited recordings | Unlimited |
| Granola | Unlimited meetings, 30-day history | Unlimited (older notes hidden) |
| Fireflies | 400 minutes of storage | About 13 stored at a time |
| Otter | 300 minutes a month | About 10 a month |
| Jamie | 10 meetings a month, up to 30 minutes each | 10 a month |
| Read AI | 5 meetings a month | 5 a month |
| Descript | 1 hour of transcription a month | 2 a month |

For comparison, Lynkk Pro ($4 a month) has unlimited notes and AI summaries.

##### Which free AI note taker works for in-person meetings?

Most free plans in this list are built for Zoom, Teams and Google Meet. Only two of the seven record face-to-face conversations: Otter through its mobile app, and Granola through its phone app. If you run client visits, interviews or workshops, check in-person support before anything else.

If you work on a Mac, Lynkk Pro ($4 a month) records the room in 17 languages, labels each speaker, and keeps recording if Wi-Fi drops, then uploads later. Lynkk has no phone app, so for in-person meetings on a phone, Otter or Granola fit better.

##### Which free AI note taker is best for Zoom, Teams and Google Meet?

Fathom, Fireflies and Otter all record Zoom, Teams and Google Meet on their free plans. Gemini notes in Google Meet and Zoom's AI Companion both need paid plans, and Copilot in Teams is a paid add-on. Lynkk's meeting bot joins all three on Lynkk Pro, at $4 a month.

- **Microsoft Teams:** see our guide to the [AI note taker for Microsoft Teams](/blog/ai-note-taker-microsoft-teams).
- **Google Meet:** Fathom works in Google Meet on its free plan; see [how to find a Google Meet transcript](/blog/google-meet-transcript).
- **Zoom:** see our [Zoom note taker guide](/blog/zoom-note-taker).

##### Are free AI meeting notes takers safe?

A free AI meeting notes taker is as safe as the vendor's paid plan if the protections do not change with price. Check that data travels encrypted, that the vendor does not train AI models on your meetings, and who can open your notes. Those answers should be the same on a $0 plan as on a paid one.

For comparison, Lynkk sends everything over HTTPS, encrypts tokens for connected tools with AES-256-GCM, and does not train AI models on your conversations; on a personal account, no one else can open your notes unless you share them. Details are on the [Lynkk security page](/security). Consent rules apply on any plan; see our guide on whether it is legal to record a meeting.

##### When should you upgrade from a free AI note taker?

Upgrade when your free plan's limit starts shaping your week, usually after 10 to 20 recorded meetings a month. The three most common signs are hitting the cap mid-month, needing notes older than the history limit, and wanting follow-up such as summaries or answers done for you every time.

- **You hit the cap mid-month.** Minute and meeting caps are the most common reason people pay.
- **You need older notes.** A 30-day history limit hides last quarter's decisions.
- **You need more AI.** Unlimited summaries and questions across meetings usually sit on paid plans.

Upgrades in this guide start at $8.33 a month (Otter Pro). Lynkk Pro is $4 a month.

##### FAQ

###### Is there a completely free AI note taker?

Yes. All seven tools in our list have a free plan, but every free plan has a limit on minutes, meetings, meeting length, summaries or history. Fathom's unlimited recordings are the most generous for video calls. Check which limit you will hit first before you commit to one tool.

###### Is Lynkk free?

No. Lynkk is paid only, with no free plan or free trial. Lynkk Pro is $4 a month (₹250 in India) with unlimited notes and AI summaries, and Enterprise is priced on a call.

###### Is Otter.ai free?

Yes. Otter's Basic plan is free and includes 300 transcription minutes a month plus 20 AI chat queries. That covers about ten 30-minute calls. If you need more, Otter Pro costs $8.33 per user per month billed annually and raises the limit to 1,200 minutes.

###### What is the best free AI note taker app for in-person meetings?

Otter's mobile app records in-person meetings on its free plan, and Granola's phone app does too, but Granola's free plan keeps only 30 days of notes. If you record on a Mac, Lynkk Pro ($4 a month) records the room with speaker labels in 17 languages.

###### Can I use a free AI note taker for Microsoft Teams?

Yes. Fathom, Fireflies and Otter all support Teams on their free plans. Microsoft's own Copilot recap costs $30 per user per month on top of a Microsoft 365 license, and intelligent recap needs Teams Premium, so free third-party tools are the cheaper route.

###### Do free AI note takers have time limits?

Most do. Jamie stops at 30 minutes per meeting, Fireflies at 2 hours per recording, and Otter at 300 minutes a month. Read AI caps you at 5 meetings a month. Check the per-meeting limit if you run long workshops or interviews before you rely on one.

###### How much does it cost to upgrade from free?

Upgrades on the free tools in this guide start around $8 to $16 per user per month: Otter Pro is $8.33, Fireflies Pro $10, Granola Business $14, Fathom and Read AI from $15, and Descript from $16. Lynkk Pro costs less, at $4 a month (₹250 in India).

##### Conclusion

Every free AI note taker has a limit, so pick the one whose limit you will not hit. Fathom is the most generous for video calls, Otter suits a few live transcripts a week, and Granola works if you only need the last 30 days. When you outgrow a free plan, Lynkk Pro gives you unlimited notes and AI summaries, Ask Lynkk and in-person recording for $4 a month. [Get Lynkk Pro](/pricing).

### 10.2 `/blog/ai-note-taker-microsoft-teams`

This post said Lynkk "starts free" in 10 places. Lynkk stays the #1 pick, now as a paid tool at $4 a month, which is still the cheapest paid option for Teams. The page also gets the fixes from the GSC deep dive: it has 2,309 impressions and 1 click at an average position of 20.4, so the title and meta are rewritten and the how-to section is renamed to match "how to add an AI note taker to Teams" searches. Microsoft and competitor facts are unchanged from the live post (checked 30 September 2026); recheck them before publishing.

- **URL:** keep `/blog/ai-note-taker-microsoft-teams`
- **Meta title (55 chars):** AI Note Taker for Microsoft Teams: 7 Picks, No Copilot
- **Meta description (147 chars):** Copilot costs $30 a user. Compare Teams Premium recap, free Teams transcription, Otter, Fireflies, Fathom and Lynkk ($4/mo) for a 10-person team.
- **Byline line:** By Samarth Wagh · 4 October 2026 · Updated 16 November 2026 · Pricing checked 30 September 2026
- **CTA buttons on this page:** "Download for Mac" and "Get Lynkk Pro, $4 a month" (replace "Start for free")

#### Best AI Note Takers for Microsoft Teams (2026)

**Quick answer:** Teams has two built-in AI note takers: Microsoft 365 Copilot, a $30 per user per month add-on, and intelligent recap in Teams Premium. Without either license, Teams gives you a free transcript but no AI summary. Third-party tools fill the gap; Lynkk is an [AI note taker for Microsoft Teams](/integrations/microsoft-teams) that costs $4 a month (₹250 in India) and needs no Copilot license.

**Disclosure:** This guide is published by Lynkk, and Lynkk is one of the tools reviewed. Microsoft details come from Microsoft Support and Microsoft Learn; other tools' details come from each vendor's own pricing page, checked on the date above.

##### Does Teams have an AI note taker?

Yes. Teams has two built-in AI note takers: Microsoft 365 Copilot, a $30 per user per month add-on, and intelligent recap in Teams Premium. Both write a summary of what was said. Without either license, Teams still records and transcribes meetings for free, but you get the raw transcript with no AI summary or action items.

A Teams AI note taker is software that listens to a Teams meeting and writes the notes for you: a summary, key decisions and action items. There are two kinds: Microsoft's own features above, and third-party assistants that join or record your Teams calls. The right choice depends on your Microsoft 365 licenses, whether you also meet outside Teams, and what should happen after the meeting.

##### Our quick picks

We picked seven Teams AI options, from Microsoft's own features to third-party meeting assistants, and list each one's cost and admin story below. Prices are the lowest published, checked 30 September 2026. For tools across every platform, see our comparison of the [best AI note takers](/blog/best-ai-note-takers).

| Rank and option | Best for | What you get | SSO, SCIM and admin | Cost |
|---|---|---|---|---|
| 1. Lynkk (our product) | Teams plus Zoom, Meet and in person | Notes, tasks, Jira, cited answers | No SSO on Pro; Enterprise adds a shared workspace for up to 10, set up with the Lynkk team | Pro $4/month (₹250); Enterprise custom |
| 2. Microsoft 365 Copilot | Companies all-in on Microsoft 365 | Recap and Q&A in Teams | Runs inside your Microsoft 365 tenant | $30/user/month add-on |
| 3. Teams Premium intelligent recap | AI recap without full Copilot | Recap of recorded meetings | Runs inside your Microsoft 365 tenant | Teams Premium license |
| 4. Teams built-in transcription | Free transcript in Teams | Transcript only | Runs inside your Microsoft 365 tenant | Included with Teams |
| 5. Otter | Live transcript in Teams | Transcript and notes | SSO and SCIM on Enterprise | Free 300 min; Pro $8.33/user/month |
| 6. Fireflies | Searchable Teams call library | Transcript and summaries | SSO and SCIM on Enterprise ($39/seat/month, yearly) | Free; Pro $10/seat/month |
| 7. Fathom | Free Teams recording | Summaries | Check with Fathom | Free; paid from $15/user/month |

##### Free AI note taker options for Teams

You can get free AI notes in Teams without Copilot. Teams' own transcript costs nothing but has no summary. Fathom's free plan includes unlimited recordings and AI summaries, Otter's free plan gives 300 minutes a month, and Fireflies has a free plan with 400 minutes of storage.

| Free option | What is free | The catch |
|---|---|---|
| Teams built-in transcription | Recording and transcript | No summary or action items |
| Fathom Free | Unlimited recordings, transcripts and summaries | New Team plans have no free seats |
| Otter Basic | 300 transcription minutes a month | Minutes run out on busy weeks |
| Fireflies Free | Transcription with 400 minutes of storage | Recordings capped at 2 hours |

Lynkk has no free plan. If you outgrow these limits, Lynkk Pro is $4 a month (₹250 in India) with unlimited notes and AI summaries, less than any paid plan above. More $0 options, for every platform, are in our guide to [free AI note takers](/blog/best-free-ai-note-takers). Sources: each vendor's pricing page, checked 30 September 2026.

##### 1. Lynkk (our product): best for Teams plus Zoom, Google Meet and in-person meetings

Lynkk writes a note after every Teams call, with a summary, action items with owners and due dates, decisions and a transcript with speaker labels, in 17 languages. It needs no Copilot or Teams Premium license. It also records Zoom, Google Meet and in-person meetings, so all your meetings sit in one searchable account.

###### How does Lynkk record Microsoft Teams meetings?

Lynkk records Teams in three ways, so you can match each meeting.

- **Meeting bot:** the [Lynkk meeting bot for Teams, Zoom and Meet](/features/meeting-bot) joins when you paste the Teams link, or on its own from a connected Google Calendar. It waits in the lobby until the host lets it in.
- **Browser, no bot:** the [Lynkk Chrome extension](/features/chrome-extension) records Teams in the browser with no extra participant.
- **Mac app:** notices a call in the Teams app or browser and asks whether to record, with nothing joining the call.

###### What does Lynkk do that Microsoft's Teams AI does not?

- **No Microsoft add-on:** AI notes for $4 a month, with no Copilot or Teams Premium license and no admin setup.
- **Every platform:** Teams, Zoom, Google Meet and in-person meetings in one account.
- **Tasks:** [action items with owners and due dates](/features/action-items) on one task board, sent to Jira when you choose.
- **Answers across meetings:** [ask about a customer or project](/features/ask-your-meetings) and get one answer from every call, with sources.

**Pricing:** Lynkk Pro is $4 a month (₹250 in India), and Enterprise is priced on a call. See [Lynkk pricing](/pricing).

##### 2. Microsoft 365 Copilot: best for Microsoft 365 companies

Microsoft 365 Copilot costs $30 per user per month as an add-on with an annual commitment, and it needs a qualifying Microsoft 365 license. In Teams, Copilot can recap meetings and answer questions about what was said, as long as the meeting is transcribed. It also works across Word, Excel and Outlook, which is most of what you pay for.

**Best for:** companies that want Copilot across Word, Excel, Outlook and Teams, not only for meeting notes.

**Where Lynkk goes further:** Lynkk costs $4 a month instead of $30, covers Zoom, Google Meet and in-person meetings as well as Teams, and lets you send tasks to Jira from the meeting.

Source: Microsoft 365 Copilot pricing page, checked 30 September 2026.

##### 3. Teams Premium intelligent recap: AI recap without full Copilot

Teams Premium adds three main extras: intelligent recap, which summarizes recorded Teams meetings, live translated captions and advanced meeting controls. To use intelligent recap, each user needs a Teams Premium or Microsoft 365 Copilot license, and the meeting must be recorded and transcribed. It is the cheaper Microsoft route to AI recaps.

**Best for:** Teams-only companies that want AI recaps without buying Copilot for everyone.

**Where Lynkk goes further:** Lynkk needs no extra Microsoft license and turns the recap into owned tasks you can send to Jira.

Source: Microsoft Learn, checked 30 September 2026.

##### 4. Teams built-in transcription: free transcript in Teams

Microsoft Teams includes recording and live transcription at no extra cost, with the transcript available in the calendar event right after the meeting. Organizers can download it as a .docx or .vtt file. It is a complete written record of who said what, but it does not summarize the meeting or pull out action items.

**Best for:** teams that only need a written record, not a summary or action items.

**Good to know:** all participants see a notice when transcription starts, and it stops when everyone leaves. Organizers, co-organizers and presenters can stop and restart it during the meeting.

**Where Lynkk goes further:** a transcript is the raw material. Lynkk writes the summary, assigns action items and answers questions across every meeting.

Source: Microsoft Support, checked 30 September 2026.

##### 5. Otter: best for a live transcript in Teams

Otter's free plan includes 300 transcription minutes a month, and Pro costs $8.33 per user per month billed annually. Otter shows a live transcript during the Teams meeting, which suits people who like to read along. Its Enterprise plan is custom-priced and adds HIPAA support, SSO and SCIM. See [Lynkk vs Otter](/compare/otter).

**Best for:** people who like to read along during Teams calls.

**Where Lynkk goes further:** Lynkk lets you send action items from the meeting to Jira, and its Mac app records in-person meetings with no bot.

Source: Otter pricing page, checked 30 September 2026.

##### 6. Fireflies: best for a searchable Teams call library

Fireflies includes transcription on all four plans, with 400 minutes of storage per team on the free plan. Pro costs $10 per seat per month billed annually. Recordings are capped at 2 hours on the Free and Pro plans and 3 hours on Business. It suits sales teams that search past calls by keyword. See [Lynkk vs Fireflies](/compare/fireflies).

**Best for:** sales teams that want to search past Teams calls by keyword.

**Where Lynkk goes further:** Lynkk records in-person meetings and handles 17 languages with mid-sentence switching.

Source: Fireflies pricing page, checked 30 September 2026.

##### 7. Fathom: best free Teams recorder

Fathom's free plan includes unlimited recordings, transcripts and AI summaries, and paid plans start at $15 per user per month. It works with Teams, Zoom and Google Meet. New Team and Business plans no longer include free seats, so every member of a team needs a paid seat. See [Lynkk vs Fathom](/compare/fathom).

**Best for:** individuals who want free Teams recordings with a summary afterward.

**Where Lynkk goes further:** Lynkk records in-person conversations with its Mac app and sends action items to Jira.

Source: Fathom pricing page, checked 30 September 2026.

##### Can Copilot take meeting notes?

Yes. Copilot can take meeting notes in Teams when each user has a Microsoft 365 Copilot license, at $30 per user per month, and the meeting is transcribed. Copilot meeting notes include a recap and let you ask questions about what was said. A Teams Copilot meeting summary is only available to users with that license.

For a 10-person team, that is about $300 a month on top of Microsoft 365. Lynkk Pro is $4 a month (₹250 in India) per person.

##### How much does Teams AI cost for a 10-person team?

Teams AI note takers cost between $0 and about $300 a month for 10 people, based on the lowest published prices checked on 30 September 2026. Teams' own transcript is free but has no summary, Copilot is the most expensive, and most third-party tools sit between $80 and $150 for the team.

| Option | Price per user | 10 people per month |
|---|---|---|
| Teams built-in transcription | Included | $0 (no AI summary) |
| Lynkk Pro | $4 (₹250) | $40 (₹2,500); a shared [workspace](/features/workspaces) for up to 10 is on Enterprise, priced on a call |
| Otter Pro | $8.33 | About $83 |
| Fireflies Pro | $10 | $100 |
| Fathom | From $15 | From $150 |
| Microsoft 365 Copilot | $30 add-on | $300 |

##### Where do Teams recordings and transcripts go?

Teams saves recordings in one of two places, depending on the meeting type. Channel meeting recordings go to the channel's SharePoint site in a Recordings folder. Other meetings go to the OneDrive of the person who pressed Record. Transcripts appear in the meeting's calendar event right after the meeting ends.

With Lynkk, notes, transcripts and action items from every Teams call sit in one searchable account instead.

##### How to add an AI note taker to Microsoft Teams

You can add an AI note taker to Teams in four steps with Lynkk, with no Copilot license. Lynkk's calendar connection is Google Calendar only, so if your invites come from Outlook, paste the Teams link instead. With Microsoft's own tools, each user needs a Copilot or Teams Premium license and the meeting must be recorded and transcribed.

1. Get Lynkk Pro ($4 a month) on the web app.
2. Choose how to record: paste the Teams link to send the meeting bot, connect Google Calendar so it joins on its own, or record from the Mac app or Chrome extension with no bot.
3. Hold your Teams meeting as usual, and let the bot in from the lobby if you used it.
4. Open your notes after the call: summary, action items with owners you can send to Jira, and the transcript.

##### How do you remove or turn off an AI note taker in Teams?

If a note taker bot joined a meeting you host, remove it from the participant list like any other guest. Most note takers join from a calendar connection, so the lasting fix is in that tool's settings, not in Teams: ask the attendee who sent it to switch off auto-join for your meetings.

In Lynkk, the notetaker only joins when you paste a link or turn on auto-join for your connected Google Calendar. Turn auto-join off and it stays out of your calls, while the Mac app and Chrome extension still let you record with no bot.

##### What should you check before rolling out a Teams AI note taker?

Check five things before you roll out any Teams AI note taker across a company: licenses, admin consent, data handling, consent notices and platform coverage. These questions come up in almost every IT review, and the answers differ a lot between Microsoft's add-ons and third-party tools.

- **Licenses:** does it need Copilot or Teams Premium for every user?
- **Admin consent:** does the tool need tenant-level permissions, SSO or SCIM?
- **Data handling:** does the vendor explain how meetings are stored and protected?
- **Consent notices:** do participants see when a meeting is recorded?
- **Coverage:** will it also handle Zoom, Google Meet and in-person meetings?

Lynkk's bot joins as a visible participant, and it covers every platform in one account.

##### Is a Teams AI note taker secure enough for business?

A Teams AI note taker is secure enough for business when it encrypts data, explains how meetings are stored and does not train AI models on your meetings. Ask each vendor about all three in writing, and check where the recordings live, who on the vendor's side can open them, and how you delete them.

Ask which encryption it uses; the [NIST Advanced Encryption Standard (FIPS 197)](https://csrc.nist.gov/pubs/fips/197/final) is the usual benchmark, and the [EU General Data Protection Regulation (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) applies if you meet people in the EU. Lynkk sends everything over HTTPS, encrypts tokens for connected tools with AES-256-GCM, and does not train AI models on your conversations. Details are on the [Lynkk security page](/security). Recording consent rules still apply; see our guide on [whether it is legal to record a meeting](/blog/is-it-legal-to-record-a-meeting), and announce your note taker at the start of each call.

##### FAQ

###### What is the best Teams AI note taker?

If you are all-in on Microsoft 365, Copilot works inside Teams for $30 per user per month. If you also meet on Zoom, Google Meet or in person, or do not want a Microsoft add-on, a third-party note taker covers more for less: Lynkk Pro is $4 a month. The quick picks table compares seven.

###### Is Microsoft Teams AI free?

Teams includes free recording and transcription, but its AI features cost extra. Microsoft 365 Copilot is a $30 per user per month add-on, and intelligent recap needs Teams Premium or Copilot. Free third-party note takers, such as Fathom's free plan, add AI summaries without a Microsoft license.

###### Is Lynkk free for Teams?

No. Lynkk is paid only, with no free plan or free trial. Lynkk Pro is $4 a month (₹250 in India) and includes the Teams meeting bot, the Chrome extension, the Mac app and unlimited AI notes.

###### Can I use an AI note taker in Teams without admin approval?

It depends on your company's Microsoft 365 settings, so check with IT first. Some third-party bots need tenant-level permissions. Tools that record from your own computer, such as a desktop app or a Chrome extension, add nothing to the meeting, but your company's recording policy still applies.

###### Does Copilot work in Zoom or Google Meet?

Microsoft 365 Copilot's meeting recap is built into Microsoft Teams meetings and needs a Copilot license. If your company meets on several platforms, a cross-platform note taker is simpler. See our guides to [Zoom note takers](/blog/zoom-note-taker) and getting a [Google Meet transcript](/blog/google-meet-transcript).

###### How accurate are Teams AI meeting notes?

Accuracy depends on audio quality, accents and people talking over each other, more than on the tool. Ask attendees to use headsets, keep one person speaking at a time on important calls, and check names and numbers in the notes before you share them with anyone outside the meeting.

###### Can a Teams AI note taker send tasks to Jira?

Yes, Lynkk can. After a Teams meeting, open the note and send its action items to Jira: Lynkk creates one issue per action item, with the owner and due date from the meeting. Nothing is pushed automatically, so you choose which meetings reach Jira.

##### Conclusion

Microsoft's Teams AI features work well if you live entirely inside Microsoft 365 and can pay $30 per user per month. For everyone else, Lynkk Pro costs $4 a month, records Teams with or without a bot, lets you send action items from meetings to Jira, and covers Zoom, Google Meet and in-person meetings too. [Get Lynkk Pro](/pricing).
