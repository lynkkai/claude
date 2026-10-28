# Critique loop

The first render is a draft. The loop below is where the quality comes from, and it is
the cheapest part of the process to run because it needs no new ideas, only honest
looking.

## Protocol

1. Render at working quality (half size is fine, full frame rate is not optional since
   pacing problems hide at low frame rates).
2. Extract stills across the timeline and actually look at them:
   ```bash
   ffmpeg -i out/film.mp4 -vf fps=2 out/review/%03d.png
   ```
   Also watch the strong accents at full rate, because flicker and overlap live between
   the stills.
3. Score each dimension below from 1 to 10 and write the scores into `critique.md` with
   one concrete sentence of evidence each. A score without evidence is a guess.
4. Fix only what scored below 8, lowest first.
5. Re-render, re-score, repeat. Stop when nothing is below 8, or when two rounds in a row
   produce no gain, which means the problem is in the concept rather than the execution:
   go back to `shots.md` and say so.

Keep every round in `critique.md`. The user wants to see what moved from 6 to 8 and why.

## Rubric

| Dimension | 1 to 3 | 4 to 7 | 8 to 10 |
|---|---|---|---|
| Composition | Everything centered, no depth | Reasonable framing, some dead space | Deliberate hierarchy, confident negative space |
| Motion quality | Linear, uniform, jittery | Eased but uniform in rate | Varied easing, stagger, weight, one clear lead per moment |
| Continuity | Hard cuts between unrelated states | Mixed cuts and transitions | Shared elements morph, the eye never loses its place |
| Type | Default fonts, too much copy | Brand font, slightly long lines | Brand font, under seven words a card, readable in its shot |
| Color | Gradient slop or pure black and white | On-brand but flat | Three to five colors, accent used only where attention belongs |
| Texture and finish | Flat vector template | Some grain or vignette | Grain, vignette and timing imperfection that read as craft |
| Sound sync | Silent, or music over unrelated motion | Music on grid, few effects | Accents on beats, one sound per motion, silence used on purpose |
| Brand fidelity | Invented logo, wrong colors, misspelled name | Right assets, loose application | Real assets, correct spelling, correct claims, would pass brand review |
| Legibility | Text clipped or unsafe margins | Mostly safe | Safe in 16:9, 9:16 and 1:1, readable muted |
| Story | A list of features | A sequence with an ending | A spine: tension, demonstration, payoff |

## Common 6-to-8 fixes

- Replace a crossfade with a shared-element morph
- Cut the longest text card in half and give it more time
- Add 60 ms of stagger to anything appearing as a group
- Move the accent 80 ms earlier so it lands with the beat rather than after it
- Hold the final logo card 400 ms longer
- Add grain at 3 to 6% and a soft vignette
- Delete a shot. Fifteen seconds with six shots beats fifteen with nine.
