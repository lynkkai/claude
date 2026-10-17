# Lynkk site messaging and hero graphic draft: clarity audit

Scope: what lynkk.ai currently says and shows (homepage, use-case pages, how-it-works, pricing, FAQ, integrations), plus a heuristic audit of the draft 1600x1188 use-case hero graphic ("Client meeting, lease dispute"). All pages fetched live on 2026-10-17. The draft graphic itself was not viewed as an image; the audit is based on the written spec in the assignment brief ("Draft spec" below). Brand memory: /home/user/claude/memory/lynkk-brand.md.

Formatting note: per the repo writing rule, these notes use no em dashes or en dashes.

## Q1. What do the live lynkk.ai pages say and show (headline, subhead, visuals, before/after slider, first screen)?

### Takeaway
The live use-case pages already follow one template: a plain-language "AI for X: ..." headline, a "Lynkk listens, you focus" subhead, a hero app mockup with a Before / During / After timeline, a named persona story, and, lower down, a draggable "Without Lynkk / With Lynkk" slider using the same messy-notepad vs structured-note idea as the draft graphic. The homepage leads with memory ("remembers everything your team discusses"), not with the before/during/after lifecycle, and several product claims in the brand memory file (CRM field updates, voice answers that "speak when needed") are not supported, or are contradicted, by the live site.

### Cited Findings

**Homepage (https://lynkk.ai/)**
- Page title "Lynkk: AI Meeting Notes & Conversation Intelligence"; hero headline "The AI assistant that remembers everything your team discusses."; subhead says Lynkk links conversations, decisions, and tasks so teams know what happened and what comes next; note "Unlimited recording · No credit card required."; CTAs "Start for free" and "See how it works." ([lynkk.ai](https://lynkk.ai/))
- Hero visual is a product mockup of a "Q4 launch sync" meeting (18:07 recording) with Transcript / Summary / Action items tabs, a highlighted decision from "Priya", and a "Memory" panel; a sidebar lists Today and Earlier meetings. ([lynkk.ai](https://lynkk.ai/))
- Section order: "Everything your meetings leave behind." (Capture everything / Remember context / Ask anything), "Everything your team knows, connected in one place.", "Ask anything your team has ever discussed." (Q&A with three numbered sources), "Turn what was said into what happens next." (sends decisions and action items "to Jira and other workflows"), pricing, FAQ, testimonials, platforms, blog. ([lynkk.ai](https://lynkk.ai/))
- Homepage pricing card: Free ($0) lists "Unlimited recording and transcription"; Pro ($15/month) lists "Meeting Brief, in-call answers (Cue), extracted tasks, Ask Lynkk with citations, and Jira and Microsoft actions." ([lynkk.ai](https://lynkk.ai/))
- No before/after comparison or slider on the homepage. ([lynkk.ai](https://lynkk.ai/))
- Use-case pages linked: sales-calls, user-interviews, team-standups, field-interviews, lectures, customer-research, lawyers, one-on-one-meetings, real-estate-agents, financial-advisors. Compare pages: otter, fireflies, granola, fathom. ([lynkk.ai](https://lynkk.ai/))

**Team standups (https://lynkk.ai/use-cases/team-standups)**
- Title "Standup Meeting Notes: AI for Project Managers | Lynkk"; headline "AI for project managers: your standup meeting, written down every day."; subhead "Lynkk joins your team's standup meeting, listens, and writes down who is doing what. Nobody needs to take notes."; CTAs "Start for free", "Download for Mac". ([team-standups](https://lynkk.ai/use-cases/team-standups))
- Hero visual: "Tuesday standup" note (Google Meet, 12 min, 5 people) with Yesterday / Today / Blocked / New task sections, and a timeline "Before the standup" (09:58), "During the standup" (10:03), "After the standup" (10:12). ([team-standups](https://lynkk.ai/use-cases/team-standups))
- "Jake's day" carousel: the bot joins on its own; screen shows "Lynkk Notetaker joined" and the label "Lynkk joins on its own"; during the call "Lynkk Notetaker" appears as a participant tile. The page does not say Lynkk speaks or answers questions in the call; the only Q&A described is in Slack (Pro). ([team-standups](https://lynkk.ai/use-cases/team-standups))
- Slider section "Standups, before and after Lynkk": left "Without Lynkk", right "With Lynkk", caption "Drag the line to see the same conversation before and after."; messy file "standup.txt" with lines "mon standup", "megan blocked? design", "export fix done (?)", "tell leo", "(nobody wrote the rest)". Rows: "Nobody writes the standup down" vs "Lynkk writes it every day"; "Blockers are forgotten by Thursday" vs "Blockers are listed with the time they were raised"; "People who missed it ask around" vs "They read the note". ([team-standups](https://lynkk.ai/use-cases/team-standups))
- Closing CTA: "Be like Jake. Never lose a blocker again." ([team-standups](https://lynkk.ai/use-cases/team-standups))

**Lawyers (https://lynkk.ai/use-cases/lawyers), the live home of the "lease dispute" example**
- Title "AI for Lawyers: Client Meeting Notes and Transcripts | Lynkk"; headline "AI for lawyers: client meeting notes you don't have to type."; subhead: Lynkk records client meetings with the client's permission and writes up key facts and next steps so the lawyer can focus on listening. ([lawyers](https://lynkk.ai/use-cases/lawyers))
- Hero visual: app window "Client meeting, lease dispute" (38 min, **in the office**), timeline "14:00 Before the meeting", "14:12 During the meeting", "14:38 After the meeting"; notes panel with Key facts, Documents to collect, Next step with owner and due date; persona card "Laura, Lawyer at Clearwater Legal LLP." ([lawyers](https://lynkk.ai/use-cases/lawyers))
- "Meet Laura": the client talks fast, Laura's notes are hard to read later; notepad visual "new client.txt" with lines like "notice 2nd?? or 12th" and "(can't read this line)". ([lawyers](https://lynkk.ai/use-cases/lawyers))
- "Laura's day": Before = asks the client for permission to record ("Recording 00:01"); During = "Recording the room 11:40" with transcript timestamps 11:20, 11:34, 11:37; After = "Note ready" with AI Summary / Transcript tabs and a 38:00 timeline. "The note" section: each line links to the audio, playback at 11:20 of 38:00. ([lawyers](https://lynkk.ai/use-cases/lawyers))
- Slider "Client meetings, before and after Lynkk": rows "You write while the client talks" vs "You listen. Lynkk writes."; "Facts get lost between meetings" vs "You ask Lynkk what the client said"; "Notes are in many places" vs "Notes are in one place, in the region you choose". ([lawyers](https://lynkk.ai/use-cases/lawyers))
- "What else": offline recording on Mac, video call recording (Zoom, Meet, Teams), data region, audio retention controls. FAQ: not a court-certified transcript; always ask permission first; in-office recording via Mac app. Closing: "Be like Laura. Look at your client, not your notepad." ([lawyers](https://lynkk.ai/use-cases/lawyers))

**Sales calls (https://lynkk.ai/use-cases/sales-calls)**
- Headline "AI for sales calls: you talk, Lynkk writes the notes."; persona Jessica, buyer Dana at "Bluestone Logistics LLC"; timeline "09:40 Before the call", "10:00 During the call", "10:32 After the call". ([sales-calls](https://lynkk.ai/use-cases/sales-calls))
- This is the only use-case page found that visualises all three lifecycle stages with real product behaviour: Before = "Ask Lynkk" panel, "What is still open with Bluestone?" answered with a 21:37 citation and "Play from 21:37"; During = "Zoom call detected" prompt (Record / Not now) and Lynkk's answer to "what was agreed last time" appearing **in a side panel** (text, not voice); After = "Note ready". ([sales-calls](https://lynkk.ai/use-cases/sales-calls))
- Slider caption "Drag the line to see the same conversation before and after."; rows include "You search old emails before a call" vs "You ask Lynkk what is still open". ([sales-calls](https://lynkk.ai/use-cases/sales-calls))
- FAQ on CRM: Lynkk **does not work with CRMs yet**; tasks can go to Jira. "What else" mentions "recording without a bot". ([sales-calls](https://lynkk.ai/use-cases/sales-calls))

**Use-cases index, How it works, Pricing, FAQ, Integrations**
- Use-cases index headline "Lynkk use cases: AI notes for every conversation."; sample "Meeting Brief" card for "Acme renewal call" (Zoom, 32 min) with timestamped takeaways, owners, due dates, a decision box. Lawyers card is tagged Free; sales and standups cards tagged Pro. ([use-cases](https://lynkk.ai/use-cases))
- How it works: headline "From a conversation to connected knowledge in three steps"; section "Record. Process. Connect. In under 30 seconds."; chips "Summary", "Actions", "Decisions", "Quotes", "15+ langs" (body says 17 languages plus auto-detect). FAQ there says notes arrive "shortly after the recording finishes uploading." In-call answers / Cue and CRM are not mentioned; before-meeting context is not described. ([how-it-works](https://lynkk.ai/how-it-works))
- Pricing: Free "5 notes per month", "2 hours max per note", "5 hours of AI meeting summaries"; Pro $15/month adds unlimited notes, "Ask Lynkk AI chat", "Decision log + action tracker", "Meeting bot with video", "Weekly digest". Cue, in-call answers, Meeting Brief, Jira and CRM are not listed. ([pricing](https://lynkk.ai/pricing))
- FAQ: bot "joins as a visible participant named after you" and emails the summary when the call ends; 17 languages plus auto-detect, Hinglish included; regions US, EU, UK, India, Singapore, Australia; integrations Slack, Google Calendar, Jira, Calendly, Cal.com, custom MCP. ([faq](https://lynkk.ai/faq))
- Integrations: HubSpot, Notion, Linear, Asana marked "Soon"; Salesforce not mentioned; no mention of Cue, voice, or the bot speaking. ([integrations](https://lynkk.ai/integrations))

### Inferences
- The draft graphic is essentially a static, richer version of the slider that already exists mid-page on every use-case page. Used as a hero it would repeat the slider lower on the same page; either replace the slider with it or differentiate the hero (for example, show the lifecycle as the sales page does).
- **Factual mismatch, lawyers page:** the live lawyers hero says the lease-dispute meeting is "in the office", and Laura's story is about in-person recording on the Mac app. The draft says "Google Meet · 38 min". One of the two should change so the page tells one story. Minor mismatches too: live notepad is "new client.txt" with "notice 2nd?? or 12th"; draft uses "new note.txt" and "notice 2/9??"; live transcript timestamps 11:20 / 11:34 / 11:37 vs draft markers 11:20 / 22:30 / 35:12.
- **Claim risk:** brand memory lists "CRM fields updated" and "speaks when needed / answers live by voice", but the live sales page says no CRM support yet (HubSpot "Soon"), and in-call answers are shown as text in a side panel and only named on the homepage pricing card ("Cue"). Adding CRM or voice to the graphic would put an unsupported claim in a hero. The brand memory file should be reconciled with the live site.
- **Site-level confusion a cold visitor may hit:** homepage Free card says "Unlimited recording" while pricing and FAQ say 5 notes per month; "15+ langs" chip vs "17 languages"; "In under 30 seconds" vs "shortly after the recording finishes uploading"; Cue / Meeting Brief appear on the homepage Pro card but not on the pricing page.
- The live use-case pages already speak plain language ("You listen. Lynkk writes."), which sets the tone bar the graphic should match.

### Gaps
- Could not view rendered visuals or measure font sizes on live pages; descriptions come from page text and markup via a fetch tool.
- Did not fetch user-interviews, field-interviews, lectures, customer-research, one-on-one, real-estate, financial-advisors pages individually; the index and footer show they exist and follow the same card format, but their hero visuals and sliders were not confirmed.
- Whether "Cue" in-call answers are delivered by voice anywhere in the product: no live page says so.

## Q2. Heuristic audit of the draft hero graphic: ranked confusion risks

### Takeaway
The draft's core idea (same meeting, your messy notes vs Lynkk's linked note) is strong and matches the site, but it asks a cold visitor to parse about 15 to 20 separate elements, puts the negative ("Without Lynkk") where the eye lands first, never shows Lynkk as a visible actor, and becomes illegible at phone width. The highest-severity issues are focal overload, missing actor, and mobile legibility.

### Cited Findings
- Users often leave pages within 10 to 20 seconds, "the first 10 seconds of the page visit are critical", and to earn more attention "you must clearly communicate your value proposition within 10 seconds." ([Nielsen, NN/g, 2011](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/))
- Without strong structure, readers fixate on the top and the start of lines (F-pattern); visually distinct items (bold, colored, bulleted) attract fixations ("spotted" pattern); headings-first scanning ("layer cake") is the most effective; walls of text hurt comprehension. ([Pernice, NN/g, 2019](https://www.nngroup.com/articles/text-scanning-patterns-eyetracking/))
- Five-second tests show a design briefly and ask what people recall; practitioners note the 5-second duration is largely based on researcher experience, and longer exposures (up to 20 s) are used for complex designs. ([Smashing Magazine case study](https://smashingmagazine.com/2023/12/five-second-testing-case-study)); aesthetic judgments can form in about 50 ms per Lindgaard et al. 2011 as cited by ([UX Psychology](https://uxpsychology.substack.com/p/5-second-tests-measuring-first-impressions)) (secondary source).
- The draft layout, labels, quotes and tags are as listed in the assignment's draft spec (no URL; not independently viewed).
- The live site's own hero visuals show Lynkk as an actor ("Lynkk Notetaker joined", "Lynkk joins on its own", "Recording the room", "Zoom call detected") ([team-standups](https://lynkk.ai/use-cases/team-standups), [lawyers](https://lynkk.ai/use-cases/lawyers), [sales-calls](https://lynkk.ai/use-cases/sales-calls)).

### Inferences (ranked by severity)

**Severity 1 (likely to defeat the 5-second test)**
1. **Too many focal points.** Count from the spec: header label + 2-item legend, waveform, 3 markers, 3 speech bubbles, "Note ready" pill, 3 arrows, notepad with 6 fragments, 4 red tags, panel footer, 2 panel headers with sublabels, note header, 3 cards with timestamp chips, bottom caption. That is roughly 20 competing elements and 3 color systems (green markers/arrows, red error tags, green/blue gradient). In 5 seconds a visitor will likely remember "a waveform and a messy note", not "Lynkk writes the note for me".
2. **Lynkk is not a visible actor.** There is no Lynkk mark, bot tile, recording indicator, or "Lynkk" label on the timeline. The legend lists only "Laura, lawyer" and "Client". The product appears only as a word in panel headers and the caption, so cause (Lynkk listening) to effect (note) has to be inferred from arrows. The live pages already solve this with "Lynkk Notetaker joined" / "Recording the room".
3. **Mobile legibility.** A 1600 px canvas shown at about 343 px (375 px phone minus 16 px gutters) is scaled to about 21 percent. Body text drawn at 24 px becomes about 5 px; to stay at 12 px on a phone, source text would need to be about 56 px. The quotes, notepad fragments, red tags and card bodies will be unreadable on mobile; the image would be about 255 px tall, so only shapes survive. At a 1200 px desktop display (75 percent), source text must be at least about 21 px to render at 16 px.

**Severity 2 (misreadings likely for a share of visitors)**
4. **Reading order starts with the negative.** In an LTR F-pattern the left panel is read first, and it is "Without Lynkk" with four red tags, the most visually loud element (red, bold tags attract fixations). A skimmer may leave thinking the product is the notepad, or that the red tags are Lynkk's output.
5. **Arrow routing.** Three arrows from markers spread across the waveform are bundled along the right edge into the right panel. Parallel lines in one color with long runs are hard to trace; the arrow from 11:20 crosses the width of the canvas and likely passes near the bubbles and the "Note ready" pill. The numbers 1/2/3 do the real work; the arrows add load. Also, arrows only feed the right panel, so the left panel looks disconnected from the meeting it is supposed to be a record of.
6. **Story mismatch with the live lawyers page:** "Google Meet · 38 min" vs the page's "in the office" persona and Mac in-room recording. A lawyer reading the page top to bottom sees two different meetings.
7. **"You" is ambiguous.** "Typed by you, while trying to listen" assumes the visitor is Laura; the legend introduces Laura in the third person. Pick one voice: either "Laura's notes" / "Lynkk's note" or "Your notes" / "Lynkk's note".
8. **Timestamp chips "▶ 11:20" read as video play buttons.** Nothing says they replay the audio. The lawyers page explains it ("each line links to the audio"); the graphic does not, except in the caption phrase "linked to the moment it was said".

**Severity 3 (polish, label clarity, density)**
9. **Header label is meta, not a message.** "The meeting · what was said, minute by minute" describes the diagram rather than the benefit, and it is the first text read. The middle dot separators appear in several labels and add visual noise.
10. **Date-format trap.** "notice 2/9?? email or post" is read as 9 February by US visitors and 2 September by others. It is meant to look "guessed", but it may read as a deliberate wrong fact rather than a messy note.
11. **"Note ready in 30 s"** uses an abbreviation and sits at the far right end of the waveform where arrows also run; easy to miss and slightly cryptic. Also the site's FAQ says "shortly after the recording finishes uploading", so "30 s" is a claim to keep consistent.
12. **Text density.** Three full-sentence quotes in bubbles plus the same facts repeated in the right cards means the visitor reads the key content twice. Consider shortening bubbles to 3 to 5 words or dropping them and letting cards carry the quotes.
13. **Speaker attribution.** All three markers are the same green; whether bubble 1 is the client and 2 and 3 are Laura depends on bubble color only. If the bubbles are not colored to the legend, attribution is lost.
14. **Blinking cursor** only works if the asset is animated; in a static PNG/WebP it is just a stray bar.
15. **Caption ends the sentence on the main idea** ("with every point linked to the moment it was said"), which is good, but it sits at the bottom, below the fold of the graphic on most screens, so it does not help the 5-second read.

**Quick fixes implied**
- Add a Lynkk actor on the timeline (for example, a "Lynkk is recording" chip with the logo at minute 0) and put the Lynkk mark in the right panel header.
- Make the right panel visually dominant (larger, first in reading order on mobile, or place it right but larger with the left desaturated).
- Replace three long arrows with numbered chips: marker "1" on the waveform matches card "1". Keep at most one arrow, or none.
- Produce a separate mobile crop: timeline strip + the "With Lynkk" note only, 2 cards max, text at least about 56 px in source.
- Reduce red tags to one or two, or replace them with a single footer line.

### Gaps
- No user testing data for this graphic; all severity rankings are heuristic judgments.
- Actual font sizes, colors, and contrast ratios in the draft were not given, so legibility numbers are calculated from assumed source sizes (24 px body) and the stated canvas width.
- Could not confirm whether the draft is static or animated.

## Q3. Which key differentiators are absent from the graphic, and which matter most for a use-case hero?

### Takeaway
The graphic shows only the "after" stage of one meeting. Absent: the bot or recorder as visible actor, before-meeting context, in-call answers, cross-meeting memory / Ask Lynkk, Jira push, in-person and offline capture, and data region. For a use-case hero the most valuable additions are (1) a visible Lynkk actor and (2) one hint of memory ("ask Lynkk what the client said"), because memory is the homepage promise and the stated edge over Otter and Fireflies. CRM push and voice answers should not be added, since the live site says CRM is not supported yet and does not describe voice answers.

### Cited Findings
- Brand positioning: "One AI across the entire meeting lifecycle: before, during and after, not just after"; tagline "joins your meetings, speaks when needed, remembers everything, and does the work after." (/home/user/claude/memory/lynkk-brand.md, repo file)
- Homepage hero promise is memory: "The AI assistant that remembers everything your team discusses." ([lynkk.ai](https://lynkk.ai/))
- FAQ positions Lynkk against Otter.ai and Fireflies for teams that record in person, use multiple languages, or want cross-meeting answers. ([faq](https://lynkk.ai/faq))
- Lawyers slider row: "Facts get lost between meetings" vs "You ask Lynkk what the client said"; "Notes are in one place, in the region you choose". ([lawyers](https://lynkk.ai/use-cases/lawyers))
- Sales page Before stage shows Ask Lynkk "What is still open with Bluestone?" with a timestamp citation; During stage shows an answer in a side panel. ([sales-calls](https://lynkk.ai/use-cases/sales-calls))
- Bot joins as a visible participant; Jira gets one issue per action item. ([faq](https://lynkk.ai/faq), [integrations](https://lynkk.ai/integrations))
- CRM: "does not work with CRMs yet" ([sales-calls](https://lynkk.ai/use-cases/sales-calls)); HubSpot marked "Soon" ([integrations](https://lynkk.ai/integrations)).
- Lawyers card is Free; memory (cross-meeting search) on the lawyers page is Pro. ([use-cases](https://lynkk.ai/use-cases), [lawyers](https://lynkk.ai/use-cases/lawyers))

### Inferences
Missing items, with fit for a use-case hero:

| Differentiator | In draft? | Live site support | Fit for use-case hero |
|---|---|---|---|
| Lynkk visible as actor (bot tile / "recording the room") | No | Yes, all use-case pages | **Highest.** Fixes cause and effect at low cost |
| Cross-meeting memory / Ask Lynkk | No (single meeting only) | Yes, Pro | **High.** Core homepage promise; one small "Ask Lynkk" line suffices |
| Every line linked to audio | Yes (chips, caption) | Yes | Keep, but explain "tap to hear" |
| Jira push of the new task | No | Yes | Medium for standups / sales; low for lawyers |
| Before-meeting context (Meeting Brief / "what's still open") | No | Sales page only; Meeting Brief on homepage Pro card | Medium; best as a separate lifecycle strip, not crammed in |
| In-person / offline capture | No (draft says Google Meet) | Yes, central to lawyers story | **High for lawyers**, fix the "Google Meet" label to "In the office" |
| Data region / privacy / consent | No | Yes, lawyers FAQ and slider | High for lawyers, as a small badge |
| In-call answers | No | Text side panel on sales page; "Cue" on homepage pricing only | Low; inconsistent naming, avoid in hero |
| Voice answers ("speaks when needed") | No | Not found on any live page | Do not add until confirmed |
| CRM field updates | No | Explicitly not supported yet | Do not add |
| Multilingual | No | Yes, 17 languages | Low for this hero |

- For the lawyers hero specifically: swap "Google Meet" for "In the office", add a small "Recorded with the client's permission" or region badge, and add one memory line on the right panel (for example "Next meeting: ask Lynkk what the client said about the notice").
- For standups: the actor is "Lynkk Notetaker" in the call grid, and the most relevant extra is the task going to the Tasks board / Jira.

### Gaps
- No analytics or test data on which differentiator drives sign-ups.
- Could not verify whether "Cue" is live, voice-based, or Pro-only beyond the homepage pricing card text.

## Q4. Candidate simplified headline and caption lines (no em dashes or en dashes)

### Takeaway
Shorter, actor-first lines that reuse the site's existing voice ("You listen. Lynkk writes.") will test better than the current meta label. All lines below avoid em and en dashes and avoid unsupported claims (CRM, voice).

### Cited Findings
- Existing live lines that already work: "You listen. Lynkk writes." and "Be like Laura. Look at your client, not your notepad." ([lawyers](https://lynkk.ai/use-cases/lawyers)); "Lynkk joins your team's standup meeting, listens, and writes down who is doing what. Nobody needs to take notes." and "Blockers are listed with the time they were raised" ([team-standups](https://lynkk.ai/use-cases/team-standups)); "Drag the line to see the same conversation before and after." ([sales-calls](https://lynkk.ai/use-cases/sales-calls))
- Value proposition must land within about 10 seconds. ([NN/g](https://www.nngroup.com/articles/how-long-do-users-stay-on-web-pages/))
- Repo rule: never use em dashes or en dashes. (/home/user/claude/CLAUDE.md)

### Inferences (suggested copy)

Headline over the graphic (pick one):
- "You listen to the client. Lynkk writes the note."
- "Same meeting. Your notes vs. Lynkk's note."
- "Three key moments. Lynkk caught all three."
- "Look at your client, not your notepad." (reuses the page's closing line)
- Standups variant: "Nobody takes notes. Lynkk writes the standup."

Replacement for the top label "The meeting · what was said, minute by minute":
- "The meeting (38 min, in the office)"
- "What the client said, and when"

Panel labels:
- Left: "Your notes" / sublabel "Typed while trying to listen"
- Right: "Lynkk's note" / sublabel "Ready about 30 seconds after the call"
- Timeline actor chip: "Lynkk is recording" (or, for video calls, "Lynkk Notetaker joined")

Timestamp chip helper (small text near the first card): "Tap a time to hear that moment."

Bottom caption (pick one):
- "Lynkk records the meeting, then writes the key facts, the documents to collect, and the next step. Tap any line to hear it."
- "Every point in Lynkk's note links back to the moment it was said."
- "You focus on the client. Lynkk writes it down, and remembers it for next time."

Left footer replacement (shorter):
- "3 key moments. None written down in full."

Memory hint line for the right panel (Pro):
- "Next time, ask Lynkk: what did the client say about the notice?"

Mobile crop caption (very short):
- "You listen. Lynkk writes."

### Gaps
- None of these lines have been tested with users; A/B or five-second testing would be needed to choose.
- "About 30 seconds" should be checked against the FAQ wording ("shortly after the recording finishes uploading") before publishing.
