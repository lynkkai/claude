# Director's brief

For anything ambitious (characters, narration, more than about 20 seconds, a story
rather than a feature tour) a one-liner will not carry it. Fill in this brief instead,
then build. The best public examples of code-rendered film are built this way, over many
model calls and several hours, not in one pass.

Open with the role, because it sets the scope of what you are responsible for:

> You are the director, animator, sound designer and render engineer for [name], a film
> made in code.

Then the twelve sections:

1. **The film in one line.** What a viewer would tell a friend it was. If you cannot
   write this, the piece has no spine yet.
2. **References.** Links or files, plus one line each on what you are taking from them.
   Grammar only (see `reference-mining.md`).
3. **Tools and keys.** Which route (see SKILL.md), which frameworks, which APIs or MCP
   servers are available for images, video, voice and music, and which are off limits.
4. **Character bible.** One section per character: proportions, palette, silhouette, how
   they read at small size, three to five expressions, how they move. Consistency across
   shots comes from this document, not from memory. Store generated character plates in
   `assets/characters/` and reuse them rather than regenerating.
5. **World bible.** Locations, lighting, time of day, props, the rules of the space.
6. **Beat sheet.** The shot table from SKILL.md, with emotional intent per beat.
7. **Text on screen.** Every word, verbatim, with its in and out times. Nothing on
   screen that is not listed here. Follow the repo writing rules for the copy.
8. **Sound design.** Tempo, score direction, the hit list, voiceover script with timings,
   where silence sits.
9. **Workflow gates.** Explicit stop points where you show work and wait: after the beat
   sheet, after the first shot at full quality, after the first full silent render, after
   the mix. Gates are what keep a long build from going hours in the wrong direction.
10. **Critique loop.** The rubric and the target score (see `critique-loop.md`).
11. **Gotchas.** Everything that must not happen: brand misspellings, banned visual
    cliches, claims legal will not allow, competitors' marks, text in unsafe margins.
12. **Deliverables.** Files, aspect ratios, durations, caption variants, where they go.

## Why the gates matter

A long build is a sequence of commitments. Each gate converts an assumption into a
confirmed fact cheaply, while changing it is still a text edit rather than a re-render.
When you reach a gate, show the artifact (the table, the still, the slice), say what you
are about to do next, and ask for a yes or a change.
