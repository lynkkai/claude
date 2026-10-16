# lynkk.ai Use-Case Pages: Audit and Plan

> Built from the live site on 2026-10-16 (lynkk.ai homepage, /use-cases, /use-cases/sales-calls,
> /use-cases/user-interviews, sitemap.xml), the keyword data in `research/use-case-keyword-research.md`
> and the Google guidance in `research/use-case-page-structure.md`. **Where those two docs disagree with this
> one, this one wins**, because it reflects what Lynkk actually does today.

---

## 1. What lynkk.ai already has

| Section | Live URLs |
|---|---|
| Use-case hub | `/use-cases` |
| Use cases (6) | `/use-cases/sales-calls`, `/use-cases/team-standups`, `/use-cases/user-interviews`, `/use-cases/lectures`, `/use-cases/doctor-visits`, `/use-cases/field-interviews` |
| Compare (4) | `/compare/otter`, `/compare/fireflies`, `/compare/granola`, `/compare/fathom` |
| Features | `/features/meeting-notes`, `/features/ask-your-meetings`, `/features/multilingual-transcription`, `/features/hinglish-transcription`, `/features/meeting-bot`, `/features/action-items`, `/features/dictation`, `/features/workspaces`, `/features/chrome-extension` |
| Blog posts that can support use cases | `/blog/sales-conversation-intelligence`, `/blog/recruiting-interview-transcription`, `/blog/meeting-minutes-sample`, `/blog/meeting-minutes-to-jira`, `/blog/action-items-examples-template`, `/blog/one-on-one-meeting`, `/blog/daily-standup-meeting`, `/blog/legal-transcription-service`, `/blog/medical-transcription-software`, `/blog/founders-meeting-notes`, `/blog/meeting-knowledge-management` |

So we are **improving and extending an existing cluster**, not starting from zero.

## 2. Verified product facts to use in copy (from the live site)

| Topic | What the site says |
|---|---|
| Capture | Mac app (records without joining the call, also in-room), meeting bot (Zoom, Google Meet, Microsoft Teams, Webex; calendar auto-join), Chrome extension, web app. Offline recording on Mac, upload later. Dictation. |
| Output | Meeting Brief: next steps with owner, due date, priority; decisions; open questions; key takeaways with timestamps; transcript with speaker labels; topics. Follow-up email draft. "Shapes" such as Sales Call and Customer Interview (Pro). |
| Memory | Ask Lynkk across meetings, answers cite the source conversation (Pro). Cue: answers during calls (Pro). Decision log, weekly digest (Pro). |
| Tasks / integrations | Tasks with owners and dates; push to Jira and Microsoft tools; Slack; Google Calendar. |
| **CRM** | **No CRM sync.** The sales-calls FAQ says so. |
| Languages | 17 languages + auto-detect, Hinglish; Tamil, Telugu, Marathi, Bengali in beta. |
| Data region | Per-workspace AI model region: US, EU, UK, India, Singapore, Australia. |
| Security | Private by default; AES-256 in transit and at rest; retention options (forever, 90 days, 30 days, delete after upload); not used to train models; "built to comply" with GDPR, UK GDPR and India's DPDP Act; consent flow for multi-party recording. No SOC 2 or HIPAA claim. |
| Pricing | Free $0, Pro $15/month. **Conflict:** the homepage says Free has unlimited recording, the FAQ says 5 notes a month up to 2 hours each. Fix this before use-case pages quote the free plan. |
| Proof | Logos: Microsoft, Groww, Wissen Technology, EXL Service, Home Credit Indonesia. 5 named testimonials on the homepage. 5.0 from 16 reviews on F6S. |

**Do not claim on use-case pages:** CRM updates, Salesforce/HubSpot, Calendly/Cal.com, SOC 2, HIPAA, clinical scribing.

## 3. Audit: existing use-case pages vs Google's guidance

Checked `/use-cases/sales-calls` and `/use-cases/user-interviews` in detail (the other four share the same template).

### Already good (keep)
- Clear, specific H1 that says what the reader gets ("AI notes for sales calls, with the next steps already written down").
- Problem section, then how Lynkk helps.
- **Real sample output as text**: a sample sales call note and a sample follow-up email. This is exactly the "original information" and "first-hand experience" Google asks for, and AI Overviews can quote it.
- Honest FAQ answers ("Does Lynkk connect to a CRM? No."). Honest limits build trust.
- Capture-method section, related use cases, related guides, breadcrumb, closing CTA, "Last updated" date.
- Around 1,000-1,200 words of body copy, which is enough when every section is useful.

### Gaps to fix (in priority order)
1. **No proof on any use-case page.** Add a real testimonial or a short customer story to each page, from someone who uses Lynkk for *that* conversation type. Homepage testimonials (Groww, Microsoft, Wissen, EXL, Home Credit) can be reused only where they match the use case.
2. **No security and privacy block.** Add a short section: private by default, choose your data region, consent flow, AES-256, not used for training, retention options, link to `/security`. This matters most on user-interviews, field-interviews, doctor-visits and any recruiting page.
3. **No author or reviewer.** The blog already has author pages (`/blog/authors/samarth-wagh`). Add "Reviewed by [name, role]" next to "Last updated" on use-case pages.
4. **No comparison block.** Add a short table, for example "Lynkk vs typing notes vs bot-only note takers", and link to the matching `/compare/` page. This serves the comparison intent we saw in the SERPs.
5. **Visuals.** Keep the sample notes as HTML text. Add one real screenshot or a 30-60s screen recording per page, with descriptive alt text and `VideoObject` schema.
6. **Titles don't always match how people search.** People search "ai note taker for sales calls", not "AI notes for sales calls". Suggested: `AI Note Taker for Sales Calls: Next Steps and Owners | Lynkk`. User interviews could add "customer interviews" to also capture the marketing angle.
7. **Pages look strongly templated.** That's fine as long as the content inside each section is unique (it mostly is). Strengthen the role-specific parts (walkthrough steps, sample note, FAQ) rather than the shared parts.
8. **Check what WebFetch can't see:** meta descriptions, canonical tags, `BreadcrumbList` and `Organization` schema, and whether the main content is server-rendered. Use Google's Rich Results Test and URL Inspection in Search Console.

On structured data, skip `SoftwareApplication` star ratings unless reviews are shown on the page itself. The F6S score lives on another site.

## 4. New use-case pages to add

These follow the existing URL style (named after the conversation) and only promise what Lynkk does today.

| Priority | New page | Target keywords (US / India volume) | Lead with | Link to existing |
|---|---|---|---|---|
| 1 | `/use-cases/meeting-minutes` | ai meeting minutes 1,600 / 210; minutes of meeting 1,900 / 27,100; board meeting minutes 1,000 | Full MoM sample (attendees, decisions, action items with owners), multilingual minutes, push actions to Jira | `/blog/meeting-minutes-sample`, `/blog/meeting-minutes-to-jira`, `/blog/action-items-examples-template` |
| 1b | Template: expand `/blog/meeting-minutes-sample` (or add `/templates/minutes-of-meeting-format`) | minutes of meeting format 14,800 India, SD 10 | Free Word / Google Docs / Excel format + filled sample + "generate it automatically" | `/use-cases/meeting-minutes` |
| 2 | `/use-cases/recruiting-interviews` | ai recruiting 3,600 / 1,900; interview transcription 1,300; interview notes 480 (SD 19) | Speaker labels, in-person and online, revocable share link for the hiring panel, ask across all interviews, consent flow, data region | `/blog/recruiting-interview-transcription`, `/use-cases/user-interviews` |
| 3 | `/use-cases/in-person-meetings` | ai note taker for in person meetings 480 + long tail (~670 total), weak SERP | No bot needed, Mac app and web app in the room, offline then upload, speaker labels, 17 languages + Hinglish | `/use-cases/field-interviews`, `/download` |
| 4 | `/use-cases/one-on-one-meetings` | one on one meeting 2,400 | Meeting Brief and open items from the last 1:1, tasks with owners, Ask Lynkk across past 1:1s | `/blog/one-on-one-meeting` |
| 5 | `/use-cases/client-meetings` (consultants, agencies, lawyers, advisors on one page) | ai for consultants 140; ai for lawyers 2,400 / 720; ai for financial advisors 210 | Client call notes, decisions, follow-up email, data region, retention controls, consent | `/blog/legal-transcription-service` |

**Expand instead of creating new pages** (avoids near-duplicate pages):
- **Marketing:** extend `/use-cases/user-interviews` to "User and customer interview notes", with a customer-research and focus-group section, instead of a thin marketing page.
- **Project managers / Jira:** extend `/use-cases/team-standups` with sprint reviews and retros, and target "ai note taker for project managers" and "meeting notes to Jira". Link `/blog/meeting-minutes-to-jira`.
- **Sales:** keep `/use-cases/sales-calls`. Position it around next steps, decisions, open questions, the follow-up email, Ask Lynkk across an account, in-person and offline meetings, and Jira handoff. **Not** CRM. Use "conversation intelligence" only through the existing blog post.

**Not now:**
- Real estate and financial advisors as separate pages. Buyers there expect CRM sync, which Lynkk doesn't have.
- Any "AI medical scribe" positioning. `/use-cases/doctor-visits` is for patients keeping personal records, which is fine; clinicians expect HIPAA and EHR integration.

## 5. Recommended order of work

1. Upgrade `/use-cases/sales-calls`: title, testimonial, security block, comparison block, reviewer line.
2. Build `/use-cases/meeting-minutes` and the MoM format template (biggest India opportunity).
3. Build `/use-cases/recruiting-interviews`.
4. Build `/use-cases/in-person-meetings`.
5. Expand `/use-cases/team-standups` (project managers, Jira) and `/use-cases/user-interviews` (customer interviews, marketing).
6. Build `/use-cases/one-on-one-meetings` and `/use-cases/client-meetings`.
7. Add the missing sections (proof, security, comparison, reviewer) to lectures, doctor-visits and field-interviews.
8. Add every new page to the `/use-cases` hub cards, the footer "Use cases" column and the sitemap.

## 6. The lynkk.ai use-case page template

This keeps your current live structure and adds the missing pieces. **UNIQUE** means it must be written fresh for each page.

| # | Section | Status on live pages | Notes |
|---|---|---|---|
| 0 | Title, meta description, H1, breadcrumb, "Last updated" + **Reviewed by** | Partly (add reviewer, check meta) | Title: `AI Note Taker for [Conversation]: [Outcome] \| Lynkk` |
| 1 | Hero: H1, 1-2 sentence outcome, Start for free + Download for Mac | Keep | Add one real screenshot or short video |
| 2 | "Why [X] goes wrong, and how Lynkk fixes it" (problem / how Lynkk helps) **UNIQUE** | Keep | Role-specific pains in the reader's words |
| 3 | "What the note gives you" (numbered parts of the Meeting Brief) **UNIQUE** | Keep | Only the parts that matter for this conversation |
| 4 | **Sample note** as HTML text (+ sample follow-up email where relevant) **UNIQUE** | Keep, most important | Realistic, specific, no lorem ipsum |
| 5 | Step-by-step walkthrough of one real meeting **UNIQUE** | **Add** | 4-6 steps: before (Meeting Brief), during (Cue), after (note, tasks, Jira) |
| 6 | How to capture it (Mac app, bot, Chrome extension, web app) | Keep | Put the method that fits best first (in-person: Mac or web app) |
| 7 | **Proof**: testimonial or customer story **UNIQUE** | **Add** | Real name, role, company, one specific result |
| 8 | **Privacy & security** | **Add** | Data region, consent flow, AES-256, no training, retention, link to `/security` |
| 9 | **Comparison** table | **Add** | Lynkk vs manual notes vs bot-only tools; link `/compare/*` |
| 10 | FAQ, 5-8 questions **UNIQUE** | Keep | Include honest "No" answers; use real searched questions |
| 11 | More use cases + related guides | Keep | Descriptive anchor text |
| 12 | Closing CTA | Keep | |

## 7. Internal linking map

```
/use-cases (hub)
 ├─ /use-cases/sales-calls ........ /blog/sales-conversation-intelligence, /compare/fireflies, /compare/fathom
 ├─ /use-cases/meeting-minutes .... /blog/meeting-minutes-sample, /blog/meeting-minutes-to-jira, /blog/action-items-examples-template
 ├─ /use-cases/recruiting-interviews  /blog/recruiting-interview-transcription, /compare/otter
 ├─ /use-cases/in-person-meetings . /use-cases/field-interviews, /download, /features/multilingual-transcription
 ├─ /use-cases/team-standups ...... /blog/daily-standup-meeting, /blog/meeting-minutes-to-jira, /features/action-items
 ├─ /use-cases/user-interviews .... /features/ask-your-meetings, /compare/granola
 ├─ /use-cases/one-on-one-meetings  /blog/one-on-one-meeting
 ├─ /use-cases/client-meetings .... /blog/legal-transcription-service, /security
 ├─ /use-cases/lectures, /use-cases/doctor-visits, /use-cases/field-interviews
 └─ every use-case page links back to /use-cases, /security and /pricing
```

Each supporting blog post should link *up* to its use-case page with descriptive anchor text, for example
"AI note taker for recruiting interviews".
