# Lynkk: page optimizations (October 2026)

Implementation brief for the existing lynkk.ai pages, based on `seo/2026-10-seo-analysis.md`.
Everything below is ready to paste. Copy only uses facts already published on lynkk.ai
(pricing page, feature pages, integration pages). Items marked **Confirm** need a team check
before going live.

Keyword data: Ubersuggest, US, monthly searches. SD = SEO difficulty (0 to 100).

## Priority order

| # | Page | Main change | Target keyword (volume, SD) | Effort |
|---|---|---|---|---|
| 1 | Sitewide | Internal links to integration pages, FAQ schema, language count | n/a | 1 to 2 h |
| 2 | 5 compare pages | Keyword-first titles, one new FAQ each | plaud alternative (320, 10), granola alternative (320, 28), otter ai alternative (480, 34) | 1 h |
| 3 | Homepage | Keyword H1 and H2s, plain-language block, `data-nosnippet` on demo UI | ai note taker (27,100, 48), ai meeting assistant (4,400, 60) | 3 to 4 h |
| 4 | /integrations/microsoft-teams + Teams blog post | Split intent, cross-link | ai note taker for teams (590, 29) | 1 h |
| 5 | /integrations/google-meet + Google Meet posts | Cross-link, free FAQ | ai note taker for google meet (210, 39), google meet transcript (1,000, 53) | 1 h |
| 6 | /features/chrome-extension | Say "Chrome extension" in title and H2 | otter/read ai chrome extension demand | 30 min |
| 7 | /features/meeting-notes | Add "meeting minutes generator" section | ai meeting minutes generator (140, 30) | 1 h |
| 8 | List posts (best, best free, Otter alternatives) | Links, FAQ schema | already ranking for AI features | 1 h |

---

## 1. Sitewide fixes

### 1a. Link to the integration pages from body copy

`/integrations/microsoft-teams` and `/integrations/google-meet` are the best commercial pages
for "AI note taker for Teams / Google Meet", but no blog, compare or feature page links to them
inside the article body (only menus do). Links from body text pass far more weight.

| From | Add link to | Anchor text | Where |
|---|---|---|---|
| /blog/ai-note-taker-microsoft-teams | /integrations/microsoft-teams | AI note taker for Microsoft Teams | Section "1. Lynkk (our product)", first paragraph |
| /blog/best-ai-note-takers | /integrations/microsoft-teams | Lynkk for Microsoft Teams | FAQ "Does Microsoft Teams have an AI note taker?" |
| /blog/best-ai-note-takers | /integrations/google-meet | Lynkk for Google Meet | FAQ "Does Google Meet have an AI note taker?" |
| /blog/best-free-ai-note-takers | /integrations/microsoft-teams, /integrations/google-meet, /integrations/zoom | Teams, Google Meet, Zoom | Section "Which free AI note taker is best for Zoom, Teams and Google Meet?" |
| /blog/google-meet-transcript | /integrations/google-meet | AI note taker for Google Meet | Section "What is the best AI note taker for Google Meet?" |
| /blog/google-meet-transcript | /blog/google-meet-ai-note-taker | Google Meet note takers for Hindi and Hinglish teams | Same section, last sentence |
| /features/hinglish-transcription | /blog/google-meet-ai-note-taker | Hinglish notes in Google Meet | Body |
| /blog/best-ai-note-takers | /compare/plaud | a Plaud alternative with no device | Section "Can an AI note taker record in-person meetings?" |
| /blog/best-ai-note-takers | /use-cases/field-interviews | record field interviews offline | Same section |
| Homepage | /integrations/zoom, /integrations/google-meet, /integrations/microsoft-teams | Zoom, Google Meet, Microsoft Teams | Integrations section (see 3e) |
| Homepage | /features/chrome-extension, /features/meeting-bot | Chrome extension, meeting bot | "Capture" step of the workflow section |

`/blog/google-meet-ai-note-taker` (the India post) currently has no body links pointing to it
from any of the pages checked. The two links above fix that.

### 1b. Add FAQPage structured data where the FAQ is visible but unmarked

These posts have a visible FAQ section but no `FAQPage` JSON-LD (every other post has it):

- /blog/otter-ai-alternatives
- /blog/google-meet-ai-note-taker

Use the same component the other posts use. Questions and answers in the JSON-LD must match the
visible text word for word.

### 1c. Use one language count everywhere (Confirm)

The homepage body says "15+ languages". The homepage meta description and /features/meeting-bot
say "17 languages". Pick the true number and use it everywhere, including structured data. This
brief uses "17 languages".

### 1d. Check the homepage AggregateRating (Confirm)

The homepage JSON-LD has `AggregateRating` 5.0 from 16 reviews. Google only allows this if the
reviews are real and shown on the page (or clearly sourced, for example a G2 or Product Hunt
profile). If they are not visible, remove the `aggregateRating` block. A rating Google considers
misleading can cause a manual action against the whole site.

### 1e. Refresh `dateModified` when a post changes

Every post below that gets edited should get a new `dateModified` and a visible "Updated" date.
AI features favour fresh pages, and these posts were all published in early October.

---

## 2. Compare pages

All five are strong pages (comparison table with `<thead>`, FAQ schema, updated 2026-10-22).
The only gap: the title, which carries the most weight, never says "alternative".

### Titles and meta descriptions

| Page | New title | Chars |
|---|---|---|
| /compare/plaud | `Plaud Alternative With No Device: Lynkk vs Plaud \| Lynkk` | 56 |
| /compare/granola | `Granola Alternative for In-Person Meetings \| Lynkk` | 50 |
| /compare/otter | `Otter.ai Alternative: Lynkk vs Otter Compared \| Lynkk` | 53 |
| /compare/read-ai | `Read AI Alternative Without Scores: Lynkk vs Read AI \| Lynkk` | 60 |
| /compare/fireflies | `Fireflies Alternative: Lynkk vs Fireflies.ai \| Lynkk` | 52 |

The current meta descriptions already open with "Looking for a ... alternative?". Keep them.

### One new FAQ per page (add to the visible FAQ and the FAQPage JSON-LD)

**/compare/plaud**

> **Do I need an AI wearable or recorder to take notes in person?**
> No. Lynkk records in-person meetings from the Mac app you already have open, so there is no
> pendant, recorder or second device to buy, charge or carry. The same account also records
> Zoom, Google Meet and Teams calls, so notes from the room and from the call end up in one
> place.

**/compare/granola**

> **What is the best Granola alternative for in-person meetings?**
> Lynkk records the room as well as the call. The Mac app captures in-person meetings, a meeting
> bot or the Chrome extension captures Zoom, Google Meet and Teams, and every note comes back
> with a summary, decisions and action items. It handles Hindi, Hinglish and 17 languages in
> total, and the free plan includes the Mac app, the Chrome extension and the web app.

**/compare/otter**

> **What is the best free Otter.ai alternative?**
> Lynkk's free plan records unlimited meetings of up to 2 hours each, includes your first
> 5 hours of AI summaries, and works with Zoom, Google Meet, Teams and in-person meetings. Pro is
> $15 a month and removes the summary limit.

**/compare/read-ai**

> **Is there a Read AI alternative without meeting scores?**
> Yes. Lynkk writes the notes, decisions and action items, and lets you ask questions across
> your meetings, without scoring the people in them.

**/compare/fireflies**

> **Is there a Fireflies alternative that works without a bot?**
> Yes. Lynkk's Chrome extension records Google Meet, Zoom and Teams from your own browser tab, so
> nothing joins the call. When a bot is welcome, Lynkk has one too.

---

## 3. Homepage

The page is technically sound, but Google reads mostly demo content: "Corvane" appears 54
times, "Priya" 29, while "meeting assistant", "note taker" and "transcription" appear 0 times.

### 3a. Title and meta description

| | Current | New |
|---|---|---|
| Title | Lynkk: AI Meeting Notes & Conversation Intelligence | `Lynkk: AI Meeting Assistant & Note Taker for Sales Teams` (56) |
| Meta | Lynkk turns every meeting, online or in person, into structured, searchable notes, action items and answers. 17 languages. Start free. | `Lynkk is the AI meeting assistant that takes notes on Zoom, Meet, Teams and in person, then drafts your follow-ups. 17 languages. Start free.` (141) |

"Conversation intelligence" searches are mostly about a book, HubSpot, Twilio and Salesforce,
so it is a weak head term for the title. It stays in the body (see 3c).

### 3b. H1

Keep the revenue line as the big visual headline, but move it out of the `<h1>` and make the
`<h1>` the category statement, styled as the eyebrow or the subline:

```html
<p class="hero-display">Your revenue lives in your conversations. Don't lose it.</p>
<h1 class="hero-sub">The AI meeting assistant that remembers every sales conversation</h1>
```

If design wants the revenue line to stay the `<h1>`, the fallback is to put the category line
in a `<p>` directly under it. That helps, but less.

### 3c. H2s: put the plain topic in the heading, keep the clever line as display text

Same pattern for every section: the `<h2>` names the topic, the current line stays as the large
styled text.

| Current `<h2>` (keep as display text) | New `<h2>` |
|---|---|
| The deal didn't go cold. The context did. | Meeting prep with context from every past call |
| Good conversations deserve great follow-through. | AI meeting notes, action items and follow-ups |
| While you're talking, it's connecting the dots. | A live AI assistant during the call |
| It's listened. Now let it help. | Follow-up emails, tasks and Jira tickets from every call |
| A shared memory. A personal advantage. | Conversation intelligence for sales reps, leaders and RevOps |
| Same calendar. A very different day. | A day with an AI meeting assistant |
| Your tools. Now in the loop. | Integrations: Zoom, Google Meet, Microsoft Teams, Slack and Jira |
| Real conversations. Real-world selling. | Online and in-person meetings, in 17 languages including Hinglish |
| Start free. Upgrade when you're hooked. | Pricing: a free AI note taker, Pro at $15 a month |
| A little context. A better sales day. | Guides for sales meetings |
| Let's clear things up. | AI meeting assistant FAQ |

### 3d. Add a plain-language "What is Lynkk?" block

Place it right after the hero or before the FAQ. About 170 words. Visible text, not hidden.

> **What is Lynkk?**
>
> Lynkk is an AI meeting assistant and AI note taker for sales teams. It records your Zoom,
> Google Meet and Microsoft Teams calls with a meeting bot, from the Chrome extension with no
> bot, or from the Mac app, and it records in-person meetings and customer visits too. When the
> call ends, Lynkk writes the meeting notes: a summary, decisions, action items and a full
> transcript with speaker names. It understands 17 languages, including Hindi and the Hinglish
> in between, and keeps working offline.
>
> Every conversation joins one searchable meeting memory. Before your next call, ask Lynkk what
> was promised last time. During the call, Cue answers questions on screen. After it, Lynkk
> drafts the follow-up email, and sends tasks to Jira and answers to Slack.
>
> The free plan records unlimited meetings of up to 2 hours each and includes your first
> 5 hours of AI summaries. Pro is $15 a month.

**Confirm:** "keeps working offline" (from the homepage "Even offline" line) and Cue's
availability (homepage says "In beta in the Mac app, by invite"; if so, add "in beta").

### 3e. Integrations section: link out

In the "Your tools. Now in the loop." section, make the Zoom, Google Meet and Microsoft Teams
logos or labels link to `/integrations/zoom`, `/integrations/google-meet` and
`/integrations/microsoft-teams`, and Jira to `/integrations/jira`. In the "Capture" step, link
"Chrome extension" to `/features/chrome-extension` and "meeting bot" to `/features/meeting-bot`.

### 3f. Keep demo content out of snippets

Wrap each mock product UI block (the Corvane, Priya and Kelso screens) so Google cannot quote
it in a snippet or AI Overview. This is a supported Google attribute, not hidden text:

```html
<div class="demo-window" data-nosnippet>
  <!-- mock call UI, illustrative names -->
</div>
```

Do not hide these blocks with CSS or remove them for crawlers. The goal is that the real copy
in 3c and 3d outweighs them.

### 3g. Two new homepage FAQs (visible and in FAQPage JSON-LD)

> **Is Lynkk an AI note taker?**
> Yes, and more. Lynkk takes notes on Zoom, Google Meet, Microsoft Teams and in-person meetings,
> then connects every conversation so you can ask what changed, track commitments and draft the
> follow-up.

> **Does Lynkk work with Zoom, Google Meet and Microsoft Teams?**
> Yes. Send the meeting bot with the call link or from your calendar, record from the Chrome
> extension with no bot, or let the Mac app notice the call. The meeting bot is included on the
> free plan.

---

## 4. Microsoft Teams: integration page and blog post

Two pages target Teams. Give each a clear job so they do not compete:

- `/integrations/microsoft-teams`: the product page for "AI note taker for Teams" and
  "Microsoft Teams AI note taker" (buy intent).
- `/blog/ai-note-taker-microsoft-teams`: the list page for "best AI note taker for Teams"
  (research intent). It is already the #2 page for AI-feature impressions (217).

### /integrations/microsoft-teams

- Title, current: `Microsoft Teams AI Note Taker, With or Without a Bot | Lynkk` (60). Keep.
- Add a FAQ:

> **Is there a free AI note taker for Microsoft Teams?**
> Yes. Lynkk's free plan includes the meeting bot for Teams (audio), unlimited notes of up to
> 2 hours each and your first 5 hours of AI summaries. You do not need Teams Premium or a
> Copilot license.

- In "Lynkk or Microsoft's own AI tools?", add a sentence linking to the blog:
  "For a side-by-side of seven options, read [our guide to the best Teams AI note
  takers](/blog/ai-note-taker-microsoft-teams)."

### /blog/ai-note-taker-microsoft-teams

- Title: `Best AI Note Takers for Microsoft Teams in 2026: 7 Options | Lynkk` is 66 characters, so
  use `Best AI Note Taker for Teams in 2026: 7 Options | Lynkk` (55).
- In section "1. Lynkk (our product)", link "AI note taker for Microsoft Teams" to
  `/integrations/microsoft-teams`.
- New H2 after "How do you get AI meeting notes in Teams?", answering demand the current results
  miss ("turn off read ai meeting notes in teams", "microsoft teams ai note taker turn off"):

> **How do you remove or turn off an AI note taker in Teams?**
>
> If a note taker bot joined a meeting you host, remove it from the participant list like any
> other guest, and ask attendees to switch off auto-join in their own tool. Most note takers
> join from a calendar connection, so the lasting fix is in that tool's settings, not in Teams.
> In Lynkk, calendar auto-join is a switch on each meeting, and nothing records until someone
> presses record or sends the bot.

  **Confirm** the Lynkk sentence against current product behaviour (/features/meeting-bot
  says "Calendar auto-join, in your control" and the Teams page says "Nothing records without a
  press").

---

## 5. Google Meet: transcript post, integration page, India post

### /blog/google-meet-transcript (top AI-feature page, 405 impressions)

- Title and H1: keep.
- In "What is the best AI note taker for Google Meet?", add:
  "Lynkk works as an [AI note taker for Google Meet](/integrations/google-meet) two ways: a
  notetaker that joins from your calendar, or the [Chrome extension](/features/chrome-extension)
  that records your tab with no bot. Teams that speak Hindi or Hinglish should read [our guide
  to Google Meet note takers in India](/blog/google-meet-ai-note-taker)."
- New FAQ (visible and JSON-LD):

> **Can I get a Google Meet transcript if my Workspace plan does not include it?**
> Yes. A third-party note taker can transcribe the call instead. Lynkk's free plan records
> Google Meet with its meeting bot or Chrome extension and returns a transcript with speaker
> names, plus your first 5 hours of AI summaries.

### /integrations/google-meet

- Title, current: `Google Meet AI Note Taker, With or Without a Bot | Lynkk` (56). Keep.
- Add the Teams-style free FAQ:

> **Is there a free AI note taker for Google Meet?**
> Yes. Lynkk's free plan includes the meeting bot for Google Meet (audio) and the Chrome
> extension, with unlimited notes of up to 2 hours each and your first 5 hours of AI summaries.

- Link to `/blog/google-meet-transcript` with anchor "how to get a Google Meet transcript".

### /blog/google-meet-ai-note-taker (India)

- Title: `Google Meet AI Note Takers for Hindi & Hinglish Teams (2026)` (60) or keep current.
  India is 10% of AI-feature impressions and "hinglish transcription" has 110 global monthly
  searches with little competition.
- Add FAQPage JSON-LD (see 1b).
- Gets new inbound links from 1a.

---

## 6. /features/chrome-extension

People search for "otter ai chrome extension" and "read ai chrome extension", but this page
never says "Chrome extension" in its title or headings.

| | Current | New |
|---|---|---|
| Title | Record Meet, Zoom and Teams Without a Bot \| Lynkk | `AI Note Taker Chrome Extension, No Bot \| Lynkk` (46) |
| Meta | (keep) | Lynkk's Chrome extension records Google Meet, Zoom and Teams from your own tab. Nothing joins the call and nobody has to admit a guest. |
| H1 | Record the call without putting a bot in the room. | Keep, and add a `<p>` under it: "The Lynkk Chrome extension is an AI note taker for Google Meet, Zoom and Teams that records from your own tab." |
| First H2 | Nothing joins the call, so nothing shows up in it. | `A Chrome extension note taker with no bot in the call` |

New FAQ:

> **Is the Lynkk Chrome extension free?**
> Yes. The Chrome extension is included on the free plan, along with the Mac app and the web
> app.

---

## 7. /features/meeting-notes

Target: "ai meeting minutes generator" (140 a month, SD 30). The page already mentions minutes
in the title.

- Title: `AI Note Taker & Meeting Minutes Generator | Lynkk` (49).
- New H2 after "What's in every AI meeting note, section by section":

> **An AI meeting minutes generator that writes as you talk**
>
> Minutes are the formal record of a meeting: who attended, what was decided and who owns each
> next step. Lynkk writes them for you when the call ends. Every note opens with what, when, how
> long and who, then the summary, decisions with the reason behind them, action items with an
> owner and a date, and open questions nobody settled. Copy it into your minutes template, send
> it to attendees, or push the action items to Jira.
>
> See a [meeting minutes sample](/blog/meeting-minutes-sample) or the difference between
> [meeting notes and minutes](/blog/meeting-notes-vs-minutes).

- New FAQ: "**Can Lynkk generate meeting minutes?** Yes. Every Lynkk note includes attendees,
  decisions, action items with owners and open questions, which is what formal minutes need."

---

## 8. List posts

### /blog/best-ai-note-takers (136 impressions)

- Title and H1: keep.
- Add the links in 1a (integration pages, /compare/plaud, /use-cases/field-interviews).

### /blog/best-free-ai-note-takers

- Title and H1: keep. Make sure "Lynkk" facts match the pricing page: unlimited notes up to
  2 hours each, first 5 hours of AI summaries, meeting bot (audio), every language, Mac app,
  Chrome extension and web app.
- Add the integration links in 1a.

### /blog/otter-ai-alternatives

- Title: `Best Otter.ai Alternatives in 2026: 8 Tools Compared | Lynkk` (60). The current title is
  the only blog post without the "| Lynkk" suffix.
- Add FAQPage JSON-LD (see 1b).
- In "Is Otter AI really free?", add the demand phrase "Otter AI free plan limits" as an H3 or
  in the first sentence.

---

## After launch

1. Request indexing in Search Console for each changed URL.
2. In 2 to 3 weeks, export **Search results** (not AI features) with the **Queries** and
   **Pages** tabs, and compare against this brief.
3. Re-run the InfraNodus gap analysis on the updated homepage text to confirm the demo names no
   longer lead the graph.
