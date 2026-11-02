# Lynkk.ai: Brand & Product Memory

> Source of truth for tool/directory submissions.
> **Revised 2026-11-02 from the live site** (lynkk.ai was directly reachable this time: homepage,
> /blog, /security, /integrations). The earlier version of this file was built from search-result
> snippets in Sept 2026 and was materially wrong on positioning, integrations, privacy and
> features. Corrections are marked **[CORRECTED 2026-11-02]**.

## Identity

| Field | Value |
|---|---|
| Brand name | **Lynkk** (double "k") |
| Website | https://lynkk.ai/ |
| Contact email | marketing@lynkk.ai (site lists **admin@lynkk.ai** for support, security, deletion and sales) |
| Page title (live) | **Lynkk: AI Meeting Assistant & Note Taker for Sales Teams** **[CORRECTED]** |
| Meta description (live) | "Lynkk is the AI meeting assistant that takes notes on Zoom, Meet, Teams and in person, then drafts your follow-ups. 17 languages. Start free." |
| Category | AI meeting assistant / AI note taker for **sales teams** |
| Pricing | **Free; Pro $15/mo ($9.75/mo billed yearly); Enterprise (teams up to 10, priced on a call)** **[CORRECTED: was "to confirm"]** |
| Social | Instagram @lynkk.ai; reviews on F6S **[CORRECTED: no LinkedIn/X/PH found on site]** |

**Do not confuse with:** Lynk (getlynk.ai), Lynk AI (getlynk.co), Lynk (lynk.run), Linnk AI, Link AI.
Always spell it **Lynkk** / **lynkk.ai**.

## Positioning **[CORRECTED: this is now sales-specific, not generic knowledge work]**

- **H1 (live):** The AI meeting assistant that remembers every sales conversation.
- **Supporting line:** Your revenue lives in your conversations. Lynkk turns every customer
  conversation into follow-ups, action items and your next best move.
- **og:title:** Lynkk: Record any conversation. Get notes, tasks, and answers.
- **Closing line:** Make every conversation count. You build the relationship, Lynkk remembers
  what moves it forward.
- **Differentiator:** account-level memory. Every call with an account sits together, and
  "Ask Lynkk" answers across all of them with the source quote attached.

## Features (as the live site describes them)

### Capture: four ways in
- Meeting bot sent via call link or calendar (**on the free plan**)
- Chrome extension, records with **no bot in the call**
- Mac app notices the call automatically, records both sides locally
- In-person recording on the Mac

### Notes and follow-through
- Notes, action items, commitments, and a conversation-at-a-glance summary
- Follow-up email drafts, grounded in what was said. **You send it yourself, nothing auto-sends.**
- Jira issues linked back to the call
- CRM logging on the deal record
- "What did I promise this week?" across every call

### Spotter: the live in-call assistant
- Panel on the Mac that reads your screen and the call, suggests answers live
- Hears your mic as "Me" and the call as "Them"
- Modes: Sales, Support, Interview prep, or your own pasted notes
- **Never hidden from a screen share. Screen is read as text, never sent as an image.**
- **Status: in development, early access on Pro by request.** Do not write about it as shipped.

### Platform
- Web app, **Mac app** (current build 2.6.10), **Chrome extension**, Slack app
- Dictation (words erased from Lynkk servers after 7 days)
- Workspaces with admin roles

### Languages
- **17 languages, plus a dedicated Hinglish mode** for calls that move between Hindi and English.
  India is clearly a priority market. **[CORRECTED: "multilingual" was vague before]**

## Integrations **[CORRECTED]**
- **CRM: HubSpot, Salesforce, Pipedrive, Zoho CRM, Attio** (set up with the Lynkk sales team)
- **Meetings: Zoom, Google Meet, Microsoft Teams**
- **Google Calendar** (auto-join)
- **Slack** (reads only its mentions, DMs and /lynkk)
- **Jira**
- **NOT on the site: MCP, Calendly, Cal.com.** The earlier claims of "connect anything via MCP"
  and Calendly/Cal.com integrations are **not supported anywhere on lynkk.ai**.
  **MCP is confirmed NOT on the roadmap (team, 2026-11-02). Never publish it as a Lynkk
  capability.** Calendly and Cal.com remain unconfirmed; do not publish until product confirms.

## Security and privacy: what the /security page actually says **[CORRECTED, important]**

The earlier "pick a region and everything is processed there" data-residency claim is **the
opposite of what the site says.** Verbatim from /security:

- **"Your data may be processed outside your country, including in India and the US."**
- "Under the GDPR and India's DPDP Act, you can see, correct, export or delete your data."
  (This is a **data-rights statement, not a certification.**)
- **AES-256-GCM encrypts tokens for Google Calendar, Jira and Slack only**, with keys kept outside
  the database. It is **not** described as covering recordings.
- **"Lynkk isn't end-to-end encrypted, because it has to read a recording to write the note."**
- Everything between device and Lynkk travels over HTTPS; upload links are signed and expire in
  10 minutes; playback links expire after an hour; share links last 30 days.
- The Mac app deletes its local copy 7 days after upload.
- **"No AI training on this conversation."** Audio and transcript go to speech-to-text and AI
  model providers over HTTPS.
- Workspace admins can read notes unless marked Personal; they never get the recording.
- Export: one zip of every note and recording, from Settings. Deletion: email admin@lynkk.ai.
- The bot appears in the participant list as "<Name>'s Notetaker" and **does not announce itself
  out loud**, so the site tells users to disclose recording themselves.
- **No SOC 2 claim. No data residency. No accuracy percentage anywhere on the site.**

### Claims NOT to publish
- **"97% transcription accuracy"**: appears in the Ubersuggest project business summary. It is
  **nowhere on lynkk.ai**. Unsourced. Do not use.
- **"AES-256 encryption"** as a blanket claim: token-only in reality.
- **"GDPR compliant"** as a certification: the site claims data rights, not an audit.
- **"Data residency / pick a region"**: contradicted by the live security page.
- **"MCP"**: not a product capability, and **confirmed not on the roadmap (2026-11-02)**. Closed.
- **"Knowledge graph"**: the homepage uses the phrase twice, but the user-facing framing is
  "one connected memory" and "Ask Lynkk". Prefer the site's own words.

## Target users (live site)
Sales teams first: sellers, sales leaders, RevOps. Use-case pages also cover customer research,
user interviews, field interviews, 1:1s, team standups, lectures, financial advisors, lawyers,
real estate agents.

## Site structure (for internal linking)
- `/features/`: meeting-notes, action-items, ask-your-meetings, spotter, dictation,
  chrome-extension, meeting-bot, workspaces, hinglish-transcription
- `/integrations/`: hubspot, salesforce, pipedrive, zoho-crm, attio, zoom, google-meet,
  microsoft-teams, google-calendar
- `/compare/`: otter, fireflies, fathom, granola, read-ai, avoma, circleback, clari-copilot,
  gong, meetgeek, notta, plaud
- `/use-cases/`: sales-calls, customer-research, user-interviews, field-interviews,
  one-on-one-meetings, team-standups, lectures, financial-advisors, lawyers, real-estate-agents
- Other: /blog, /pricing, /security, /privacy, /terms, /refund, /faq, /how-it-works, /demo,
  /download, /web-app, /slack, /support, /meeting-and-dictation

## Submission copy, rewritten for the live positioning

- **Name:** Lynkk
- **Tagline (<=60 chars):** The AI meeting assistant that remembers every call
- **Short description (<=160 chars):** Lynkk takes notes on Zoom, Meet, Teams and in-person sales
  calls, then drafts the follow-up, the tasks and the CRM update. 17 languages. Start free.
- **Long description:**
  Lynkk is an AI meeting assistant and note taker built for sales teams. It records Zoom, Google
  Meet, Microsoft Teams and in-person conversations, four ways: a meeting bot, a Chrome extension
  with no bot in the call, automatic capture in the Mac app, or in-person on your Mac. After the
  call you get notes, action items and the commitments people made, plus a follow-up email draft
  grounded in what was actually said, Jira issues, and the summary logged on the deal in HubSpot,
  Salesforce, Pipedrive, Zoho or Attio. Every call with an account sits together, so you can ask
  "what did they say about budget across our last three calls" and get the answer with its source.
  17 languages, including a Hinglish mode. Free to start, Pro at $15 a month.
- **Tags:** AI meeting assistant, AI note taker, sales, CRM automation, meeting notes, follow-up
  emails, transcription, Jira, Hinglish, productivity

## Still to confirm with the team
- [ ] Is there any measured accuracy figure, and measured how? (Needed before any post quotes one.)
- [ ] SOC 2 status, DPA availability, named sub-processors
- [ ] Which speech-to-text and AI model providers are used
- [ ] Windows / iOS / Android roadmap (Web, Mac, Chrome confirmed)
- [ ] Spotter GA date
- [ ] Company legal name, founding year, HQ, founders
- [ ] Logo files, screenshots, demo video URL
