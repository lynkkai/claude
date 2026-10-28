# Lynkk preset

Read this before any Lynkk video, together with `/memory/lynkk-brand.md` (full brand
memory) and `/CLAUDE.md` (house writing rules). This file is the video-specific layer:
what goes on screen, what must not, and the shot lists that are already approved in
shape so you are not starting from a blank page every time.

## Non-negotiables

- **Spelling.** Lynkk, double k. Never Lynk, Linnk, Link AI, LYNKK in body copy. Several
  unrelated products use the near-miss spellings, so a typo in a frame points the viewer
  at a competitor. Check every frame of on-screen text, including the URL card.
- **URL on screen.** lynkk.ai (lowercase).
- **No em dashes or en dashes in any on-screen word or voiceover line.** Use a comma,
  colon, parentheses, or two sentences. Plain hyphens are fine for ranges and compound
  words. This is a repo-wide rule and it applies to captions and subtitle files too.
- **No invented claims.** The feature list below is what the site says. Anything in the
  "to confirm" section of the brand memory (platform names, CRM names, language counts,
  regions, certifications) does not go on screen until the team confirms it. A video is
  harder to quietly correct than a web page.
- **No competitor marks or logos**, and no screenshots of other meeting tools.

## Asset gate

Before building, get these. The brand memory was written from search results because the
site was not reachable from the build environment, so it has the words but not the
pixels. Ask once, in one message, and say what you will use as a stand-in meanwhile:

- [ ] logo: SVG, both the mark alone and the wordmark
- [ ] brand colors: exact hex values, and which one is the accent
- [ ] fonts: the real files or the family names, licensed for video
- [ ] product screenshots: the meeting view, the notes and action items output, the
      knowledge graph or search view, the Mac app including dictation at the cursor
- [ ] any existing motion or a reference film the team likes

Until the real tokens arrive, use `assets/lynkk-tokens.css`, which is deliberately
neutral and marked as placeholder, and say in the handover that colors and type are
stand-ins. Do not guess a palette from the logo of a similarly named company.

## The story that works

Lynkk's differentiator is the lifecycle: one AI before, during and after the meeting, not
a transcriber that wakes up at the end. Structure the film on that spine, because it is
both true and the thing competitors cannot say.

Three acts, in this order, whatever the runtime:

1. **Before.** Context from past meetings surfaces: what was discussed, what is still
   open, who said what. The viewer feeling: you walk in ahead, not cold.
2. **During.** Lynkk is in the meeting and speaks when asked. Pull up a document, ask
   what was decided last time, get an answer by voice, live.
3. **After.** Within about 30 seconds: structured notes, action items assigned, CRM
   fields updated, Jira tickets created, everything searchable.

Then the payoff card: online and in person, multilingual, offline-first, your choice of
data region. Then the lockup and lynkk.ai.

## Approved on-screen lines

Short enough to read in a shot, and drawn from site copy:

- One AI for every meeting: before, during and after
- Start ahead, not cold
- It joins. It speaks when you need it. It remembers everything.
- Notes, action items, answers. In about 30 seconds.
- Assigned, not just listed
- CRM updated. Tickets created.
- Every meeting, searchable
- Online and in person
- Multilingual. Offline-first.
- Your data, your region
- Connect anything via MCP
- Start free at lynkk.ai

Keep each card to one line. The full long description in the brand memory is for stores
and directories, not for frames.

## Voiceover, if used

About 2.0 words per second, so a 20 second film carries roughly 40 words. One pass that
fits:

> Every meeting starts cold. Lynkk starts ahead. It knows what was discussed, and what is
> still open. It joins the call, and speaks when you need it. Thirty seconds after you
> hang up: notes, owners, tickets, answers. Start free at lynkk.ai.

Check the line count against the beat grid before generating audio, and keep 300 ms of
silence after each sentence.

## Ready shot lists

Copy one into `shots.md` and adjust times to the beat grid. At 120 BPM a bar is 2.0 s,
which is why these land on even numbers.

### A. 15 second launch film, 16:9

| # | t_in | t_out | shot | on screen | motion | sound |
|---|------|-------|------|-----------|--------|-------|
| 1 | 0.0 | 2.0 | Cold open: an empty calendar slot filling with a meeting | "Every meeting starts cold" | card slides up, type staggers in | pad in, tick on the card |
| 2 | 2.0 | 5.0 | Before: context cards fan out from the meeting, past decisions and open items | "Start ahead, not cold" | the meeting card morphs into the context stack, never cuts | whoosh on the morph |
| 3 | 5.0 | 8.0 | During: the call view, Lynkk answering by voice, waveform responding | "Speaks when you need it" | cursor press, waveform reacts on the beat | click, then a short voice bed |
| 4 | 8.0 | 11.0 | After: notes, assigned action items, a CRM field updating, a Jira ticket appearing | "In about 30 seconds" | three panels resolve in a 60 ms stagger | three ticks, rising |
| 5 | 11.0 | 13.0 | Knowledge graph: every past meeting connecting, one node highlights on search | "Every meeting, searchable" | slow push in, nodes settle | low swell |
| 6 | 13.0 | 15.0 | Lockup | Lynkk wordmark, "Start free at lynkk.ai" | wordmark settles with a small overshoot | thump, then silence |

### B. 20 second feature explainer with voiceover, 16:9

Same spine, with the three acts given 4 seconds each, a 3 second payoff card for online
and in person plus multilingual, offline-first and data region, and a 3 second lockup.
Use the voiceover above and put every visual accent on the word it illustrates.

### C. 10 second vertical cut, 9:16

| # | t_in | t_out | shot | on screen | motion |
|---|------|-------|------|-----------|--------|
| 1 | 0.0 | 2.5 | Phone-shaped meeting card with context stack behind it | "Start ahead" | stack slides in from below |
| 2 | 2.5 | 5.0 | Voice answer in the call | "It speaks when you need it" | waveform on the beat |
| 3 | 5.0 | 8.0 | Notes, owners, tickets stacking vertically | "Notes. Owners. Tickets." | each lands on a beat |
| 4 | 8.0 | 10.0 | Lockup | lynkk.ai | wordmark settles |

Keep type out of the bottom 15% where the platform UI sits, and burn in captions, since
these play muted.

## Where files go

Build in `video/<piece-name>/` at the repo root: `brand.md` (resolved assets and tokens),
`style.md`, `shots.md`, `beats.json`, `index.html`, `out/`. Keep `out/` masters out of git
unless the team asks for them, and note the paths in the handover instead.

Reuse `style.md` across pieces. The second Lynkk video should cost an hour, not a day,
and that only happens if the first one leaves its decisions written down.
