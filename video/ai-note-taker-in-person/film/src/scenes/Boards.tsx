import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { INTER, clamp, expoOut, palette, springAt, tween } from "../lib";
import { Trail } from "../fx/fx";
import { Remi } from "../remi/Remi";
import { hop, point, remiAt, squish, type FlightPlan } from "../remi/flight";
import { BoardTitle, Pip, Plate, W, ink } from "../ui/parts";
import { Cam, breathe, type Move } from "../ui/motion";

/**
 * The two boards. The camera rides along them: it swings to each column as it
 * lands, then pulls back, and Remi flies the same path and points at what is
 * arriving, so neither board ever sits still.
 *
 * Lynkk is first in both, as the companion page has it, and every number comes
 * from that page (checked November 2026). Names are set in our own type: no
 * competitor logos, no screenshots of their apps.
 */

const COLS = [
  {
    head: "Laptop",
    sub: "on the table, plugged in",
    rows: [
      ["Apps", "Lynkk (Mac) · Granola"],
      ["Offline", "Lynkk keeps recording"],
      ["Speaker labels", "Yes, 17 languages"],
      ["Price", "Lynkk Pro $4/mo"],
    ],
    ours: true,
  },
  {
    head: "Phone",
    sub: "always with you",
    rows: [
      ["Apps", "Otter · Granola · Fireflies"],
      ["Offline", "Varies, check the app"],
      ["Speaker labels", "Yes"],
      ["Price", "$8.33 to $14 /user/mo"],
    ],
    ours: false,
  },
  {
    head: "Recorder",
    sub: "clip it on, sync later",
    rows: [
      ["Apps", "Plaud"],
      ["Offline", "Yes"],
      ["Speaker labels", "Yes"],
      ["Price", "Device + subscription"],
    ],
    ours: false,
  },
] as const;

const COL_X = (i: number) => 120 + i * 580;
const COL_MID = (i: number) => COL_X(i) + 260;

export const DeviceBoard: React.FC = () => {
  const f = useCurrentFrame() + SCENES.board.from;
  const S = SCENES.board.from;
  const keys: Move[] = [
    { f: S, x: 560, y: 470, z: 1.22 },
    { f: T.colsIn[1], x: 900, y: 500, z: 1.14 },
    { f: T.colsIn[2], x: 1250, y: 500, z: 1.1, ease: expoOut },
    { f: T.boardRows[0], x: 980, y: 540, z: 0.97 },
    { f: T.boardRows[3], x: 960, y: 560, z: 0.99, ease: (t) => t },
    { f: S + SCENES.board.dur, x: 940, y: 545, z: 1.08, ease: (t) => t },
  ];
  const plan: FlightPlan = {
    path: [
      { f: S - 10, x: -220, y: 430 },
      { f: T.colsIn[0] + 10, x: COL_MID(0) + 150, y: 300, ease: expoOut },
      { f: T.colsIn[1] + 8, x: COL_MID(1) + 150, y: 300, arc: 70 },
      { f: T.colsIn[2] + 8, x: COL_MID(2) + 150, y: 300, arc: 70 },
      { f: T.boardRows[0], x: COL_MID(2) + 210, y: 470, arc: 40 },
      { f: T.boardRows[3], x: COL_MID(0) - 110, y: 690, arc: 150, ease: expoOut },
      { f: S + SCENES.board.dur, x: COL_MID(0) - 150, y: 760 },
    ],
    faces: [
      [S - 10, "wow"],
      [T.colsIn[1], "curious"],
      [T.boardRows[0], "happy"],
    ],
    stunts: [
      point(T.colsIn[0] + 10, T.colsIn[1], 200),
      point(T.boardRows[3], T.boardRows[3] + 40, -20),
      hop(T.boardRows[2], 34, 12),
    ],
  };
  const remi = remiAt(plan, f);
  return (
    <AbsoluteFill>
      <Plate />
      <Cam f={f} keys={keys} id="board">
        <BoardTitle f={f} at={S} text="Three ways to record a room" note="checked November 2026" />
        {COLS.map((c, i) => {
          const at = T.colsIn[i];
          const k = springAt(f, at, { stiffness: 250, damping: 20 });
          const lean = (1 - k) * (i === 0 ? -70 : i === 2 ? 70 : 0);
          return (
            <div
              key={c.head}
              style={{
                position: "absolute",
                left: COL_X(i),
                top: 248 + breathe(f + i * 40, 3),
                width: 520,
                height: 620,
                borderRadius: 26,
                background: c.ours ? "rgba(112,99,190,0.16)" : "rgba(255,255,255,0.045)",
                boxShadow: `inset 0 0 0 ${c.ours ? 2 : 1}px ${c.ours ? "rgba(190,180,251,0.45)" : ink.line}`,
                opacity: clamp(k * 1.5),
                transform: `translate(${lean}px, ${(1 - k) * 90}px) rotate(${(1 - k) * (i - 1) * 3}deg)`,
                fontFamily: INTER,
                padding: "34px 34px 0",
                boxSizing: "border-box",
              }}
            >
              <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
                <div style={{ fontSize: 46, fontWeight: 700, letterSpacing: "-0.04em", color: ink.hi }}>{c.head}</div>
                {c.ours ? <Pip size={24} /> : null}
              </div>
              <div style={{ fontSize: 24, fontWeight: 500, color: ink.lo, marginTop: 6 }}>{c.sub}</div>
              <div style={{ marginTop: 30 }}>
                {c.rows.map(([label, value], r) => {
                  const rk = springAt(f, T.boardRows[r] + i * 2, { stiffness: 420, damping: 24, mass: 0.7 });
                  return (
                    <div key={label} style={{ marginBottom: 26, opacity: clamp(rk * 1.8), transform: `translateX(${(1 - rk) * 26}px)` }}>
                      <div style={{ fontSize: 19, fontWeight: 600, letterSpacing: "0.12em", color: ink.lo, marginBottom: 8 }}>{label.toUpperCase()}</div>
                      <div style={{ fontSize: 28, fontWeight: 500, lineHeight: 1.25, color: c.ours && r === 3 ? palette.lavender : ink.hi }}>{value}</div>
                    </div>
                  );
                })}
              </div>
            </div>
          );
        })}
        <Trail f={f} pos={(g) => remiAt(plan, g)} from={SCENES.board.from - 10} len={10} width={14} opacity={0.8} />
        <Remi s={remi} size={120} id="remi-board" glow={0.45} />
      </Cam>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------------ picks

type Pick = { n: number; name: string; what: string; price: string; ours?: boolean };
const PICKS: Pick[] = [
  { n: 1, name: "Lynkk", what: "Mac, records the room, offline, 17 languages", price: "$4/mo (₹250)", ours: true },
  { n: 2, name: "Otter", what: "phone, live transcript as people speak", price: "free 300 min · $8.33/user/mo" },
  { n: 3, name: "Granola", what: "phone and computer, you type your own notes", price: "$14/user/mo" },
  { n: 4, name: "Fireflies", what: "phone, same library as your online calls", price: "$10/seat/mo" },
  { n: 5, name: "Plaud", what: "a recorder you clip on, records offline", price: "device + subscription" },
  { n: 6, name: "Apple Voice Memos", what: "transcript only, no labels, no summary", price: "free" },
];

const ROW_Y = (i: number) => 262 + i * 104;

export const PicksBoard: React.FC = () => {
  const f = useCurrentFrame() + SCENES.picks.from;
  const S = SCENES.picks.from;
  const at = (i: number) => (i === 0 ? T.pickLynkk : T.picksRest[i - 1]);
  // The camera starts tight on our row and pulls back as the rest stamp in.
  const keys: Move[] = [
    { f: S, x: 700, y: ROW_Y(0) + 40, z: 1.5 },
    { f: T.pickLynkk + 20, x: 760, y: ROW_Y(0) + 70, z: 1.34, ease: expoOut },
    { f: T.picksRest[1], x: 820, y: ROW_Y(2) + 40, z: 1.12 },
    { f: T.picksRest[4], x: 850, y: ROW_Y(4) - 10, z: 0.97 },
    { f: S + SCENES.picks.dur, x: 850, y: ROW_Y(3), z: 1.04, ease: (t) => t },
  ];
  const plan: FlightPlan = {
    path: [
      { f: S - 8, x: 1900, y: ROW_Y(0) - 60 },
      { f: T.pickLynkk, x: 1600, y: ROW_Y(0) + 40, ease: expoOut },
      { f: T.picksRest[0], x: 1640, y: ROW_Y(1) + 40, arc: 36 },
      { f: T.picksRest[1], x: 1640, y: ROW_Y(2) + 40, arc: 30 },
      { f: T.picksRest[2], x: 1640, y: ROW_Y(3) + 40, arc: 30 },
      { f: T.picksRest[3], x: 1640, y: ROW_Y(4) + 40, arc: 30 },
      { f: T.picksRest[4], x: 1640, y: ROW_Y(5) + 40, arc: 30 },
      { f: S + SCENES.picks.dur, x: 1540, y: ROW_Y(0) + 40, arc: 240, ease: expoOut },
    ],
    faces: [
      [S - 8, "happy"],
      [T.picksRest[0], "curious"],
      [T.picksRest[4], "happy"],
    ],
    stunts: [point(T.pickLynkk, T.picksRest[0], 185), squish(T.pickLynkk, 0.24), hop(T.picksRest[4] + 10, 30, 12)],
  };
  const remi = remiAt(plan, f);
  return (
    <AbsoluteFill>
      <Plate />
      <Cam f={f} keys={keys} id="picks">
        <BoardTitle f={f} at={S} text="Picks by what's on the table" note="prices checked November 2026" />
        {PICKS.map((p, i) => {
          const k = springAt(f, at(i), { stiffness: 340, damping: 20 });
          const live = f >= at(i) && f < at(i) + 26;
          return (
            <div
              key={p.name}
              style={{
                position: "absolute",
                left: 120,
                top: ROW_Y(i),
                width: 1430,
                height: 86,
                borderRadius: 18,
                background: p.ours ? "rgba(112,99,190,0.2)" : live ? "rgba(255,255,255,0.09)" : "rgba(255,255,255,0.04)",
                boxShadow: `inset 0 0 0 ${p.ours ? 2 : 1}px ${p.ours ? "rgba(190,180,251,0.5)" : ink.line}`,
                opacity: clamp(k * 1.6),
                transform: `translateX(${(1 - k) * -70}px) scale(${0.97 + 0.03 * clamp(k)})`,
                display: "flex",
                alignItems: "center",
                fontFamily: INTER,
                padding: "0 28px",
                boxSizing: "border-box",
              }}
            >
              <div style={{ width: 54, fontSize: 34, fontWeight: 700, color: p.ours ? palette.lavender : ink.lo }}>{p.n}</div>
              <div style={{ width: 330, display: "flex", alignItems: "center", gap: 12 }}>
                <span style={{ fontSize: p.name.length > 10 ? 32 : 38, fontWeight: 700, letterSpacing: "-0.03em", color: ink.hi }}>{p.name}</span>
                {p.ours ? <Pip size={22} /> : null}
              </div>
              <div style={{ flex: 1, fontSize: 26, fontWeight: 500, color: ink.mid }}>{p.what}</div>
              <div style={{ fontSize: 26, fontWeight: 600, color: p.ours ? palette.lavender : ink.mid, textAlign: "right" }}>{p.price}</div>
            </div>
          );
        })}
        <Trail f={f} pos={(g) => remiAt(plan, g)} from={S - 8} len={9} width={13} opacity={0.8} />
        <Remi s={remi} size={116} id="remi-picks" glow={0.45} />
      </Cam>
    </AbsoluteFill>
  );
};
