# Sales Calls Use-Case Page (v2): Keywords, Design and Copy

> Page: lynkk.ai/use-cases/sales-calls (keep this URL). Draft v2, 2026-10-16. Replaces v1, which targeted keywords
> that were too small. Lines starting with **[EDITOR]** are instructions, not page copy. **[CONFIRM]** items must be
> checked with the product team before publishing.

---

## 1. Keyword strategy (Ubersuggest, 2026-10-16)

v1 targeted "sales call recording software" (110/mo). v2 targets the bigger sales cluster that still matches what
Lynkk does: AI for sales calls, conversation intelligence, and an AI sales assistant. The cluster below totals
**about 9,500 US searches a month**.

| Keyword | US / mo | India / mo | CPC (US) | SD | Intent | Role on page |
|---|---|---|---|---|---|---|
| ai for sales | 2,900 | 590 | $25.81 | 58 | Commercial | **Primary**: title, H1, intro |
| conversation intelligence | 1,900 | 260 | $18.00 | 60 | Commercial | **Secondary**: title, H2 |
| ai sales tools | 1,000 | - | $52.60 | 47 | Commercial | H2 (comparison), body |
| conversation intelligence platform | 880 | - | $43.16 | 37 | Commercial | H2 (features), meta description |
| sales call | 880 | - | $168.70 | 42 | Navigational | H1, body |
| ai sales assistant | 590 | 140 | $64.51 | 39 | Commercial | H2 (how it works), meta description |
| call recording software | 480 | - | $56.76 | 64 | Commercial | Body (record sales calls) |
| conversation intelligence software | 390 | - | $38.71 | 40 | Commercial | FAQ |
| ai tools for sales | 260 | - | $46.36 | 46 | Commercial | Body |
| sales call recording software | 110 | - | $108.65 | 31 | Commercial | Body |
| record sales calls | 90 | - | $36.78 | 35 | Commercial | Body |

**Why these are realistic for Lynkk:** the homepage title is already "AI Meeting Notes & Conversation Intelligence",
the product records and summarises sales calls, and Cue plus Ask Lynkk work as an AI sales assistant. The page should
**not** chase "ai crm" (2,400/mo), because Lynkk has no CRM sync.

**Avoid cannibalisation:** the blog post `/blog/sales-conversation-intelligence` is an informational guide. Keep it
targeting "how sales teams use conversation intelligence", link it from this page, and let this page own the commercial
terms ("conversation intelligence platform", "ai sales tools").

### Biggest opportunity: a separate blog post

| Keyword | US / mo | India / mo | SD |
|---|---|---|---|
| follow up email after sales call | **8,100** | 480 | 44 |
| sales follow up email | 2,400 | - | 59 |
| sales follow up email examples | 1,900 | - | 39 |
| sales follow up email sample | 1,300 | - | 57 |
| sales follow up email example | 1,000 | - | **5** |

The top 10 results are all template articles (Zendesk, HubSpot, Highspot), so this cluster (about 14,700 US searches a
month) needs its own post: `/blog/follow-up-email-after-sales-call`. This page shows one sample email and links to it.

### Keyword placement map

| Place | Text |
|---|---|
| Title tag | AI for Sales Calls: Conversation Intelligence & Notes \| Lynkk |
| Meta description | Lynkk is the AI sales assistant and conversation intelligence platform that records sales calls on Zoom, Meet, Teams or in person and writes the next steps. Start free. |
| H1 | AI for sales calls: record every call, get the next steps written for you. |
| First sentence | ...Lynkk is **AI for sales** teams that... |
| H2 #1 | How Lynkk works as your **AI sales assistant** |
| H2 #3 | **Conversation intelligence** for every sales call |
| H2 #4 | Lynkk vs other **AI sales tools** |
| FAQ | Is Lynkk **conversation intelligence software**? |

Use each phrase naturally, once or twice. Don't repeat them in every paragraph.

---

## 2. Page design (short and simple)

**9 blocks, about 900 words, one scroll on desktop for the first three blocks.** One column of content, centred,
max width about 1,100px. White background, one brand colour for buttons, light grey cards. Mobile: every multi-column
row stacks into one column.

```wire
# 1. HERO
Eyebrow: Use case · Sales calls / H1 (2 lines) / Subheading (2 lines) / [Start for free] [Download for Mac] / Small text: Zoom · Meet · Teams · in person || PRODUCT CARD / Meeting Brief: Acme pricing call / Next steps with owners / Decision / Open question
# 2. LOGO STRIP
Trusted by teams at: Microsoft · Groww · Wissen · EXL · Home Credit [CONFIRM]
# 3. HOW IT WORKS (3 columns)
BEFORE / icon / "Start ahead" / 2 lines || DURING / icon / "Answers in the call" / 2 lines || AFTER / icon / "Note is written" / 2 lines
# 4. SAMPLE NOTE + EMAIL (2 columns)
SAMPLE NOTE / Next steps / Decision / Open question / Takeaways || SAMPLE FOLLOW-UP EMAIL / Subject + 5 lines / Link: more follow-up examples
# 5. FEATURES (3 x 2 grid of cards)
Next steps with owners || Decisions and open questions || Ask Lynkk across calls
Record in person, offline || No bot needed || Send to Jira
# 6. COMPARISON (small table, 5 rows)
Criteria || Lynkk || Revenue platforms
# 7. PRIVACY STRIP (4 badges in one row)
Your data region || AES-256 encryption || Never used for training || Consent flow
# 8. FAQ (accordion, 6 questions)
Question 1 (closed) / Question 2 (closed) / ...
# 9. FINAL CTA (full-width band)
H2 one line / [Start for free] [Download for Mac] / Free plan, no credit card
```

**[EDITOR] Design notes**
- Hero product card: use the existing Meeting Brief mock. If it's an image, alt text: "Lynkk Meeting Brief for a sales call with next steps, owners, due dates, a decision and an open question."
- Keep the sample note and the email as real HTML text (not images), so Google and AI Overviews can read them.
- Icons in block 3 and 5: simple line icons, same style as the rest of the site.
- Footer area under block 9: keep the existing "More use cases" and "Related guides" links as a compact two-column link list.

---

## 3. Page metadata

| Element | Value |
|---|---|
| URL | `/use-cases/sales-calls` (unchanged) |
| Title tag | `AI for Sales Calls: Conversation Intelligence & Notes \| Lynkk` |
| Meta description | `Lynkk is the AI sales assistant and conversation intelligence platform that records sales calls on Zoom, Meet, Teams or in person and writes the next steps. Start free.` |
| H1 | AI for sales calls: record every call, get the next steps written for you. |
| Byline | Last updated [publish date] · Reviewed by [Name, role] **[CONFIRM]** |

**[EDITOR] Structured data:** update `WebPage` name, headline, description and `dateModified`. Keep `BreadcrumbList`.
Replace the `FAQPage` questions with the 6 below. `SoftwareApplication` needs real, on-page `aggregateRating` or
`review` to show stars; otherwise it shows no rich result.

---

## 4. Page copy

### Block 1. Hero

Use case · Sales calls

# AI for sales calls: record every call, get the next steps written for you.

Lynkk is AI for sales teams that would rather sell than type. It records your sales call on Zoom, Google Meet,
Microsoft Teams or in the room, then writes the next steps with owners and dates, the decisions and the open questions,
each linked to the moment it was said.

[Start for free] [Download for Mac]

Zoom · Google Meet · Microsoft Teams · In person · No bot needed

### Block 2. Logo strip

Trusted by teams at Microsoft, Groww, Wissen Technology, EXL Service and Home Credit Indonesia. **[CONFIRM permission]**

### Block 3. How it works

## How Lynkk works as your AI sales assistant

**Before the call: start ahead.**
Ask Lynkk "What's still open with Acme?" and get the open questions from every past call, with links to the moment
they were raised.

**During the call: answers in the call.**
Cue answers questions during the call, like what was agreed on pricing last time, so you don't scroll through old
notes. **[CONFIRM Cue wording]**

**After the call: the note is written.**
Next steps with owners, due dates and priority, the decisions and the open questions, ready before you're back in
your inbox.

*Ask Lynkk, Cue and the Sales Call note shape are part of Pro.*

### Block 4. Sample note and follow-up email

## See what one sales call turns into

*An example, not from a real meeting.*

**Sample note: Acme pricing call · Zoom · 32 min**

**Next steps**
- Send the revised quote to Dana. Owner: Maya. Due: Fri 2 Oct.
- Book the security review. Owner: Dev. Due: Tue 6 Oct.
- Share the pilot plan for two teams. Owner: Maya. Due: Fri 9 Oct.

**Decision:** Start with a pilot for two teams. Agreed at 14:22.

**Open question:** Who signs the annual order on Acme's side? Raised at 21:37.

**Key takeaways:** 08:12 Pricing is the main question for Acme. 17:50 They want two teams on it before a wider rollout.

**Sample follow-up email, written from the note**

> **Subject:** Acme pilot, next steps
>
> Hi Dana, thanks for your time today. We agreed to start with a pilot for two teams. I'll send the revised quote by
> Friday 2 October and the pilot plan by Friday 9 October, and Dev will book the security review for Tuesday 6 October.
>
> One question is still open: who signs the annual order on your side?
>
> Best, Maya

[More examples of a follow-up email after a sales call](/blog/follow-up-email-after-sales-call) **[EDITOR] link once the post is live**

### Block 5. Features

## Conversation intelligence for every sales call

**Next steps with owners**
Every action item gets an owner, a due date and a priority, and lands on the Tasks board.

**Decisions and open questions**
What was agreed and what the buyer still needs, each with a timestamp that plays the moment back.

**Ask Lynkk across calls**
"What did Acme say about pricing?" Answers come from every call with that account, with citations.

**Record in person, even offline**
Record the room with the Mac app or web app. No signal? It uploads later. 17 languages, plus Hinglish.

**No bot needed**
The Mac app and Chrome extension record from your computer. Prefer a bot? It joins from your calendar.

**Send to Jira**
Turn action items into Jira issues, one per item, in the project you pick.

### Block 6. Comparison

## Lynkk vs other AI sales tools

| | Lynkk | Revenue platforms |
|---|---|---|
| Best for | Notes, next steps and memory across calls | Pipeline, coaching and forecasting |
| Bot in the call | Optional | Usually |
| In-person and offline meetings | Yes | Varies |
| CRM sync | No (send action items to Jira) | Yes |
| Price to start | Free plan; Pro $15/month | Usually sales-led |

Need CRM sync and forecasting? A revenue platform fits better. Want every sales call written down and turned into next
steps, online or in the room? That's Lynkk. See [Lynkk vs Fireflies.ai](/compare/fireflies) and
[Lynkk vs Fathom](/compare/fathom).

**[EDITOR]** Check the "Revenue platforms" column with the team. Keep it general unless each claim is verified.

### Block 7. Privacy strip

**Your data region**: US, EU, UK, India, Singapore or Australia.
**AES-256 encryption**: in transit and at rest.
**Never used for training**: your calls stay yours.
**Consent flow**: for recording calls with more than one person. **[CONFIRM]**

[How Lynkk handles security](/security)

### Block 8. FAQ

## Questions about AI for sales calls

**Can Lynkk record a sales call without a bot joining?**
Yes. The Mac app and the Chrome extension record from your own computer, so nothing new appears in the call. The
meeting bot is there if you want it.

**Is Lynkk conversation intelligence software?**
Yes, for the conversation itself: it records sales calls, writes the next steps, decisions and open questions, and lets
you ask questions across every call. It doesn't do CRM sync, deal scoring or forecasting.

**Does Lynkk sync with my CRM?**
No. You can send action items to Jira and share any note with a link.

**Can I record an in-person sales meeting?**
Yes, with the Mac app or the web app. With no signal, the Mac app saves the recording and uploads it later.

**Do I need to tell the buyer I'm recording?**
Recording laws differ by country and state, and many require everyone's agreement. Tell the buyer at the start and record
only with their agreement. **[CONFIRM wording with legal]**

**Is it free?**
Yes, there's a free plan, no credit card required. Pro is $15 a month and adds unlimited notes, the Sales Call shape,
Cue and Ask Lynkk. **[CONFIRM free plan limit; the site currently gives three different versions]**

### Block 9. Final CTA

## Record your next sales call. Read the next steps after.

[Start for free] [Download for Mac]

Free plan, no credit card required · [Compare plans](/pricing)

*Below the CTA (compact links):* More use cases: [Standups](/use-cases/team-standups) ·
[User interviews](/use-cases/user-interviews) · [Field interviews](/use-cases/field-interviews) · [All use cases](/use-cases).
Guides: [How sales teams use conversation intelligence](/blog/sales-conversation-intelligence) ·
[Best AI note takers](/blog/best-ai-note-takers).

---

## 5. Before publishing

- [ ] Confirm: Cue wording, consent flow, free plan limit, reviewer name, logo permission, "Pro adds Cue"
- [ ] Update title, meta description, H1 and the `WebPage` / `FAQPage` structured data
- [ ] Keep the sample note and email as HTML text
- [ ] Publish `/blog/follow-up-email-after-sales-call` and switch on the link
- [ ] Request indexing in Search Console after publishing
