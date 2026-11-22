# Lynkk.ai SEO Audit: Why Impressions Are Not Turning Into Clicks

Date: 22 Nov 2026
Data: Google Search Console export (last 3 months, web), Ubersuggest (domain, backlinks, PageSpeed, keywords, SERP), and a live crawl of the 95 blog, compare and feature pages in the sitemap.

---

## 1. The headline numbers

| Metric | Value |
|---|---|
| Clicks / Impressions (3 months) | 460 / 92,019 |
| Overall CTR | 0.50% |
| Average position | 18.1 |
| Daily impressions, early Oct to 20 Nov | ~20/day to ~5,200/day |
| Daily clicks, latest | 18 to 39/day |
| Brand query "lynkk" | 62 clicks, 17.6% CTR, position 2.2 |
| Domain Authority (Ubersuggest) | **2** |
| Referring domains / dofollow backlinks | **8 / 2** |
| Mobile LCP / Speed Index (Ubersuggest PageSpeed) | **4.8 s / 8.8 s** |

The site is about 6 weeks into real visibility. Impressions grew roughly 250x and positions improved from about 60 to about 15. That's a healthy start, but CTR stays flat at about 0.4% because of the five problems below.

---

## 2. Root causes (in order of impact)

### Cause 1: Most impressions are not real page-1 rankings

Non-brand GSC queries, grouped by position:

| Position | Queries | Clicks | Impressions | CTR |
|---|---|---|---|---|
| 1-3 | 34 | 64 | 1,671 | 3.83% (almost all brand) |
| 4-10 | 243 | 21 | 9,190 | 0.23% |
| 11-20 | 146 | 19 | 6,065 | 0.31% |
| 21-50 | 400 | 48 | 14,482 | 0.33% |
| 50+ | 177 | 18 | 5,330 | 0.34% |

- **Short, non-brand keywords average position 31** (page 3 or 4). Nobody clicks there, so the impressions are "seen in a deep scroll or a crawl", not real exposure.
- The US gives 49% of all impressions (45,489) at **position 25.1 with 0.17% CTR**. India ranks at position 10 with 1.64% CTR. Your main market is the one where you rank worst.

### Cause 2: About 5,500 impressions are AI Mode / AI Overview citations, not blue links

141 queries are long, chat-style questions (8+ words), for example:

- "how do founders keep track of everything said in investor and team meetings?" (325 impr, pos 4.4)
- "which zoom ai companion alternatives also cover google meet calls and in-person interviews?" (297 impr, pos 4.2)
- "rolling out an ai notetaker to 300 reps: which plans include sso, scim and an admin dashboard?" (205 impr, pos 3.6)

Together: **5,553 impressions, average position 7.0, 2 clicks (0.04%)**. These are Google AI Mode / AI Overviews citing your pages. They are good for brand visibility, but they drag the 4-10 position bucket CTR down to 0.23% and make GSC look like "we're on page 1 and nobody clicks". Filter them out when you track CTR (GSC regex filter: `^(\S+\s){7,}\S+`).

### Cause 3: Titles and meta descriptions give the answer away (zero-click by design)

The pages that rank best for real keywords answer the query in the snippet itself, so the searcher has no reason to click:

| Page | Impr | Pos | CTR | What the snippet already says |
|---|---|---|---|---|
| /blog/google-meet-transcript | 13,277 | 8.4 | 0.30% | "Google Meet saves the transcript to the organizer's Google Drive. Find it in 3 steps..." |
| /blog/granola-ai-pricing | 3,323 | 9.2 | **0%** | Title: "Free, $14 and $35 Plans". Meta: "Granola is free with 30 days of history. Business is $14..." |
| /blog/fathom-ai-pricing | 1,168 | 12.3 | 0.17% | Title: "Free vs $16, $15 and $25 Plans" |
| /blog/gong-pricing | 1,582 | 11.5 | 0.51% | Title: "$1,300 to $1,600 a User + Fees" |
| /blog/ai-notetaker-security | 806 | **3.7** | **0%** | Ranks top 4 and gets zero clicks |
| /blog/zoom-ai-companion-alternatives | 1,439 | 5.8 | **0%** | Ranks top 6 and gets zero clicks |
| /blog/founders-meeting-notes | 719 | 5.2 | **0%** | Ranks top 6 and gets zero clicks |

Look at the live SERP for "granola pricing" (Ubersuggest, US, today): scribbl.co ranks #4 with *"Granola Pricing 2026: Is the Granola AI App Free? Every Plan"*. That title asks a question and hints at a catch. Yours states the full answer.

### Cause 4: Almost no authority (DA 2, 8 referring domains, 2 dofollow links)

With 76 blog posts and only 2 followed backlinks, Google has no reason to put you above Granola, Fathom, Otter, Zapier, Tactiq and others for competitive terms. This is why "ai meeting assistant" sits at 36.7, "best ai note taker" at 18.8, "zoom ai note taker" at 40, and "otter ai alternative" at 76. **More blogs alone will not fix this.** Each new post starts at position 30+ too.

### Cause 5: Slow on mobile

Ubersuggest PageSpeed audit, mobile: LCP 4.8 s, Speed Index 8.8 s, TTI 6.4 s, TBT 365 ms, server response ~590 ms, redirects ~630 ms, 179 KB unused JS. Desktop is fine (LCP 0.95 s). Core Web Vitals are a small ranking factor, but a 4.8 s LCP also raises pogo-sticking, which hurts the pages that do get clicks.

---

## 3. Cannibalisation: there IS some

The GSC export doesn't have query-by-page rows, so this is based on titles, ranking URLs (Ubersuggest) and the GSC page list. These clusters compete with each other:

| Cluster | Pages competing | Evidence | Fix |
|---|---|---|---|
| Otter alternatives | /compare/otter vs /blog/otter-ai-alternatives | "otter ai alternative" ranks at **76.8** with the blog page; /compare/otter sits at 4.5 for other queries | Merge the blog into /compare/otter (301), or make the blog the list and the compare page strictly 1:1, with a clear internal link |
| Audio transcription | /blog/transcribe-audio-to-text ("Best Software to Transcribe Audio to Text: 5 Picks") vs /blog/ai-transcription-software ("AI Transcription Software: 7 Best Tools") | Same intent, both listicles | Merge into one, 301 the other |
| Meeting minutes | /blog/meeting-minutes-sample, /blog/meeting-notes-vs-minutes, /blog/meeting-summary-template, /blog/meeting-notes-template | "meeting minutes example" queries split between 14 and 35 | Give each page one distinct intent (example vs definition vs summary vs notes), cross-link with exact anchors |
| Zoom | /blog/zoom-note-taker, /blog/zoom-meeting-recorders, /blog/how-to-transcribe-zoom-meetings, /blog/zoom-bot-join-meeting, old /articles/zoom-note-taker | /articles/ URL still has 1,271 impressions (it now 301s to /blog/, Google is still consolidating) | Remove /articles/ URLs from the sitemap and internal links, re-submit |
| Best AI note takers | /blog/best-ai-note-takers, /blog/best-free-ai-note-takers, /blog/ai-powered-meeting-assistants, /blog/best-ai-meeting-notes-for-teams | best-free-ai-note-takers has only **5 impressions** even though "free ai note taker" has 2,400 US searches | Check indexing (URL Inspection), then link it from best-ai-note-takers and the homepage |
| Voice to text | /blog/voice-to-text-apps (title says "Dictation Software for Small Business"), /blog/dictate-in-microsoft-word, /blog/speech-to-text-mac | voice-to-text-apps ranks for "voice to text software" at **56** because its title targets a different keyword | Retitle to "Best Voice to Text Apps (2026)" or split |

**How to confirm in GSC:** Performance > Queries > click a query > Pages tab. If two or more URLs show impressions for the same query, they're cannibalising.

---

## 4. What to do on the website (priority order)

### A. This week: rewrite titles and metas on the 15 pages with the most impressions (biggest, fastest win)

Rules: put the keyword first, add a reason to click (a verdict, a hidden cost, a comparison, a free download), and **don't put the full answer in the snippet**.

| Page | Current title | Suggested title | Suggested meta |
|---|---|---|---|
| google-meet-transcript | Google Meet Transcript: Where to Find It and How to Get One | Google Meet Transcript Missing? Find It, Fix It, or Get One Free | Transcript not in Drive? The 4 reasons it fails (wrong plan, not organizer, turned off, still processing) and a free way to get one on any Meet plan. |
| granola-ai-pricing | Granola Pricing (Nov 2026): Free, $14 and $35 Plans | Granola Pricing 2026: Is It Free? The Limits Nobody Mentions | What Granola's free plan really caps, what a 10-person team pays per year, and 3 cheaper options. Updated Nov 2026. |
| fathom-ai-pricing | Fathom Pricing (Nov 2026): Free vs $16... | Fathom Pricing 2026: Is the Free Plan Enough? (Real Team Cost) | What breaks on Fathom Free, which plan teams actually need, and what 5, 10 and 25 seats cost per year. |
| gong-pricing | Gong Pricing (Nov 2026): $1,300 to $1,600 a User + Fees | Gong Pricing 2026: Real Quotes, Hidden Fees and Cheaper Options | Gong doesn't publish prices. Here are real per-seat quotes, platform fees, renewal increases and 5 tools at a fraction of the cost. |
| follow-up-email-after-meeting (4,856 impr, 0.37%) | Follow-Up Email After a Meeting: 15 Templates to Copy | 15 Follow-Up Email Templates After a Meeting (Copy and Send) | Keep "Free Google Doc" or "copy-paste" in the meta. Add FAQ rich results. |
| action-items-examples-template (4,058, 0.12%) | Action Item Template: Free for Sheets, Excel + 12 Examples | Free Action Item Template (Google Sheets + Excel Download) | Add an actual download button. Template searchers click on "download". |
| meeting-summary-template (3,527, 0.28%) | Meeting Summary Template + Examples | Meeting Summary Template: 7 Free Examples (Email + Doc) | Covers "meeting summary email" (pos 4.5) too |
| meeting-minutes-sample (3,172, 0.25%) | Meeting Minutes Format (MoM): Templates and Examples | Meeting Minutes Example: 10 Free MoM Templates (Word, Docs) | Matches the 3,600/mo "examples of meeting minutes" cluster |
| voice-memo-transcription (3,070, 0.29%) | Voice Memo Transcription on iPhone: Free in 3 Taps | Transcribe iPhone Voice Memos to Text (Free, Plus Long Files) | Hint at what the built-in way can't do |
| ai-notetaker-security (806, pos 3.7, 0%) | AI Notetaker Security in 2026: SSO, SCIM, Retention | Is Your AI Notetaker Safe? 12-Point Security Checklist (2026) | Offer the checklist as a download |
| zoom-ai-companion-alternatives (1,439, pos 5.8, 0%) | Zoom AI Companion Alternatives: 7 Tools Compared (2026) | 7 Zoom AI Companion Alternatives That Also Work on Meet and Teams | Matches the AI Mode questions you already appear for |
| founders-meeting-notes (719, pos 5.2, 0%) | How Founders Track Every Investor and Team Meeting | Founder Meeting Notes: The System to Track Every Investor Call (Template) | |
| voice-to-text-apps | Best Dictation Software for Small Business | Best Voice to Text Apps in 2026 (Free and Paid, Tested) | Fixes intent mismatch |
| /compare/otter, /compare/fireflies, /compare/granola | Already good | Keep. These have your best non-brand CTR | |

Track each change for 14 days in GSC (Compare date ranges, filter by page).

### B. Next 30 days: build authority (biggest long-term lever)

Goal: go from 8 to 40+ referring domains in 90 days.

1. **AI tool directories** (fast, often dofollow): There's An AI For That, Futurepedia, Toolify, AI Tool Hunt, TopAI.tools, SaaSHub, AlternativeTo, G2, Capterra, Product Hunt. The copy is ready in `memory/lynkk-brand.md` and `launch/producthunt-submission.md`.
2. **"Alternative to" listings**: get Lynkk listed on AlternativeTo / SaaSHub pages for Otter, Fireflies, Granola, Fathom, Gong.
3. **Guest posts / roundups**: pitch to "best AI note taker" roundup authors (Zapier, TechRadar, Tom's Guide, Indian SaaS blogs). Offer the Hinglish/multilingual and $4/month angle, which is unique.
4. **Linkable assets**: publish original data (e.g. "We analyzed 10,000 meetings: how long action items take to close") or a free tool (meeting cost calculator, MoM generator). These earn links on their own.
5. **Brand entity**: Organization schema with `sameAs` (LinkedIn, X, Crunchbase, Product Hunt, YouTube), a Crunchbase profile, and a Wikidata entry. "lynkk" ranks at 2.2, not 1. Fixing the entity should give you sitelinks and position 1.

### C. Technical fixes

1. **Mobile speed**: cut the redirect chain (630 ms), cache HTML at the edge to bring TTFB from ~600 ms to under 200 ms, defer or remove ~180 KB of unused JS, preload the hero image/font. Target LCP under 2.5 s.
2. **Indexing check**: many new posts (granola-vs-fathom, granola-vs-otter, jamie-ai-review, teams-transcript, meeting-notes-template, how-to-record-google-meet, how-to-record-teams-meeting) don't show up in GSC yet. Run URL Inspection and request indexing.
3. **Remove `/articles/` URLs** from the sitemap and internal links (they 301 to `/blog/`).
4. **Internal linking**: every blog post should link to 1 money page (a /compare/ or /features/ page) with keyword-rich anchor text. Add a "Compare" block to the footer of every post. Currently the compare pages get few impressions (otter 258, fathom 21, read-ai 17), mostly because nothing links to them.
5. **Schema**: Keep FAQPage. Add `SoftwareApplication` with `offers` (price $4) and `aggregateRating` (once you have real G2/Capterra reviews) on the homepage, pricing and compare pages. Star ratings plus a price in the SERP lift CTR the most. Also check why blog posts have `CollegeOrUniversity` markup (probably author `alumniOf`). It's harmless, but tidy it up.
6. **Translated results**: 114 impressions came from Google auto-translating your pages (Mexico has 7.8% CTR, 47 clicks). Consider proper Spanish versions of your 3-5 best pages, plus hreflang.

### D. Content refresh (before writing anything new)

Pages already in the 8-20 range that can reach the top 5 with a refresh plus 3-5 internal links:
- google-meet-transcript (8.4), hindi-transcription (8.6), meeting-preparation (7.8), live-caption-apps (7.7), granola-ai-pricing (9.2), fireflies-pricing (11.3), ai-voice-recorders (11.3), gong-pricing (11.5), fathom-ai-pricing (12.3), zoom-bot-join-meeting (10.9), follow-up-email-after-meeting (12.7), voice-memo-transcription (12.3).

For each one: update the date in the title, add a comparison table above the fold, add a "Try Lynkk free" CTA box after the first answer, add 3 FAQs taken from the matching AI Mode questions in GSC, and add internal links from 3 related posts.

---

## 5. New blogs to write (built for clicks and sign-ups)

The selection rule: **commercial or comparison intent** (someone choosing a tool), **low SEO difficulty (SD under 35)**, **high CPC** (shows buyer intent), and a **real Lynkk advantage** (in-person, no bot, $4/mo, Hindi/Hinglish, 17 languages, data residency). Template and definition posts (standup, BANT, SPIN, RevOps) get impressions but almost never get clicks, because AI Overviews answer them. Write fewer of those.

Volumes are Ubersuggest, US, monthly.

### Tier 1: write first (bottom of funnel, clear Lynkk advantage)

| # | Blog title | Main keyword | Vol | SD | CPC | Why it converts |
|---|---|---|---|---|---|---|
| 1 | Best AI Note Taker for In-Person Meetings (No Bot, No Device) | ai note taker for in person meetings | 720 | 41 | $20.99 | Your core differentiator. Plus "in person meeting ai note taker" (90), "free ai note taker for in person meetings" (50) |
| 2 | 7 Granola Alternatives in 2026 (Cheaper, Work on Windows and In Person) | granola alternatives | 320 | 32 | $16.09 | You already get 684 impressions for "granola pricing". Link pricing to this page |
| 3 | Gong Alternatives: 7 Cheaper Conversation Intelligence Tools | gong alternatives | 210 | 31 | **$80.17** | Highest CPC found. gong-pricing already ranks 11.5 and can feed it |
| 4 | Fireflies vs Otter (2026): Which Is Better, and What's Cheaper? | fireflies vs otter | 110 (+40) | 21 | **$42.15** | Low SD, very high buyer intent. Lynkk as the "third option" |
| 5 | 6 Fireflies Alternatives That Don't Send a Bot | fireflies alternatives | 110 | **14** | **$40.21** | Very low difficulty |
| 6 | Fathom AI Note Taker Review 2026: Free Plan Tested | fathom ai note taker | 5,400 | **21** | $4.47 | Huge volume, low SD. Link to fathom-ai-pricing and /compare/fathom |
| 7 | Bot-Free AI Note Taker: Record Meetings Without a Bot Joining | ai note taker that doesn't join meetings / bot free ai note taker | 90 + 110 + 30 | 30 | $21.61 | Exact Lynkk feature. Keep the feature page /features/chrome-extension as the money page and link to it |
| 8 | Read AI Alternatives (No Meeting Scores, No Bot) | read ai alternatives | 70 | 20 | $12.91 | Matches /compare/read-ai angle |

### Tier 2: competitor X vs Y pages (your best converting template)

Your best non-brand CTRs come from comparison pages: /compare/circleback **15.5%**, /compare/meetgeek **14%**. Queries like "circleback vs bliro" (100% CTR) and "meetgeek vs recordmeeting" (67%) show that people searching two competitors click through. Build a series:

- Fathom vs Fireflies
- Otter vs Fathom
- Granola vs Fireflies
- tl;dv vs Fathom
- Read AI vs Fireflies
- Fireflies vs Gong
- Plaud vs Granola (in-person angle)
- Jamie vs Granola (bot-free angle)

Format: a side-by-side table, a verdict in the first 100 words, a "when to choose neither (Lynkk)" section, and a FAQ. Each post is 1,200 to 1,800 words.

### Tier 3: high-volume commercial, needs links to rank (write after authority work starts)

| Blog | Keyword | Vol | SD | CPC |
|---|---|---|---|---|
| Otter AI Note Taker Review 2026 | otter ai note taker | 3,600 | 62 | $8.07 |
| Fireflies AI Note Taker Review 2026 | fireflies ai note taker | 3,600 | 50 | $13.75 |
| Granola AI Note Taker Review 2026 | granola ai note taker | 2,400 | 29 | $6.71 |
| Does Microsoft Teams Have an AI Note Taker? (Copilot vs Free Options) | does microsoft teams have an ai note taker | 170 | 29 | $17.23 (fold into the existing Teams post as an H2 if you want to avoid a new URL) |
| Does Google Meet Have an AI Note Taker? (Gemini vs Free Options) | does google meet have an ai note taker | 140 | 42 | $22.86 |

### Tier 4: only if you can back the claim

- **HIPAA Compliant AI Note Taker** (260, SD 31, CPC $31) and **AI Note Taker for Therapists** (90, CPC $50.63). Only write these if Lynkk actually has a BAA or HIPAA coverage. This is unconfirmed in brand memory.

### Do NOT create new posts for these (fix the existing page instead)

- "free ai note taker" (2,400, SD 25): you already have /blog/best-free-ai-note-takers, but it gets only 5 impressions. Fix indexing and internal links.
- "microsoft teams ai note taker" (590, SD 26): /blog/ai-note-taker-microsoft-teams exists, at position 18-30.
- "zoom ai note taker" / "ai note taker for zoom" (390 + 480): /blog/zoom-note-taker exists.

### Every new post needs

1. Keyword-first title with a click hook (year, number, "tested", "cheaper", "no bot").
2. A verdict or comparison table in the first screen.
3. A CTA box ("Lynkk: $4/mo, no bot, works in person. Start free") after the first answer and at the end.
4. At least 3 internal links in and 2 out (to /compare/ and /pricing).
5. FAQ schema using real questions from GSC AI Mode queries.
6. At least one backlink earned within 30 days (directory, guest post or roundup).

---

## 6. 90-day plan

| Week | Action |
|---|---|
| 1 | Rewrite titles/metas on the 15 pages in section 4A. Fix indexing of new posts. Remove /articles/ from the sitemap |
| 1-2 | Merge transcribe-audio-to-text + ai-transcription-software, and otter-ai-alternatives into /compare/otter |
| 2 | Mobile speed fixes (redirects, TTFB, unused JS). Add SoftwareApplication schema |
| 2-6 | Submit to 20 AI directories and review sites. Start 2 guest posts a month |
| 3-6 | Publish Tier 1 blogs (8 posts, 2 a week) |
| 6-10 | Publish Tier 2 X vs Y series (8 posts) |
| 4, 8, 12 | Re-export GSC, compare CTR by page with AI-Mode queries filtered out |

**Expected result:** title fixes alone on pages already at 4-12 usually take CTR from 0.3% to 1.5-3%. On the ~40,000 impressions those 15 pages get, that's about 300-900 extra clicks a quarter, before any ranking gains.

---

## 7. Data gaps to close

- Export **query + page** pairs (GSC API or Looker Studio) to confirm cannibalisation exactly.
- Ubersuggest has no competitor data for lynkk.ai yet (the domain is too new). Re-run in 60 days.
- Confirm pricing, HIPAA/SOC 2 status, and supported CRMs before publishing Tier 4 and the review posts (see "To confirm" in `memory/lynkk-brand.md`).
