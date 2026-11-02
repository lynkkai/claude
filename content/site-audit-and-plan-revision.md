# lynkk.ai Site Audit and Revision of the 12-Topic Plan

**Date:** 2026-11-02
**Checked:** lynkk.ai homepage, /blog, /security, /integrations (fetched live, HTTP 200)
**Verdict:** the 12-topic plan needs revising. Four of the twelve collide with pages Lynkk has
already published, and one is built on a product capability the site does not claim.

---

## 1. Lynkk is a sales product now, not a generic meeting tool

The live title is **"Lynkk: AI Meeting Assistant & Note Taker for Sales Teams"** and the H1 is
**"The AI meeting assistant that remembers every sales conversation."** Supporting line:
"Your revenue lives in your conversations."

My earlier plan was written for a general knowledge-worker audience, because that is what the
brand memory file described. That file was built from search snippets in September and was wrong
on positioning, integrations and privacy. I have rewritten `memory/lynkk-brand.md` from the live
site; the corrections are marked in it.

**What this changes:** the reader for all 12 posts is a seller, a sales leader or RevOps, not a
generic "person with too many meetings". That rewrites the framing of nearly every topic, and it
means the sales-methodology vocabulary (pipeline, discovery, commitments, follow-through, CRM
hygiene) belongs in the copy.

**Confirmed product facts now available:** Free / **Pro $15 a month** ($9.75 yearly) / Enterprise.
**17 languages with a Hinglish mode.** Four capture routes: meeting bot, Chrome extension with no
bot, automatic Mac capture, in-person on Mac. **Spotter**, the live in-call assistant, is
**in development with early access on Pro**, so it cannot be written about as shipped.

---

## 2. The blog is not empty. It has roughly 28 posts and they are good

This is the finding that most changes the plan. `/blog` is positioned as
"Plain answers and straight comparisons on AI note takers, transcription and dictation, from the
team that builds Lynkk," and it already covers:

- **Competitor pricing, one post per rival:** Otter, Fireflies, Fathom, Granola, Gong
- **Comparisons:** "Best Otter.ai Alternatives, Tested (2026)", "Read AI vs Otter AI in 2026",
  "Best AI note takers, compared", "Best note takers for Zoom"
- **Sales methodology, a deep seam:** MEDDIC, BANT, SPIN, lead qualification, mutual action plans,
  key account planning, QBR template, sales forecast template, RevOps, sales enablement tools
- **Meeting mechanics:** meeting notes vs minutes, meeting summary template, follow-up email
  examples, meeting preparation checklist, board meeting agenda, action items template
- **India / Hinglish:** "Hindi Audio to Text Converter: 6 Free Ways (Hinglish Too)",
  "Google Meet AI Note Takers for Hindi and Hinglish Teams (2026)"
- **Legal:** "Is It Legal to Record a Meeting? Consent Rules by State and Country"

There are also **12 `/compare/` pages** (otter, fireflies, fathom, granola, read-ai, avoma,
circleback, clari-copilot, gong, meetgeek, notta, plaud) and a full set of `/features/`,
`/integrations/` and `/use-cases/` pages.

### Collisions with my 12 topics

| My topic | Collides with | Call |
|---|---|---|
| **M1** Best AI note takers, tested | `/blog/best-ai-note-takers` and "Best AI note takers, compared" | **Cut as written.** Lynkk already owns this. A Medium duplicate competes with its own page. |
| **M4** Otter vs Fireflies vs Granola vs Lynkk | "Best Otter.ai Alternatives, Tested (2026)" + 12 `/compare/` pages | **Cut as written.** Heavily covered. |
| **S3** Where does your meeting audio go | "Is It Legal to Record a Meeting? Consent Rules by State and Country" | **Reframe.** The consent angle is taken. The unclaimed angle is what the /security page admits. |
| **S1** The meeting is the database | "Meeting Notes vs Minutes" (secondary only) | **Keep.** Thesis is distinct. |
| **H1** MCP server | Nothing. But see section 3. | **Cut, closed.** Not a product capability and not on the roadmap. |

**M2 (bot-free capture)** survives and is now stronger than I thought: `/features/chrome-extension`
and `/features/meeting-bot` exist as supporting pages, but there is no blog post on the choice
between them. **M3 (in-person)** survives; `/use-cases/field-interviews` is adjacent but there is
no in-person capture guide. **H2, H3, H4, S2, S4** are untouched by existing content.

---

## 3. The MCP topic is cut. It was my top recommendation

> **Resolved 2026-11-02:** the team confirmed **MCP is not on the roadmap**. This topic is closed,
> not parked. Do not revive it, and do not let the keyword volume tempt it back into a future plan.

I recommended H1 ("mcp server", 60,500/mo at SD 23) as the single biggest opening. I was working
from the brand memory line "connect anything via MCP".

**MCP appears zero times on the homepage, the integrations page and the security page.** The real
integration list is CRM (HubSpot, Salesforce, Pipedrive, Zoho, Attio), Zoom, Meet, Teams, Google
Calendar, Slack and Jira. Calendly and Cal.com, also in the old memory file, are likewise absent.

So the keyword opening is real, but Lynkk cannot credibly claim it today. Publishing an MCP build
post would mean either writing about something Lynkk does not do, or writing a generic MCP tutorial
with no product tie, which earns traffic that never converts. **Cut.** The 60,500/mo at SD 23 was
the largest low-difficulty opening in the research set, and dropping it is a real cost, but
ranking for it would bring developers looking for an integration Lynkk does not have. The nearest
honest substitute is H1-new in section 5, which targets the same developer audience on something
Lynkk did build.

---

## 4. The compliance claims are worse than "unverified". Two are contradicted

In the last document I flagged "97% accuracy", "AES-256" and "GDPR" from the Ubersuggest project
summary as needing verification. The live /security page settles it:

| Claim | Reality on lynkk.ai |
|---|---|
| 97% transcription accuracy | **Appears nowhere on the site.** No accuracy figure is published at all. Do not use it. |
| AES-256 encryption | True but narrow: **"Tokens for Google Calendar, Jira and Slack are encrypted with AES-256-GCM."** It is not claimed for recordings. The page states plainly: **"Lynkk isn't end-to-end encrypted, because it has to read a recording to write the note."** |
| GDPR | A **data-rights** statement, not a certification: "Under the GDPR and India's DPDP Act, you can see, correct, export or delete your data." |
| Data residency, "pick a region" | **Contradicted.** The page says: **"Your data may be processed outside your country, including in India and the US."** |
| SOC 2 | No claim anywhere. |

The genuinely strong, publishable privacy facts are different ones: **no AI training on your
conversations**, signed upload links that expire in 10 minutes, playback links that expire in an
hour, the Mac app deleting its local copy after 7 days, dictation erased after 7 days, admins never
receiving recordings, and full export as a zip. Those are concrete and verifiable. Write those.

---

## 5. Revised topic set

Five of the original twelve stand, three are reframed, four are replaced.

### Stands as written
- **M2** AI Note Takers That Do Not Join Your Meeting (`ai note taker that doesn't join meetings`,
  90/mo, SD 30, CPC $21.61). Now better supported: Lynkk genuinely offers bot and no-bot capture,
  and the site explains the trade-off.
- **M3** AI Note Taker for In-Person Meetings (`ai note taker for in person meetings`, 480/mo,
  SD 40). Reframe the examples as field sales visits rather than generic meetings.
- **H4** Building a Voice Agent That Speaks Inside a Live Meeting (`voice ai agent`, 880/mo,
  SD 47, CPC $28.34). Spotter is real, with published mechanics: reads the screen as text not
  images, never hidden from a screen share, mic as "Me" and call as "Them". Must say early access.
- **S2** Nobody Reads the Recap. Now sharper: Lynkk's own position is that nothing auto-sends,
  you send the follow-up yourself.
- **S4** From Note Taker to Teammate. Spotter is the proof point.

### Reframed
- **H3** Turning Meetings Into Account Memory (was "a knowledge graph"). Use the site's own framing,
  "one connected memory" and Ask Lynkk, and make the engineering story about cross-call entity
  resolution at account level. Keep `knowledge graph rag` (390/mo, SD 51) as the search target
  since that is what engineers type.
- **H2** Speaker Diarization in Production. Add the Hinglish dimension: code-switching mid-sentence
  is a genuinely hard diarization and ASR problem and Lynkk ships a mode for it. That makes this
  post Lynkk-specific rather than generic.
- **S3** now becomes **"The Honest Version of the AI Notetaker Privacy Page"**: an essay arguing
  vendors should publish what they cannot do, using Lynkk's own "not end-to-end encrypted, because
  it has to read the recording" and "may be processed outside your country" as the model. This
  does not collide with the consent post, and it is defensible precisely because it does not
  overclaim. Still needs sign-off before publishing.

### Replacements for M1, M4 and H1

Chosen to support existing lynkk.ai pages rather than compete with them, and to sit on the
sales-team positioning:

- **M1-new: "Your CRM Is a Graveyard of Half-Written Call Notes"**
  Target: `crm data entry automation` (low volume) plus the commercial sales tail; the real job is
  sending Medium's audience to `/integrations/salesforce` and `/integrations/hubspot`. Medium
  ranks well for workflow essays aimed at sellers, and this frames the CRM-logging feature as the
  pain it removes.
- **M4-new: "AI Note Takers for Hindi and Hinglish Sales Calls"**
  Target: the Hindi/Hinglish cluster. Lynkk ships a Hinglish mode that Gemini-in-Meet does not
  match, the blog already proves this seam converts, and Medium has reach in India. Supports
  `/features/hinglish-transcription` rather than duplicating the two existing posts, by covering
  sales calls specifically.
- **H1-new: "Recording Both Sides of a Call Without Putting a Bot in the Room"**
  The engineering post behind M2: system audio capture, mic separation, consent UX, why the
  participant-list bot exists at all. Targets `bot free ai note taker` (110) and the dev-adjacent
  tail, and it is a real thing Lynkk built. This replaces the MCP post with something Lynkk can
  actually claim.

---

## 6. Internal linking, corrected

The earlier link table pointed at placeholder pages. Real targets now:

| Post | Link 1 | Link 2 |
|---|---|---|
| M1-new | /integrations/salesforce | /integrations/hubspot |
| M2 | /features/chrome-extension | /features/meeting-bot |
| M3 | /use-cases/field-interviews | /features/meeting-notes |
| M4-new | /features/hinglish-transcription | /blog/hindi-transcription |
| H1-new | /features/chrome-extension | /security |
| H2 | /features/hinglish-transcription | /features/meeting-notes |
| H3 | /features/ask-your-meetings | /features/workspaces |
| H4 | /features/spotter | /how-it-works |
| S1 | /features/ask-your-meetings | /use-cases/sales-calls |
| S2 | /features/action-items | /blog/action-items-examples-template |
| S3 | /security | /privacy |
| S4 | /features/spotter | /use-cases/sales-calls |

**Do not** link Medium posts to `/blog/best-ai-note-takers` or the `/compare/` pages with
comparison anchor text. Those pages are trying to rank for the same commercial terms, and an
external post with matching anchors competing on the same query helps nobody.

---

## 7. Still outstanding

1. **GSC** is still the gap. With roughly 28 published posts and 12 compare pages, lynkk.ai now
   has real query data, and that matters more than anything above. Several of these posts are
   probably ranking on page 2 for terms worth a title rewrite instead of a new article. Export
   Queries and Pages, 6 months, or connect the connector.
3. **Confirm accuracy**: is there a measured figure, measured how? If not, we publish none.
4. **Spotter GA date**, so H4 and S4 describe it correctly.
5. **Check the full blog list.** I read the `/blog` index, which showed about 28 posts; if there
   is pagination I have not seen the tail, so there may be further collisions.
