# Lynkk.ai: Brand & Product Memory

> Source of truth for tool/directory submissions. Collected 2026-10-11 from the live site
> (lynkk.ai pages, /llms.txt, /sitemap.xml, /pricing, /faq, /security, /integrations,
> /download, /terms, /privacy). Earlier notes from 2026-09-27 came from search results only
> and several of them were wrong; they have been corrected below.
> Items under "Still to confirm" must be filled in by the team before submitting.

## Identity

| Field | Value |
|---|---|
| Brand name | **Lynkk** (double "k") |
| Website | https://lynkk.ai/ |
| Contact email (ours, for submissions) | marketing@lynkk.ai |
| Public contact on site | admin@lynkk.ai |
| Page title | Lynkk: AI Meeting Notes & Conversation Intelligence |
| Category | AI meeting notes / AI note taker / meeting memory / conversation intelligence / productivity |
| Pricing model | Freemium: Free $0, Pro $15/month, Enterprise custom (details below) |
| Legal jurisdiction | Terms are governed by the laws of India |
| Billing | Paddle.com is Merchant of Record (handles payments and taxes) |

**Do not confuse with:** Lynk (getlynk.ai, enterprise AI enablement), Lynk AI (getlynk.co, no-code AI agents), Lynk (lynk.run), Linnk AI (document intelligence), Link AI (agentic business suite), Lynq AI (relationship management). Always spell it **Lynkk** / **lynkk.ai**.

## Positioning (live site copy)

- **Hero headline:** The AI assistant that remembers everything your team discusses.
- **Hero subline:** Lynkk connects your conversations, decisions, and tasks, giving you the context you need to know what happened and what comes next.
- **Footer tagline:** Meeting memory for teams. It records, it writes things down, and it remembers.
- **Closing line:** Your conversations, connected. Start remembering today.
- **llms.txt summary:** Lynkk is an AI meeting notes app. It records your meetings, online and in person, and turns them into notes you can search: a summary, action items with owners and due dates, decisions, and a transcript with speaker labels.
- **Differentiators the site leans on:** records in person as well as online; many ways to record (web, Mac app with no bot, Chrome extension with no bot, or a meeting bot); 17 languages with Hinglish as the default; Ask Lynkk answers across every meeting with cited sources; model region pinning for compliance.

> Retired copy: "Lynkk joins your meetings, speaks when needed, remembers everything, and does the work after" and "One AI across the entire meeting lifecycle" no longer appear on the site. Do not use them.

## Ways to record

- **Web app:** records in the browser (in-person or calls), plus the full dashboard for reviewing notes.
- **Mac app (beta, v2.2.0):** menu bar app. Notices calls in Zoom, Google Meet (in 9 browsers incl. Chrome, Safari, Arc, Brave, Edge), Microsoft Teams, Slack huddles, Webex, WhatsApp and FaceTime, asks once, and records both sides with **no bot in the call** and no calendar needed. Keeps recording if the connection drops and uploads later. Requires Apple silicon and macOS 14.2 or later; Intel Macs should use the browser. Not yet signed with an Apple Developer ID (install needs one Terminal command).
- **Chrome extension:** records Google Meet, Zoom (browser) and Microsoft Teams from your own tab, audio only, nothing joins the call, works on Free. https://chromewebstore.google.com/detail/dmnbcgdjlekmcllcobbdpfoibchblecl
- **Meeting bot:** joins Zoom, Google Meet and Microsoft Teams from a pasted link, or automatically once Google Calendar is connected. Joins as a visible participant named after you. Audio only on Free, video on Pro.

## What you get from each meeting

- Meeting Brief: summary, key takeaways, topics, action items (owner, due date, and the moment it was said), decisions, open questions, key quotes.
- Speaker-labelled transcript; timestamps play the audio from that moment.
- Auto-tags, and people/companies/projects picked out so related meetings link together.
- Summary emailed to you when the call ends.
- Ready about 30 seconds after the recording uploads ("Record. Process. Connect. In under 30 seconds.").

## Features

- **Ask Lynkk (Pro):** ask one note or all of them about a customer, person or project; answers cite the note and the minute. Answers only from your own notes.
- **Search:** hybrid semantic + keyword search across every meeting (basic search on Free).
- **Tasks:** every action item lands on one task board (Kanban or list) with status, due date and priority.
- **Jira:** send a note's action items to Jira, one issue per item, with the project and issue type you choose. **Manual, not automatic** ("Nothing is pushed automatically").
- **Decision log, action tracker, weekly digest** (Pro).
- **Share links** (read-only, revocable).
- **Lynkk for Slack:** mention @Lynkk and it answers in the thread from your meeting notes, with sources.
- **Dictation on Mac:** hold fn and speak, words are typed at the cursor in any app. Instant mode is free, on-device, English only. Accurate and Polished modes (Pro) run in the cloud, hear 18 languages, and Polished removes fillers.
- **Cue (Pro):** listed on the homepage pricing card as "Cue, answering during the call". No other detail on the site.
- **Workspaces:** team plan for up to 10 seats, billed per seat (price not stated), needs a company email. Every seat gets Pro; admins can read notes unless the owner marks them Personal, and every admin read is logged. Enterprise adds admin controls and audit log across teams.

## Languages

17 languages plus auto-detect, with **Hinglish as the default** (handles Hindi/English switching mid-sentence): English, Hindi, Spanish, French, German, Portuguese, Italian, Dutch, Japanese, Chinese, Korean, Arabic, Russian, plus Tamil, Telugu, Marathi and Bengali in beta.

## Pricing (from /pricing, USD)

| Plan | Price | Includes |
|---|---|---|
| Free | $0 forever | 5 notes/month, 2 hours max per note, 5 hours of AI meeting summaries, basic search, Mac app + web. Meeting bot records audio only. No credit card. |
| Pro | $15/month, or $117/year (yearly saves 35%, "early-bird pricing"; yearly price from /compare) | Unlimited notes, 2 hours max per note, unlimited AI summaries, Ask Lynkk AI chat, decision log + action tracker, multilingual transcription, meeting bot with video, weekly digest |
| Enterprise | Custom, priced on a call | Everything in Pro for every seat, shared notes across teams, admin controls and audit log, centralized billing, priority support |

Cancel anytime. Refund policy at https://lynkk.ai/refund.

## Integrations (connected today)

Google Calendar, Microsoft Teams & Outlook Calendar, Jira, Calendly, Cal.com, Slack, and any custom MCP server.
**Coming soon:** Notion, Linear, Asana, HubSpot.
**No CRM integration today** (HubSpot is "soon"; Salesforce not mentioned).

## Privacy & security

- Notes private by default; audio and notes encrypted in transit and at rest with AES-256; integration credentials encrypted with per-deployment keys.
- Never trains models on your conversations; export or delete everything anytime.
- Audio retention you control: keep forever, auto-delete after 30, 90 days or a year, or wipe after upload.
- "Built to comply with" GDPR and India's DPDP Act; consent flow for multi-party recording.
- **Region pinning:** model calls can be pinned per workspace to the US, EU, UK, India, Singapore or Australia (transcription, summaries, assistant and search embeddings). Set up with the Lynkk team, not a self-serve toggle.
- Data may be processed in India and the United States (privacy policy).

## Target users / use cases (site pages)

Sales calls, team standups, user interviews, lectures, doctor visits, field interviews (record with no signal, upload later). Also recruiting interviews (blog). Comparison pages exist vs Otter.ai, Fireflies.ai, Granola and Fathom.

## Social proof

- 5.0 from 16 reviews on F6S: https://www.f6s.com/company/lynkk
- Testimonials on the homepage from users at Microsoft, Groww, Wissen Technology, EXL Service and Home Credit Indonesia (individual users, not company endorsements).

## Links

| Link | URL |
|---|---|
| X / Twitter | https://x.com/meetlynkk |
| LinkedIn | https://www.linkedin.com/company/lynkk-ai/ |
| YouTube | https://www.youtube.com/channel/UCeOhV4DzYQ7yLEZ2VgIKfkA |
| Instagram | https://www.instagram.com/lynkk.ai |
| F6S | https://www.f6s.com/company/lynkk |
| Chrome extension | https://chromewebstore.google.com/detail/dmnbcgdjlekmcllcobbdpfoibchblecl |
| Mac download | https://lynkk.ai/download |
| Book a demo | https://lynkk.ai/demo |
| Pricing | https://lynkk.ai/pricing |
| Blog / RSS | https://lynkk.ai/blog, https://lynkk.ai/blog/rss.xml |
| Site icon / OG image | https://lynkk.ai/icon, https://lynkk.ai/apple-icon, https://lynkk.ai/opengraph-image |

## Ready-to-use submission copy (matches the live site)

- **Name:** Lynkk
- **Tagline (≤60 chars):** Meeting memory for teams: notes, tasks and answers
- **Short description (≤160 chars):** Lynkk records meetings online and in person and turns them into searchable notes, action items and decisions. Ask across every call, with sources.
- **Long description:**
  Lynkk is meeting memory for teams. Record in the browser, with the Mac app or Chrome extension (no bot in the call), or send a meeting bot to Zoom, Google Meet and Microsoft Teams. Shortly after each meeting you get a summary, action items with owners and due dates, decisions, and a speaker-labelled transcript, in 17 languages plus auto-detect, Hinglish included. Every action item lands on one task board and can be sent to Jira. Ask Lynkk answers questions across all your meetings, citing the note and the minute, and you can ask it in Slack too. Notes are private and encrypted, Lynkk never trains on your conversations, and model processing can be pinned to the US, EU, UK, India, Singapore or Australia. Start free; Pro is $15/month.
- **Tags:** AI meeting notes, AI note taker, meeting transcription, meeting assistant, conversation intelligence, Hinglish transcription, multilingual, dictation, productivity, Jira, Slack, MCP

## Site inconsistencies to flag to the team

- Homepage pricing card says Free has "Unlimited recording and transcription", but /pricing and the FAQ say 5 notes/month. Use the /pricing numbers.
- /llms.txt says "Lynkk has no iPhone or Android app", but /how-it-works says "Catch conversations on mobile" and the Terms mention iOS and Android. Treat mobile as **not available** until the team confirms.
- Homepage logo strip lists Webex as a platform, but the bot and extension only cover Zoom, Meet and Teams (Webex works only via the Mac app).
- Homepage Pro card mentions "Cue" and "Microsoft actions from chat", which are not described anywhere else.
- Mac dictation (cloud) supports 18 languages, a different list from the 17 transcription languages.
- Homepage testimonial from "Samarth Wagh, Groww" does not say he is a Lynkk co-founder (the blog author page does). Review sites and directories may object to an undisclosed founder testimonial.

## Status of items to confirm

- [x] Paid plan names, prices, and free-tier limits (see Pricing; Pro yearly is $117 per /compare; Workspaces per-seat price not stated on site)
- [x] Platforms: Web, Mac (beta, Apple silicon), Chrome extension, meeting bot. No Windows app (use browser). iOS/Android: not available per llms.txt, but see inconsistencies above
- [x] Supported meeting platforms: Zoom, Google Meet, Microsoft Teams (bot and extension); Mac app also Slack huddles, Webex, WhatsApp, FaceTime
- [x] Which CRMs: none today; HubSpot coming soon
- [x] Number of supported languages: 17 plus auto-detect (4 of them in beta)
- [x] Available data regions: US, EU, UK, India, Singapore, Australia
- [ ] Company legal name, founding year, HQ location, founders: co-founder **Samarth Wagh** confirmed (blog author page: ex-Groww product manager, B.Tech + M.Tech Engineering Design, IIT Madras, https://www.linkedin.com/in/samarth-wagh-iitm/). Legal name, founding year, HQ and other founders not stated on site (Terms are governed by Indian law)
- [x] Social links: X, LinkedIn, YouTube, Instagram, F6S (Product Hunt not found on site)
- [ ] Logo files (SVG/PNG, square + wide), screenshots, demo video URL: no press kit or demo video on site; only /icon, /apple-icon and /opengraph-image
- [ ] Security/compliance certifications: no SOC 2 / ISO 27001 / HIPAA stated; site only says "built to comply with" GDPR and DPDP
