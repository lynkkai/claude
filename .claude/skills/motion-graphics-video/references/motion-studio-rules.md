# Motion studio rules

Four parts: the render contract, the look, the motion craft, the gotchas. These are the
harness. They matter more than the prompt.

## 1. Render contract

The renderer screenshots a page frame by frame, so the page must be a pure function of
time. Anything that drifts, animates on its own clock, or depends on the network will
tear, flicker or render a blank frame.

Requirements for `index.html`:

- Expose `window.renderFrame(t)`, `t` in seconds from 0. It may be async. It must draw
  the complete frame for `t` and nothing else. Calling it with the same `t` twice must
  produce identical pixels.
- Declare the timeline up front:
  ```js
  window.FPS = 30;          // 30 for UI motion, 60 only if the motion needs it
  window.DURATION = 15;     // seconds
  window.WIDTH = 1920;
  window.HEIGHT = 1080;
  ```
- No `Date.now()`, no `performance.now()`, no `setTimeout` or `setInterval` driving
  state, no `requestAnimationFrame` loop. Time comes only from the `t` argument.
- No CSS `transition` or `animation` properties. They run on their own clock and will not
  match `t`. Set values directly from `t` instead.
- Seed any randomness (a small mulberry32 is enough) so grain, particles and jitter are
  identical on every render.
- Embed assets: fonts as base64 `@font-face` or local files, images local, SVG inline. No
  CDN, no Google Fonts link, no remote JSON.
- If you use video elements, set `currentTime` from `t` and await `seeked`, never `play()`.
- Keep state in a single object derived from `t`. Shots are functions of local shot time,
  not of accumulated mutation.

Sanity checks before a full render: call `renderFrame(0)`, then `renderFrame(DURATION)`,
then `renderFrame(mid)` twice and diff. Any difference means hidden state.

## 2. The look: what is banned

These are the tells of AI slop. Avoid them unless the brand genuinely is this.

- Centered white sans-serif text on a purple or blue-to-pink gradient
- A full-screen word fading in and out as an entire shot, repeatedly
- Default system font stacks (`-apple-system`, Arial, Helvetica) standing in for brand type
- Pure `#000` to pure `#fff` with nothing in between, or neon-on-black with glow on everything
- Generic easing: `linear`, or `ease` on everything, or every element moving at the same rate
- Floating geometric shapes and particle fields with no narrative role
- Lens flares, mirror reflections, infinite starfields, blockchain cube grids
- Stock emoji or icon-font glyphs where the brand has real icons
- Every shot the same length, every transition a crossfade
- Text that enters and leaves the same way every time

## 3. Motion craft

- **Easing.** Use custom cubic beziers. Entrances decelerate (ease-out), exits
  accelerate (ease-in), moves that both start and stop use ease-in-out. A useful default
  is `cubic-bezier(.22,1,.36,1)` for entrances. Overshoot slightly on energetic brands,
  never on enterprise ones.
- **Stagger.** Groups of things move in sequence, 40 to 80 ms apart, not together.
- **Hierarchy.** One thing leads per moment. If three elements move at once with equal
  weight, the eye has nowhere to go.
- **Continuity.** Prefer morphing one element over cutting between two. Shared-element
  transitions are what make product film look expensive.
- **Shot length.** 1.2 to 3.0 seconds for a punchy piece. Vary them. Hold the payoff
  longer than the setup.
- **Type.** Two weights of one family is plenty. On-screen copy under about seven words.
  No sentence the viewer cannot finish in its shot. Set `text-rendering` and letter
  spacing deliberately at large sizes.
- **Color.** Three to five colors, one of them dominant, one accent used sparingly for
  the thing you want looked at.
- **Texture.** A little grain, a subtle vignette and slightly imperfect timing read as
  craft. Perfectly clean vectors read as a template.
- **Safe margins.** Keep type and logos inside 6% of each edge, and inside the 9:16 and
  1:1 crops if those cuts are coming.

## 4. Gotchas

- Fonts not loaded at frame 0: `await document.fonts.ready` inside `renderFrame` before
  drawing, or the first second renders in a fallback face.
- Images not decoded: preload and `await img.decode()` once, then reuse.
- Canvas cleared mid-frame: draw the full frame in one pass, never partial repaints.
- Device pixel ratio: render at the real output size rather than scaling up a small
  canvas, or edges go soft.
- Subpixel jitter: round positions of static text to whole pixels.
- Audio desync: the picture is the master. Retime the picture to the beat grid, do not
  stretch the audio to the picture.
- Time units: pick seconds everywhere. Mixing seconds, frames and milliseconds is the
  most common source of off-by-a-shot errors.
