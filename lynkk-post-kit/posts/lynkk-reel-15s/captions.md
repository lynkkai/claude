# Lynkk reel, fast cut: captions, hooks and edit notes

Built with the lynkk-design skill. Claims from `docs/TRUTHS.md` (checked 2026-09-29).
Sample data (Q4 launch sync, Acme, Priya, Sam, Alex) is fictional.

## Files

| File | What |
|---|---|
| `out/lynkk-reel-with-hook.mp4` | 1080x1920, 30 fps, 20 s, with music. Opens on the hook "Your meeting ended. The work didn't." |
| `out/lynkk-reel-no-hook.mp4` | Same reel and music with the hook headline left out, so you can type your own hook over the first 2 s in the editing app |
| `out/music.wav` | The music bed on its own (20 s, -14 LUFS), if you want to re-cut or swap it |

Render again:

```bash
python3 posts/lynkk-reel-15s/music.py
node scripts/video.mjs posts/lynkk-reel-15s --audio posts/lynkk-reel-15s/out/music.wav --name lynkk-reel-with-hook
node scripts/video.mjs posts/lynkk-reel-15s --audio posts/lynkk-reel-15s/out/music.wav --query hook=0 --name lynkk-reel-no-hook
```

## Music

An original track made from code in `music.py`, so there is nothing to license: 120 BPM, A minor
(Am F C G), light electronic with a four-on-the-floor kick. A build sits under the hook, the beat
drops when the Lynkk mark lands at 2.0 s, the arpeggio lifts an octave for the feature cuts at
10 s, every scene change gets a hit and every website scroll stop gets a short swish. It ends on one
chord at 19 s.

To use a trending sound instead, mute this track in the Instagram or TikTok editor and add the
sound there. The cuts sit on a 120 BPM grid, so any track near 120 or 60 BPM lines up.

## Timeline (every cut is on the beat)

| Time | Scene |
|---|---|
| 0.0 | Hook, over the build |
| 2.0 | Lynkk mark, the drop |
| 3.0 | lynkk.ai scrolling: a new stop every second (capture, briefing, action items, Mac, Start free) |
| 10.0 | Meeting Brief |
| 11.0 | Dictation on the Mac |
| 12.0 | 17 languages |
| 13.0 | Ask Lynkk (Pro) |
| 14.0 | Who it's for |
| 16.0 | Start free at lynkk.ai (holds to the end) |

## Hooks for the first 2 seconds

Pick one for the no-hook version. All of them hold to TRUTHS.md.

1. Your meeting ended. The work didn't. (in the video)
2. Nobody on the call took notes. Lynkk did.
3. POV: you never write meeting notes again.
4. Your next meeting will write its own brief.
5. Record any call on your Mac. Nothing joins it.
6. Hold one key, talk, and it types for you.
7. Sales calls: walk in knowing what's still open.
8. Stop taking notes. Start finishing meetings.

---

## Instagram Reels

**Option A (pairs with the hook in the video)**

```
Your meeting ended. The work didn't.

Lynkk records the call and writes the Meeting Brief: decisions, open questions, and action items with owners and due dates.

Record on the Mac with nothing joining the call, in Chrome, with the meeting bot, or with your mic in the browser.

Transcripts in 17 languages. Start on the Free plan.

lynkk.ai, link in bio.

#meetingnotes #productivity #aimeetingassistant #worksmarter #lynkk
```

**Option B (short)**

```
Talk in the meeting. Lynkk writes it up.

Notes, decisions and tasks with owners, after every call. Send tasks to Jira from the note.

Start free. lynkk.ai, link in bio.

#meetingnotes #productivity #aimeetingassistant #lynkk
```

## TikTok

```
POV: you never write meeting notes again.
Lynkk records the call and pulls out the decisions and tasks. Start free at lynkk.ai
#meetingnotes #productivity #worktok #lynkk
```

## YouTube Shorts

Title:

```
Your meeting ended. The work didn't. | Lynkk
```

Description:

```
Lynkk is an AI meeting assistant. It records your meetings, writes the notes, and pulls out the tasks.

After every call you get a Meeting Brief: decisions, open questions, and action items with owners and due dates. Send action items to Jira from the note. Ask Lynkk (Pro) answers from your own notes, with the sources.

Record on the Mac (no bot joins the call), with the Chrome extension, with the meeting bot for Google Meet, Zoom and Teams, or with your mic at lynkk.ai. Transcripts in 17 languages, four of them in beta.

Start free: https://lynkk.ai

#Shorts #MeetingNotes #AIMeetingAssistant #Productivity #Lynkk
```

## LinkedIn

```
Most meetings end the same way: nobody is sure who owns what.

Lynkk is an AI meeting assistant that records the meeting and does the write-up:

- A Meeting Brief after every call: decisions, open questions, and action items with owners and due dates
- Send action items to Jira from the note, one issue each
- A morning briefing email before your meetings: who you're meeting and what's still open
- Ask Lynkk (Pro): ask your own notes what was decided, with the sources
- On the Mac, nothing joins the call, and you can hold fn to dictate into any app

Transcripts in 17 languages, four of them in beta. Teams get a workspace for up to 10 seats, and everyone in it gets Pro.

Start free: https://lynkk.ai
```

## X

```
Your meeting ended. The work didn't.

Lynkk records the call and writes the brief: decisions, open questions, tasks with owners. Send them to Jira from the note.

Start free at lynkk.ai
```

## Alt text

A 20 second vertical video for Lynkk, set to an upbeat electronic track. It opens on "Your meeting
ended. The work didn't." over a card that lists missing notes, tasks and decisions. The Lynkk mark
spins in on the beat drop. The lynkk.ai site scrolls in a browser, section by section, with the
headlines "Record any meeting. Online or in person.", "Walk in prepared. Leave with the decisions.",
"Every task gets an owner. Send it to Jira from the note." and "Record any call. Nothing joins it."
Quick scenes follow: a Meeting Brief, dictation landing words at the cursor, "17 languages. Four of
them in beta.", an Ask Lynkk answer with a source, and who it's for. It ends on an orange plate:
"Stop taking notes. Start finishing meetings." and the button "Try it free at lynkk.ai".
