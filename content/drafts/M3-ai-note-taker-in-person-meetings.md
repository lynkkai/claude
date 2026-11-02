---
platform: Medium
status: draft v1, needs review
primary_keyword: "ai note taker for in person meetings" (480/mo, SD 40, CPC $14.62)
secondary_keywords:
  - "in person meeting ai note taker" (90, CPC $22.39)
  - "in person ai note taker" (50)
  - "free ai note taker for in person meetings" (50, CPC $17.25)
  - "wearable ai note taker" (720)
  - "ai note taker device" (590)
  - "best ai note taker for conferences" (30)
intent: Transactional, with an informational layer
internal_links:
  - https://lynkk.ai/use-cases/field-interviews
  - https://lynkk.ai/features/meeting-notes
word_count: ~1,950
---

# AI Note Taker for In-Person Meetings: What Works When There Is No Meeting Link

**Subtitle for Medium:** Every AI note taker is built for calls. Here is what actually changes when
the meeting happens in a room, and how to set up for it.

---

Every AI note taker on the market was designed around a single assumption: there is a link.

You paste a Zoom or Google Meet URL, a bot joins the call, and the platform hands it a clean audio
stream with one participant per channel. Speaker separation is almost free, because the software
already knows who is speaking from the stream it arrived on. Consent is handled, more or less, by a
name in the participant list.

None of that exists in a room.

There is no link to paste, no participant list, no per-speaker channel. There is one microphone,
four people, a coffee machine, and someone sitting slightly too far from the table. If you have
tried to use a call-based note taker for a client visit, a site walk, a customer interview or a
coffee meeting, you have probably watched it produce a transcript that reads like one long run-on
sentence with no names attached.

In-person capture is a different engineering problem wearing the same product label. This is what
changes, and how to get a usable note out of a real room.

## Why in-person is genuinely harder

Four things break at once when you leave the call.

**One stream, many people.** On a video call, separating speakers is largely a routing problem. In
a room it is an acoustic one: the software has to cluster voices by their sound alone, then keep
those clusters stable for an hour. This is called speaker diarization, and it is the single
biggest quality difference between a good in-person note and a bad one. If a tool will not tell
you whether it labels speakers for in-person audio, assume it does not.

**Distance kills accuracy before the model ever sees it.** Speech recognition quality falls off
sharply with microphone distance, and no amount of model quality recovers detail that was never
captured. A phone face-down in the middle of a table of six is already a compromise. A laptop with
its lid half-closed at the end of the table is worse.

**Rooms are loud in ways calls are not.** Air conditioning, a street outside, chairs, cutlery, and
the particular problem of two side conversations starting while the main one continues. Call
platforms do a lot of noise suppression before a note taker ever receives the audio. Record in a
room and you get the room.

**Nobody is announced.** A bot in a call shows up in the participant list. In a room, the only
thing that tells people they are being recorded is you, out loud. That is not a technicality, and
I will come back to it.

## The four ways people actually capture in person

Setting marketing aside, there are four real options, and they fail differently.

**1. Your phone's voice recorder.** Free, always with you, and genuinely fine for a two-person
conversation across a small table. It falls apart with groups, it gives you an audio file rather
than a note, and you will not go back and listen to a 50-minute recording. Realistically it is a
capture device that needs something else to do the thinking.

**2. Dedicated hardware.** Pocket recorders and wearable pins built for this job, with better
microphones than a laptop and long battery life. If you do this all day, every day, in difficult
rooms, the microphone quality is a real advantage. The trade-offs are that it is one more device
to charge and carry, your notes live in that vendor's app rather than alongside your call notes,
and the search problem splits in two: in-person notes here, call notes there.

**3. The laptop you already brought.** A Mac or PC app that records the room through the built-in
microphone. The microphone is mediocre compared to dedicated hardware, but the laptop is already
open, already charged, and, crucially, the notes land in the same place as your call notes. For
most knowledge workers this is the practical answer, and it is the one with the lowest chance of
you forgetting the device at home.

**4. A note-taking bot you dial into the room.** Some people start a Meet or Zoom call on a laptop
in the room purely so their usual bot can join and listen. It works, and it is a hack. You are
paying a quality tax by routing room audio through a platform tuned for one-person-per-channel,
and you look slightly odd doing it.

There is no universally correct answer here. There is a correct answer for how often you do this
and how hard your rooms are.

## Microphone placement matters more than the tool

This is the part no comparison post covers, and it changes output quality more than switching
vendors will.

- **Put the device between the people who talk most**, not in the geometric centre of the table.
  In a sales meeting that usually means closer to the customer than to you. You already know what
  you said.
- **Hard surface, not soft.** Directly on the table beats on a notebook, a jacket or your lap.
- **Lid up, screen on, if you are recording on a laptop.** Closing the lid muffles the microphone
  and may suspend the machine mid-recording.
- **Restaurants and cafes are the hardest rooms there are.** Booths beat open floors, corners beat
  centres, and a device on the table beats one in a pocket by a wide margin. If the meeting
  genuinely matters, do not take it over lunch.
- **Say names early.** "Thanks for joining, Priya, and you brought Neha from IT." You have just
  given every diarization system in existence a labelled sample of two voices, in the first ten
  seconds. This one habit improves speaker labelling more than any setting you can change.
- **Check the battery and the storage before you walk in**, especially for a long session. An
  interview that stops at 40 minutes because a disk filled is not recoverable.

## Consent, which is the part people skip

In a call, the bot in the participant list does some of this work for you. In a room, nothing does.

The rules vary by where you are. Some US states require only one party to consent, others require
everyone. The UK, the EU, India, Canada and Australia all differ again, and the answer changes
depending on whether the conversation is private, who holds the recording, and what you do with it
afterwards. If you want the detail, Lynkk's own guide to
[whether it is legal to record a meeting](https://lynkk.ai/blog/is-it-legal-to-record-a-meeting)
breaks it down by state and country.

The practical version is short. **Ask out loud, before you press record, in the language the
conversation will happen in.** A script that works:

> "May I record our conversation? It is only so I don't miss anything you say, and I'll share the
> notes with you afterwards. You can ask me to stop at any time."

Three things make this land rather than create a pause in the room. Ask before you start, not
after. Say what it is for. Offer to share the notes, and then actually share them, which turns the
recording from something done to the other person into something done for them.

For field research and interviews, where the person may be less familiar with recording and the
language may not be English, Lynkk publishes a consent script in both English and Hindi on its
[field interviews page](https://lynkk.ai/use-cases/field-interviews). Translating it into the
language of the room is worth the two minutes.

## What a usable in-person note actually contains

A transcript is not a note. If you are evaluating tools, these are the output features that
determine whether you ever open the thing again:

- **Speaker labels that survive the whole session.** Not just "Speaker 1" and "Speaker 2" for the
  first five minutes before they drift.
- **Timestamps you can click to hear that moment.** In-person transcription will get some lines
  wrong. What saves you is being able to jump straight to the audio for the one line that matters,
  rather than re-listening to an hour.
- **Action items with an owner and a date**, separated from the summary. "Jamie sends the security
  overview by Friday" is useful. "The team discussed next steps" is not.
- **Decisions kept apart from discussion.** What was agreed, and the context it rested on.
- **Search across every conversation, not one note at a time.** The value of in-person notes
  compounds only if the fourth visit to a customer can see the first three.
- **The commitments you made.** The sentences beginning "I'll send" are the ones that cost you a
  deal when they are forgotten, and they are easy to extract and easy to miss.

## If your meetings are not in English

This is where in-person and multilingual collide badly. Real conversations in India, and in plenty
of other markets, move between languages inside a single sentence. Hindi and English blend into
Hinglish constantly, and most speech recognition handles it by picking one language and mangling
the rest.

If that is your reality, ask vendors a specific question rather than a general one. Not "do you
support Hindi", which almost everyone will say yes to, but "what happens when a sentence starts in
Hindi and ends in English". The answers separate the tools quickly.

## A short checklist for choosing

1. Does it record in person at all, or only join calls?
2. Does it label speakers for room audio, and does it say so plainly?
3. Does it work with no internet, and upload later? Field visits and basements are real.
4. What is the maximum length of one recording?
5. Can you click a line of transcript and hear that moment?
6. Do in-person notes land in the same searchable place as your call notes?
7. What does it do with your audio, and does the vendor train models on it?
8. Is there a free tier large enough to test it on real meetings before you pay?

Question 7 deserves more weight than it usually gets. You are recording other people, often
customers, sometimes about their budgets and their problems. Read the security page, and prefer a
vendor that publishes what it does **not** do over one that just says "enterprise-grade".

## How Lynkk handles it, including the limits

Full disclosure: I work on Lynkk, so take this as the vendor's own account rather than a review.

Lynkk records in-person conversations through the Mac app, and the same notes land alongside notes
from Zoom, Google Meet and Microsoft Teams calls, in one searchable place. When the recording ends
you get a summary, decisions, action items with owners, and a full transcript with each speaker
labelled, where clicking any line plays the call from that moment. Action items go to Jira only
when you press send, and follow-up emails are drafted for you to send yourself rather than sent
automatically.

For field work, the Mac app records with **no internet at all** and uploads when you are back
online, which is the specific reason it exists: field research happens where there is no signal.
It handles Hindi and Hinglish, including sentences that switch mid-way, along with Spanish, French,
German, Portuguese, Italian, Dutch, Japanese, Chinese, Korean, Arabic and Russian, with Tamil,
Telugu, Marathi and Bengali in beta.

The limits, stated plainly:

- **Offline recording is Mac only.** The web app needs an internet connection.
- **One recording maxes out at two hours.** For a longer session you start a new one.
- **The free plan gives unlimited recordings and transcripts, but the AI notes are capped at your
  first 5 hours**, counted over the life of the account rather than per month. Past that, new
  meetings still record, transcribe and appear in search, but you need Pro, at $15 a month, for
  the summary and action items.
- **It is not end-to-end encrypted**, and Lynkk says so on its security page, because the service
  has to read a recording to write a note. What it does commit to is that your conversations are
  not used to train AI models.
- **There is no in-room announcement.** Like any device-based recorder, the only thing that tells
  the room is you. Use the script above.

If you want the output format in detail, the [meeting notes page](https://lynkk.ai/features/meeting-notes)
shows what every note contains. Starting is free and takes no card.

---

## The thing worth remembering

The tool matters less than three habits: ask for consent out loud before you press record, put the
microphone closer to the person you are there to listen to, and say everyone's name in the first
minute. Do those three things with a mediocre recorder and you will get a better note than someone
doing none of them with the best hardware on the market.

---

## Publishing notes

**Medium tags:** AI, Productivity, Sales, Note Taking, Meetings
**Suggested Medium title A/B:**
- A: "AI Note Taker for In-Person Meetings: What Works When There Is No Meeting Link"
- B: "Every AI Note Taker Assumes There Is a Zoom Link. Here Is What to Do in a Room."

**Canonical:** publish Medium-first, no canonical to lynkk.ai. This post is written to rank on
Medium's authority for a query lynkk.ai does not currently have a page for. Do not cross-post to
the Lynkk blog without rewriting, or the two will compete.

**Open items before publishing:**
1. ~~Confirm the "is it legal to record a meeting" blog URL.~~ **Verified 2026-11-02:**
   `/blog/is-it-legal-to-record-a-meeting` is the real slug. Both other internal links
   (`/use-cases/field-interviews`, `/features/meeting-notes`) are verified live too.
2. **Confirm the language count.** The pricing page says "every language, Hinglish included", the
   homepage FAQ says 17 languages, and the field interviews page lists 13 named plus 4 in beta.
   I used the specific list rather than the number. Worth aligning site-wide.
3. **Byline.** The "I work on Lynkk" disclosure assumes a Lynkk team member publishes this. If it
   goes out under a personal account with no affiliation stated, that disclosure has to stay in
   regardless; Medium readers and the FTC both expect it.
4. No competitor is named with a specific claim anywhere in this draft, deliberately. I have not
   tested Plaud, Otter or the others on in-person audio, so I have written about device categories
   instead of making comparative claims I cannot support.
