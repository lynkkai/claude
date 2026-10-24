# Lynkk off-site blog package: Medium, Hashnode, Substack (30 articles)

Prepared 24 October 2026. Ten original articles per platform, each written to that
platform's audience and rules, each linking back to two to four pages that are **live on
lynkk.ai today**.

| Folder | Articles | Audience and format |
|---|---|---|
| `medium/` | 10 | Professionals reading about productivity, work and AI. Essay-style, practical, 4 to 6 minute reads |
| `hashnode/` | 10 | Developers. Technical tutorials with working code: meeting bots, transcript APIs, diarization, ASR testing, RAG |
| `substack/` | 10 | Founders, sales leaders, managers. Newsletter issues for a publication called *After the Call (by Lynkk)* |

Every file has YAML frontmatter with the title, subtitle, tags, the target queries, the
**evidence** behind the topic (GSC and Ubersuggest figures), the lynkk.ai pages it links to,
and canonical instructions. Strip the frontmatter when pasting into each editor.

---

## 1. What the research found

### Inputs used

- **Old drafts** (`lynkk-blogs.zip`, 15 articles) and **new drafts** (`lynkk-blogs_1.zip`, 41 articles, revision 4 with `GSC-FINDINGS.md`).
- **Search Console export** (22 July to 21 October 2026): 12,822 impressions, 98 clicks, 66 pages, 1,000 queries.
- **Ubersuggest** keyword suggestions for the developer, meeting-notes, sales and Hinglish clusters (US and India).
- **The live site**: sitemap, all 38 live blog posts, and the pricing, FAQ, security, integrations and features pages, fetched 24 October 2026.

### Which drafts are live

Of the 41 drafts, only **2 are live**: `/blog/bant-sales-qualification` and `/blog/gong-pricing`
(both published 23 October). The other 39 are not on the site yet, so **no syndicated article
links to them**. When they go live, add them as a second link in the matching posts (see section 6).

The live blog has 38 posts. **Every one of them gets at least one link** from this package.
The highest-opportunity pages get two to four (see section 5).

### What GSC says about content that works

1. **The site ranks for long, conversational questions** (positions 2 to 9, almost zero clicks).
   Several articles here are built directly on those questions, quoted where it reads naturally:
   - "zoom ai companion gives us summaries but nothing in our crm..." (66 impr, pos 2.3), **S01**
   - "how do founders keep track of everything said in investor and team meetings?" (40 impr, pos 4.1), **M06**
   - "our daily standups run 15 minutes and by afternoon nobody remembers..." (19 impr, pos 7.6), **M05**
   - "which notetakers offer searchable meeting history with source-linked answers?" (36 impr, pos 2.7), **H08**
2. **Meeting-bot queries are developer intent** (399 impressions: "meeting bot", "join zoom call bot",
   "how to make a meeting bot"). The earlier analysis dropped them because a marketing blog can't
   serve them. **Hashnode can**, so H01, H02, H09 and H10 target that cluster.
3. **India converts and the US doesn't**: India gives 48 of 98 clicks at 6.1% CTR, the US 6 clicks
   from 6,249 impressions. S04 and H04 (Hinglish) are aimed at the audience that clicks.
4. **High-impression pages are stuck off page one**: `/blog/google-meet-transcript` (3,450 impr, pos 9.6),
   `/blog/voice-to-text-apps` (1,080, pos 36), `/blog/voice-memo-transcription` (947, pos 10.3),
   `/blog/ai-note-taker-microsoft-teams` (875, pos 23.6). These get the most syndicated links and
   go in the first two weeks of the schedule.

### Live site facts used

All product claims come from the **live site** (pricing page "last checked 19 October 2026").
`memory/lynkk-brand.md` was rewritten from the live site on 24 October 2026, and all 30 articles
were re-checked against it, including its "Do not claim" list. The old memory file had these
claims, which the articles avoid:

| Old brand memory said | Live site says (24 Oct 2026) |
|---|---|
| "CRM fields updated" after meetings | "No CRM sync yet. Copy any brief into Salesforce or HubSpot." HubSpot listed as not connected |
| "Pick a region" for data residency | FAQ: "No, there is no region setting today." Data may be processed in India and the US |
| Calendly and Cal.com integrations | Integrations today are Google Calendar, Jira and Slack |
| Joins meetings and "speaks when needed" | The bot "does not speak". Live help during calls is **Cue**, in beta, Mac, by invite |
| Paid tiers: to confirm | Free: unlimited notes (2 hours each), first 5 hours of AI summaries in total. Pro: $15/month or $117/year. Workspaces up to 10 members |

The older drafts also say Pro costs **$19**; the live price is **$15**. Use `memory/lynkk-brand.md`
as the source of truth for any edits to these articles.

---

## 2. Platform guidelines, and how each article follows them

### Medium

| Rule or norm | What the articles do |
|---|---|
| Stories with AI assistance must **disclose it near the top**; undisclosed or fully AI-generated stories go to the writer's network only, not general distribution ([Medium AI policy](https://help.medium.com/hc/en-us/articles/22576852947223-Artificial-Intelligence-AI-content-policy); summaries of the 2023 rules in [Plagiarism Today](https://www.plagiarismtoday.com/?p=42690)) | Each story opens with a one-line disclosure. **A person must genuinely edit each story before publishing**, or the disclosure isn't true and distribution suffers |
| Medium's policy bans AI content made **solely to rank in search with affiliate links** | No affiliate links. Each article teaches something on its own |
| **Member-only (paywalled) stories may not exist mainly to drive traffic to a product**, and can't carry CTAs such as sign-ups ([Member Content Guidelines](https://policy.medium.com/member-content-guidelines-e81e2e345294)) | Publish all 10 as **free (non-member) stories**. Product mentions are short and sit at the end |
| Boost and general distribution favor original, experience- or research-backed, well-made stories ([Distribution help](https://help.medium.com/hc/en-us/articles/360006362473)) | Each story offers original frameworks (the six questions, five rules, four questions) rather than a rewrite of a lynkk.ai page |
| Up to 5 tags; title plus subtitle | Set in frontmatter |
| Canonical links are for republished stories ([Set a canonical link](https://help.medium.com/hc/en-us/articles/360033930293-Set-a-canonical-link)) | **Do not set one**. These are original stories, not copies |

Outbound links on Medium are generally `nofollow`, so value comes from referral traffic,
discovery and AI-answer citations, not link equity. Check with Inspect on a published story.
Submitting to established Medium publications in productivity, startups or work widens reach
a lot. Each publication has its own submission rules.

### Hashnode

| Rule or norm | What the articles do |
|---|---|
| "AI-generated content is permitted, but you must **review and take responsibility** for everything you publish" ([Code of Conduct](https://hashnode.com/code-of-conduct)) | Footer discloses AI assistance. **An engineer should run or review each code sample before publishing** |
| No "using the platform **primarily for self-promotion** without contributing to the community" | Each post is a real tutorial with code that works without Lynkk. Lynkk appears once near the end as an example |
| No **bulk automated content**, engagement farming, misleading links or SEO abuse | Publish on the staggered schedule in section 4, never all at once |
| Relevant links to docs, repos and articles are "welcome and encouraged" | 3 lynkk.ai links per post, each relevant to the section it sits in |
| Republished posts can set an original URL ([Hashnode support](https://support.hashnode.com/en/articles/6420682-writing-a-blog-post)) | Not needed. These are original |

Publish under a Lynkk team blog on Hashnode (for example `lynkk.hashnode.dev`) rather than
personal accounts, so the posts build one profile. Use up to 5 tags from the frontmatter.

### Substack

| Rule or norm | What the articles do |
|---|---|
| Substack is "vehemently anti-spam" and bars repetitive self-promotion in comments, threads and Notes ([Content guidelines](https://substack.com/content), [Community guidelines](https://on.substack.com/p/community-guidelines)) | Issues are written as a real newsletter, and product mentions are labelled disclosures |
| Imported lists must be **people who opted in to your publication**; no bought or scraped emails | Start the list from opted-in Lynkk users only, or from zero |
| **No canonical URL setting** for posts (third-party reports; no official canonical feature found) | Every issue is original. **Never paste a lynkk.ai article into Substack**, or you create an uncanonicalised duplicate |

Newsletter format: a short welcome line, one idea per issue, sections, a "This week's
takeaway", and a reply prompt. Share each issue as a Substack Note on the same day, and look
for cross-recommendations with other productivity and sales newsletters once you have a few
issues out.

---

## 3. Article index

| # | File | Title | Links to lynkk.ai |
|---|---|---|---|
| M01 | `medium/01-google-meet-transcript-nobody-can-find.md` | The Google Meet Transcript Nobody Can Find | /blog/google-meet-transcript, /blog/google-meet-ai-note-taker, /blog/meeting-summary-template |
| M02 | `medium/02-meeting-notes-are-not-minutes.md` | Your Meeting Notes Are Not Your Minutes (and Neither Is Your Memory) | /blog/meeting-notes-vs-minutes, /blog/meeting-minutes-sample, /blog/meeting-knowledge-management |
| M03 | `medium/03-action-items-die-in-the-chat.md` | Action Items Die in the Chat. Here Are 5 Rules That Keep Them Alive. | /blog/action-items-examples-template, /blog/follow-up-email-after-meeting, /blog/meeting-minutes-to-jira |
| M04 | `medium/04-typing-is-the-bottleneck.md` | Typing Is the Bottleneck. What Voice-to-Text Actually Fixes, and What It Doesn't. | /blog/voice-to-text-apps, /blog/dictation-on-mac, /blog/dictate-in-microsoft-word |
| M05 | `medium/05-standup-nobody-remembers-by-lunch.md` | The 15-Minute Standup Nobody Remembers by Lunch | /blog/daily-standup-meeting, /blog/action-items-examples-template, /use-cases/team-standups |
| M06 | `medium/06-founders-are-the-companys-hard-drive.md` | Founders Are the Company's Hard Drive. That's a Problem. | /blog/founders-meeting-notes, /blog/meeting-knowledge-management, /blog/meeting-preparation |
| M07 | `medium/07-should-an-ai-bot-be-in-your-meeting.md` | Should an AI Bot Be in Your Meeting? An Honest Look at Bots vs Bot-Free Note Takers | /blog/zoom-bot-join-meeting, /blog/zoom-note-taker, /blog/ai-note-taker-microsoft-teams |
| M08 | `medium/08-five-minutes-before-a-meeting.md` | The Five Minutes Before a Meeting Decide Everything | /blog/meeting-preparation, /blog/ai-powered-meeting-assistants, /blog/one-on-one-meeting |
| M09 | `medium/09-voice-memos-underrated-note-taking-tool.md` | Voice Memos Are the Most Underrated Note-Taking Tool on Your Phone | /blog/voice-memo-transcription, /blog/transcribe-audio-to-text, /blog/ai-voice-recorders |
| M10 | `medium/10-choose-an-ai-note-taker-without-40-comparisons.md` | How to Choose an AI Note Taker Without Reading 40 Comparison Posts | /blog/best-ai-note-takers, /blog/best-free-ai-note-takers, /blog/zoom-ai-companion-alternatives, /blog/otter-ai-alternatives |
| H01 | `hashnode/01-how-meeting-bots-join-zoom-meet-teams.md` | How Meeting Bots Actually Join a Zoom, Google Meet or Teams Call | /features/meeting-bot, /blog/zoom-bot-join-meeting, /blog/zoom-ai-companion-alternatives |
| H02 | `hashnode/02-google-meet-transcripts-with-meet-rest-api.md` | Pulling Google Meet Transcripts With the Meet REST API (Python) | /blog/google-meet-transcript, /blog/google-meet-ai-note-taker, /integrations/google-meet |
| H03 | `hashnode/03-speaker-diarization-whisper-pyannote-python.md` | Speaker Diarization Explained: Who Said What, With Whisper and pyannote in Python | /blog/ai-transcription-software, /blog/transcribe-audio-to-text, /use-cases/user-interviews |
| H04 | `hashnode/04-testing-hinglish-speech-recognition-wer.md` | Code-Switching Breaks Speech Recognition: How to Test Hinglish ASR With WER and CER | /features/hinglish-transcription, /blog/hindi-transcription, /features/multilingual-transcription |
| H05 | `hashnode/05-meeting-action-items-to-jira-python.md` | From Meeting Action Items to Jira Issues: A Small Python Service | /blog/meeting-minutes-to-jira, /blog/action-items-examples-template, /integrations/jira |
| H06 | `hashnode/06-record-tab-audio-chrome-mv3-extension.md` | Recording Tab Audio and the Microphone in a Chrome MV3 Extension | /features/chrome-extension, /blog/how-to-transcribe-zoom-meetings, /blog/zoom-meeting-recorders |
| H07 | `hashnode/07-capture-system-audio-macos-core-audio-taps.md` | Capturing System Audio on macOS Without a Virtual Driver: Core Audio Taps (macOS 14.2+) | /download, /features/dictation, /blog/dictation-on-mac |
| H08 | `hashnode/08-ask-your-meetings-rag-with-timestamp-citations.md` | Ask Your Meetings: Building Q&A Over Transcripts With Timestamped Citations | /features/ask-your-meetings, /blog/meeting-knowledge-management, /blog/sales-conversation-intelligence |
| H09 | `hashnode/09-microsoft-teams-transcripts-graph-api.md` | Getting Microsoft Teams Meeting Transcripts With the Graph API | /blog/ai-note-taker-microsoft-teams, /integrations/microsoft-teams, /blog/meeting-summary-template |
| H10 | `hashnode/10-zoom-cloud-recording-transcripts-api.md` | Downloading Zoom Cloud Recording Transcripts With the Zoom API (and Parsing the VTT) | /blog/how-to-transcribe-zoom-meetings, /blog/zoom-note-taker, /integrations/zoom |
| S01 | `substack/01-zoom-ai-companion-summaries-empty-crm.md` | Zoom AI Companion Gave Us Summaries. Our CRM Stayed Empty. | /blog/zoom-ai-companion-alternatives, /blog/sales-conversation-intelligence, /blog/follow-up-email-after-meeting |
| S02 | `substack/02-bant-is-not-dead-its-badly-written-down.md` | BANT Isn't Dead. It's Just Badly Written Down. | /blog/bant-sales-qualification, /use-cases/sales-calls, /blog/meeting-preparation |
| S03 | `substack/03-what-gong-costs-and-what-small-teams-need.md` | What Gong Costs, and What a 10-Person Sales Team Actually Needs | /blog/gong-pricing, /blog/sales-conversation-intelligence, /compare/gong |
| S04 | `substack/04-hinglish-is-how-india-meets.md` | Hinglish Is How India Actually Meets. Most Meeting Tools Still Pretend It Isn't. | /blog/hindi-transcription, /blog/google-meet-ai-note-taker, /features/hinglish-transcription |
| S05 | `substack/05-the-follow-up-email-is-the-meeting.md` | The Follow-Up Email Is the Meeting | /blog/follow-up-email-after-meeting, /blog/meeting-summary-template, /features/meeting-notes |
| S06 | `substack/06-board-meetings-agenda-easy-minutes-hard.md` | Board Meetings: The Agenda Is Easy. The Minutes Are Hard. | /blog/board-meeting-agenda, /blog/meeting-minutes-sample, /blog/meeting-notes-vs-minutes |
| S07 | `substack/07-one-on-one-where-managers-lose-the-thread.md` | The One-on-One Is Where Managers Lose the Thread | /blog/one-on-one-meeting, /use-cases/one-on-one-meetings, /blog/meeting-preparation |
| S08 | `substack/08-recruiters-debrief-starts-before-interview-ends.md` | Recruiters: The Interview Debrief Starts Before the Interview Ends | /blog/recruiting-interview-transcription, /blog/transcribe-audio-to-text, /blog/meeting-summary-template |
| S09 | `substack/09-lawyers-doctors-limits-of-ai-transcription.md` | Lawyers, Doctors and the Limits of AI Transcription | /blog/legal-transcription-service, /blog/medical-transcription-software, /use-cases/lawyers |
| S10 | `substack/10-read-ai-otter-or-neither-a-buyers-letter.md` | Read AI, Otter, Copilot or None of the Above? A Letter to Someone Choosing a Note Taker | /blog/read-ai-vs-otter-ai, /blog/otter-ai-alternatives, /blog/ai-note-taker-microsoft-teams, /blog/best-free-ai-note-takers |

---

## 4. Publishing schedule (5 weeks, 6 posts a week)

Two posts per platform per week, never more than one per platform per day. The order puts the
pages with the most GSC impressions and the newest, unlinked posts first.

| Week | Medium | Hashnode | Substack |
|---|---|---|---|
| 1 | M01 Google Meet transcript, M04 Voice-to-text | H01 Meeting bots, H02 Meet REST API | S04 Hinglish (India), S01 Zoom AI Companion and CRM |
| 2 | M09 Voice memos, M07 Bots vs bot-free | H09 Teams Graph API, H10 Zoom API | S02 BANT, S03 Gong |
| 3 | M10 Choosing a note taker, M03 Action items | H04 Hinglish WER, H08 Ask your meetings | S05 Follow-up email, S10 Buyer's letter |
| 4 | M05 Standups, M06 Founders | H05 Jira service, H03 Diarization | S06 Board minutes, S07 One-on-ones |
| 5 | M02 Notes vs minutes, M08 Prep | H06 Chrome extension, H07 macOS taps | S08 Recruiters, S09 Law and medicine |

---

## 5. Link coverage on lynkk.ai

| lynkk.ai page | Syndicated posts linking to it |
|---|---|
| /blog/meeting-preparation | 4 (M06, M08, S02, S07) |
| /blog/meeting-summary-template | 4 (H09, M01, S05, S08) |
| /blog/action-items-examples-template | 3 (H05, M03, M05) |
| /blog/ai-note-taker-microsoft-teams | 3 (H09, M07, S10) |
| /blog/follow-up-email-after-meeting | 3 (M03, S01, S05) |
| /blog/google-meet-ai-note-taker | 3 (H02, M01, S04) |
| /blog/meeting-knowledge-management | 3 (H08, M02, M06) |
| /blog/sales-conversation-intelligence | 3 (H08, S01, S03) |
| /blog/transcribe-audio-to-text | 3 (H03, M09, S08) |
| /blog/zoom-ai-companion-alternatives | 3 (H01, M10, S01) |
| /blog/best-free-ai-note-takers | 2 (M10, S10) |
| /blog/dictation-on-mac | 2 (H07, M04) |
| /blog/google-meet-transcript | 2 (H02, M01) |
| /blog/hindi-transcription | 2 (H04, S04) |
| /blog/how-to-transcribe-zoom-meetings | 2 (H06, H10) |
| /blog/meeting-minutes-sample | 2 (M02, S06) |
| /blog/meeting-minutes-to-jira | 2 (H05, M03) |
| /blog/meeting-notes-vs-minutes | 2 (M02, S06) |
| /blog/one-on-one-meeting | 2 (M08, S07) |
| /blog/otter-ai-alternatives | 2 (M10, S10) |
| /blog/zoom-bot-join-meeting | 2 (H01, M07) |
| /blog/zoom-note-taker | 2 (H10, M07) |
| /features/hinglish-transcription | 2 (H04, S04) |
| /blog/ai-powered-meeting-assistants | 1 (M08) |
| /blog/ai-transcription-software | 1 (H03) |
| /blog/ai-voice-recorders | 1 (M09) |
| /blog/bant-sales-qualification | 1 (S02) |
| /blog/best-ai-note-takers | 1 (M10) |
| /blog/board-meeting-agenda | 1 (S06) |
| /blog/daily-standup-meeting | 1 (M05) |
| /blog/dictate-in-microsoft-word | 1 (M04) |
| /blog/founders-meeting-notes | 1 (M06) |
| /blog/gong-pricing | 1 (S03) |
| /blog/legal-transcription-service | 1 (S09) |
| /blog/medical-transcription-software | 1 (S09) |
| /blog/read-ai-vs-otter-ai | 1 (S10) |
| /blog/recruiting-interview-transcription | 1 (S08) |
| /blog/voice-memo-transcription | 1 (M09) |
| /blog/voice-to-text-apps | 1 (M04) |
| /blog/zoom-meeting-recorders | 1 (H06) |
| /compare/gong | 1 (S03) |
| /download | 1 (H07) |
| /features/ask-your-meetings | 1 (H08) |
| /features/chrome-extension | 1 (H06) |
| /features/dictation | 1 (H07) |
| /features/meeting-bot | 1 (H01) |
| /features/meeting-notes | 1 (S05) |
| /features/multilingual-transcription | 1 (H04) |
| /integrations/google-meet | 1 (H02) |
| /integrations/jira | 1 (H05) |
| /integrations/microsoft-teams | 1 (H09) |
| /integrations/zoom | 1 (H10) |
| /use-cases/lawyers | 1 (S09) |
| /use-cases/one-on-one-meetings | 1 (S07) |
| /use-cases/sales-calls | 1 (S02) |
| /use-cases/team-standups | 1 (M05) |
| /use-cases/user-interviews | 1 (H03) |

Every link was checked against the live sitemap on 24 October 2026. Anchor text is descriptive
and varied, never exact-match keyword stuffing.

---

## 6. Links to add when the drafts go live

These drafts from `lynkk-blogs_1.zip` are not live yet. Once each one is published, add it as
an extra in-context link in the article shown.

| Draft (not live yet) | Add a link from |
|---|---|
| `meeting-notes-to-crm` | S01 (section "Three gaps, not one") |
| `ai-note-taker-without-a-bot` | M07 (section "How bot-free note takers work") |
| `copilot-teams-vs-ai-note-taker` | S10 (section "Start with what you already pay for"), H09 |
| `multilingual-meeting-transcription` | H04, S04 |
| `who-sees-your-meeting-transcripts` | M10 (question 6), S09 (checklist) |
| `enterprise-ai-note-taker-controls` | H08 (section "Permissions are part of retrieval") |
| `free-ai-note-taker-limits` | M10 (question 5) |
| `meeting-decision-log` | M02, H05 |
| `retrospective-notes` | M05 |
| `user-interview-transcription` | H03 (diarization in interviews) |
| `record-in-person-meetings` | M09, M07 |
| `call-recording-laws-by-state` (after legal review) | M07 (consent section), S08 |
| `gdpr-compliant-ai-meeting-tools` | S09 |
| `otter-ai-pricing`, `fireflies-pricing`, `fathom-ai-pricing`, `granola-ai-pricing` | S10, M10 |
| `meddic-sales`, `spin-selling`, `sales-methodology` | S02 |
| `sales-enablement-tools`, `revenue-operations` | S03 |
| `chatgpt-meeting-notes` | M01 |

---

## 7. Before you publish each article

1. **A person edits it.** Medium and Hashnode both require it, and the disclosure line says it happened. Add a real example or opinion from the team where you can; that's what Medium's Boost curators look for.
2. **Run or review the code** in every Hashnode post (H01 to H10). API shapes were written against public documentation as of October 2026. **H07 (macOS Core Audio taps)** is a sketch and needs a Swift engineer's check. Don't add any claim about which capture API Lynkk's Mac app uses unless engineering confirms it.
3. **Strip the frontmatter.** Copy the title and subtitle into the editor fields and the tags into the tag field.
4. **Add a cover image** (suggestion in each frontmatter; a 16:9 image such as 1600x900 is a safe size) and alt text.
5. **Don't set a canonical URL.** These are original articles. Substack can't set one anyway.
6. **Check prices and competitor facts** on publish day. Pro is $15/month or $117/year as of 19 October 2026.
7. **Optional tracking:** add `?utm_source=medium|hashnode|substack&utm_medium=referral&utm_campaign=syndication` to lynkk.ai links if you want campaign-level reporting beyond the referrer.
8. **After publishing**, log the URL and date. After 4 to 6 weeks, compare GSC impressions and position for the linked pages against this baseline (the export in `lynkk.ai-Performance-on-Search-2026-10-24`).

## 8. Checks already run

- No em dashes or en dashes in any file (CLAUDE.md writing rule).
- Brand spelled "Lynkk" throughout; no "Lynk", "Linnk" or "Link AI".
- Every lynkk.ai link in every article resolves to a URL in the live sitemap.
- Every link listed in the frontmatter appears in the article body.
- No invented customer stories, statistics or testimonials. Hypothetical scenarios are framed as hypothetical ("Picture a 12-person team...").
- Product claims match the live pricing, FAQ, security and integrations pages; limitations (no CRM sync, no region setting, no Windows or phone app) are stated plainly where relevant.
