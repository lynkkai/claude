---
name: motion-graphics-video
description: >
  Generate real motion graphics videos (product launch films, show reels, feature
  explainers, animated UI, social cuts) by writing render code and rendering it to MP4,
  with brand assets, a beat grid, synthesized sound or voiceover, and a scored critique
  loop. Use this skill whenever the user asks for a video, animation, launch film, promo,
  product demo video, teaser, trailer, show reel, animated logo, "motion graphics", a
  9:16 / vertical cut, or asks to animate a UI, a Figma design or a screenshot, and also
  when they just say "make something that shows off X" and a moving picture is the obvious
  answer. Use it even if they do not say the word "video". This repo's videos are Lynkk
  videos: for any Lynkk piece, read references/lynkk.md first, since it carries the
  approved story, the on-screen lines, the spelling and claim rules, and ready shot lists.
---

# Motion graphics video, rendered from code

## What this actually is

You cannot emit an MP4. You can write code that draws frames, and then render those
frames. So every video here is a small software project: a deterministic timeline in
code, rendered frame by frame in headless Chromium, encoded with ffmpeg, with audio
mixed in.

The prompt is about 10% of the result. The other 90% is the harness: the render
contract, the brand input, the beat grid, the gotcha list, the critique loop. People who
paste one clever sentence get centered white text on a purple gradient. The work below is
what separates that from something a studio would invoice for.

Plan for iteration, not for one-shot. Good results come from tens of render cycles, not
from one perfect prompt. Budget accordingly and tell the user that up front if they are
expecting a single pass.

## Pick a route first

Four routes exist. State which one you are taking, and why, before writing code.

1. **Zero dependency code render (default).** One `index.html` with inline
   HTML/CSS/SVG/Canvas/WebGL, a deterministic `renderFrame(t)` function, Playwright
   screenshots, ffmpeg encode. Pick this for UI motion, kinetic type, logo animation,
   data and chart motion, abstract design work: anything where crisp vector edges and
   exact control matter. It is also what you are best at.
2. **A motion framework.** Remotion, Hyperframes, Diffusion Studio. Only when the user
   names one, the repo already uses one, or the piece needs real sequencing and audio
   tooling you would otherwise rebuild. Check for an installed plugin or MCP server before
   assuming it is available.
3. **Mixed pipeline.** Generative image or video models for plates and characters, then
   composite, grade, and add type on top in code. Pick this when the brief needs
   photographic or hand-drawn worlds you cannot draw with vectors. Image and video model
   tools may be available in session (for example an OpenART MCP server): check, and ask
   before spending the user's credits.
4. **Edit existing footage.** The user has clips and wants cuts, captions, B-roll,
   reframing. This is an ffmpeg and transcript job, not an animation job.

If the user named no route, take route 1 and say so.

## The pipeline

Work in a dedicated project folder. Write these files as you go, because they are what
makes round two cheap: `brand.md`, `style.md`, `shots.md`, `beats.json`, `index.html`,
`render.mjs` output, `critique.md`.

### 1. Gather the brand, do not invent it

Generic output is almost always missing-input output. Before writing a frame, get:

- logo files (SVG preferred), exact brand colors, real fonts
- real product screenshots, or the live URL to pull them from
- the actual product claims, in the product's own words

If the user gives a URL instead of assets, fetch the site, pull the palette, type and
screenshots from it, and write what you found into `brand.md` so later rounds and later
videos reuse it rather than re-deriving it. If something is missing, ask once for the
things that would visibly change the output (logo, fonts, screenshots) and proceed with
documented stand-ins for the rest.

**For Lynkk, start from the preset.** `references/lynkk.md` has the approved
before/during/after story, the on-screen lines drawn from site copy, the spelling and
claim rules, the asset gate and three ready shot lists (15 second launch film, 20 second
explainer with voiceover, 10 second vertical cut). Read it together with
`memory/lynkk-brand.md` and the writing rules in `CLAUDE.md`, and use
`assets/lynkk-tokens.css` as a clearly labelled stand-in until the real logo, colors and
fonts arrive.

### 2. Set the direction, in motion language

A direction is a rule about how things move, not a mood board adjective. Write two or
three sentences of it into `style.md`. For example: "Product film, UI motion. One
container, never a cut. Every state is the same element changing size, radius and fill
while its content swaps behind a short blur."

That constraint is what produces coherence. "Modern, clean, dynamic" produces slop.

If the user has a reference video they like, mine it instead of guessing. See
`references/reference-mining.md`: it extracts frames, writes a style guide of palette,
type, shot lengths, transition types, camera moves, grain and text entrances, and keeps
you to the grammar of the reference rather than its content, logos or characters.

### 3. Beat grid before code

Write `shots.md` as a table and show it to the user before you write the timeline:

| # | t_in | t_out | shot | on screen | motion | sound |
|---|------|-------|------|-----------|--------|-------|

For a 15 second film expect six to eight shots. This gate is cheap and catches the
expensive mistakes (wrong story, wrong pacing, too much text) before any render.

### 4. Build to the render contract

Start from `assets/timeline-template.html`: it already implements the contract, with
seeded grain, easing helpers, a shot table and the font-loading guard. Copying it is
faster than rebuilding those pieces, and they are the ones that cause the subtle
render bugs.


The contract is what makes rendering deterministic and resumable. Full details, including
the hard bans on the generic look, are in `references/motion-studio-rules.md`. Read it
before writing the timeline. The short version:

- `index.html` exposes `window.renderFrame(t)` where `t` is seconds, pure and seekable:
  the same `t` always draws the same frame
- no wall-clock time, no `requestAnimationFrame` driving state, no CSS transitions or
  animations, no `Math.random()` without a seeded generator
- declare `window.DURATION`, `window.FPS`, `window.WIDTH`, `window.HEIGHT`
- all fonts and images embedded or local, so rendering never races the network

### 5. Render

Use the bundled renderer rather than writing a new one each time:

```bash
node .claude/skills/motion-graphics-video/scripts/render.mjs \
  --html out/index.html --out out/film.mp4 --fps 30
```

It reads duration and size from the page, screenshots every frame in headless Chromium,
and encodes with ffmpeg. Prerequisites: Node, Playwright (preinstalled in this environment, so do not install it
again) and ffmpeg. Flags: `--duration`, `--width`, `--height`, `--audio`,
`--scale`, `--range` (render a slice while iterating), `--keep-frames`. Run
`--range 0:2 --scale 0.5` for fast look checks and full size only when the look is
settled.

### 6. Sound, if the piece needs it

Silent motion graphics look unfinished. Two layers, both worth doing:

- **Score and effects in code.** Synthesize a track at a fixed tempo, write
  `beats.json` with bpm, beats, downbeats and hits, then retime the animation to that
  grid so every morph, cut and text entrance lands on a beat. Add UI sounds: a click on
  each cursor press, a whoosh on each container morph, a thump on the logo.
- **Voiceover.** Write the script to the beat grid, then generate it with whatever
  text-to-speech tool the session has (check for an MCP server; ask before signing the
  user up for anything). Keep it under 2.2 words per second of runtime.

`references/sound-and-sync.md` has the beats.json shape, the retiming approach, and the
ffmpeg mix commands.

### 7. Critique loop

Do not hand over the first render. Score your own work, then fix the low scores. Use the
rubric in `references/critique-loop.md`: it scores composition, motion quality, type,
color, sound sync, brand fidelity, legibility and story on 1 to 10, and keeps iterating
until nothing is below 8. Write each round into `critique.md` so the user can see what
changed and why.

Watch the render, do not just reason about it: extract stills across the timeline and
look at them, because flicker, overlap, clipped type and dead air are visible and not
inferable.

### 8. Ship

Deliver the master plus the cuts the user actually needs: 16:9 for site and YouTube,
9:16 for stories and shorts, 1:1 for feeds, and a muted autoplay variant with burned-in
captions where it will play without sound. Reframe per aspect by changing the layout in
the timeline, not by cropping the 16:9 master, since cropping destroys the composition.
`references/delivery.md` has the specs and the ffmpeg recipes.

## Working habits that matter

- **Write the markdown memory.** `brand.md` and `style.md` are the reason the second
  video takes an hour instead of a day. Keep them current.
- **Gate before expense.** Beat grid before code, low-res slice before full render, one
  shot polished before all eight.
- **Real pixels over placeholders.** A screenshot of the actual product beats a drawn
  approximation of it every time.
- **Say what you could not get.** If a font was unavailable or a screenshot was stale,
  say so in the handover instead of quietly shipping a stand-in.

## Reference files

- `references/lynkk.md`: the Lynkk preset. Read first for any Lynkk video.
- `references/motion-studio-rules.md`: the render contract, banned generic patterns,
  motion craft rules. Read before building the timeline.
- `references/reference-mining.md`: turning a reference video into a style guide.
- `references/directors-brief.md`: the long-form brief template for ambitious pieces
  (character bibles, workflow gates, deliverables). Read when the piece has characters,
  narration or more than about 20 seconds.
- `references/sound-and-sync.md`: score, beat grid, UI sound, voiceover, mixing.
- `references/critique-loop.md`: the scoring rubric and the iteration protocol.
- `references/delivery.md`: aspect ratios, encode settings, caption burn-in.
- `assets/timeline-template.html`: contract-compliant starter timeline.
- `assets/lynkk-tokens.css`: placeholder Lynkk tokens, to be replaced with real ones.
- `scripts/render.mjs`: the frame-by-frame renderer and encoder.
