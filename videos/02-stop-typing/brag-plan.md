# Short #2: Stop Typing During Discovery Calls

Source: `lynkk-shorts-content.csv`, row ID 2 (Cluster A. Sales follow-ups).
Built with the /brag (brag-slim) workflow, adapted from a 20s launch video to a VO-led vertical short.

| Field | Value |
|---|---|
| Format | Vertical 1080x1920, 30fps, ~38.8s |
| Feature | Meeting notes: summary, decisions, action items, transcript with speaker labels |
| Primary keyword | AI note taker for sales calls |
| Hook (0-3s) | "Your buyer can hear you typing." |
| On-screen text | "Present, not preoccupied." / Summary, Decisions, Action items, Transcript |
| CTA | Start free at lynkk.ai |
| Tone | `polished` with a playful hook: calm, editorial, matches lynkk.ai |

## Angle

The sound of typing is the villain. The video opens on loud, messy keystrokes over a buyer who is mid-sentence,
then goes quiet the moment Lynkk takes over the notes. Silence becomes the product benefit: you get to listen.

## Visual identity (from lynkk.ai, captured 2026-10-26)

- Headlines: Schibsted Grotesk, weight 500, tracking -0.04em, two-tone lines (second line at 50% opacity), like the site's section headers.
- UI: Inter. Labels: JetBrains Mono, uppercase, small.
- Colors: ink `#111111`, coal `#171717` / `#1d1d1d` / `#2e2e2e`, sand `#ece9e2`, paper `#f9f9fa`,
  violet `#7063be`, violet tint `#e2e0f2`, lavender `#beb4fb`, live red `#ff3b30`, leaf `#93b45c`, pink `#f7b7ef`.
- Product UI: the dark "Corvane Logistics · Discovery call" note from the site hero, rebuilt in HTML.
  All names and quotes (Corvane, Priya Shah, Jamie Davis, "$30K set aside", "bring our IT team in") are the
  site's own illustrative data; the video labels it "Illustrative data" the same way the site does.
- Warm hero gradient (cream to copper) frames the product, as on the site.

## Music and sound

- Bed: "Happy Beats / Business Moves Vol. 10", Sascha Ende, ende.app (CC BY 4.0). 109.96 BPM, beat = 0.5457s.
  Every scene cut sits on a beat from the track's beat grid.
- Hook: real keyboard keypress samples (CC0, Kenney), loud and messy; they stop dead at the reveal.
- Soft impacts on the reveal and punchline, quiet clicks on tab switches, one bell on the CTA.
- Music ducks under VO in the final mix (VO not recorded yet; see "VO" below).

## Storyboard (cuts on beats)

| # | Time | VO | Picture |
|---|---|---|---|
| 1 Hook | 0.00-5.19 | "Your buyer can hear you typing. And they can tell you're not listening." | Google Meet tile: Priya talking, live caption. Below, a notes file typing furiously with typos. Jamie's mic meter jumps on every keystroke. On "not listening", Priya's caption blurs out. |
| 2 Problem | 5.19-11.47 | "Discovery calls are where deals are won, but most reps spend them half-listening, half-typing." | Screen splits in two: HALF LISTENING / HALF TYPING. Pain, Budget, Timeline chips fall past, struck through: MISSED. |
| 3 Reveal | 11.47-14.73 | "Lynkk takes the notes for you." | Typing stops. Dip to sand. Lynkk mark lands on the beat, then the red-dot pill "Lynkk is taking notes". |
| 4 Product | 14.73-24.01 | "Every call gets a summary, the decisions, the action items, and a full transcript with speaker labels, so you know exactly who said what." | The Lynkk note in its warm frame. Tabs Summary, Decisions, Action items, Transcript light up and tick as each word is spoken. Transcript rows with speaker labels; labels pulse on "who said what". |
| 5 Present | 24.01-31.65 | "That means you can actually ask the second question. And the third. The ones that uncover real pain." | Back on the call, no typing. QUESTION 02, QUESTION 03 counter. Jamie asks, Priya answers. Violet chip: "Pain point · captured by Lynkk". |
| 6 Punchline | 31.65-34.92 | "Be present, not preoccupied." | Big two-tone type on ink. |
| 7 CTA | 34.92-38.80 | "Get Lynkk free at lynkk.ai." | Sand end card: Lynkk mark, "Start free at lynkk.ai", black "Start for free" button gets clicked. |

## VO

Scratch VO from Kokoro TTS, voice `am_fenrir` at speed 1.1: the same voice as the earlier Lynkk short
(`brag-male.mp4`, verified by matching its audio). Every line fits its slot at that speed. Measured timing lives in
`src/vo_timing.json` and drives captions, tab clicks, the question counter and the pain chip.
Burned-in captions stay on regardless, since most shorts are watched muted.

## Safe zones

Key content sits between y=200 and y=1480 and x=60 to x=1020, clear of Shorts/Reels/TikTok UI at the bottom and right.
