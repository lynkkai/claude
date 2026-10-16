# Lynkk: Hashnode publication setup copy

Field-by-field copy for the Hashnode publication dashboard, plus a welcome post and a
starter content plan. Anything marked TODO needs a real value before publishing.

Hashnode's audience skews toward developers and technical builders, so the copy leans
into integrations, MCP, and how the product works, while staying true to the site copy in
`memory/lynkk-brand.md`.

---

## General settings

### Publication name
Primary:
```
Lynkk Blog
```
Alternates:
```
The Lynkk Blog
```
```
Lynkk: Notes from the Meeting Lifecycle
```

### Display title (shown in the blog header if you don't use a logo)
```
Lynkk
```

### Subdomain
```
lynkk.hashnode.dev
```
(Fallbacks if taken: `lynkkai.hashnode.dev`, `blog-lynkk.hashnode.dev`)

### Custom domain (recommended)
```
blog.lynkk.ai
```
TODO: add the DNS record Hashnode shows on the Domain settings page, then wait for SSL to
provision. A custom domain keeps the SEO value on lynkk.ai.

### About this publication
Short:
```
The official blog of Lynkk, the AI meeting assistant that works before, during and after every meeting. Product updates, guides, and how we build it.
```

Long:
```
Lynkk is one AI across the entire meeting lifecycle. Before a call, it surfaces context from past meetings. During the call, it joins and speaks when you need it. Within 30 seconds after, you get structured notes, action items, CRM updates and Jira tickets, all searchable in a knowledge graph.

This is where we share product updates, practical guides for running better meetings, and the engineering behind it all: live voice AI, multilingual capture, data residency, and connecting everything through MCP.

Try Lynkk free at https://lynkk.ai
```

### Meta description (SEO, aim for 150-160 chars)
```
Product updates, guides and engineering stories from Lynkk, the AI meeting assistant for notes, action items, CRM updates and Jira tickets.
```

### Meta title
```
Lynkk Blog: AI Meeting Notes, Voice AI and Productivity
```

---

## Navbar links

| Label | URL |
|---|---|
| Product | https://lynkk.ai |
| Start free | https://lynkk.ai (TODO: direct sign-up URL if there is one) |
| Contact | mailto:marketing@lynkk.ai |

---

## Social links

- Website: https://lynkk.ai
- TODO: X / Twitter
- TODO: LinkedIn
- TODO: YouTube
- TODO: GitHub (only if Lynkk has a public org, e.g. for MCP examples)
- TODO: Product Hunt page (after launch)

---

## Branding

- TODO: Logo (square, PNG/SVG) for the publication avatar
- TODO: Wide logo for the header (light and dark versions if available)
- TODO: Favicon
- TODO: Default OG / social share image (1200x630), product name plus the one-line promise
- TODO: Brand color hex for the header accent

---

## Newsletter

### Newsletter subscribe prompt
```
Get new posts from Lynkk in your inbox: product updates, meeting playbooks, and the engineering behind voice AI that actually shows up for the meeting.
```

---

## Author / team bio (for the publication's member profiles)

Short company bio:
```
Building Lynkk, the AI teammate for every meeting: before, during, after. Notes, tasks, CRM updates and Jira tickets, automatically.
```

---

## Tags to use on posts

Primary: `ai`, `productivity`, `meetings`, `artificial-intelligence`

Secondary (pick per post): `mcp`, `voice-ai`, `llm`, `saas`, `startups`, `sales`,
`jira`, `crm`, `remote-work`, `machine-learning`, `privacy`

---

## Welcome post (pin this first)

### Title
```
Introducing Lynkk: one AI for every meeting, before, during and after
```

### Subtitle
```
Why we stopped building "just another AI notetaker" and what Lynkk does instead
```

### Tags
`ai`, `productivity`, `meetings`, `mcp`, `startups`

### Body

> Most AI notetakers show up at the wrong time. They transcribe the call and hand you a
> summary after everyone has already moved on, and you still walk into the *next* meeting
> cold, with no idea what was promised in the last one.
>
> We built Lynkk to cover the whole meeting lifecycle, not just the last part of it.
>
> ## Before the meeting: start ahead, not cold
>
> Lynkk surfaces context from your past meetings before every call: what was discussed,
> what's still open, and who said what.
>
> ## During the meeting: an assistant that can speak
>
> Lynkk joins your meeting and speaks when you need it. Ask for context from a past call,
> pull up a document, or get an answer live, by voice, without leaving the conversation.
> Meeting detection and recording happen automatically.
>
> ## After the meeting: the work, done in about 30 seconds
>
> - Structured notes
> - Action items assigned
> - CRM fields updated
> - Jira tickets created
> - Everything searchable in a knowledge graph of all your meetings
>
> ## A few things we care about
>
> - **In-person counts too.** Not every meeting has a dial-in. Lynkk records the room.
> - **Multilingual and offline-first,** so it works in whatever language the meeting
>   actually happens in, and when the Wi-Fi doesn't.
> - **You pick the region.** Every model behind Lynkk processes and answers from the
>   region you choose, which matters when legal and compliance have opinions.
> - **It connects to your stack:** calendar, Jira, Calendly, Cal.com, your CRM, or
>   anything else via MCP.
> - **Web app and Mac app,** including dictation that puts text at your cursor in any app.
>
> ## What you'll find on this blog
>
> - **Product updates:** what shipped and why.
> - **Playbooks:** running better sales calls, standups, interviews and 1:1s with AI in the room.
> - **Engineering:** live voice AI, multilingual capture, data residency, and building on MCP.
>
> Lynkk is free to start. Try it on your next meeting at [lynkk.ai](https://lynkk.ai)
> and tell us where it falls short: marketing@lynkk.ai.

---

## Starter content plan

### Content pillars
1. **Product updates:** release notes and feature deep dives.
2. **Meeting playbooks:** practical guides by role (sales, product, founders, consultants).
3. **Engineering and AI:** how the product works, written for a technical audience.
4. **Privacy and compliance:** data residency and handling meeting data responsibly.

### First 10 post ideas
1. Introducing Lynkk: one AI for every meeting, before, during and after (welcome post above)
2. Why AI notetakers show up too late, and what "before the meeting" context looks like
3. Connecting Lynkk to anything with MCP: a practical walkthrough
4. From meeting to Jira ticket in 30 seconds: how product teams use Lynkk
5. Sales call prep with past context: never ask the same discovery question twice
6. Building a voice assistant that knows when to speak in a live meeting
7. Data residency for AI: what "pick your region" means for every model behind Lynkk
8. Recording in-person meetings and interviews: tips for clean, usable notes
9. Multilingual meetings: capturing action items across languages
10. Your meetings as a knowledge graph: searching everything ever said

TODO: confirm any technical details (models, latency, architecture) with the engineering
team before publishing the engineering posts.

---

## Setup checklist

- [ ] Claim subdomain and create the publication
- [ ] Connect `blog.lynkk.ai` and confirm SSL
- [ ] Upload logo, favicon and default OG image
- [ ] Paste About, meta title and meta description
- [ ] Add navbar links and social links
- [ ] Enable the newsletter
- [ ] Invite team members as writers/editors
- [ ] Publish and pin the welcome post
- [ ] Add a "Blog" link on lynkk.ai pointing to the publication
