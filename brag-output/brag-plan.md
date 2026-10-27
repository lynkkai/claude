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
- **Who is it for?** Sales and GTM teams: reps, sales leaders and RevOps, matching the site's "Built for your whole revenue team" section.
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

## Storyboard (102s, 1920x1080, 30fps, cuts on a 120 BPM grid)

The first 19 seconds (hook, reveal, capture, the note) are unchanged from v1.

| Time | Scene | Voice | On screen |
|---|---|---|---|
| 0.0-4.0 | **Hook** | "Your buyer can hear you typing, and they can tell you're not listening." | Live call with Priya. Messy notes type in, keycaps fly, her voice bars go flat, bubble: "Sorry, are you still with me?" "not listening." in red. |
| 4.0-8.0 | **Reveal** | "So stop typing. Lynkk remembers every sales conversation for you." | Lynkk mark spins in, wordmark, a memory graph draws out from the logo. |
| 8.0-13.5 | **01 / Capture** | "On Zoom, Meet, Teams, or in the room. Seventeen languages, even offline." | Four capture cards pop on each platform name, 17 counter with greetings, "Hinglish-native", "Works offline". |
| 13.5-19.0 | **The note** | "Every call becomes clear notes, decisions, and action items." | Lynkk app: summary streams in, Key decision and Next step cards, "3 action items, 2 commitments". |
| 19.0-26.0 | **02 / Before the call** | "Before your next call, just ask: what did we promise them? You get the answer, with its source." | Ask Lynkk types the question, answer streams with citations, three source calls. |
| 26.0-37.5 | **03 / Account memory** | "Every conversation becomes one connected memory. Thirty K at discovery. IT at the demo. Fifty K at commercials. Lynkk keeps the whole story." | The site's Corvane timeline: Oct 06 "We have $30K set aside", Oct 13 "Let's bring our IT team in", Oct 20 "We can stretch to $50K", each landing as it is spoken. A budget bar fills from $30K to $50K. |
| 37.5-46.5 | **04 / During the call: Cue (Beta)** | "During the call, Cue sits at the top of your screen. Ask it anything, or press command return, and it reads the conversation for you." | Mac screen with a live call. The buyer asks "How does this compare to what you quoted us last time?" Cue drops in at the top, ⌘↩ is pressed, and the answer appears. Footnote: "In beta in the Mac app, by invite. Only text leaves your Mac." |
| 46.5-54.0 | **05 / After the call** | "After the call, your follow-up is already drafted. Follow up in five minutes, not three days." | Email summary, cursor clicks "Send to 2", "Follow up in 5 minutes. Not 3 days." |
| 54.0-60.5 | **06 / Hand off** | "Action items land in Jira, answers reach Slack, and every brief is ready for your CRM." | Action items wire out to Jira, Slack and CRM. |
| 60.5-79.0 | **07 / For revenue teams** | "Lynkk is built for your whole revenue team. Reps walk into every call prepped, with the whole story." / "Sales leaders know every deal, without the quick update. Just ask what's blocking." / "And RevOps gets clean, consistent notes, connected to your calendar, Slack, and Jira." | The site's "Built for your whole revenue team" section, tabbed like the site. **Sales reps:** "Sell more. Type less." Ask Lynkk preps next week's calls. **Sales leaders:** "Know every deal. Without the 'quick update?'" Ask Lynkk answers "What's blocking our open deals?" with sources. **RevOps:** "Clean notes. Connected systems. Less chasing." Sales Call summary shape plus Calendar, Slack and Jira. |
| 79.0-86.0 | **08 / Dictation** | "On your Mac, just hold one key and talk. Your words are typed at the cursor, in any app." | "Hold one key and talk." A mail draft types itself while the dictation pill listens. |
| 86.0-94.5 | **09 / Privacy** | "Your conversations stay yours. Lynkk never trains AI on them, and you can export everything, any time." | Four tiles from the security page: No AI training, Export everything, HTTPS everywhere, Only text leaves your Mac. |
| 94.5-102.5 | **Outro** | "The call ends. The opportunity shouldn't. Lynkk. Start free at lynkk.ai." | Logo lockup, "Conversation intelligence for sales reps, leaders and RevOps.", "Start free", lynkk.ai, trust row. |

### Why there is no data residency scene

The security page (last reviewed 18 October 2026) says Lynkk and its providers "may process your
data in countries other than yours, including India and the United States". A "choose your
region" scene would contradict it, so the scene shows the privacy claims the site makes today.
If region selection ships, scene 09 is where it goes.

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
