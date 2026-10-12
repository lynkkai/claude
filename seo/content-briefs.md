# Lynkk Blog: Keyword Map, E-E-A-T Rules and Content Structure (30 Posts)

> **Product facts:** the briefs below predate `lynkk-post-kit/docs/TRUTHS.md`. Where a brief mentions CRMs, regions, phone apps or voice answers, follow TRUTHS.md instead.

> Companion to `seo/usa-blog-plan-2026.md`. Market: United States. Keyword data: Ubersuggest (US), checked 2026-09-30.
> Volume / SD shown as (monthly US searches / SEO difficulty 0-100). Questions come from Google autocomplete via Ubersuggest.
> Nothing here is published yet. Items marked **(confirm)** need a fact check from the Lynkk team; until confirmed, they are left out of articles (no placeholders in article text).

---

## Part 1. How to read each brief

Every post gets five keyword layers. Use them in this order of importance:

| Layer | Where it goes |
|---|---|
| **Primary keyword** | H1 (title), URL slug, first 100 words, meta title, meta description, one H2, image alt text on the hero image |
| **Secondary keywords** | H2s and H3s, naturally in body copy (once or twice each) |
| **Semantic / related terms** | Throughout the body so the page covers the topic fully. Do not force them in |
| **Questions** | FAQ section (3-6 questions), or as H2s when the question is big enough |
| **Reddit queries** | A "What users say" section or FAQ answers that address real complaints (price, privacy, bots, accuracy) |

Rules:
- One primary keyword per post. No two posts share a primary keyword (avoids cannibalization).
- Write for the reader first. Keyword density is not a target; coverage of the question is.
- Never use em dashes or en dashes in copy (house rule from CLAUDE.md).

---

## Part 2. E-E-A-T rules for every post

Google's guidance asks whether content shows **Experience, Expertise, Authoritativeness and Trust**. Trust matters most. For a vendor writing about its own category, that means being open about bias and backing claims with evidence.

### Experience (show you actually used it)
- Test every tool you write about. Record real meetings (internal or with consent) and use what you learned.
- Add original screenshots (not vendor press images), short screen recordings, and real output samples (redacted).
- Include a **"How we tested"** box on every listicle and comparison: what meetings, how many, which platforms, which date, which plan (free/paid).
- Use first-person observations: "In our test of 12 Zoom calls, the transcript missed speaker changes twice."

### Expertise (show who wrote it)
- Named author with a short bio and photo. No "Admin" or "Lynkk Team" bylines.
- Author bio states relevant experience (for example: "runs 20+ customer calls a week", "product manager for 8 years").
- For legal (#28) and healthcare (#29) posts: add a **named reviewer** with the right background (attorney, clinician or compliance specialist) and a "Reviewed by" line.

### Authoritativeness (show others back it up)
- Cite primary sources. **Never hyperlink competitor sites** (vendor pricing pages, help docs, product pages): name the source in plain text with the date checked. Link only neutral authorities (laws, regulators, standards bodies, independent studies).
- Add original data where possible (your own accuracy test, time saved, survey of your users).
- Internal links: every post links to at least 3 related posts and one Lynkk feature page.
- Earn links: pitch the original data (for example the accuracy test in #5) to newsletters and communities.

### Trust (the most important)
- **Disclosure box** at the top of every listicle and Lynkk vs post: "Lynkk makes an AI meeting assistant. We include it in this list, and we explain how we tested every tool, including our own."
- Lynkk is always the #1 / best overall pick in our own articles (team rule, 2026-09-30). Describe competitors factually and fairly; never make false or disparaging claims about them.
- Date every price and feature claim ("Pricing checked October 2026") and show a **Last updated** date.
- No fake reviews, testimonials or ratings. No review star schema on your own product.
- Do not make claims Lynkk has not confirmed (HIPAA, SOC 2, languages, accuracy, platforms, CRMs).
- Privacy and consent: remind readers to get consent before recording meetings.

### Page elements checklist (all posts)
- [ ] H1 with primary keyword
- [ ] Author byline, bio, photo, and "Last updated" date
- [ ] Disclosure box (listicles and Lynkk vs posts)
- [ ] Key takeaways / TL;DR box near the top
- [ ] Table of contents for posts over 1,500 words
- [ ] Original screenshots with descriptive alt text
- [ ] "How we tested" (listicles, comparisons, #5 accuracy post)
- [ ] FAQ section using the question keywords
- [ ] Sources section with outbound links to primary sources
- [ ] Schema: `Article` + `FAQPage` (FAQ) + `ItemList` (listicles) + `BreadcrumbList`
- [ ] 3+ internal links and one clear CTA ("Try Lynkk free")

---

## Part 3. Content structure templates

### Template A: Best / Top listicle (posts #1-#10)
Target length: 2,500-3,500 words.

1. **H1**: title with primary keyword
2. Intro (100-150 words): the problem, who this list is for, primary keyword in first 100 words
3. Disclosure box
4. **Key takeaways**: quick picks ("Best overall", "Best free", "Best for in-person", etc.)
5. **Comparison table**: tool, best for, free plan, starting price, platforms, standout feature
6. **H2: How we tested** (tools, meetings, dates, criteria and weights)
7. **H2 per tool** (6-10 tools), each with:
   - H3: Best for
   - H3: What we liked (with screenshot)
   - H3: What could be better
   - H3: Pricing (dated)
8. **H2: How to choose** (buying criteria that match secondary keywords)
9. **H2: What Reddit users say** (summarized sentiment, no usernames)
10. **H2: FAQ** (3-6 questions)
11. Conclusion + CTA
12. Sources

### Template B: Lynkk vs X (posts #11-#15)
Target length: 1,800-2,500 words.

1. **H1**: Lynkk vs X title
2. Intro: who should read this, verdict in two sentences
3. Disclosure box
4. **Quick verdict table**: "Choose Lynkk if..." / "Choose X if..."
5. **Feature comparison table** (sourced and dated)
6. **H2: How we tested**
7. **H2 per dimension**: capture, notes quality, live assistance, integrations, privacy, pricing
8. **H2: Where X is stronger** (required, for fairness)
9. **H2: Other X alternatives worth a look** (2-3 short entries, captures "alternatives" searches)
10. **H2: What users say about X** (Reddit sentiment)
11. **H2: FAQ**
12. Conclusion + CTA, Sources

### Template C: How-to (posts #16-#20)
Target length: 1,200-1,800 words.

1. **H1**: how-to title
2. Short answer in the first 2-3 sentences (target the featured snippet)
3. **H2: Step-by-step** with numbered steps and a screenshot per step
4. **H2: Common problems and fixes**
5. **H2: A faster way** (where Lynkk fits, one section only, not the whole post)
6. **H2: FAQ**
7. CTA, Sources (official help docs)

### Template D: Use case (posts #21-#30)
Target length: 1,500-2,200 words.

1. **H1**: use case title
2. Intro: the pain for this role, with a real example or quote (with permission)
3. **H2: What [role] needs from meetings** (the job to be done)
4. **H2: The manual way vs the AI way** (before/after workflow)
5. **H2: Step-by-step workflow with Lynkk** (screenshots, real output sample)
6. **H2: Template / checklist** (downloadable where it fits, useful as a lead magnet)
7. **H2: Results** (time saved or other metric, only if measured)
8. **H2: FAQ**
9. CTA, Sources

---

## Part 4. Keyword briefs for all 30 posts

### Best / top listicles (Template A)

#### 1. Best AI Note Takers in the USA (2026): Tested on Zoom, Teams, Google Meet and In-Person Meetings
- **Slug:** /blog/best-ai-note-takers
- **Intent:** commercial (comparing tools before buying)
- **Primary:** best ai note taker (1,900 / 43)
- **Secondary:** best ai note taker for meetings (260 / 41), what is the best ai note taker (170 / 42), best ai note taker app (140 / 29), ai note taker app (880 / 32)
- **Semantic terms:** AI meeting assistant, meeting transcription, speaker identification, action items, meeting summary, bot-free recording, in-person recording, CRM integration, free plan
- **Questions (FAQ):** Which AI note taker is best? Are AI note takers safe? Can AI take notes from an in-person meeting? Do AI note takers work with Zoom, Teams and Google Meet? Is there a free AI note taker?
- **Reddit queries:** best ai note taker reddit, what is the best ai note taker reddit, best ai meeting note taker app reddit
- **E-E-A-T focus:** test each tool on the same 3 meetings (Zoom, Teams, in person); publish the scoring rubric; disclose Lynkk is ours.
- **Internal links:** #2, #4, #9, #11

#### 2. Best Free AI Note Takers in the USA for 2026: What Each Free Plan Really Includes
- **Slug:** /blog/best-free-ai-note-takers
- **Intent:** commercial, price-sensitive
- **Primary:** free ai note taker (2,400 / 43)
- **Secondary:** ai meeting notes taker free (320 / 29), best free ai note taker (260 / 32), best ai note taker free (90 / 35)
- **Semantic terms:** free plan limits, minutes per month, transcript history, free trial vs free forever, upgrade cost, storage limits
- **Questions (FAQ):** Is there a completely free AI note taker? Is Otter.ai free? What do free AI note takers limit? Are free AI note takers safe for work meetings?
- **Reddit queries:** ai note taker reddit free, best free ai meeting note taker reddit, otter ai free reddit
- **E-E-A-T focus:** a table of free-plan limits with the date checked and links to each pricing page; sign up for each free plan yourself.
- **Internal links:** #1, #11, #14 **(confirm Lynkk free-plan limits)**

#### 3. Top Zoom Meeting Recorders for US Teams in 2026
- **Slug:** /blog/zoom-meeting-recorders
- **Intent:** commercial / transactional
- **Primary:** zoom meeting recorder (2,900 / 17)
- **Secondary:** zoom meeting recorder software (480 / 27), zoom ai transcription (390 / 25)
- **Semantic terms:** Zoom cloud recording, local recording, recording permissions, auto-record, transcript, meeting bot, recording storage
- **Questions (FAQ):** Where do Zoom recordings go? Is meeting recording free in Zoom? Can you record a Zoom meeting without the host's permission? Can Zoom transcribe meetings automatically?
- **Reddit queries:** zoom meeting recorder reddit
- **E-E-A-T focus:** show real Zoom settings screenshots; explain consent rules; link Zoom's official help docs.
- **Internal links:** #9, #10, #16, /features/meeting-bot

#### 4. Best AI Note Takers for Microsoft Teams in 2026 (for US Businesses)
- **Slug:** /blog/ai-note-taker-microsoft-teams
- **Intent:** commercial
- **Primary:** microsoft teams ai note taker (590 / 26)
- **Secondary:** ai note taker for teams (590 / 29), teams ai note taker (590 / 28), can copilot take meeting notes (390 / 30), does teams have an ai note taker (260 / 14), best ai note taker for microsoft teams (50 / 31)
- **Semantic terms:** Microsoft Copilot, Teams Premium, intelligent recap, Teams transcript, admin approval, tenant permissions
- **Questions (FAQ):** Does Microsoft Teams have an AI note taker? Can Copilot take meeting notes? Do I need Teams Premium for AI notes? How do I remove a note-taker bot from Teams?
- **Reddit queries:** best ai note taker for microsoft teams reddit, otter ai vs copilot reddit, ai note taker for teams reddit
- **E-E-A-T focus:** explain Copilot licensing with a link to Microsoft's page; test in a real Teams tenant. **(confirm Lynkk Teams support)**
- **Internal links:** #1, #23

#### 5. Top Voice Recognition Transcription Software in 2026: Accuracy Tested (US Guide)
- **Slug:** /blog/voice-recognition-transcription-software
- **Intent:** commercial + informational
- **Primary:** voice recognition transcription software (1,000 / 20)
- **Secondary:** how to transcribe audio to text (2,900 / 37), ai transcription free (1,000 / 31), free ai transcription audio to text (260 / 24)
- **Semantic terms:** word error rate (WER), speaker diarization, accents, background noise, real-time vs post-meeting transcription, multilingual transcription
- **Questions (FAQ):** How accurate is AI transcription? Which transcription software is best? Can AI transcribe voice recordings? Is voice recognition software AI?
- **Reddit queries:** (low demand)
- **E-E-A-T focus:** this is the "original data" post. Run the same audio set through every tool and publish word error rates and the method. Great for backlinks. **(confirm Lynkk accuracy and language figures before quoting)**
- **Internal links:** #7, #8, #22

#### 6. Top AI Voice Recorders in 2026: Plaud Note Pro, Pocket and App-Based Alternatives
- **Slug:** /blog/ai-voice-recorders
- **Intent:** commercial (hardware vs app)
- **Primary:** plaud note pro (12,100 / 26)
- **Secondary:** plaud note ai voice recorder (8,100 / 34), wearable ai voice recorder (1,600 / 34), best ai voice recorder (480 / 35), ai voice recorder app (170 / 30), ai voice recorder (6,600 / 49, stretch)
- **Semantic terms:** wearable recorder, NotePin, battery life, subscription cost, transcription minutes, phone app vs device, privacy of in-person recording
- **Questions (FAQ):** Which AI voice recorder is best? How does an AI voice recorder work? Can AI summarize a voice recording? Is there an AI voice recorder app instead of a device? Is Plaud worth it?
- **Reddit queries:** plaud ai note taker reddit, pocket ai note taker review reddit
- **E-E-A-T focus:** hands-on with the devices (photos, battery test, subscription math over 12 months).
- **Internal links:** #13, #9, #19

#### 7. Best Transcription Apps in the USA: Otter.ai and 7 Other Options Worth Trying
- **Slug:** /blog/transcription-apps
- **Intent:** commercial / navigational (Otter-aware buyers)
- **Primary:** otter ai transcription app (3,600 / 7)
- **Secondary:** otter ai transcript (2,900 / 19), otter ai audio transcription (2,400 / 6), otter.ai transcription software (1,300 / 13), otter ai transcript generator (720 / 5)
- **Semantic terms:** live transcription, transcript export, audio upload, speaker labels, transcription minutes, mobile app
- **Questions (FAQ):** Is Otter.ai free? How accurate is Otter.ai? What is better than Otter.ai? Can I upload audio files to Otter?
- **Reddit queries:** otter ai reddit review, otter ai alternatives reddit, is otter ai worth it reddit
- **E-E-A-T focus:** fair review of Otter first (it is the reason people search), then the alternatives. Use your own transcripts as samples.
- **Internal links:** #11, #5

#### 8. Best Dictation Software for Mac, Windows and Microsoft Word (2026)
- **Slug:** /blog/dictation-software
- **Intent:** commercial
- **Primary:** dictation software (1,900 / 32)
- **Secondary:** dictation software app (1,900 / 31), dictation software for windows (880 / 25), best dictation software (390 / 44), best dictation software for mac (110 / 32)
- **Semantic terms:** Dragon, Apple Dictation, Windows voice typing, Word Dictate, push-to-talk, punctuation commands, offline dictation
- **Questions (FAQ):** What is the best dictation software? What is dictation software? Is dictation software AI? What dictation software do doctors use? Where is dictation on a Mac?
- **Reddit queries:** best speech to text mac reddit
- **E-E-A-T focus:** dictate the same 500-word passage in each tool and report errors and speed. **(confirm Lynkk dictation is Mac only; do not claim Windows)**
- **Internal links:** #17, #18

#### 9. Best AI Meeting Recorders for Online and In-Person Meetings in the US
- **Slug:** /blog/ai-meeting-recorders
- **Intent:** commercial
- **Primary:** meeting recorder (1,900 / 32)
- **Secondary:** meeting recorder app (590 / 37), ai meeting recorder (480 / 37), iphone meeting recorder (390 / 36), meeting recorder and transcriber (320 / 37), best meeting recorder app (210 / 30)
- **Semantic terms:** auto-join, calendar sync, in-person recording, phone recording, storage, consent notice
- **Questions (FAQ):** Is it legal to record a meeting? Can meetings be recorded without consent? Where are Teams meeting recordings saved? Can I record a meeting on my computer?
- **Reddit queries:** best ai meeting recorder reddit, meeting recording software reddit
- **E-E-A-T focus:** include a short, sourced note on US consent laws (one-party vs two-party states) with a link to a legal source; not legal advice.
- **Internal links:** #3, #6, #1

#### 10. Top Zoom AI Companion Alternatives for 2026
- **Slug:** /blog/zoom-ai-companion-alternatives
- **Intent:** commercial + informational
- **Primary:** zoom ai companion meeting summary (390 / 26)
- **Secondary:** what is zoom ai companion (480 / 41), turn off zoom ai companion (260 / 24), how to turn off zoom ai companion (260 / 24), how to use zoom ai companion (210 / 28), zoom ai companion (5,400 / 43, stretch)
- **Semantic terms:** Zoom Workplace, AI Companion summary, meeting questions, smart recording, cross-platform note taker
- **Questions (FAQ):** What is Zoom AI Companion? Can Zoom AI Companion take notes? Does Zoom AI Companion notify participants? Where do Zoom AI Companion notes go? Can Zoom AI Companion be disabled?
- **Reddit queries:** (low demand)
- **E-E-A-T focus:** show AI Companion's real summary vs alternatives on the same call; link Zoom's official docs.
- **Internal links:** #3, #16

### Lynkk vs comparisons (Template B)

#### 11. Lynkk vs Otter.ai: Which AI Note Taker Does More After the Meeting?
- **Slug:** /compare/lynkk-vs-otter
- **Intent:** commercial (switching / evaluating)
- **Primary:** otter ai alternatives (390 / 15)
- **Secondary:** otter ai review (880 / 30), otter ai alternative (480 / 34), otter ai alternative free (40 / 26), otter ai alternative reddit (30 / 30)
- **Semantic terms:** OtterPilot, live transcript, meeting bot, action items, integrations, data privacy, pricing tiers
- **Questions (FAQ):** What is better than Otter.ai? Is Otter.ai safe? How much does Otter.ai cost? Can I import my Otter transcripts?
- **Reddit queries:** otter ai alternatives reddit, better than otter ai reddit, otter ai privacy reddit, otter ai spam reddit
- **E-E-A-T focus:** side-by-side output of the same meeting; dated pricing; a "Where Otter is stronger" section.
- **Internal links:** #7, #1, #2

#### 12. Lynkk vs Granola: Personal Notepad or Shared Team Meeting Memory?
- **Slug:** /compare/lynkk-vs-granola
- **Intent:** commercial
- **Primary:** granola ai alternatives (210 / 14)
- **Secondary:** granola ai review (320 / 22), otter vs granola (110 / 11), granola ai alternative (70 / 18), granola ai competitors (40 / 13), granola ai (27,100 / 29, stretch)
- **Semantic terms:** AI notepad, bot-free, Mac app, Windows and Android availability, team sharing, templates
- **Questions (FAQ):** Is Granola AI free? How does Granola AI work? Is Granola available on Windows or Android? Is Granola AI safe?
- **Reddit queries:** granola ai reddit review, granola alternative reddit, granola vs otter reddit
- **E-E-A-T focus:** use both tools for a week; show the difference between personal notes and shared team memory.
- **Internal links:** #1, #24 **(confirm Lynkk platforms)**

#### 13. Lynkk vs Plaud (and Pocket): Do You Need an AI Recorder Device or Just an App?
- **Slug:** /compare/lynkk-vs-plaud
- **Intent:** commercial
- **Primary:** plaud vs pocket (1,000 / 12)
- **Secondary:** pocket vs plaud (880 / 11), pocket ai vs plaud (480 / 11), plaud alternatives (320 / 12)
- **Semantic terms:** hardware recorder, subscription, in-person meetings, battery, transcription quota, phone app
- **Questions (FAQ):** Is Plaud better than Pocket? Do I need a device to record in-person meetings? How much does a Plaud subscription cost? Can a phone app replace an AI recorder?
- **Reddit queries:** plaud ai note taker reddit, pocket ai note taker review reddit
- **E-E-A-T focus:** record the same in-person meeting with all three; compare 12-month total cost.
- **Internal links:** #6, #9

#### 14. Lynkk vs Fireflies.ai: Features, Pricing and Which One Fits Your Team
- **Slug:** /compare/lynkk-vs-fireflies
- **Intent:** commercial (pricing focused)
- **Primary:** fireflies ai price (880 / 26)
- **Secondary:** fireflies ai pricing (480 / 37), fireflies alternatives (110 / 14), otter vs fireflies (90 / 17), fireflies alternative (70 / 29)
- **Semantic terms:** AI credits, storage limits, Fred assistant, conversation intelligence, integrations, seats
- **Questions (FAQ):** How much does Fireflies.ai cost? Is Fireflies.ai free? Is Fireflies.ai safe? What is better than Fireflies?
- **Reddit queries:** fireflies ai reddit review, fireflies ai credits reddit, is fireflies ai safe reddit
- **E-E-A-T focus:** pricing table with plan-by-plan limits, dated and linked.
- **Internal links:** #1, #2, #21

#### 15. Lynkk vs Fathom: Free Note Taker or Full Meeting Assistant?
- **Slug:** /compare/lynkk-vs-fathom
- **Intent:** commercial
- **Primary:** fathom ai note taking app (390 / 6)
- **Secondary:** fathom vs granola (110 / 17), fathom vs fireflies (110 / 32), fathom alternatives (50 / 14), otter vs fathom (50 / 14), fathom ai note taker (5,400 / 45, stretch)
- **Semantic terms:** free forever plan, call highlights, CRM sync, meeting bot, team plan
- **Questions (FAQ):** Is Fathom really free? Does Fathom work with Teams and Google Meet? What is better than Fathom? Does Fathom join meetings as a bot?
- **Reddit queries:** otter ai vs fathom reddit, granola vs fathom reddit
- **E-E-A-T focus:** clearly show what Fathom's free plan includes (it is generous; say so).
- **Internal links:** #2, #21

### How-tos (Template C)

#### 16. How to Get a Zoom Transcript (Even Without Recording the Meeting)
- **Slug:** /blog/how-to-get-zoom-transcript
- **Intent:** informational
- **Primary:** zoom transcript (880 / 28)
- **Secondary:** how to get zoom transcript (210 / 34), how to download zoom transcript (210 / 24), how to get zoom transcript after meeting (170 / 28), how to get zoom transcript without recording (170 / 24), how to save zoom transcript (140 / 27)
- **Semantic terms:** audio transcript, cloud recording, closed captions, full transcript, VTT file, Zoom web portal
- **Questions (FAQ):** Can I get a Zoom transcript after the meeting ends? Where is the Zoom transcript saved? Can I get a transcript without recording? How do I export a Zoom transcript?
- **Reddit queries:** (low demand)
- **E-E-A-T focus:** step screenshots from a real Zoom account; note which Zoom plans support it (link Zoom docs).
- **Internal links:** #3, #10

#### 17. Mac Dictation Not Working? Fixes and Smarter Speech-to-Text Options
- **Slug:** /blog/mac-dictation-not-working
- **Intent:** informational (problem solving)
- **Primary:** speech to text mac (1,600 / 25)
- **Secondary:** voice dictation software for mac (590 / 28), dictation mac not working (480 / 12), dictation mac shortcut (480 / 24), enable dictation mac (260 / 23)
- **Semantic terms:** macOS dictation settings, microphone permissions, keyboard shortcut, on-device dictation, language settings
- **Questions (FAQ):** Where is dictation on a Mac? Where is dictation saved on Mac? How do I turn on dictation on Mac? Why is my Mac dictation not working?
- **Reddit queries:** best speech to text mac reddit
- **E-E-A-T focus:** test fixes on a current macOS version and name the version; link Apple Support.
- **Internal links:** #8, #18

#### 18. How to Dictate in Microsoft Word (and When You Need Dictation Software)
- **Slug:** /blog/dictate-in-microsoft-word
- **Intent:** informational
- **Primary:** dictation software for microsoft word (1,600 / 8)
- **Secondary:** microsoft word dictation software (1,300 / 30), good voice to text app (590 / 21)
- **Semantic terms:** Word Dictate button, Microsoft 365, voice commands, punctuation, Word for Mac, transcribe feature
- **Questions (FAQ):** Where is dictation on Microsoft Word? Is Word dictation free? Can Word transcribe audio? Which dictation software works with Word?
- **Reddit queries:** (low demand)
- **E-E-A-T focus:** show Word's built-in Dictate on Mac and Windows; be honest that it is enough for many users.
- **Internal links:** #8, #17

#### 19. How to Transcribe Voice Memos on iPhone and Turn Them Into Notes
- **Slug:** /blog/transcribe-voice-memos-iphone
- **Intent:** informational
- **Primary:** transcribe voice memo (1,600 / 26)
- **Secondary:** iphone transcribe voice memo (880 / 24), transcribe voice memo iphone (720 / 32), how to transcribe voice memo on iphone (480 / 19)
- **Semantic terms:** Voice Memos app, iOS transcription, share audio file, summary, action items
- **Questions (FAQ):** Can iPhone transcribe voice memos? Why is iPhone voice memo transcription not working? How do I turn a voice memo into notes?
- **Reddit queries:** (low demand)
- **E-E-A-T focus:** name the iOS version you tested; link Apple Support. **(confirm whether Lynkk has an iOS app or accepts audio uploads)**
- **Internal links:** #6, #9

#### 20. Does Google Meet Have an AI Note Taker? What Gemini Can and Can't Do
- **Slug:** /blog/google-meet-ai-note-taker
- **Intent:** informational + commercial
- **Primary:** google meet ai note taker (590 / 40)
- **Secondary:** ai note taker for google meet (210 / 39), does google meet have an ai note taker (140 / 42), google meet transcript (1,000 / 53, stretch)
- **Semantic terms:** Gemini "Take notes for me", Google Workspace plans, Meet transcripts, Google Docs notes
- **Questions (FAQ):** Does Google Meet have an AI note taker? Which Workspace plans include Gemini notes? Where are Google Meet transcripts saved? Will Google Meet record if I leave?
- **Reddit queries:** google meet ai note taker reddit
- **E-E-A-T focus:** show Gemini's notes on a real call; link Google Workspace docs.
- **Internal links:** #1, #3

### Use cases (Template D)

#### 21. How Sales Teams Use Conversation Intelligence to Close More Deals (Without Gong Pricing)
- **Slug:** /use-cases/sales-conversation-intelligence
- **Intent:** commercial + informational
- **Primary:** conversation intelligence platform (880 / 37)
- **Secondary:** gong alternatives (210 / 31), what is conversation intelligence (210 / 39), sales call recording software (110 / 31)
- **Semantic terms:** call recording, deal intelligence, CRM auto-update, call prep, follow-up email, talk ratio, objection tracking
- **Questions (FAQ):** What is conversation intelligence? What is conversation intelligence software? What is HubSpot conversation intelligence? What are Gong alternatives?
- **Reddit queries:** ai note taker for phone calls reddit
- **E-E-A-T focus:** a real (anonymized) sales call walkthrough from prep to CRM update. **(confirm supported CRMs)**
- **Internal links:** #14, #15

#### 22. How Recruiters Use AI Interview Transcription to Speed Up Hiring
- **Slug:** /use-cases/recruiting-interview-transcription
- **Intent:** informational
- **Primary:** interview transcription (1,300 / 25)
- **Secondary:** interview transcription example (880 / 25), software for interview transcription (260 / 21), transcription software interviews (260 / 23)
- **Semantic terms:** interview debrief, scorecard, candidate consent, speaker labels, structured interview, bias reduction
- **Questions (FAQ):** What is interview transcription? What do interview transcripts look like? How do you transcribe an interview? Do candidates need to consent to recording?
- **Reddit queries:** otter ai for interviews reddit
- **E-E-A-T focus:** include a redacted real transcript example and a debrief template; quote a recruiter (with permission).
- **Internal links:** #5, #25

#### 23. How Product Teams Turn Meeting Minutes Into Jira Tickets Automatically
- **Slug:** /use-cases/meeting-minutes-to-jira
- **Intent:** commercial + informational
- **Primary:** app for meeting minutes (1,000 / 24)
- **Secondary:** meeting minutes app (880 / 36), action item tracker (320 / 31)
- **Semantic terms:** sprint planning, backlog, action items, owners and due dates, Jira integration, decision log
- **Questions (FAQ):** Can AI create Jira tickets from meetings? What should meeting minutes include? How do you track action items after a meeting?
- **Reddit queries:** best ai meeting minutes reddit
- **E-E-A-T focus:** show a real planning meeting turned into Jira tickets (screenshots of both).
- **Internal links:** #26, #4

#### 24. How Founders Handle Back-to-Back Meetings With One AI Teammate
- **Slug:** /use-cases/founders-back-to-back-meetings
- **Intent:** informational
- **Primary:** team ai meeting notes (720 / 25)
- **Secondary:** ai note taker app (880 / 32), meeting notes taker (720 / 29)
- **Semantic terms:** investor calls, customer calls, hiring interviews, context switching, meeting prep, follow-ups
- **Questions (FAQ):** How do founders keep track of meetings? Can AI prepare me for my next meeting? What should I do after a meeting?
- **Reddit queries:** best ai meeting notes reddit
- **E-E-A-T focus:** a founder's real week (with permission): meetings count, time spent on notes before and after.
- **Internal links:** #1, #25, #12

#### 25. Your Meetings Are Your Knowledge Base: How Teams Build Searchable Meeting Memory
- **Slug:** /use-cases/searchable-meeting-memory
- **Intent:** informational + commercial
- **Primary:** km software (720 / 21)
- **Secondary:** knowledge management software (880 / 38)
- **Semantic terms:** knowledge graph, institutional knowledge, decision history, search across meetings, onboarding, cited answers
- **Questions (FAQ):** What is knowledge management software? How do teams capture knowledge from meetings? Can AI answer questions about past meetings?
- **Reddit queries:** (low demand)
- **E-E-A-T focus:** a real "Ask Lynkk" query with a cited answer (screenshot).
- **Internal links:** #24, #23

#### 26. How Engineering Teams Run Faster Daily Standups With AI Meeting Notes
- **Slug:** /use-cases/daily-standup-meeting-notes
- **Intent:** informational
- **Primary:** standup meeting (2,400 / 19)
- **Secondary:** standup meeting agenda (480 / 31), standup meeting template (390 / 28), scrum standup meeting questions (110 / 30), daily standup meeting notes (70 / 23)
- **Semantic terms:** daily scrum, blockers, yesterday/today/blockers, async standup, sprint, Jira
- **Questions (FAQ):** What is a standup meeting? What is the purpose of a daily standup? How do you run a standup meeting? What should I say in a standup? Can standups be weekly?
- **Reddit queries:** (low demand)
- **E-E-A-T focus:** a standup template plus a real before/after of blockers turned into tickets. Quote an engineering manager.
- **Internal links:** #23, #27

#### 27. How Managers Run Better One-on-One Meetings With AI Notes (Questions and Template Included)
- **Slug:** /use-cases/one-on-one-meetings
- **Intent:** informational
- **Primary:** one on one meeting questions (1,600 / 27)
- **Secondary:** one on one meeting template (1,600 / 19), questions for one on one meeting (1,000 / 6), sample one on one meeting agenda (390 / 22), one on one meeting notes template (110 / 23)
- **Semantic terms:** career growth, feedback, blockers, recurring 1:1, manager notes, follow-up commitments
- **Questions (FAQ):** What is a one-on-one meeting? What should I say in a one-on-one with my manager? What questions should managers ask in a 1:1? Are one-on-one meetings effective?
- **Reddit queries:** (low demand)
- **E-E-A-T focus:** downloadable 1:1 template (lead magnet); author should be an experienced people manager.
- **Internal links:** #26, #24

#### 28. How Law Firms Use AI Transcription for Client Meetings and Case Notes
- **Slug:** /use-cases/legal-transcription
- **Intent:** commercial + informational (YMYL, handle with care)
- **Primary:** best legal transcription software (320 / 20)
- **Secondary:** legal transcription (480 / 30), what is legal transcription (140 / 18), sample legal transcription (90 / 22), legal transcription software (70 / 19)
- **Semantic terms:** attorney-client privilege, confidentiality, data residency, retention, verbatim transcript, case file
- **Questions (FAQ):** What is legal transcription? Is AI transcription accurate enough for legal work? How is client confidentiality protected? Where is my data stored?
- **Reddit queries:** (low demand)
- **E-E-A-T focus:** **reviewed by a practicing attorney**; no legal advice; link bar association guidance on AI and confidentiality. **(confirm Lynkk security certifications and retention controls)**
- **Internal links:** #29, #25

#### 29. How Clinicians Cut Documentation Time With AI Dictation and Note Taking
- **Slug:** /use-cases/clinical-documentation
- **Intent:** commercial + informational (YMYL, handle with care)
- **Primary:** medical dictation software (880 / 25)
- **Secondary:** hipaa compliant ai note taker (260 / 31), is otter ai hipaa compliant (170 / 25), best medical dictation software (110 / 12), ai medical dictation software (70 / 12)
- **Semantic terms:** clinical notes, SOAP notes, EHR, BAA (business associate agreement), patient consent, PHI
- **Questions (FAQ):** What dictation software do doctors use? What is medical dictation? Is an AI note taker HIPAA compliant? What is a BAA?
- **Reddit queries:** hipaa compliant ai note taker reddit
- **E-E-A-T focus:** **reviewed by a clinician or compliance expert**; link HHS HIPAA guidance. **Do not claim Lynkk is HIPAA compliant or signs a BAA unless confirmed.** If it is not, position this as a checklist for choosing tools.
- **Internal links:** #8, #28

#### 30. How Boards Automate Meeting Minutes With AI (Sample Minutes Included)
- **Slug:** /use-cases/board-meeting-minutes
- **Intent:** informational
- **Primary:** board meeting minutes sample (2,400 / 15)
- **Secondary:** sample of board meeting minutes (1,900 / 36), board meeting minutes (1,000 / 38), corporation meeting minutes (880 / 27)
- **Semantic terms:** motions, resolutions, quorum, approval of minutes, corporate secretary, nonprofit board, record retention
- **Questions (FAQ):** What should board meeting minutes include? Who takes board meeting minutes? Are board meeting minutes legally binding? Do board minutes need to be approved? Can board meetings be recorded? How long do you keep board minutes?
- **Reddit queries:** (low demand)
- **E-E-A-T focus:** a clean sample minutes document (downloadable); cite a governance source; recommend checking bylaws and state law.
- **Internal links:** #23, #9

---

## Part 5. Review checklist for you

Before we start writing, please confirm:
1. The primary keyword and slug for each post (Part 4).
2. Who will be the named author for each group, and who reviews #28 (legal) and #29 (healthcare).
3. The open product facts marked **(confirm)**: free-plan limits, platforms (Windows/iOS/Android), supported CRMs, Teams/Zoom/Meet support, accuracy and language figures, HIPAA/BAA, security certifications.
4. Whether we can run the tests the E-E-A-T sections call for (tool sign-ups, test meetings, the accuracy test in #5).
