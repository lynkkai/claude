import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { INTER, clamp, expoOut, palette, springAt, tween } from "../lib";
import { Trail } from "../fx/fx";
import { Remi } from "../remi/Remi";
import { point, remiAt, type FlightPlan } from "../remi/flight";
import { BoardTitle, H, Pip, Plate, W, ink } from "../ui/parts";

/**
 * The two boards. Lynkk is first in both, as the companion page has it, and
 * every number on them comes from that page (checked November 2026). Names
 * are set in our own type: no competitor logos, no screenshots of their apps.
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

export const DeviceBoard: React.FC = () => {
  const f = useCurrentFrame() + SCENES.board.from;
  return (
    <AbsoluteFill>
      <Plate />
      <BoardTitle f={f} at={SCENES.board.from} text="Three ways to record a room" note="checked November 2026" />
      {COLS.map((c, i) => {
        const at = T.colsIn[i];
        const k = springAt(f, at, { stiffness: 260, damping: 22 });
        const x = 120 + i * 580;
        return (
          <div
            key={c.head}
            style={{
              position: "absolute",
              left: x,
              top: 248,
              width: 520,
              height: 620,
              borderRadius: 26,
              background: c.ours ? "rgba(112,99,190,0.16)" : "rgba(255,255,255,0.045)",
              boxShadow: `inset 0 0 0 ${c.ours ? 2 : 1}px ${c.ours ? "rgba(190,180,251,0.45)" : ink.line}`,
              opacity: clamp(k * 1.5),
              transform: `translateY(${(1 - k) * 60}px)`,
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
                const rk = tween(f, T.boardRows[r], T.boardRows[r] + 7, 0, 1, expoOut);
                return (
                  <div key={label} style={{ marginBottom: 26, opacity: rk, transform: `translateX(${(1 - rk) * 18}px)` }}>
                    <div style={{ fontSize: 19, fontWeight: 600, letterSpacing: "0.12em", color: ink.lo, marginBottom: 8 }}>{label.toUpperCase()}</div>
                    <div style={{ fontSize: 28, fontWeight: 500, lineHeight: 1.25, color: c.ours && r === 3 ? palette.lavender : ink.hi }}>{value}</div>
                  </div>
                );
              })}
            </div>
          </div>
        );
      })}
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

export const PicksBoard: React.FC = () => {
  const f = useCurrentFrame() + SCENES.picks.from;
  const at = (i: number) => (i === 0 ? T.pickLynkk : T.picksRest[i - 1]);
  const rowY = (i: number) => 262 + i * 104;
  const plan: FlightPlan = {
    path: [
      { f: SCENES.picks.from, x: W + 200, y: rowY(0) + 34 },
      { f: T.pickLynkk, x: 1600, y: rowY(0) + 34, ease: expoOut },
      { f: T.picksRest[0], x: 1660, y: rowY(1) + 34 },
      { f: T.picksRest[2], x: 1660, y: rowY(3) + 34 },
      { f: T.picksRest[4], x: 1660, y: rowY(5) + 34 },
      { f: SCENES.picks.from + SCENES.picks.dur, x: 1660, y: rowY(5) + 34 },
    ],
    faces: [
      [SCENES.picks.from, "happy"],
      [T.picksRest[0], "curious"],
      [T.picksRest[4], "happy"],
    ],
    stunts: [point(T.pickLynkk, T.picksRest[0], 185)],
  };
  const remi = remiAt(plan, f);
  return (
    <AbsoluteFill>
      <Plate />
      <BoardTitle f={f} at={SCENES.picks.from} text="Picks by what's on the table" note="prices checked November 2026" />
      {PICKS.map((p, i) => {
        const k = springAt(f, at(i), { stiffness: 320, damping: 21 });
        const lit = p.ours ? 1 : 0.9;
        return (
          <div
            key={p.name}
            style={{
              position: "absolute",
              left: 120,
              top: rowY(i),
              width: 1430,
              height: 86,
              borderRadius: 18,
              background: p.ours ? "rgba(112,99,190,0.2)" : "rgba(255,255,255,0.04)",
              boxShadow: `inset 0 0 0 ${p.ours ? 2 : 1}px ${p.ours ? "rgba(190,180,251,0.5)" : ink.line}`,
              opacity: clamp(k * 1.6) * lit,
              transform: `translateX(${(1 - k) * -40}px)`,
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
      <Trail f={f} pos={(g) => remiAt(plan, g)} from={SCENES.picks.from} len={8} width={13} opacity={0.75} />
      <Remi s={remi} size={120} id="remi-picks" glow={0.45} />
    </AbsoluteFill>
  );
};
