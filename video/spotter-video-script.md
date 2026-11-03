# Spotter: product video script

For https://lynkk.ai/features/spotter

Target length: 75 seconds (hero cut). A 30-second vertical cutdown is at the bottom.
Format: 16:9 hero, 1:1 and 9:16 crops. Design the motion graphics at 16:9 but keep
every hero element inside a 1:1 safe area so the crops are a reframe, not a rebuild.
**No voiceover.** On-screen text, sound design and motion carry the film.

Two acts:

- **Act 1 (0:00 to 0:14) is live action.** A real Mac, a real keyboard, a real call.
  This is the only part of the film shot with a camera, and it exists to prove Spotter
  is a thing that happens on your actual machine.
- **Act 2 (0:14 to 1:08) is motion graphics.** The Spotter bar lifts off the laptop
  screen and we follow it into a built space where each feature gets one animated
  device. Nothing here pretends to be a screen recording.

Then a short return to the real machine for the end.

Everything claimed must be true of the early build. Any shortcut on screen has to
match the real default binding. Where Act 2 shows app UI, rebuild it from the real
components in Figma rather than keying over screenshots, so the type stays crisp at
any scale.

---

## Art direction for Act 2

Settle this before a single frame is animated. The whole act lives or dies on it.

**The space.** Near-black canvas, not pure black, with a soft radial falloff so the
center sits forward. One light source implied from the top left, matching the way the
screen glow fell across the keys in Act 1. A faint grid, visible only where light
catches it, to give scale and parallax.

**Depth.** Everything is a flat plane in 3D space, UI as glass cards with slight
thickness and a rim light on the top edge. Cards cast soft contact shadows onto the
grid. Camera has a shallow depth of field so background layers go gently soft. Never a
hard perspective box, never a skewed "isometric dashboard" look.

**Color.** Dark base, one accent for Spotter's own activity (the bar, the answer
writing in, the listening state), one neutral for everything that belongs to the call
or the user's own app. Only two families, and the accent appears only where Spotter is
acting. That restraint is what will make it feel like a product film instead of a
template. Swap in the brand values before animating.

**Light as the hero.** The recurring motif: the accent travels as a line of light.
Input flows toward the bar, the answer flows out of it. Every feature beat in Act 2 is
a variation on that one idea, which is what keeps seven different devices feeling like
one film.

**Type.** The brand UI typeface, same as the product. Cards animate in by mask and
slight Y offset, never a scale pop, never a letter-by-letter typewriter except for the
one place it is literal (the answer writing into the bar).

**Motion rules.**

- One hero move per beat. If two things need to move, one of them is a supporting
  drift at ten percent of the energy.
- Ease out hard, ease in soft. Fast start, long settle. Nothing linear, nothing bouncy.
- 0.4s for an element entering, 0.25s for one leaving, 0.8s for a camera push.
- Overlap by two to four frames so beats breathe into each other instead of cutting
  dead.
- The camera is always moving a little, slow dolly or slow parallax, never static,
  never a whip.
- Hold the final frame of each beat for at least half a second before the next one
  starts. This is the single most common thing to get wrong.

**Build notes.** UI components from Figma, exported for animation. Keycaps modeled and
rendered rather than faked in 2D, they need real bevel and material. Waveforms,
particles and the graph driven procedurally, not hand keyframed, so timing changes do
not mean a rebuild.

---

## Sound design

No voice, so sound is the script's other half.

- 0:00 to 0:08 is near silent: room tone, and a muffled voice from the call as if heard
  through a laptop speaker. No music.
- The first deliberate sound is the key click at 0:05.
- The Spotter chime lands on that keypress, once, and is never used again.
- At the Act 1 to Act 2 transition the room tone drops away completely. The air change
  sells the move into the built space.
- Music enters with Act 2: low, rhythmic, percussive, no melody to speak of. It should
  feel like typing.
- Each animated beat gets one sound: a soft transient for a card landing, a filtered
  sweep for the light travelling, a click for a key.
- Call audio stays present but never intelligible. We never make out words, so nobody
  wonders what was really said.
- Music drops out entirely for the privacy beat. Silence does the work there.
- End card: one soft resolve, then nothing.

---

## Text rules

- One idea per card. Never more than seven words on screen at once.
- A card holds for at least 1.5 seconds, longer if the viewer also has to read
  something inside the UI in the same beat. Never both at once: either the card is up
  or the answer is readable, not the two competing.
- Cards sit lower third on 16:9, centered on the vertical crops.
- Shortcut glyphs (⌘↩, ⌘⇧\, ⌘\) are a separate element, small, stamped the instant the
  key goes down.
- Burn the cards in rather than using a caption track, so they survive every crop.

---

# ACT 1: LIVE ACTION

### 1. Cold open: the keyboard (0:00 to 0:05)

**Visual:** Extreme close-up, macro, shallow depth of field. A MacBook keyboard lit
from the side, screen glow spilling across the keys. We are tight on the bottom-left
cluster so the ⌘ key fills most of the frame. A thumb rests on it. Nothing moves.

**Sound:** Room tone. Muffled call voice underneath. No music.

**On-screen text:** nothing for the first three seconds, then, small:
```
You are asked something
you do not have ready.
```

---

### 2. The press (0:05 to 0:08)

**Visual:** The thumb presses ⌘ and the other hand hits Return. Single clean key
travel, shot at 120fps and played slightly slow so you feel the click. On the press,
pull focus from the keys up to the screen behind.

**Sound:** One crisp key click. The chime lands on it.

**On-screen text:** the card clears on the press. `⌘↩` stamps in, bottom center, held
one second.

---

### 3. Spotter appears on the call (0:08 to 0:14)

**Visual:** Rack focus completes onto the laptop screen. A live call is running,
gallery view, a real face mid-sentence. The Spotter bar slides down from the top of the
screen, over the call, and an answer writes itself into it line by line.

The question on the call is the kind nobody has ready: a pricing objection, or a "how
does this handle our data?" The answer is specific and short.

Hold long enough to actually read it, around three seconds, with no card competing.

**On-screen text:** one card as the bar lands, then nothing:
```
Spotter reads your screen
and hears the call.
```

---

### 4. The handoff (0:14 to 0:17)

The hinge of the film. Get this right and the two halves feel like one thing.

**Visual:** Camera pushes in on the Spotter bar until the laptop bezel leaves frame.
At the moment the bar fills the width, the real footage behind it desaturates and falls
away as a plane, the room light goes with it, and the bar is left floating in the dark
built space of Act 2. The bar itself never cuts. It is the one element continuous
across the transition, so the eye tracks it and the cut reads as a move rather than a
scene change.

**Sound:** Room tone drops to nothing. A filtered sweep as the plane falls away. Music
starts underneath it.

**On-screen text:** none. Let the move be the move.

---

# ACT 2: MOTION GRAPHICS

Each beat is one device. They share the light motif and the same space, so they cut
together as a sequence rather than seven separate explainers.

### 5. Hears both sides (0:17 to 0:26)

**Device:** two waveforms.

**Animation:** The bar sits center. Two lines of light grow in from the left and right
edges toward it, each one a live audio waveform. The left is labelled "Me" and reacts
to the mic, the right is labelled "Them" and reacts to system audio. They are visibly
different shapes, one closer and drier, one thinner and processed.

As they reach the bar they fold into a single line that runs along its underside and
pulses. The bar wakes: the listening state lights up.

Then the stop. `⌘⇧\` stamps, the waveforms flatten to still lines and the light drains
out of the bar from the center to both edges. The point reads without a word: it hears
nothing until you press Listen.

**Camera:** slow dolly in during the build, settle on the stop.

**On-screen text:**
```
Hears both sides.
```
then
```
Nothing is heard
until you press Listen.
```

---

### 6. Reads your screen (0:26 to 0:35)

**Device:** a window reduced to light.

**Animation:** A window card flies up behind the bar, a real app the user would have
open: a deal record, a doc, a dashboard. It lands and holds for a beat as recognisable
UI.

Then `⌘↩` stamps and a band of light sweeps down the card, top to bottom, like a
scanner pass. Everything the sweep crosses is abstracted: paragraphs collapse to
weighted lines, numbers lift off as glowing tokens, the chrome fades. The tokens that
matter detach, travel up along the light path, and flow into the bar.

The bar writes its answer, and the answer visibly contains the number that came off the
card. That connection is the whole shot, so make the number unmistakable and make it
land on the same frame in both places.

Then the card re-forms to normal UI and drifts back. Nothing was taken, it was read.

**Camera:** slow parallax left so the card and the bar separate in depth.

**On-screen text:**
```
Reads the front window,
when you ask.
```

---

### 7. Three keys (0:35 to 0:45)

**Device:** rendered keycaps in space.

**Animation:** Cut to three keycaps floating in a row, rendered with real bevel and
material, lit by the same top-left source. Each one presses in turn, and on each press
a small panel swings out beside it showing the result.

1. `⌘↩` presses. A question panel opens, text types in, the answer writes beneath it.
2. `⌘⇧\` presses. The listening indicator lights, the two waveforms from beat 5 return
   as a miniature.
3. `⌘\` presses. The whole bar slides up out of frame and the call grid is left clean
   behind it, then slides back.

Cut the three presses on the music. This is the only beat in Act 2 with a visible
rhythm, and it is what stops the act feeling slow in the middle.

**Camera:** locked for the three presses. After the long dolly moves either side, the
stillness reads as emphasis.

**On-screen text:** one word per press: `Ask.` / `Listen.` / `Hide.`

---

### 8. Seven modes (0:45 to 0:54)

**Device:** a radial dial, then one answer morphing.

**Animation:** The bar rotates to face us and seven chips arc out around it in a
radial: General, Meeting, Sales, Support, Lecture, Interview prep, Mock interview. The
dial spins once with real inertia, the chips trailing slightly, and settles on Sales
with a soft detent.

Then the payoff. The answer from beat 6 is on screen. Sales is swapped for Support and
the answer re-writes itself in place, line by line, into something visibly different in
shape and length. Same question, different help. Do this as a text morph in one
continuous card, not a cut, so the viewer sees it change rather than sees two slides.

Finally an eighth chip draws itself in, empty, and fills with a custom instruction and
a block of notes.

**Camera:** push in on the dial, pull back for the morph.

**On-screen text:**
```
Seven modes, and your own.
```

---

### 9. Visible in every share (0:54 to 1:01)

**Device:** multiplying attendee views.

**Animation:** The presenter's screen sits center with the bar on it. It duplicates
once to the right, then the pair duplicates, then again, until a grid of nine attendee
views fills the frame, each one a slightly different window chrome. The bar is present
in every single one.

Camera pulls back through the grid. No highlight, no arrow pointing it out. The
repetition is the argument.

**Sound:** music drops out here.

**On-screen text:**
```
Visible in every screen share.
On purpose.
```

---

### 10. Nothing kept (1:01 to 1:07)

**Device:** dissolve to particles, one caught.

**Animation:** The grid collapses back to a single session card holding the asks from
the call. It holds for a beat. Then it dissolves from the bottom up into particles of
light that drift and go out. The space is empty and stays empty for a full second,
which is longer than feels comfortable and is exactly the point.

Then one deliberate click: a single card re-forms, this time as a saved note, and docks
into a notes list. Kept, because someone chose to keep it.

**Camera:** static. The only still frame in the act, besides the keycaps.

**On-screen text:**
```
Nothing kept,
unless you keep it.
```

---

### 11. Today into tomorrow (1:07 to 1:14)

**Device:** the knowledge graph building.

**Animation:** The saved note becomes a node. Edges draw out to other nodes, other
meetings, people, open questions, and a graph builds outward across the dark space in
one continuous move, the light travelling along each edge as it forms. Fast enough to
feel like scale, slow enough to read as structure.

Then the graph collapses inward, down to a single card: tomorrow's meeting, with the
context panel already populated and the open question from today still flagged on it.

**Sound:** music returns, resolving.

**On-screen text:**
```
Today's call
is tomorrow's context.
```

---

### 12. End card (1:14 to 1:20)

**Visual:** The card recedes. One last beat of the real machine: a two second cut back
to the live-action laptop from Act 1, hands off the keys, Spotter's bar quiet at the
top of the screen. Then cut to black.

Logo. Below it the ⌘↩ glyph, then the URL.

**On-screen text:**
```
Spotter
Live AI help on your calls.

Early access on Lynkk Pro, Mac app.
Apple silicon, macOS 14.2 or later.

lynkk.ai/features/spotter
```

---

## All on-screen text, in order

The entire script, for the editor and the localization pass.

1. You are asked something you do not have ready.
2. `⌘↩`
3. Spotter reads your screen and hears the call.
4. Hears both sides.
5. Nothing is heard until you press Listen.
6. Reads the front window, when you ask.
7. Ask. / Listen. / Hide.
8. Seven modes, and your own.
9. Visible in every screen share. On purpose.
10. Nothing kept, unless you keep it.
11. Today's call is tomorrow's context.
12. Spotter. Live AI help on your calls. Early access on Lynkk Pro, Mac app. Apple
    silicon, macOS 14.2 or later. lynkk.ai/features/spotter

Roughly 50 words of body copy across 80 seconds. If a beat feels tight in the edit,
cut the card, not the animation.

---

## 30-second cutdown (social, 9:16)

Built from the same assets. Act 1 compressed to six seconds, three motion beats, out.

| Time | Visual | On-screen text |
|---|---|---|
| 0:00 to 0:03 | Macro ⌘ key, thumb resting, muffled call underneath | "You are asked something you do not have ready." |
| 0:03 to 0:06 | The press. Chime. Rack focus to the screen. | `⌘↩` |
| 0:06 to 0:11 | Spotter bar drops over the live call, answer writes in, then the handoff push | "Spotter reads your screen and hears the call." |
| 0:11 to 0:17 | Beat 5, two waveforms converging into the bar | "Hears both sides. Only when you ask." |
| 0:17 to 0:22 | Beat 6, the scanner sweep, tokens flowing into the answer | "Reads the front window, when you ask." |
| 0:22 to 0:27 | Beat 9, the grid of attendee views, bar in every one | "Visible in every share. Nothing kept." |
| 0:27 to 0:30 | End card | "Spotter. Early access on Lynkk Pro. lynkk.ai" |

Same rules: no voice, plays fine muted, cards burned in.

---

## Production notes

- The cold open only works silent. No music under the first five seconds. The first
  sound in the film is the key click.
- The handoff in beat 4 is the riskiest shot in the film. Animate it before anything
  else. If the bar does not stay continuous through it, the two acts will feel like two
  videos and no amount of polish downstream will fix that.
- Shoot the macro keyboard and the on-screen footage separately, then match cut. Trying
  to get both sharp in one take will cost a day and look worse.
- Use a real call with a real second person for Act 1. A fake call reads as fake within
  a second, and the whole claim is that Spotter is in the room with you.
- Every answer shown, in live action or rebuilt in Act 2, must be a real Spotter output.
  If an answer is too long to read in the cut, change the question, not the answer.
- With no voiceover, the risk is filling the space with more cards. Do the opposite:
  fewer cards, longer holds. In motion graphics the second most common failure is
  everything moving at once, so keep the one-hero-move rule even when a beat feels
  empty on the first pass.
- Rebuild Act 2 UI from real components, do not animate over screenshots. Blurry type
  at scale is the fastest way to look cheap.
- Label footage as the early build wherever a frame could be mistaken for the shipped
  product.
- Shortcuts to keep accurate on screen: ⌘↩ ask, ⌘⇧\ listen, ⌘\ show or hide, ⌘R new
  chat, ⌘← and ⌘→ move the bar, ⌘⇧↑ and ⌘⇧↓ scroll the answer. These are the defaults
  and can be changed in Settings, so if the demo machine has custom bindings, reset it
  before shooting.
- Deliver the motion beats as separate numbered comps. Every one of them is a standalone
  social asset, and the feature page can autoplay beat 5 or 6 on its own as a loop.

## To confirm before shooting

- [ ] Brand accent and neutral values for the Act 2 palette, plus the UI typeface files
- [ ] Which meeting platform can we show on screen (Zoom, Google Meet, Teams)
- [ ] Which app is the front window in beat 6, and can we show real data in it
- [ ] Is "Answer questions on its own" shown in the video, or held back
- [ ] Early access wording and the sign-up destination for the end card
- [ ] Logo lockup for the end card
- [ ] Whether a named customer will appear on the call
