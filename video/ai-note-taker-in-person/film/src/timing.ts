/**
 * "Best AI Note Taker for In-Person Meetings", 2:00, 1920x1080.
 * 120 BPM at 30 fps: beat 15 frames, bar 60 frames (2 s), 60 bars.
 * Every scene start, card stamp and hit is a bar or a beat, so the picture
 * and the soundtrack (audio/lines.json, the music edit) cannot disagree.
 */

export const FPS = 30;
export const BPM = 120;
export const BEAT = (FPS * 60) / BPM; // 15
export const BAR = BEAT * 4; // 60 frames, 2 s
export const DURATION = BAR * 60; // 3600 frames, 120 s

export const bar = (n: number) => n * BAR;
export const beat = (n: number) => n * BEAT;
/** Seconds to frames, for reading the script's timecodes straight across. */
export const sec = (s: number) => Math.round(s * FPS);

/**
 * One entry per piece of the 2:00. `kind` says who makes it: "G" is a Remi
 * graphic rendered here, "shot" is footage the team films (a slate stands in
 * for it so the whole 2 minutes can be watched).
 */
export const SCENES = {
  hook: { from: sec(0), dur: sec(4) },
  shotIntro: { from: sec(4), dur: sec(16) },
  card1: { from: sec(20), dur: sec(2) },
  shotDevices: { from: sec(22), dur: sec(6) },
  board: { from: sec(28), dur: sec(10) },
  shotNoPhone: { from: sec(38), dur: sec(2) },
  card2: { from: sec(40), dur: sec(2) },
  micMap: { from: sec(42), dur: sec(8) },
  shotConsent: { from: sec(50), dur: sec(4) },
  record: { from: sec(54), dur: sec(4) },
  column: { from: sec(58), dur: sec(4) },
  note: { from: sec(62), dur: sec(8) },
  card3: { from: sec(70), dur: sec(2) },
  labels: { from: sec(72), dur: sec(10) },
  shotTips: { from: sec(82), dur: sec(4) },
  card4: { from: sec(86), dur: sec(2) },
  offline: { from: sec(88), dur: sec(8) },
  online: { from: sec(96), dur: sec(4) },
  card5: { from: sec(100), dur: sec(2) },
  picks: { from: sec(102), dur: sec(12) },
  end: { from: sec(114), dur: sec(6) },
} as const;

/** Key moments, absolute frames. Comments say what the eye sees. */
export const T = {
  // Hook, 0 to 4 s.
  eyesOpen: 14,
  windowIn: 26, // the call window slides in
  charge: 46, // Remi flies at it
  shatter: bar(1), // 2.0 s: the window breaks, the room is behind it
  title1: [bar(1) + 4, bar(1) + BEAT + 4] as const, // "No link?" "No problem."

  // Chapter cards, one bar each, on the chapter's first frame.
  cards: [sec(20), sec(40), sec(70), sec(86), sec(100)] as const,

  // Device board, 28 to 38 s: a column per bar, rows on beats.
  colsIn: [sec(28), sec(30), sec(32)] as const,
  boardRows: [sec(33), sec(34), sec(35), sec(36)] as const,

  // Mic map, 42 to 50 s.
  tableIn: sec(42),
  ringOut: sec(44), // the "clear voice" ring reaches the seats
  crosses: [sec(46), sec(47), sec(48)] as const, // far end, by the fan, phone in a pocket

  // Record now, 54 to 58 s.
  menuOpen: sec(55),
  click: sec(56) + 6, // the trackpad click on Record now
  recOn: sec(57),

  // The column, 58 to 62 s.
  columnIn: sec(58),
  liveWords: [sec(59), sec(60), sec(61)] as const,

  // The note, 62 to 70 s.
  noteIn: sec(62) + 4,
  stamps: [sec(64), sec(65), sec(66)] as const, // summary, decision, action item
  land: sec(67), // Remi lands on the action item

  // Speaker labels, 72 to 82 s.
  transcriptIn: sec(72),
  speakers: [sec(74), sec(75), sec(76), sec(77)] as const, // four labels light in turn
  rename: sec(79), // one label is renamed

  // Offline, 88 to 100 s.
  wifiOff: sec(89),
  diskFrom: sec(90),
  diskTo: sec(95),
  wifiOn: sec(96) + 10,
  uploaded: sec(99),

  // Picks, 102 to 114 s: Lynkk holds, the other five stamp in every 1.5 s.
  pickLynkk: sec(102) + 6,
  picksRest: [sec(106), sec(107.5), sec(109), sec(110.5), sec(112)] as const,

  // End card, 114 to 120 s.
  circleFrom: sec(114),
  logo: sec(116), // the trail's circle locks into the sphere
  cta: sec(117),
  price: sec(117.5),
  perch: sec(118), // Remi lands on the CTA, the music's last chord
  fine: sec(118.5),
} as const;

/** Every impact the camera feels, with how hard. */
export const HITS = [
  { f: T.shatter, amp: 1 },
  ...T.cards.map((f) => ({ f, amp: 0.6 })),
  { f: T.click, amp: 0.22 },
  ...T.stamps.map((f, i) => ({ f, amp: 0.3 + i * 0.1 })),
  { f: T.land, amp: 0.3 },
  { f: T.rename, amp: 0.25 },
  { f: T.pickLynkk, amp: 0.45 },
  { f: T.logo, amp: 0.7 },
  { f: T.perch, amp: 0.5 },
];
