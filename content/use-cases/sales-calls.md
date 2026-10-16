# Updated content: lynkk.ai/use-cases/sales-calls

> Status: draft for review, 2026-10-16. Replaces the live page copy (last updated 29 September 2026).
> Keep the URL `/use-cases/sales-calls` (no redirect needed).
> Lines starting with **[EDITOR]** are instructions, not page copy. Items marked **[CONFIRM]** must be checked
> with the product team before publishing.

---

## A. SEO brief (Ubersuggest, 2026-10-16)

Ubersuggest has no ranking data for lynkk.ai yet (the domain and this page don't rank for any tracked keyword),
so this page is starting from zero.

### Keywords this page targets

| Keyword | US / mo | India / mo | CPC (US) | SD | Intent | Where it goes |
|---|---|---|---|---|---|---|
| sales call recording software | 110 | - | $108.65 | 31 | Commercial | **Primary.** Title, H1, intro |
| record sales calls | 90 | - | $36.78 | 35 | Commercial | Intro, H2 "Three ways to record" |
| sales call recording | 70 | 30 | $175.70 | 33 | Info / Commercial | Meta description, body |
| ai for sales calls | 30 | - | $74.92 | 39 | Commercial | Body |
| sales meeting notes | 30 | - | - | 38 | Informational | Sample note section |
| sales call notes | 10 | - | - | 17 | - | H2 "What you read after the call" |
| conversation intelligence software | 390 | - | $38.71 | 40 | Commercial | Comparison section, link to the existing blog post |
| ai sales assistant | 590 | - | $64.51 | 39 | Commercial | Mention once in the comparison section; the page doesn't target it |

"ai note taker for sales calls", "best ai note taker for sales", "sales call summary" and "sales call transcription"
all show **0** US volume, so the page doesn't target them directly. They still appear naturally in the copy.

### What ranks today
- **"sales call recording software":** AI Overview, then Gong, Reddit, a listicle, then Zoom, Clari, Salesloft and Avoma product pages. Product pages rank, so a strong use-case page can compete. Most of these competitors lead with CRM sync, which Lynkk doesn't have, so the page wins on no-bot recording, in-person and offline meetings, data region and price.

### Separate content to create (not on this page)
| Keyword | US / mo | India / mo | SD | Why separate |
|---|---|---|---|---|
| follow up email after sales call | **8,100** | 480 | 44 | The top 10 results are all template articles (Zendesk, Highspot, HubSpot, Mailshake, Reddit), so a product page won't rank here. |
| sales follow up email | 2,400 | - | 59 | Same intent |
| sales follow up email examples | 1,900 | - | 39 | Same intent |
| sales follow up email sample | 1,300 | - | 57 | Same intent |
| sales follow up email example | 1,000 | - | **5** | Very easy to rank for |

**[EDITOR]** Create `/blog/follow-up-email-after-sales-call` (examples and templates, about 14,700 US searches a month
across the cluster) and link it from this page's follow-up email section. Use the sample email below as example #1.

---

## B. What changed vs the live page, and why

| Change | Why (Google guidance / data) |
|---|---|
| Title and H1 now lead with "sales call recording" | That's the commercial term people search. "AI notes for sales calls" has no measurable volume. |
| New meta description | Mentions the platforms, in-person recording, outputs and the free plan |
| Added "Reviewed by" next to "Last updated" | Google: "Is it self-evident to your visitors who authored your content?" |
| New section: one sales call, before, during and after | Shows first-hand experience and covers Meeting Brief, Cue and Ask Lynkk in one realistic flow |
| New section: Proof | Use-case pages had no social proof; trust is the most important part of E-E-A-T |
| New section: Privacy and recording consent | Buyers care whether recording is allowed; data region, AES-256 and no training are strong trust signals |
| New section: honest comparison | Matches the comparison intent in the SERP; honesty about no CRM sync builds trust |
| FAQ expanded from 6 to 9 questions | Adds consent, in-person and free-plan questions people actually ask |
| Follow-up email section now links to the new blog post | Captures the 8,100/mo follow-up email intent without making this page a template page |
| Kept: sample note, sample email, capture methods, related use cases | Already strong, original and specific |

---

## C. Page metadata

| Element | New value | Live value |
|---|---|---|
| Title tag | `Sales Call Recording Software with AI Notes \| Lynkk` | AI Notes for Sales Calls: Next Steps and Owners \| Lynkk |
| Meta description | `Record sales calls on Zoom, Google Meet, Teams or in person. Lynkk writes the note: next steps with owners and dates, decisions and open questions. Start free.` | Record sales calls on Zoom, Google Meet or Teams and Lynkk writes the note: next steps with owners and due dates, the decisions and the open questions. |
| H1 | Record sales calls and get AI notes with the next steps already written down. | AI notes for sales calls, with the next steps already written down. |
| URL | `/use-cases/sales-calls` (unchanged) | |
| Breadcrumb | Home > Use cases > Sales calls (unchanged) | |

**[EDITOR] Structured data:**
- Update `WebPage.name`, `headline` and `description` to the new values, and set `dateModified` to the publish date. Optionally add `reviewedBy` (Person).
- Keep `BreadcrumbList` and `FAQPage`, adding the 3 new questions. FAQ markup gives no rich result now, but it's harmless and matches the visible text.
- `SoftwareApplication` currently has no `aggregateRating` or `review`, which Google requires for an app rich result. Either add ratings that are visible on this page and come from real users, or accept that it won't show stars. Don't copy the F6S score into the markup unless it's shown on the page.
- If you add a demo video, add `VideoObject`.

---

## D. Page copy

### Hero

Use case · Sales calls

# Record sales calls and get AI notes with the next steps already written down.

On a sales call you are selling, listening and taking notes at once. Lynkk records the call, on Zoom, Google Meet,
Microsoft Teams or in the room, and gives you back the next steps with owners and dates, the decisions and the open
questions, each linked to the moment it was said.

[Start for free] [Download for Mac]

Zoom, Google Meet, Microsoft Teams and in-person meetings · Last updated [publish date] · Reviewed by [Name, role] **[CONFIRM name]**

*(Keep the existing Meeting Brief mock card: "Acme pricing call · Zoom · 32 min · Maya, Dev, Dana from Acme".)*

**[EDITOR]** If the mock card is an image, add alt text: "Lynkk Meeting Brief for a sales call showing two next
steps with owners and due dates, a decision and an open question."

---

### The guide

## Why next steps slip after a sales call, and how Lynkk keeps them.

Every note starts as a [Meeting Brief](/features/meeting-notes). Here is how it fits a sales call.

### The problem

Next steps are the first thing to slip after a sales call. You were selling and listening at the same time, so the
notes are thin, the promise about a quote is half remembered, and the follow-up waits until the evening. A week later,
nobody is sure who said they would send what, or what the buyer actually asked about pricing.

### How Lynkk helps

When a Zoom, Teams, Webex or Google Meet call starts, the [Mac app](/download) notices it and offers to record, so
nobody new joins the call. If you would rather send a bot, the meeting bot joins from a pasted link or from your calendar.

After the call, the note lists the next steps with an owner, a due date and a priority, the decisions and the questions
still open. Every timestamp plays the recording from that moment, so you can hear exactly how the buyer put it. When you
are ready, send the action items to Jira from the note.

On Pro, the Sales Call shape rewrites the same meeting for a sales call, and [Ask Lynkk](/features/ask-your-meetings)
answers questions like "What did Acme say about pricing?" across every call with that account, with citations that open
the moment it was said.

---

### One deal, three meetings *(NEW)*

## One sales call with Lynkk, before, during and after.

Here is how a rep, Maya, uses Lynkk across one deal with Acme.

### Before the call: start ahead, not cold

Ten minutes before the second call with Acme, Maya asks Ask Lynkk: "What is still open with Acme?" The answer lists the
open question from the first call, who signs the annual order, and links to the exact moment Dana raised it. She opens
the call knowing what to ask first.

### During the call: an answer without breaking eye contact

Dana asks what was agreed about the pilot size last time. Instead of scrolling through old notes, Maya gets the answer
from Cue during the call, on Pro: "Start with a pilot for two teams, agreed at 14:22 on the first call." **[CONFIRM
how Cue is triggered and shown, and adjust this sentence]**

### After the call: the note is already written

By the time Maya is back in her inbox, the note is ready: three next steps with owners and due dates, the decision, and
the open question. She writes the follow-up email straight from the note, then sends the action items to Jira so the
security review isn't forgotten.

**[EDITOR]** Add one real screenshot per step (Ask Lynkk answer, Cue during a call, finished note) with descriptive alt
text, or one 30-60 second screen recording of the whole flow.

---

### What the note gives you

## What you read after the sales call.

The sample at the top of the page is one of these notes. Every timestamp in it plays the recording from that moment.

**01 Next steps**: Each action item has an owner, a due date and a priority, and lands on the Tasks board.

**02 Decisions**: What was agreed on the call, with the context around it.

**03 Open questions**: What the buyer still needs answered before the next call.

**04 Key takeaways**: The points that mattered, each with the time it was said. One click plays it back.

**05 The transcript**: Every word of the call, with speaker labels.

**06 Send to Jira**: Create one Jira issue per action item from the note, in the project you pick.

---

### Example

## Sample sales call note

An example of the note Lynkk writes after a sales call, not from a real meeting. If you are weighing up
[conversation intelligence software](/blog/sales-conversation-intelligence), this is what one call turns into.

**Next steps**
- Send the revised quote to Dana. Owner: Maya. Due: Fri 2 Oct.
- Book the security review. Owner: Dev. Due: Tue 6 Oct.
- Share the pilot plan for two teams. Owner: Maya. Due: Fri 9 Oct.

**Decisions**
Start with a pilot for two teams. Agreed at 14:22.

**Open questions**
Who signs the annual order on Acme's side? Raised at 21:37.

**Key takeaways**
08:12 Pricing is the main question for Acme. 17:50 They want two teams on it before a wider rollout.

**The transcript**
Every word of the 32 minute call, with speaker labels for Maya, Dev and Dana.

**Send to Jira**
3 action items, one Jira issue each, when you choose to send them.

---

### Example

## Sample follow-up email after a sales call

A follow-up written from the sample note above. It's an example, not a template Lynkk sends for you. Every fact in it,
from the dates to the owners to the open question, comes straight from the note. For more examples, see our guide to
[writing a follow-up email after a sales call](/blog/follow-up-email-after-sales-call). **[EDITOR] Link once the post is live.**

> **Subject:** Acme pilot, next steps
>
> Hi Dana,
>
> Thanks for your time today. We agreed to start with a pilot for two teams. On our side, I will send the revised quote
> by Friday 2 October and the pilot plan by Friday 9 October, and Dev will book the security review for Tuesday 6 October.
>
> One question is still open: who signs the annual order on your side? Let me know when you can.
>
> Best,
> Maya

---

### In the room

## Record in-person and offline sales meetings

Not every sales meeting is a call. When you meet a buyer in person, record the room with the Mac app through its
microphone, or from the [web app](/web-app) in your browser.

It works with no signal too. The recording is saved on the Mac and uploads once you are back online, and the note follows,
with the same next steps, decisions and open questions as a call. Lynkk transcribes 17 languages, plus Hinglish, so a
meeting that switches between Hindi and English still ends in one clear note. Each recording can run up to 2 hours.

---

### How to capture it

## Three ways to record sales calls.

Every recording can run up to 2 hours, and every way ends in the same note.

### Mac app
Offers to record when a Zoom, Teams, Webex or Google Meet call starts. It records from your Mac, so nothing joins the call.
[Download Lynkk for Mac](/download)

### Meeting bot
Joins Google Meet, Zoom and Teams links. Turn on calendar auto-join and it goes to the calls on your calendar.
[How Lynkk meeting notes work](/features/meeting-notes)

### Chrome extension
Records a Google Meet, Zoom or Teams call running in a Chrome tab, from that tab.
[The Lynkk Chrome extension](/features/chrome-extension)

---

### Proof *(NEW)*

## What sales teams say about Lynkk

**[EDITOR]** Add one real quote from someone who uses Lynkk for sales or customer calls: name, role, company, photo,
and one specific result (for example "I send follow-ups the same hour now"). Only reuse a homepage testimonial if that
person actually uses Lynkk for sales calls. If no sales quote exists yet, leave this section out rather than invent one.

> "[Real quote about using Lynkk on sales calls]"
> [Name], [Role], [Company]

Trusted by teams at Microsoft, Groww, Wissen Technology, EXL Service and Home Credit Indonesia.
**[CONFIRM permission to show logos on use-case pages]**

---

### Privacy *(NEW)*

## Recording sales calls, privately and with consent

Buyers share pricing, budgets and plans on sales calls, so the recording has to be handled carefully.

- **Private by default.** Notes are yours until you share them, and share links can be revoked.
- **Encrypted.** AES-256 in transit and at rest.
- **Your data region.** Pin your workspace's AI models to the US, the EU, the UK, India, Singapore or Australia.
- **Retention you control.** Keep audio forever, delete it after 90 or 30 days, or wipe it after upload.
- **Never used for training.** Your conversations are not used to train models.
- **Consent built in.** Lynkk includes a consent flow for recording calls with more than one person. **[CONFIRM how it works]**

[How Lynkk handles security](/security)

---

### Compare *(NEW)*

## Lynkk vs typing notes vs revenue platforms

| | Typing notes yourself | Lynkk | Revenue platforms |
|---|---|---|---|
| Built for | Any meeting | Notes, next steps and memory across calls | Pipeline, coaching and forecasting |
| Bot in the call | No | Optional: record from your Mac or a Chrome tab | Usually |
| In-person and offline meetings | Yes, by hand | Yes, Mac app and web app, uploads later | Varies |
| Next steps with owners and dates | If you remember | Automatic, with timestamps | Yes |
| CRM sync | Manual | No (send action items to Jira instead) | Yes, usually the core feature |
| Data region choice | n/a | 6 regions | Varies by vendor |
| Price to start | Free | Free plan; Pro $15/month | Usually sales-led pricing |

**If CRM sync, deal scoring and forecasting are what you need, a full revenue platform fits better. If you want every sales
conversation written down, searchable and turned into next steps, online or in the room, Lynkk is built for that.**

See how Lynkk compares with [Otter.ai](/compare/otter), [Fireflies.ai](/compare/fireflies), [Granola](/compare/granola)
and [Fathom](/compare/fathom).

**[EDITOR]** Check the "Revenue platforms" column with the team before publishing. Keep it general (no named
competitor claims) unless each claim is verified.

---

### Questions

## Questions about recording sales calls with Lynkk

The short answers. For plans and what they include, see [pricing](/pricing).

**Can Lynkk record a sales call without a bot joining?**
Yes. The Mac app and the Chrome extension record from your own computer, so nothing new appears in the call. The meeting
bot is there if you want it: paste a meeting link, or turn on calendar auto-join.

**Do I need to tell the buyer I'm recording the call?**
Recording laws differ by country and by state, and many require everyone on the call to agree. The safest habit is to
tell the buyer at the start and record only with their agreement. Lynkk includes a consent flow for multi-party
recording. **[CONFIRM wording with legal]**

**Can I record an in-person sales meeting?**
Yes. Record the room with the Mac app or the web app. With no signal, the Mac app saves the recording and uploads it when
you're back online, and the note follows.

**Does Lynkk sync with my CRM?**
No. Lynkk does not connect to a CRM. From a note you can send action items to Jira, and you can share the note with a link.

**Can I send next steps to Jira?**
Yes, by hand. From a note, choose Send and Lynkk creates one Jira issue per action item in the project you pick. It does
not sync on its own.

**What is the Sales Call shape?**
Summary Shapes rewrite a note for one kind of meeting. Sales Call is one of them, alongside Daily Stand-up, Customer
Interview, 1:1 and others. Summary Shapes are part of Pro. Without them, the note is a Meeting Brief.

**Can I ask questions across every call with one account?**
On Pro, yes. Ask Lynkk answers from your own notes, for example "What did Acme say about pricing?", and each answer cites
the notes it came from and opens the moment it was said.

**Is Lynkk free for sales calls?**
Yes, there is a free plan with AI summaries and action items, no credit card required. Pro is $15 a month and adds
unlimited notes, the Sales Call shape and Ask Lynkk across calls. **[CONFIRM free plan limit: the site currently says
both "5 notes a month, up to 2 hours each" and "5 hours of AI summaries"]**

**How long can a sales call recording be?**
Up to 2 hours per recording, on every plan and every way of recording.

---

### More use cases

## Other conversations people record with Lynkk.

*(Keep the existing five cards: Standup notes, User interview notes, Lecture notes, Notes from a doctor visit, Field
interview notes. Add new use-case pages here as they go live.)*

[All use cases](/use-cases)

---

### From the blog

## Related guides

- [How Sales Teams Use Conversation Intelligence to Prepare, Follow Up and Close More Deals](/blog/sales-conversation-intelligence)
- [How to write a follow-up email after a sales call, with examples](/blog/follow-up-email-after-sales-call) **[EDITOR] new post**
- [The Best AI Note Takers in the US for 2026, Compared Online and In Person](/blog/best-ai-note-takers)
- [Top Zoom AI Companion Alternatives for 2026, Compared on Price, Features and Follow-Up](/blog/zoom-ai-companion-alternatives)

---

### Closing CTA

## Record your next sales call. Read the next steps after.

Download the Mac app and it offers to record when the call starts, or send the meeting bot from your calendar.

[Start for free] [Download for Mac]

Free plan, no credit card required · [Compare plans](/pricing)

---

## E. Before publishing (checklist)

- [ ] Confirm: Cue wording, consent flow, free plan limit, reviewer name, logo permission
- [ ] Add a real sales testimonial, or remove the Proof quote block
- [ ] Add screenshots or a short video, with alt text
- [ ] Update title, meta description, H1 and the `WebPage` / `FAQPage` JSON-LD
- [ ] Publish `/blog/follow-up-email-after-sales-call`, then switch on both links
- [ ] Request indexing in Search Console after publishing
