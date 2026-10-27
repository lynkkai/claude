# Lynkk homepage demo video: plan

Made with the /brag-slim method (https://latent-spaces.github.io/brag/), adapted to Lynkk's
own design system as it appears on https://lynkk.ai today.

## The brief

- **Where it lives:** the lynkk.ai homepage hero. It will autoplay **muted**, so every line the
  voice says is also on screen as kinetic type. Sound is a bonus, not a requirement.
- **Focus:** the first 20 seconds. Hook, reveal, capture, and the note itself all land before 20s.
- **Voice:** the supplied take ("Your buyer can hear you typing...") opens the video as recorded.
  Every later line is generated in a clone of that same voice (the second, Fenrir take).

## Answers before planning

- **What is it?** An AI meeting assistant that remembers every sales conversation and turns it into
  notes, follow-ups, action items and your next move.
- **Who is it for?** Sales and customer-facing teams who live on calls.
- **What sets it apart?** Memory across calls (ask a question, get the answer with its source),
  plus capture anywhere: Zoom, Meet, Teams, in person, 17 languages, offline.
- **Hook:** the pain everyone recognises: typing notes while the buyer is talking.
- **Visual hook:** a live call where keycaps fly off your notes and the buyer asks "Sorry, are you
  still with me?"
- **Share caption:** see `share-copy.txt`.

## Visual identity (taken from lynkk.ai CSS)

| Token | Value | Use |
|---|---|---|
| Canvas | `#111` / coal `#171717`, `#1d1d1d` | background, app chrome |
| Paper | `#fff`, `#f9f9fa` | light cards (email, action items) |
| Violet | `#7063be`, lavender `#beb4fb`, tint `#e2e0f2` | eyebrows, Ask Lynkk, citations |
| Orange | `#f57b3a` with warm gradient beds | product "beds" as on the site |
| Live | `#ff3b30` | recording dots, "not listening" |
| Display font | Schibsted Grotesk 500, tracking -0.04em | headlines |
| UI font | Inter | product UI |
| Mono | JetBrains Mono | eyebrows like `01 / Capture`, labels |
| Logo | the site's own SVG mark | reveal and end card |

Product UI is rebuilt from the site's own illustrative data (Corvane Logistics, Priya Shah,
Jamie Davis). These are the fictional sample accounts lynkk.ai already shows, so no real customer
data appears.

## Storyboard (47s, 1920x1080, 30fps, cuts on a 120 BPM grid)

| Time | Scene | Voice | On screen |
|---|---|---|---|
| 0.0-4.0 | **Hook** | "Your buyer can hear you typing, and they can tell you're not listening." | Live call with Priya. Messy notes type in, keycaps fly, her voice bars go flat, bubble: "Sorry, are you still with me?" Headline words land with the voice; "not listening." in red. |
| 4.0-8.0 | **Reveal** | "So stop typing. Lynkk remembers every sales conversation for you." | "So stop typing." Then the Lynkk mark spins in, wordmark, a memory graph draws out from the logo (Discovery, $30K to $50K, IT review...). "that remembers every sales conversation for you." |
| 8.0-13.5 | **01 / Capture** | "On Zoom, Meet, Teams, or in the room. Seventeen languages, even offline." | "Every call. Every language. Even offline." Four capture cards pop on each platform name (meeting bot, Chrome extension, Mac app, in the room). 17 counter with greetings cycling, "Hinglish-native", "Works offline". |
| 13.5-19.0 | **The note** | "Every call becomes clear notes, decisions, and action items." | Lynkk app window on a warm bed. Summary streams in, Key decision and Next step cards pop as they are named, "Nothing slips through: 3 action items, 2 commitments". |
| 19.0-26.0 | **02 / Before the call** | "Before your next call, just ask: what did we promise them? You get the answer, with its source." | "Wait, what did we promise them?" Ask Lynkk types the question, answer streams with citations, three source calls appear. |
| 26.0-33.0 | **03 / After the call** | "After the call, your follow-up is already drafted. Follow up in five minutes, not three days." | Email summary drafts itself, cursor clicks "Send to 2", toast "Summary sent". "Follow up in 5 minutes. Not 3 days." with the strike. |
| 33.0-39.5 | **04 / Hand off** | "Action items land in Jira, answers reach Slack, and every brief is ready for your CRM." | Action items wire out to Jira, Slack and CRM cards as each is named; checkboxes tick. |
| 39.5-47.0 | **Outro** | "The call ends. The opportunity shouldn't. Lynkk. Start free at lynkk.ai." | Site's own line, then the logo lockup, "Start free" and lynkk.ai, trust row. |

## Sound

- Hook is dry: just the voice and keyboard clatter, with the music bed muffled underneath.
- The bed opens up on the beat exactly at the reveal and ducks under every voice line.
- Effects (card pops, click on Send, logo hits) sit on the same beat grid, quiet and warm.
- Final mix: -16 LUFS integrated, -1.5 dBTP.

## Credits and licences

- Music: "Happy Beats / Business Moves Vol. 1" by Sascha Ende, ende.app, **CC BY 4.0**.
  Credit line to keep somewhere public (site footer, credits page or video description):
  `Music: Sascha Ende, ende.app (CC BY 4.0)`.
- Sound effects: Kenney.nl, CC0.
- Fonts: Schibsted Grotesk, Inter, JetBrains Mono, Noto Sans (all SIL Open Font License).
- Voice: lines after the hook are AI-generated (Chatterbox) from the supplied voice sample. The
  model embeds an inaudible watermark identifying the audio as AI-generated.
