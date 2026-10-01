# Content changes: lynkk.ai/features/meeting-notes

Each number below matches a red arrow on the annotated screenshots in this folder.
Keywords are from `seo/meeting-notes-keyword-plan.md` (sections 4B and 4D).
The page's voice (short, plain, editorial sentences) is kept on purpose. Most changes add
a keyword to text that already exists rather than replacing the design.

**Before you publish, confirm:**
- [ ] The homepage title moves away from "AI Meeting Notes" (to "AI meeting assistant"), so this page can own "AI note taker" and "meeting notes" without the two pages competing.
- [ ] The Board Meeting shape produces minutes (needed for change 12 and the minutes FAQ).
- [ ] The number of supported languages (change 11). Search snippets say "15+ languages".
- [ ] The Mac app records in-person meetings, not only calls (changes 3, 16, 17 and FAQ C).

---

## 0. Behind the page (not visible, set in the CMS / page head)

| Field | Current | New |
|---|---|---|
| Title tag | (check current) | `AI Note Taker for Meeting Notes & Minutes \| Lynkk` (49 chars) |
| Meta description | (check current) | `Lynkk's AI note taker writes your meeting notes when the call ends: an AI summary, key takeaways, decisions, action items and minutes, online or in person. Start free.` (154 chars) |
| URL | /features/meeting-notes | Keep. (Optional: /features/ai-note-taker with a 301 redirect, while the page has no rankings yet.) |
| Schema | (check current) | `SoftwareApplication` (name Lynkk, category BusinessApplication, offers price 0) + `FAQPage` for the FAQ block |
| Open Graph title | (check current) | Same as the title tag |

---

## Screenshot A: hero (`A-hero.png`)

### 1. Eyebrow pill
- **Current:** `Meeting notes · Transcript, summary and tasks`
- **New:** `AI note taker · Meeting notes, summaries and action items`

### 2. H1 headline
- **Current:** `The call ends. The note is already writing itself.`
- **New (recommended):** `The AI note taker that writes your meeting notes when the call ends.`
- **Alternative if you want to keep the current line:** keep it as the visible headline but make it a `<p>` styled as a headline, and turn the eyebrow pill (change 1) into the `<h1>`. Google reads the H1 tag, not the font size.

### 3. Intro paragraph (right side)
- **Current:** `This page is one Lynkk note, read from the top. Each section is what you get after a meeting, and the margin says what Lynkk did to write it.`
- **New:** `Lynkk is an AI notetaker for online and in-person meetings. When the call ends, you get meeting notes with an AI summary, key takeaways, decisions, action items and the full transcript. This page is one Lynkk note, read from the top, and the margin says what Lynkk did to write it.`

### 4. Second button
- **Current:** `Read the note`
- **New:** `See a sample meeting note`

### 5. Product demo (image / animation)
- **Alt text (if it is an image or video):** `Lynkk AI note taker writing meeting notes and an AI summary after a Google Meet call`
- **Add a one-line caption under the demo (small grey text):** `A real Lynkk note: 32-minute Google Meet call, four people, written in Hinglish.`
- If the demo is built in HTML (not an image), no alt text is needed. Google can already read the text inside it.

---

## Screenshot B: note sections 01 to 03 (`B-note-sections-1.png`)

### 6. Bridge line above the note
- **Current:** `Below is the note, section by section. Click any time to play from there.` (plain text)
- **New:** make it an `<h2>`:
  `What's in every AI meeting note, section by section`
  and keep the second sentence as a sub-line: `Click any time to play the call from there.`

### 7. Section 02 (left margin)
- **Label, current:** `The summary`
- **Label, new:** `AI meeting summary`
- **Title:** keep `Thirty-two minutes in two sentences.`
- **Description, current:** `Written from the whole transcript after the call, so it reads like someone who was there wrote it for someone who was not.`
- **Description, new:** `Lynkk summarizes the meeting from the whole transcript after the call, so it reads like someone who was there wrote it for someone who was not.`

### 8. Section 03 (left margin)
- **Label:** keep `Key takeaways and topics` (already matches "meeting takeaways").
- **Description:** keep the current text and **add one line at the end:**
  `Together with the summary, it is the meeting recap you would have written yourself.`

---

## Screenshot C: note sections 04 and 05 (`C-note-sections-2.png`)

### 9. Section 04: Decisions (left margin)
- **Description:** keep the current text and **add one line at the end:**
  `Send the summary and decisions as a meeting recap to anyone who missed the call.`

### 10. Section 05: Action items (left margin)
- **Label, current:** `Action items`
- **Label, new:** `Action items, tracked`
- **Title:** keep `Who does what, by when.`
- **Bullets:** keep all three, and **change the second bullet:**
  - Current: `Put them on your task board, open until someone moves them.`
  - New: `Put them on your task board as an action item tracker, open until someone moves them.`

---

## Screenshot D: transcript (`D-transcript.png`)

### 11. Section 07: The transcript (left margin)
- Keep the three bullets. **Add a fourth bullet** (confirm the number first):
  `Writes notes in 15+ languages, including calls that switch between them.`

### 12. NEW section 08: Meeting minutes (insert after the transcript row)
Add a new row in the same two-column layout:

- **Number + label:** `08` `Meeting minutes`
- **Title (left):** `Minutes, without a minutes taker.`
- **Description (left):** `Switch the note to the Board Meeting shape and Lynkk rewrites it as AI meeting minutes: attendees, decisions and action items with owners, ready to file.`
- **Right column (content):** a short minutes preview built from the same sample call:
  - `MEETING MINUTES`
  - `Attendees: Maya Chen (host), Arjun Rao, Priya Nair, You`
  - `Decision 1: Ship the new onboarding to 20% of new sign-ups on Monday.`
  - `Decision 2: Keep the old flow behind a link for a week.`
  - `Actions: Arjun, fix the calendar step in Safari (Fri 26 Sep). You, write the in-app note (Thu 25 Sep). Priya, set up the drop-off dashboard (Mon 29 Sep).`

Keywords this row targets: ai meeting minutes, meeting minutes software, minutes taker, board meeting minutes software.

---

## Screenshot E: toolbar (`E-toolbar.png`)

### 13. Toolbar sub copy (right side)
- **Current:** `Three buttons and a menu at the top of every note. Click them below to see what each one holds.`
- **New:** `Three buttons and a menu at the top of every note: meeting notes templates, one click to Jira, and a link to share. Click them below to see what each one holds.`

### 14. Shape panel title (inside the demo)
- **Current:** `Summary Shapes`
- **New:** `Meeting notes templates`

### 15. "Shape · Pro" description (under the demo)
- **Current:** `Rewrite the summary as one of nine built-in shapes, from Daily Stand-up to Board Meeting. Every version is kept under Summary versions.`
- **New:** `Rewrite the summary with one of nine meeting notes templates: General Meeting, Daily Stand-up, Product Review, Engineering Design, Sales Call, Customer Interview, 1:1, Board Meeting and Brainstorm. Every version is kept under Summary versions.`

(The Send and Share descriptions are already good. No change.)

---

## Screenshot F: four ways in (`F-four-ways.png`)

### 16. "Four ways in" sub copy (right side)
- **Current:** `Record from the Mac menu bar, send a bot into the call, press record in a browser, or let your calendar send the bot for you. Every way in ends at the note above.`
- **New:** `Record online or in-person meetings from the Mac menu bar, send a bot into a Meet, Zoom or Teams call, press record in a browser, or let your calendar send the bot for you. Every way in ends at the same meeting notes.`

### 17. Mac app card
- **Current subtitle:** `Notices the call for you`
- **New subtitle:** `Calls and in-person meetings`

---

## Screenshot G: how it works + FAQ heading (`G-how-it-works.png`)

### 18. "How it works" H2
- **Current:** `How a call becomes a note like this.`
- **New:** `How a call becomes meeting notes like this.`

### 19. FAQ heading
- **Current:** `Questions about Lynkk meeting notes`
- **New:** `Questions about the Lynkk AI note taker`

---

## Screenshot H: FAQ list (`H-faq.png`)

### 20. Rename the first question
- **Current:** `What is in every note?`
- **New:** `What is in every AI meeting note?`

### 21. Rename the free plan question
- **Current:** `What does the free plan include?`
- **New:** `Is Lynkk a free AI note taking app?` (keep the current answer, and start it with "Yes, you can start free.")

### 22. Add six new questions at the end of the list

**A. What is an AI notetaker?**
An AI notetaker records a meeting and writes the notes for you. Lynkk captures the call, writes a transcript with speakers and times, then turns it into meeting notes: a summary, key takeaways, decisions, action items and open questions. You read the note instead of writing it.

**B. How does an AI note taker work?**
Lynkk records through the Mac app, a meeting bot, the browser or your calendar. After the call, the recording is transcribed, each speaker is labelled, and the AI writes the summary and action items from the transcript. Every point keeps the time it was said, so you can play it back.

**C. Can Lynkk take notes in in-person meetings?**
Yes. Start a recording from the Mac app and Lynkk writes the same note for a meeting in a room as it does for a Google Meet, Zoom or Teams call.

**D. Can AI write meeting minutes?**
Yes. Switch any note to the Board Meeting template and Lynkk rewrites it as meeting minutes, with attendees, decisions and action items with owners. Your original summary is kept under Summary versions.

**E. Does Lynkk track action items after the meeting?**
Yes. Every action item gets an owner, a due date and a priority, and stays open on your task board until someone moves it. Press Send to turn them into Jira issues, one per item.

**F. Can my whole team share meeting notes?**
Yes. Share a note with a public link you can revoke, with or without the audio, or invite people by email as Viewers. The summary is also emailed to you after every meeting.

---

## Keyword coverage after these changes

| Keyword | Volume | Where it now appears |
|---|---|---|
| ai note taker | 27,100 | Title, H1, eyebrow, FAQ heading, FAQ B |
| ai notetaker | 2,900 | Intro paragraph, FAQ A |
| meeting notes | 3,600 | Title, H1, eyebrow, intro, H2s, FAQ |
| ai note taking app | 4,400 | FAQ 21 |
| ai meeting minutes | 1,600 | New section 08, FAQ D, meta |
| meeting notes template | 22,200 | Toolbar sub copy, panel title, Shape text |
| ai meeting summary / summarize meeting | 170 / 590 | Section 02 label and text, intro |
| meeting recap | 390 | Sections 03 and 04 |
| meeting takeaways | 140 | Section 03 (already there) |
| action item tracker | 320 | Section 05, FAQ E |
| ai note taker for in person meetings | 480 | Intro, four ways in, Mac app card, FAQ C |
| team ai meeting notes | 720 | FAQ F |
| minutes taker | 170 | Section 08 title |
