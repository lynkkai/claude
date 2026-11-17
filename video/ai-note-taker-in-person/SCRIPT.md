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

**The presenter records the narration.** `NARRATION.md` is the sheet to read from: every line with its in and out
point on the 2:00 timeline, the window length, and which lines land on a music bar. Record each line as its own
take with room tone either side, and they drop onto the grid in the edit.

Speech totals about 82 seconds of the 120, at an unhurried pace, so a presenter can be slower or more expressive
than the budget and still fit. The copy was cut to make that true: the first 2:00 draft ran 138 seconds of speech
in a 120 second video, with 16 of its 17 lines over their windows. The lines in the tables above are the measured
versions.

An earlier synthetic read of these lines was scrapped: it was the wrong instrument for a host-led video.

**Music:** "Ramp It Up" by Ahjay Stelino, from Mixkit, under the Mixkit Stock Music Free License. The same track as
the Lynkk for Mac teaser, already cleared and credited by the video kit, and already at 120 BPM, the grid this
script is written on. Cut at bar lines: a short intro, the groove through the body, the track's own drop placed on
1:40 where the picks chapter starts, and its closing hit on 1:58 under the end card. The ambient breakdown in the
middle of the track is cut out, so the energy never dips.

The bed on the previz measures -15.0 LUFS integrated, true peak -4.4 dBFS, 120.000 s. It sits a little under the
-14 delivery target on purpose: once the presenter's voice is on top, the whole mix gets balanced to -14 with the
music ducked about 12 dB under the voice.

Mixkit music may not be registered with YouTube Content ID, and the CC BY credits go in the video description.

## The graphics are built

All ten inserts and the five chapter cards are built and rendered, in `film/` (the code) with
`in-person-2min-previz.mp4` beside it: the whole 2:00 at 1920x1080, with the scratch soundtrack on it.

Where the team's footage goes, a slate names the shot and prints the line said over it, so the two minutes can be
watched end to end now and the pacing judged before anyone books a room.

| Built | Shown as |
|---|---|
| G1 cold open, chapter cards 1 to 5, G3 device board, G4 mic map, G5a Record now, G5b recording column, G5c the note, G6 speaker labels, G7 offline and back online, G8 picks board, G9 end card | finished frames |
| The presenter on camera, the room montage, the three devices, asking consent, the label tips | slates naming the shot and its voice-over |

**Checked on the render:** 3600 frames, 1920x1080 at 30 fps, 120.000 s, and the audio runs the full length.

**The first build was slideware and was rebuilt.** It had no camera moves at all, every cut landed on a static
frame, scenes held still for 8 to 12 seconds, and Remi appeared in four of eleven scenes. The rebuild follows the
kit's motion rules: every scene has a camera that is always moving (`src/ui/motion.tsx`), every cut carries motion
across it (a whip, a punch-in or a slam down), and Remi flies through every scene and triggers what arrives: it
bonks Record now, rides the transcript and knocks a speaker label into its real name, points out each bad mic
placement, and lands on the action item and on the CTA.

**What is still a stand-in in the graphics:** the transcript lines in the speaker-label insert, and the room
behind the cold open (a kit wallpaper, not your room). Both are one-line swaps once the test is filmed, and
`film/README.md` says where.

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
