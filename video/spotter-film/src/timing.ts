/**
 * The film's clock. 120 BPM at 30 fps: one beat is 15 frames, one bar is
 * 60 frames (2 s), 16 bars is the whole film. Every scene start, every slam
 * and every press is written here as a bar or a beat, and the scenes read
 * their frames from this file, so the picture and the sound cue list
 * (scripts/write-cues.mts) can never disagree.
 */

export const FPS = 30;
export const BPM = 120;
export const BEAT = (FPS * 60) / BPM; // 15 frames
export const BAR = BEAT * 4; // 60 frames
export const DURATION = BAR * 16; // 960 frames, 32 s

/** The first frame of bar n (0-based). */
export const bar = (n: number) => n * BAR;
/** The first frame of beat n (0-based, counted from the top of the film). */
export const beat = (n: number) => n * BEAT;

/** Where each scene starts and how long it runs, in absolute frames. */
export const SCENES = {
  hook: { from: 0, dur: bar(2) }, // the keyboard in the dark, and the press
  ask: { from: bar(2), dur: bar(3) }, // the call, the bar drops, the answer
  screen: { from: bar(5), dur: bar(2) }, // the doc read as words
  listen: { from: bar(7), dur: bar(2) }, // Listen, and both sides
  open: { from: bar(9), dur: bar(4) }, // in every share, and nothing kept
  recap: { from: bar(13), dur: bar(1) },
  end: { from: bar(14), dur: bar(2) },
} as const;

/**
 * Key moments, absolute frames. A scene subtracts its own `from` to get
 * local frames. Comments say what the eye sees on that frame.
 */
export const T = {
  // Hook, 0 to 4 s: the keyboard, lit by the screen.
  glowOn: 6, // the screen's light reaches the keys
  flameOn: 10, // Remi's thruster sputters alight over the keys
  eyesOpen: 22, // Remi's eyes blink open
  titleStuck: [30, 38, 43, 50] as const, // "Stuck" "on" "a" "call?"
  cmdDown: bar(1), // 2.0 s: the ⌘ key goes down, the giant keycap slams
  retDown: bar(1) + BEAT, // ↩ follows on the next beat
  titleKeys: bar(1), // "Press ⌘↩.", a word on each key
  lift: bar(1) + BEAT * 2, // the keyboard drops away, the camera lifts
  deskHit: bar(2), // 4.0 s: the Mac screen crashes into frame

  // Ask, 4 to 10 s.
  question: bar(2) + 4, // Priya's caption on the call
  panel: bar(2) + BEAT, // the Spotter bar drops from the top
  readGlow: bar(2) + BEAT + 6, // "Reading your screen", the doc's lines light
  answerFrom: bar(2) + BEAT * 3, // the answer starts writing
  answerHit: bar(3), // 6.0 s: the answer lands
  titleLive: bar(3), // "Spotter answers. Live."
  joy: bar(3) + 2, // Remi loops
  pill: bar(3) + BEAT, // the Early access pill pops
  hops: [bar(4), bar(4) + BEAT, bar(4) + BEAT * 2] as const,

  // Screen, 10 to 14 s. The cut in is a whip-pan.
  whip: bar(5),
  titleText: bar(5) + BEAT, // "Your screen, as text."
  sweepFrom: bar(5) + BEAT, // the band starts down the doc
  sweepTo: bar(6) - 6, // it reaches the bottom
  lift1: bar(6), // the words lift off the doc
  titleWords: bar(6) + BEAT, // "Only the words go."
  picDrop: bar(6) + BEAT * 2, // the picture greys out and is gone

  // Listen, 14 to 18 s.
  listenKey: bar(7), // the ⌘⇧\ keycap slams
  dot: bar(7) + 5, // the red dot lights, Listen turns on
  titleListen: bar(7) + BEAT, // "Press Listen."
  meFrom: bar(8), // the Me meter swells
  themFrom: bar(8) + BEAT, // the Them meter answers
  titleHears: bar(8) + BEAT * 2, // "Hears both sides."

  // Open, 18 to 26 s.
  share: bar(9), // the screen duplicates into attendee views
  tiles: [bar(9), bar(9) + BEAT, bar(9) + BEAT * 2, bar(9) + BEAT * 3] as const,
  titleShare: bar(9) + BEAT, // "In every screen share."
  cross: bar(10) + BEAT * 2, // Remi flies through the grid
  smash: bar(11), // the asks shatter and blow away
  titleKept: bar(11) + BEAT, // "Nothing kept."
  empty: bar(11) + BEAT * 2, // the asks blow away, nothing is left
  keep: bar(12), // the "Keep the session as a note" switch draws in
  pull: bar(12) + BEAT * 3, // the one-beat pull-back into the drop

  // Recap, 26 to 28 s. The music's drop is on bar 13.
  drop: bar(13),
  recap: [bar(13), bar(13) + BEAT, bar(13) + BEAT * 2] as const,
  clear: bar(13) + BEAT * 3, // everything clears, Remi starts the circle

  // End card, 28 to 32 s.
  logo: bar(14), // the trail's circle locks into the sphere
  name: bar(14) + BEAT,
  button: bar(14) + BEAT * 2,
  url: bar(14) + BEAT * 3,
  perch: bar(15), // Remi lands on the button and waves, on the final chord
  fine: bar(15) + BEAT,
} as const;

/** Spotter's answer, from the site's own example (the pilot plan is on screen). */
export const ANSWER = "One team, up to 20 seats, for 30 days.";
/** How many characters of the answer show at an absolute frame. */
export const answerChars = (f: number) => {
  const t = Math.max(0, Math.min(1, (f - T.answerFrom) / (T.answerHit - 1 - T.answerFrom)));
  return Math.round(t * ANSWER.length);
};

export type Cue = {
  f: number;
  kind: string;
  id: string;
  weight?: number;
  pan?: number;
  dur?: number;
  apexFrac?: number;
  variant?: string;
};

/**
 * Every sound the picture asks for, on the frame the eye reads it. Written to
 * out/cues.json by scripts/write-cues.mts for the sound design (real-sound).
 */
export const CUES: Cue[] = [
  { f: 0, kind: "riser", id: "hook:room", dur: T.cmdDown, weight: 0.5 },
  { f: T.eyesOpen, kind: "blip", id: "hook:remi:eyes", weight: 0.6 },
  { f: T.cmdDown, kind: "key", id: "hook:key:cmd", weight: 1.3, variant: "heavy" },
  { f: T.cmdDown, kind: "hit", id: "hook:key:sub", weight: 0.9, variant: "sub" },
  { f: T.retDown, kind: "key", id: "hook:key:return", weight: 1.35, variant: "heavy" },
  { f: T.lift, kind: "riser", id: "hook:lift", dur: T.deskHit - T.lift, weight: 0.9 },
  { f: T.deskHit, kind: "hit", id: "hook:desk:impact", weight: 1.4 },

  { f: T.question + 3, kind: "pop", id: "ask:caption:pop", weight: 0.6, pan: -0.2 },
  { f: T.panel, kind: "whoosh", id: "ask:panel:drop", dur: 12, apexFrac: 0.6, weight: 0.8 },
  { f: T.readGlow, kind: "tick", id: "ask:reading", weight: 0.5, pan: 0.2 },
  { f: T.answerFrom, kind: "riser", id: "ask:answer:riser", dur: T.answerHit - T.answerFrom, weight: 0.8 },
  { f: T.answerHit, kind: "hit", id: "ask:answer:hit", weight: 1.2, variant: "bright" },
  { f: T.joy, kind: "blip", id: "ask:remi:joy", weight: 0.5 },
  { f: T.pill, kind: "pop", id: "ask:pill:pop", weight: 0.7 },
  ...T.hops.map((f, i) => ({ f, kind: "tick", id: `ask:remi:hop:${i}`, weight: 0.4 })),

  { f: T.whip - 6, kind: "whoosh", id: "screen:whip", dur: 12, apexFrac: 0.5, weight: 0.9 },
  { f: T.sweepFrom, kind: "riser", id: "screen:sweep", dur: T.sweepTo - T.sweepFrom, weight: 0.6, pan: 0.3 },
  { f: T.lift1, kind: "suck", id: "screen:words:lift", dur: 14, apexFrac: 0.75, weight: 0.9 },
  { f: T.picDrop, kind: "hit", id: "screen:picture:drop", weight: 0.8, variant: "light" },

  { f: T.listenKey, kind: "key", id: "listen:key:slam", weight: 1.3, variant: "heavy" },
  { f: T.listenKey, kind: "hit", id: "listen:key:sub", weight: 0.9, variant: "sub" },
  { f: T.dot, kind: "click", id: "listen:dot:on", weight: 0.8, variant: "confirm" },
  { f: T.meFrom, kind: "swell", id: "listen:level:me", dur: 14, apexFrac: 0.5, weight: 0.7, pan: -0.6 },
  { f: T.themFrom, kind: "swell", id: "listen:level:them", dur: 14, apexFrac: 0.5, weight: 0.7, pan: 0.6 },

  ...T.tiles.map((f, i) => ({ f, kind: "hit", id: `open:tile:${i}`, weight: 0.65 + i * 0.08, variant: "light", pan: i % 2 ? 0.4 : -0.4 })),
  { f: T.cross, kind: "whoosh", id: "open:remi:cross", dur: 12, apexFrac: 0.5, weight: 0.7 },
  { f: T.smash, kind: "hit", id: "open:asks:slam", weight: 1.2 },
  { f: T.empty, kind: "suck", id: "open:asks:clear", dur: 14, apexFrac: 0.7, weight: 0.8, variant: "reverse" },
  { f: T.keep, kind: "tick", id: "open:keep:switch", weight: 0.5 },

  { f: T.drop, kind: "drop", id: "recap:drop", weight: 1.5 },
  ...T.recap.map((f, i) => ({ f, kind: "hit", id: `recap:word:${i}`, weight: 1.1 + i * 0.1 })),
  { f: T.clear, kind: "whoosh", id: "end:trail", dur: 15, apexFrac: 0.5, weight: 0.7 },

  { f: T.logo, kind: "hit", id: "end:logo:impact", weight: 1.2 },
  { f: T.logo + 12, kind: "bell", id: "end:logo:note", weight: 0.7 },
  { f: T.perch, kind: "blip", id: "end:remi:wave", weight: 0.4 },
].sort((a, b) => a.f - b.f);
