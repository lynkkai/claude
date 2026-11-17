# Best AI Note Taker for In-Person Meetings (No Zoom Link Needed), 2:00, hosted by a presenter with Remi

Status: **draft for sign-off** (remi-video step 2). Nothing is built until the open questions at the bottom are answered.

| Field | Value |
|---|---|
| Plan row | P2, Buying, Demo plus roundup. **Plan said 3:30 to 4:30; cut to 2:00 on request.** |
| Keyword | ai note taker for in person meetings (vol 480, SD 40, CPC $14.62) |
| Companion page | lynkk.ai/blog/ai-note-taker-in-person-meetings (new page, section 11.11) |
| AI prompts to win | "How do I get AI notes from an in-person meeting?" / "Is there an AI note taker for in-person meetings?" |
| Format | **YouTube 16:9, 1920x1080 at 30 fps.** Optional extra: a 30 s 9:16 Short cut from the same timeline |
| CTA | **Get Lynkk Pro, $4 a month (₹250 in India)**, lynkk.ai. Fine print: Apple silicon · macOS 14.2 or later |

**Source of truth:** `lynkk-website-changes_3.md`, section 11.11 (the companion page), plus the pricing rules in
section 1. Where that document and the video kit's older `docs/TRUTHS.md` disagree, **the document wins**.

**The idea:** "Your best meetings don't have a link." A presenter runs a real conference-room test on camera, and
Remi (the Lynkk robot) does the graphics: chapter cards, the comparison board, the mic placement map, the picks
board, and close-ups of the real Mac UI that are too small to read in a room shot.

**Edit style:** at 2 minutes nothing gets a second pass, so every line does one job and the cut keeps moving. The
Remi inserts sit on the kit's grid (120 BPM at 30 fps: beat 15 frames, bar 2 s), so every graphic, chapter card and
cut lands on a bar line. Chapter cards are 1 bar, not 2. The camera is never still on a graphic for more than a bar.

**Music:** one bed track, 120 BPM, low under speech (ducked about 12 dB under the voice), up to full on the cold open,
the five chapter cards and the end card. Final chord on 1:58.0, the last picture beat (Remi lands on the CTA).

**Length:** 2:00 exactly (60 bars). Voice-over is about 300 words, which is a brisk but comfortable 150 a minute.

## Format and framing

Landscape YouTube, 1920x1080 at 30 fps, not a vertical reel. Checked, not assumed: a `Wide` 1920x1080 composition
was added to the kit's engine (`src/lib.ts` FORMATS, `src/index.tsx`) and test frames render through it.

| Setting | Value |
|---|---|
| Frame | 1920x1080, 16:9, 30 fps |
| Title centre line | y 880, 86 px type, 1640 px wide |
| Remi on screen | 165 px |
| Keep clear | the bottom 60 px, where YouTube's progress bar sits on hover |
| Safe zones | the kit's reel zones (top 250, bottom 420) do not apply |

The reference film packs its UI into a narrow column because a vertical reel sees only about 520 points of the Mac
screen across. Rendered at 16:9 that leaves wide empty margins. The wide scenes get roughly twice the width, so the
boards, the note and the mic map lay out across the frame instead of stacking down a column.

## What the cut from 4:12 removed

The six chapters all survive, with these losses. Say the word if any of them should come back instead of something else.

- **The chapter rundown** after the hook (a 10 s "here's what's coming" graphic). First on the floor: it only announces.
- **Per-tool detail in the roundup.** Each of the five non-Lynkk tools now gets one clause and a board row instead of a
  sentence and a reason. The board still carries their prices, so the information is on screen, just not spoken.
- **The second mic-placement test** (laptop at the far end). It stays in the shoot list because it still informs the tips,
  but it is no longer a shot.
- **The "2 hours and 5 minutes of silence" aside** is now half a line inside the Wi-Fi chapter.
- **The three-way device discussion** is one board instead of a board plus a walk-through.

## Chapters (YouTube description)

```
0:00 Why in-person is harder
0:20 Phone, laptop or recorder
0:40 Demo: recording the room on a Mac
1:10 Speaker labels in a room
1:26 When the Wi-Fi drops
1:40 Picks by setup
```
All six are at least 14 seconds, so YouTube will accept them.

## The script

Legend: **A** = presenter on camera in the room. **B** = filmed B-roll. **SCR** = screen recording of the real Mac app.
**G** = Remi graphic built in the kit (Remotion). VO lines are what the presenter says.

### 1. Why in-person is harder (0:00 to 0:20, bars 0 to 9)

| Time | Bars | Picture | VO / on camera | On-screen text | Sound |
| --- | --- | --- | --- | --- | --- |
| 0:00 to 0:04 | 0 to 1 | **G1 cold open.** Black. Remi's eyes blink open. A generic "Zoom Meeting" window slides in, Remi flies at it, the window shatters on bar 1 and the shards fall away to reveal the real conference room (B, locked wide). | none | **"No link?"** then **"No problem."** word by word | swell, glockenspiel blip on the eyes, impact on the shatter at 0:02.0 as the groove enters |
| 0:04 to 0:14 | 2 to 6 | **A.** Presenter at the head of a real meeting table, laptop open in the middle. Slow push-in. | "Most AI note takers need a Zoom link. Your best conversations don't have one. Here's how to get the same notes from a room, in two minutes." | lower third: presenter name | bed under voice |
| 0:14 to 0:20 | 7 to 9 | **B** montage on bar lines: a glass-walled room, a client's office, a site visit. | "Online, a bot hears everyone cleanly. In a room, one mic fights the fan and the echo." | **"One mic."** / **"Every voice."** | room tone, cuts on bars |

### 2. Phone, laptop or recorder (0:20 to 0:40, bars 10 to 19)

| Time | Bars | Picture | VO / on camera | On-screen text | Sound |
| --- | --- | --- | --- | --- | --- |
| 0:20 to 0:22 | 10 | **G chapter card 1.** Remi stamps the title. | none | **"Phone, laptop or recorder?"** | impact on 0:20.0 |
| 0:22 to 0:28 | 11 to 13 | **A** with the three on the table: a MacBook, a phone, a small recorder. | "Three ways to get a room into an AI note taker. Disclosure: I work on Lynkk." | **"Disclosure: I work on Lynkk."** and, small, "Other tools: their own sites, Nov 2026" | bed |
| 0:28 to 0:38 | 14 to 18 | **G3 comparison board.** Three columns slide in, one per bar, Lynkk's row first. Rows fill on beats: *Records on*, *Offline*, *Speaker labels*, *Price*. | "A laptop is on the table already: Lynkk on a Mac, or Granola. A phone goes everywhere: Otter, Granola, Fireflies. A recorder you clip on: Plaud." | column heads **Laptop** · **Phone** · **Recorder**; stamp "checked November 2026" | a tick per row, whoosh per column |
| 0:38 to 0:40 | 19 | **A** taps the MacBook. | "Lynkk has no phone app." | **"Lynkk: Mac and browser."** | whoosh into the card |

### 3. Demo: recording the room on a Mac (0:40 to 1:10, bars 20 to 34)

| Time | Bars | Picture | VO / on camera | On-screen text | Sound |
| --- | --- | --- | --- | --- | --- |
| 0:40 to 0:42 | 20 | **G chapter card 2.** | none | **"Record the room."** | impact |
| 0:42 to 0:50 | 21 to 24 | **G4 mic placement map.** Top-down drawing of the table: laptop in the middle, a ring for "clear voice" reaching every seat; red crosses on a laptop at the far end, one by the projector, one on a phone in a pocket. | "Setup is most of the result. Middle of the table, lid open, away from the fan. Don't type on it." | **"Middle of the table."** | tick per placement, buzz on each cross |
| 0:50 to 0:54 | 25 to 26 | **A** to the room. | "And ask first. Everyone here agreed on camera." | **"Ask first."** | bed |
| 0:54 to 0:58 | 27 to 28 | **SCR** menu bar, then **G5a** close-up redraw: the Lynkk sphere opens, cursor on **Record now**. | "Menu bar, Record now. No link, nothing joins." | **"Record now."** | one real trackpad click on the press |
| 0:58 to 1:02 | 29 to 30 | **B** the meeting running (4 people), cut with **G5b**: the recording column on the right edge, clock running, live words arriving. | "The column shows it hearing the far end." | none | room audio up, bed down |
| 1:02 to 1:10 | 31 to 34 | **SCR** Stop, then **G5c**: the note stamps in (summary, decisions, action items with owner and due date, open questions). Remi lands on an action item. | "Stop, and you get the same note as a Zoom call: summary, decisions, action items with owners, full transcript." | **"Same note as a call."** | three stamps on beats, a light hit as Remi lands |

### 4. Speaker labels in a room (1:10 to 1:26, bars 35 to 42)

**Check against the real test before the VO is final** (open question 1). Draft:

| Time | Bars | Picture | VO / on camera | On-screen text | Sound |
| --- | --- | --- | --- | --- | --- |
| 1:10 to 1:12 | 35 | **G chapter card 3.** | none | **"Who said what?"** | impact |
| 1:12 to 1:22 | 36 to 40 | **SCR** the transcript scrolling, then **G6** callout: one passage with its speaker labels highlighted against the B-roll of who was talking, then a label being renamed. | "One mic, four people, and the AI splits us by voice: Speaker 1, Speaker 2. Rename once. Lynkk does 17 languages, Hinglish included. [RESULT FROM THE TEST]" | **"Split by speaker."** / **"17 languages."** | tick on each highlighted label |
| 1:22 to 1:26 | 41 to 42 | **A.** | "One at a time, and say names. Over to you, Priya." | **"Say names early."** | whoosh into the card |

### 5. When the Wi-Fi drops (1:26 to 1:40, bars 43 to 49)

| Time | Bars | Picture | VO / on camera | On-screen text | Sound |
| --- | --- | --- | --- | --- | --- |
| 1:26 to 1:28 | 43 | **G chapter card 4.** | none | **"No Wi-Fi?"** | impact |
| 1:28 to 1:36 | 44 to 47 | **SCR** on camera: Wi-Fi switched off mid-recording, the clock keeps running. **G7**: a drawn disk icon filling as the audio is written. | "Wi-Fi off, mid-meeting. Still recording. It writes to disk from the first second. Lynkk is offline-first. So is Plaud." | **"Still recording."** | a soft off-click, the bed carries on |
| 1:36 to 1:40 | 48 to 49 | **SCR** Wi-Fi back on; the upload resumes; the note arrives. | "Back online, the upload resumes. Two hours per recording." | **"Uploads when you're back."** | rising tick, a light hit when the note lands |

### 6. Picks by setup (1:40 to 2:00, bars 50 to 59)

| Time | Bars | Picture | VO / on camera | On-screen text | Sound |
| --- | --- | --- | --- | --- | --- |
| 1:40 to 1:42 | 50 | **G chapter card 5.** | none | **"My picks."** | impact |
| 1:42 to 1:48 | 51 to 53 | **G8 picks board**, row 1 stamps in and holds lit, Remi points. | "On a Mac, Lynkk. The room, every speaker, 17 languages. Four dollars a month." | **1. Lynkk** · Mac · offline · 17 languages · $4/mo | tick |
| 1:48 to 1:54 | 54 to 56 | rows 2 to 6 stamp in on beats, one every 1.5 s, Remi flying down the column. | "On a phone, Otter or Granola. Fireflies for teams. A recorder, Plaud. Or Voice Memos." | **2. Otter** · free 300 min · $8.33/user/mo · **3. Granola** · $14/user/mo · **4. Fireflies** · $10/seat/mo · **5. Plaud** · recorder, offline · **6. Apple Voice Memos** · free, transcript only | a tick per row |
| 1:54 to 2:00 | 57 to 59 | **G9 end card.** Remi's trail draws a circle that locks into the Lynkk sphere. **Lynkk**, **Get Lynkk Pro**, **$4 a month (₹250 in India)**, **lynkk.ai**, fine print one beat apart. Remi lands on the button on 1:58.0 and waves. | "If that's a Mac on your table, link's below." | Lynkk · Get Lynkk Pro · $4 a month (₹250 in India) · lynkk.ai · *Apple silicon · macOS 14.2 or later* | impact on the sphere, final chord on 1:58.0 as Remi lands, ring out |

## Voice-over and music

A scratch audio track for the whole 2:00 is built and in this folder: `in-person-2min-scratch-audio.mp3`. It is the
voice-over at the timecodes in the tables, under the music bed, so you can hear the pacing before anyone films.

**The voice is a stand-in, not the final track.** It is Ryan, a local text-to-speech voice, used to measure whether
the copy fits. Nothing is sent anywhere to make it. The real voice-over is the presenter, recorded on a lav at the
shoot. There was no voice called Adam in the local set, and the stand-in costs nothing to re-render if you want a
different one: Joe, John, Norman and Bryce are the other American male voices, Alan is British.

**Why the copy got shorter.** The first 2:00 draft read as 138 seconds of speech in a 120 second video: 16 of its 17
lines overran their windows, the worst by 6 seconds. Every line was cut until it fits with a little room to breathe.
The voice-over is now 256 words. The lines in the tables above are the measured versions.

| Line | Window | Spoken | Room left |
|---|---|---|---|
| Opening, "Most AI note takers need a Zoom link" | 10.0 s | 7.2 s | 2.8 s |
| "Online, a bot hears everyone cleanly" | 6.0 s | 5.1 s | 0.9 s |
| "A laptop is on the table already" | 10.0 s | 9.5 s | 0.6 s |
| "Setup is most of the result" | 8.0 s | 5.5 s | 2.5 s |
| "Stop, and you get the same note" | 8.0 s | 6.6 s | 1.4 s |
| "One mic, four people" | 10.0 s | 9.0 s | 1.0 s |
| "Wi-Fi off, mid-meeting" | 8.0 s | 7.0 s | 1.0 s |
| "On a Mac, Lynkk" | 6.0 s | 5.2 s | 0.8 s |
| "On a phone, Otter or Granola" | 6.0 s | 5.6 s | 0.4 s |

Speech totals 82 seconds inside the 120, at an unhurried pace with no speed-up applied. Every line has room to
breathe, so a presenter can be slower or more expressive than the stand-in and still fit.

**Music:** "Ramp It Up" by Ahjay Stelino, from Mixkit, under the Mixkit Stock Music Free License. It is the same
track as the Lynkk for Mac teaser, already cleared and credited by the video kit, and it runs at 120 BPM, which is
the grid this script is written on. The edit is cut at bar lines: a 2 second intro, the groove through the body,
the track's own drop placed on 1:40 where the picks chapter starts, and its closing hit on 1:58 under the end card.
The ambient breakdown in the middle of the track is cut out, so the energy never dips.

**Measured on the finished mix:**

| Check | Result | Gate |
|---|---|---|
| Integrated loudness | -13.9 LUFS | -14 plus or minus 0.5 |
| True peak | -4.8 dBFS | at or under -1 dBTP |
| Loudness range | 4.1 LU | |
| Quietest chapter against the loudest | 1.4 LU | no chapter more than about 3 LU down |
| Length | 120.000 s | exactly the film's length |

**What I could not check:** I cannot hear. These are measurements, not judgements. Listen to the opening 10 seconds
for whether the music enters hard enough on the shatter, 1:40 for whether the drop lands with the picks board, and
1:58 for whether the last hit sits under Remi's landing.

**Content ID:** Mixkit music may not be registered with YouTube Content ID. The CC BY credits go in the video
description.

## The graphics package (what the kit builds)

All built in a new 1920x1080 composition on the kit's engine (`Wide`, next to `Reel` and `Post`), from Remi,
the drawn Mac parts, the camera and the effects. **Verified:** the `Wide` format is added and renders (see
"Format and framing" above). The YouTube edit itself (A-roll, B-roll, screen recordings) is cut
in an editor; the inserts are rendered as separate clips with the timecodes above.

| ID | Insert | Length | Built from |
|---|---|---|---|
| G1 | Cold open: call window shatters into the room | 4 s | `CallWindow`, `Shatter`, `TitleSlam`, Remi; the room plate is a still from the shoot |
| Cards 1 to 5 | Chapter cards | 2 s each | one template: title slam + whip out |
| G3 | Laptop / phone / recorder board | 10 s | new drawn board, Grid tokens, Lynkk's row first |
| G4 | Mic placement map | 8 s | new top-down table drawing |
| G5a to c | Record now, recording column, note | 4 s + 4 s + 8 s | `Desktop`, `RecordColumn`, `NoteCard`, redrawn for an in-person recording |
| G6 | Speaker label callout and rename | 10 s | new transcript callout, strings from the real test |
| G7 | Still recording / disk filling | 8 s | new, small |
| G8 | Picks board, 6 rows | 12 s | new board, same look as G3 |
| G9 | End card | 6 s | the engine's `EndCard`, retimed for 16:9 and the new CTA |
| Short | 30 s 9:16 cut of the hook for YouTube Shorts | 30 s | the kit's native `Reel` |

Total rendered graphics: about 1 minute 20 seconds, down from 2 minutes 20.

**Competitor names on screen:** plain text in the video's own typeface. No competitor logos, no screenshots of their
apps, no recreations of their UI. Lynkk is row 1 on both boards; the rest follow the companion page's order.

## Shoot list (for the team)

- **Room:** a real conference room with a glass wall or hard surfaces (so the echo is honest), seats for 4 to 6.
- **People:** 4 participants. **Written consent from everyone before recording**, and a line on camera (0:50).
- **Devices on camera:** a MacBook (Apple silicon), a phone, a small recorder. No competitor branding or app UI
  visible on the phone or recorder.
- **Screen recordings** on the recording Mac (or a second Mac mirroring the account): menu bar Record now, the
  recording column, Stop, the finished note, the transcript with speaker labels, renaming a speaker, Wi-Fi off and on
  mid-recording, the upload resuming.
- **Test protocol:** a 6 to 8 minute real meeting with an agenda, two decisions and three action items with owners and
  dates spoken out loud, so the note has something to show. Run it twice, laptop in the middle and then at the far end
  by the projector: the second run no longer appears in the video, but it is what the mic tips are based on.
- **B-roll:** room wide, hands on the table, the laptop in the middle (top-down if possible, it doubles as the plate
  for G4), a client office, a site visit, Wi-Fi being turned off.
- **Audio for the video itself:** a lav on the presenter. The Mac's recording is for the test, not the soundtrack.

## Truth checks

Every claim on screen or in VO, and where it comes from. **Source: `lynkk-website-changes_3.md`** (section 11.11 unless
another section is named).

- "records the room, labels each speaker", "offline-first ... keeps recording and uploads later", "17 languages,
  Hinglish included" → 11.11, "1. Lynkk: best for in-person meetings on a Mac".
- "Lynkk has no phone app" → 11.11, "Good to know".
- "$4 a month (₹250 in India)", CTA "Get Lynkk Pro" → section 1, pricing rules. **No free-plan claim about Lynkk anywhere.**
- "Record now in the Mac app's menu bar", "same note as a Zoom or Google Meet call" → 11.11, "How AI note takers work in
  person"; TRUTHS-web, Meeting notes FAQ.
- "nothing joins anything", "no invite" → TRUTHS, Calls: "Nothing joins the call. No bot in the participant list. No calendar."
- Recording column (clock, live words) → TRUTHS, Calls.
- Note contents (summary, decisions, action items with owners and due dates, transcript) → 11.11 and TRUTHS, The note.
- "Speaker 1, Speaker 2 ... you rename them once" → 11.11 FAQ: "Can AI tell who is speaking in an in-person meeting?"
- "up to two hours" → TRUTHS, Calls.
- Mic tips (middle of the table, external mic in large rooms, away from air conditioning, say names early)
  → 11.11, "How to get clear audio in an in-person meeting".
- Consent → 11.11, "Do you need consent to record an in-person meeting?"
- Apple silicon, macOS 14.2 or later → TRUTHS, Requirements.
- **Otter:** phone and web, free 300 minutes a month, Pro $8.33/user/month, live transcript → 11.11, picks table and section 2.
- **Granola:** phone, Mac and Windows, you type your own notes, $14/user/month → 11.11, picks table and section 3.
- **Fireflies:** phone, same library as online calls, Pro $10/seat/month → 11.11, picks table and section 4.
- **Plaud:** recorder plus app, records offline → 11.11, picks table and section 5.
- **Apple Voice Memos:** free, transcript only, no speaker labels or summary → 11.11, section 6.
- "Lynkk is offline-first, and so is Plaud" → 11.11 FAQ: "Can an AI note taker work without internet?"

## Open questions (answers needed before build)

1. **The speaker-label result.** Chapter 4 has a placeholder for how the labels actually did in the test room. That comes
   from the footage.
2. **Who presents** on camera, and the room and date for the shoot.
3. **Prices on screen.** Competitor prices are from the companion page, checked November 2026. The boards carry a
   "checked November 2026" stamp. Confirm you want prices burned into the video at all, since they date it.
4. **Music.** The kit sources CC0, CC BY and Mixkit recordings. Mixkit music may not be registered with Content ID, and
   CC BY credits must go in the YouTube description. OK?
