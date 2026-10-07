# Video 4: Sales calls with Lynkk, before, during and after

> Production kit for the official Lynkk YouTube channel. Topic 4 in `youtube/topic-research.md`.
> Built with the `lynkk-design` skill: every product claim comes from
> `lynkk-post-kit/docs/TRUTHS.md` (checked 2026-09-29) and the copy follows `docs/COPY.md`.
> **The finished, narrated video is in `04-video/`** (`04-video/out/lynkk-sales-calls.mp4`, with title,
> description, captions and thumbnail in `04-video/README.md`). This document is the plan for a later
> live-action version filmed with the real product.
> Graphics: `04-assets/`. This replaces the earlier draft of this video, which relied on
> claims TRUTHS.md does not support.

## Overview

| | |
|---|---|
| **Goal** | Show a sales rep running a full call with Lynkk: the morning briefing before, recording with no bot during, the Meeting Brief and tasks after, and Ask Lynkk to book the next meeting |
| **Audience** | Account executives, SDRs, sales managers, founders who sell |
| **Main keywords** | ai note taker (27,100/mo) · ai sales assistant (590) · ai note taker for zoom (480) · bot free ai note taker (110) · ai note taker that doesn't join meetings (90) |
| **Length** | About 6.5 min, plus 3 Shorts and a 60 s LinkedIn cut |
| **Format** | Screen recording on a Mac with a brand host voiceover. Kit graphics between scenes |
| **CTA** | Start free at lynkk.ai |

## Title

**Final pick:** *AI Note Taker for Sales Calls: Prep, Record and Follow Up | Lynkk*

Alternates for YouTube "Test & Compare":
1. *Record Every Sales Call. Nothing Joins It. | Lynkk*
2. *Sales Calls Without Typing Notes: A Lynkk Walkthrough*

Thumbnails (in `04-assets/out/thumbnails/`):
1. "Record the sales call. Nothing joins it." with the Mac call card on the night plate.
2. "The call ends. The brief is written." with the Meeting Brief on the ember plate.
3. "One app for the whole sales call." with Before, During and After plates.

---

## Production decisions

| # | Decision | Choice | Source in TRUTHS.md |
|---|---|---|---|
| 1 | How the call is recorded | **Mac app** on a Zoom desktop call. Mention the Chrome extension and the meeting bot as other ways in | Ways to record |
| 2 | Meeting platform | **Zoom** (the Mac app notices Zoom, Meet in a browser, Teams, Slack huddles, WhatsApp, FaceTime and Webex) | Ways to record > Mac app |
| 3 | Lynkk during the call | Records quietly. The rep sees live words and types a note in the column on the right edge. **Lynkk does not speak** | Mac app |
| 4 | Follow-up | The summary is **emailed to attendees** (the rep opts in), and **Ask Lynkk (Pro)** creates a Google Calendar event with a Meet link behind a confirm card | The note > Share; Ask Lynkk |
| 5 | Tasks | Action items with owner, due date and priority. The prospect's feature request goes to the product team with **Send to Jira** (manual, one issue per action item) | Tasks |
| 6 | Pro features shown | Summary Shapes (Sales Call) and Ask Lynkk, both labelled "Pro" on screen | Plans |

### Checklist

- [ ] Mac with Apple silicon, macOS 15.4 or later (so the card and column stay hidden from screen share), Lynkk Mac app installed, Pro workspace for the Pro scenes
- [ ] Google Calendar connected, with a fictional "Harborline: pilot planning" meeting at 11:00, so the morning briefing email exists
- [ ] One earlier note seeded in the account: "Harborline discovery call", about two weeks before, with action items still open
- [ ] Zoom desktop app on the rep's Mac; a second machine for the prospect (actor)
- [ ] Jira demo project for the product team
- [ ] Demo data is **fictional** only (see below). No real customers or people
- [ ] Recording consent said out loud at the start of the call, and the consent notice graphic on screen
- [ ] Run `node lynkk-post-kit/scripts/check.mjs` on this file and every caption file before publishing

## Demo scenario (fictional)

| Role | Name | Company |
|---|---|---|
| Account executive (Lynkk user) | Maya | Northpeak (fictional seller) |
| Prospect | Daniel, Head of Operations | Harborline (fictional prospect) |

**Story so far (the seeded discovery note):** Harborline's team loses hours a week to manual
reporting. Agreed next step: a 30-day pilot after a security review. Open questions: pilot size,
budget owner. Daniel mentioned Priya in finance signs off on budget.

**Today:** pilot-planning call on Zoom.

---

## Script

**VO** = brand host voiceover. **SCREEN** = what is recorded. **GFX** = kit graphic from `04-assets/out/`.
Timings are targets.

### Scene 1: Hook (0:00-0:15)

| | |
|---|---|
| **SCREEN** | Maya's Mac. A Zoom call connects. A few seconds in, a card appears top right: "Zoom call detected", with **Record** and **Not now**. She clicks Record. A slim column slides in on the right edge: clock, Pause, Stop, two levels (You, Others), live words. In the Zoom gallery there are only two people. |
| **VO** | "A sales call is starting. Lynkk noticed it, and one click starts the recording. Look at the call: two people, and nothing else joined." |

### Scene 2: The problem (0:15-0:35)

| | |
|---|---|
| **GFX** | `motion/after-every-call.mp4` (four jobs appear one by one) |
| **VO** | "After every sales call there are the same four jobs. Write up the notes. Pull out the next steps. Send the recap. Book the next meeting. Then the next call starts, and the details from this one start to fade." |

### Scene 3: The whole call (0:35-0:52)

| | |
|---|---|
| **GFX** | `motion/whole-call.mp4` (Before, During, After; each plate lights up in turn) + `overlays/notice-fictional-demo.png` |
| **VO** | "Lynkk covers the whole call: a briefing before it, notes while you talk, and a Meeting Brief with decisions and tasks after it. Here's a pilot-planning call from start to finish." |

### Scene 4: Before the call (0:52-1:45)

| | |
|---|---|
| **GFX** | `overlays/lt-before.png` at the start of the scene |
| **SCREEN** | Maya's inbox, 8:30. The Lynkk morning briefing email. For the 11:00 "Harborline: pilot planning": who she's meeting (Daniel), the most recent note with him ("Harborline discovery call"), and "3 open action items" between them. |
| **VO** | "With Google Calendar connected, Lynkk sends a morning briefing on days you have meetings. For each one: who you're meeting, your last note with them, and how many action items are still open between you." |
| **SCREEN** | She opens the discovery note. The Meeting Brief: decisions ("30-day pilot after the security review"), open questions ("Pilot size", "Budget owner"), action items. |
| **SCREEN** | Ask Lynkk (eyebrow on screen: "Ask Lynkk · Pro"). She types: "What did Harborline say about the security review?" The answer cites the discovery note with a citation chip. She clicks the evidence and the recording plays from that moment ("Play from 12:04"). |
| **VO** | "With Ask Lynkk, on Pro, you can ask your own notes a question. The answer shows its sources, and one click plays the moment it was said." |

### Scene 5: During the call (1:45-3:10)

| | |
|---|---|
| **GFX** | `overlays/lt-during.png`, then `overlays/notice-consent.png` while Maya asks for consent |
| **SCREEN** | The Zoom call. Maya: "Is it alright if I record this so I don't have to take notes?" Daniel: "Sure." |
| **VO** | "On the Mac, Lynkk records both sides of the call on two channels, so your side of the transcript is labelled 'You'. No bot joins." |
| **SCREEN** | Close on the column: live words scrolling, levels moving. Maya types in the note field: "Priya signs off budget." |
| **VO** | "The live words sit on the edge of your screen, and you can add your own notes as you go." |
| **SCREEN** | Maya shares her pilot plan slides. Cut to Daniel's screen: he sees the slides, not the card or the column. |
| **VO** | "When you share your screen, the card and the column stay hidden from the share, on macOS 15.4 and later." |
| **SCREEN** | Quick conversation (sped up, captioned): they agree on 15 pilot users and a check-in next week; Maya will send the security overview and the pilot plan; Daniel will introduce Priya. Daniel: "Could the reports export straight to our BI tool? That would help a lot." |
| **VO** | "Bad Wi-Fi doesn't cost you the call either. The Mac app writes the audio to disk from the first second and finishes the upload when you're back online. Calls in the browser? The Chrome extension records the tab. Prefer a bot? Paste a Zoom, Meet or Teams link and it joins for you." |

### Scene 6: After the call (3:10-4:50)

| | |
|---|---|
| **GFX** | `overlays/lt-after.png` |
| **SCREEN** | Daniel leaves. The column shows "The call ended. Saving in 10 s." The note opens. |
| **VO** | "When the call ends, Lynkk stops on its own and saves." |
| **SCREEN** | The Meeting Brief: title, abstract, key takeaways with timestamps, topics, decisions with context ("Pilot size: 15"), open questions ("Security review date"), action items with owner, due date and priority ("Maya: send security overview, Fri, High"; "Daniel: introduce Priya, Mon"). She clicks a takeaway's timestamp and the recording plays from there. |
| **VO** | "Then the Meeting Brief. Key takeaways, decisions, open questions, and action items with an owner, a due date and a priority. Every timestamp plays the recording from that moment." |
| **SCREEN** | She switches the Summary Shape to **Sales Call** (label "Pro"). The previous version stays in the version list. |
| **VO** | "On Pro, Summary Shapes rewrite the note for the kind of meeting it was. There's one for sales calls, and every version is kept." |
| **SCREEN** | Share settings: "Email the summary to attendees" turned on. Cut to Daniel's inbox: the summary email arrives. |
| **VO** | "The summary is emailed to you after every meeting, and to the attendees if you turn that on. That's the recap, already sent." |
| **SCREEN** | Tasks board: the action items in "Open". Maya selects Daniel's feature request, clicks **Send to Jira**, picks the product team's project and the issue type, and sends. The Jira issue appears. |
| **VO** | "Tasks land on a board. And the feature request Daniel mentioned? Send it to Jira from the note, one issue per action item, in the project you pick." |

### Scene 7: Book the next meeting with Ask Lynkk (4:50-5:35)

| | |
|---|---|
| **GFX** | `overlays/lt-ask.png` |
| **SCREEN** | Ask Lynkk: "What's still open with Harborline?" The answer lists open tasks and decisions, with citation chips. Then: "Book a 30-minute pilot check-in with Daniel next Tuesday." A confirm card shows a Google Calendar event with a Meet link. Maya clicks Confirm. |
| **VO** | "Ask Lynkk can also act for you, always behind a confirm card. Ask what's still open, then book the check-in: a Google Calendar event with a Meet link, created when you confirm." |

### Scene 8: Privacy and teams (5:35-6:05)

| | |
|---|---|
| **SCREEN** | Note visibility setting: "Admins can see this note" (default) and "Personal". Then the workspace members list. |
| **VO** | "Recordings are private to your account, and Lynkk never trains on your conversations. Sales teams can share a workspace of up to 10 seats where everyone gets Pro, and any note can be marked Personal so only you can open it." |

### Scene 9: Recap and CTA (6:05-6:30)

| | |
|---|---|
| **GFX** | `motion/whole-call.mp4` (reuse), then `motion/end-screen.mp4` |
| **VO** | "That's the whole sales call in Lynkk: a briefing before it, a recording with no bot during it, and the brief, the tasks and the next meeting after it. Lynkk is free to start, and the Mac app is free to install. Start free at lynkk.ai." |

### End screen (6:30-6:50)

`motion/end-screen.mp4`: copy and button on the left, ember plate on the right. Place the YouTube
end-screen video element over the plate and the subscribe element under the button.

---

## Chapters (paste in description)

```
0:00 Recording a sales call with no bot
0:15 Four jobs after every sales call
0:35 Before, during and after
0:52 Before: the morning briefing
1:45 During: recording on the Mac
3:10 After: the Meeting Brief and tasks
4:50 Booking the next meeting with Ask Lynkk
5:35 Privacy and teams
6:05 Start free
```

## YouTube description

```
Sales calls end and the admin begins: notes, next steps, the recap, the next meeting. This walkthrough follows one sales call with Lynkk, from the morning briefing to the follow-up.

Start free: https://lynkk.ai

What you'll see:
• Before the call: a morning briefing email with who you're meeting, your last note with them, and the action items still open
• During the call: the Lynkk Mac app records Zoom with no bot in the call, with live words on the edge of your screen
• After the call: the Meeting Brief with key takeaways, decisions, open questions and action items with owners and due dates
• Send tasks to Jira from the note, one issue per action item
• Ask Lynkk (Pro): ask your notes a question, see the sources, and book the next meeting with a Google Calendar invite

Lynkk records on the Mac (Apple silicon, macOS 14.2 or later), in Chrome, or with a meeting bot for Zoom, Google Meet and Microsoft Teams. Transcripts in 17 languages, four of them in beta. Lynkk never trains on your conversations.

CHAPTERS
0:00 Recording a sales call with no bot
0:15 Four jobs after every sales call
0:35 Before, during and after
0:52 Before: the morning briefing
1:45 During: recording on the Mac
3:10 After: the Meeting Brief and tasks
4:50 Booking the next meeting with Ask Lynkk
5:35 Privacy and teams
6:05 Start free

The companies, people and data in this video are fictional. Always tell everyone on a call when you are recording it.

#AINoteTaker #SalesCalls #MeetingNotes #Productivity #Lynkk
```

## Tags

```
ai note taker, ai note taker for sales, ai sales assistant, sales call notes, meeting notes, ai meeting notes, bot free ai note taker, ai note taker for zoom, record zoom meeting on mac, meeting brief, action items, sales follow up, lynkk
```

## Pinned comment

> Which part of a sales call takes you the longest after it ends: the notes, the recap, or booking the next meeting?
> Try Lynkk free: https://lynkk.ai

---

## Shorts (vertical 9:16)

### Short 1: "Nothing joins the call" (20 s)
- **0-4 s:** Zoom call connects. TEXT: "Sales call starting"
- **4-12 s:** "Zoom call detected" card, click Record, the column slides in. VO: "Lynkk noticed the call. One click, and it's recording."
- **12-20 s:** Zoom gallery with two people. TEXT: "Nothing joined the call." Lynkk mark. VO: "No bot. Start free at lynkk.ai."
- **Title:** *Record a sales call with no bot in it #sales #mac*

### Short 2: "The call ended" (20 s)
- **0-5 s:** Daniel leaves. The column: "The call ended. Saving in 10 s."
- **5-16 s:** The Meeting Brief scrolls: decisions, open questions, action items with owners. TEXT: "Sped up"
- **16-20 s:** TEXT: "Decisions. Tasks. Owners." Lynkk mark.
- **Title:** *What you get after every sales call #sales*

### Short 3: "Ask your notes" (25 s, Pro)
- **0-4 s:** TEXT: "What did they say about security?"
- **4-18 s:** Ask Lynkk answers with a citation chip; click it; the recording plays from 12:04.
- **18-25 s:** TEXT: "Answers from your own notes. Pro." Lynkk mark.
- **Title:** *Ask your sales calls a question #sales #productivity*

## LinkedIn cut (60 s, burned-in captions)

| Time | Content |
|---|---|
| 0-6 s | Scene 1: call card, Record, no bot in the gallery |
| 6-18 s | Morning briefing email |
| 18-40 s | Meeting Brief: decisions, action items with owners, Send to Jira |
| 40-52 s | Ask Lynkk books the check-in behind a confirm card |
| 52-60 s | "Start free at lynkk.ai" |

---

## Claims check

| Claim in the video | TRUTHS.md section |
|---|---|
| Mac app notices Zoom calls, "<App> call detected" card with Record / Not now, no bot joins | Ways to record > Mac app |
| Both sides on two channels, your side labelled "You" | Mac app |
| Column with clock, Pause, Stop, two levels, live words, note field | Mac app |
| Card and column hidden from screen share, best effort, macOS 15.4 and later | Mac app |
| Audio written to disk from the first second; upload resumes after bad Wi-Fi | Mac app |
| "The call ended. Saving in 10 s." | Mac app; Numbers |
| Chrome extension records the tab; meeting bot joins Zoom, Meet and Teams links | Ways to record |
| Morning briefing email with who, last note, open action items (Google Calendar connected) | Before the meeting |
| Meeting Brief contents; timestamps play the recording | The note |
| Summary Shapes incl. Sales Call, every version kept (Pro) | The note |
| Summary emailed to you, and to attendees if opted in | The note > Share |
| Tasks board; Send to Jira, one issue per action item, pick project and issue type (manual) | Tasks |
| Ask Lynkk answers only from your notes, citation chips, "Play from 12:04" (Pro) | Ask Lynkk |
| Ask Lynkk creates a Google Calendar event with a Meet link behind a confirm card | Ask Lynkk |
| Recordings private; never trains on your conversations | Privacy |
| Workspace up to 10 seats, everyone gets Pro, Personal notes | Workspaces |
| 17 languages, four in beta; Apple silicon, macOS 14.2 or later; free to install | The note; Mac app |
