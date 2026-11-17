import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { INTER, clamp, expoOut, palette, springAt, tween } from "../lib";
import { Trail } from "../fx/fx";
import { Remi } from "../remi/Remi";
import { point, remiAt, squish, type FlightPlan } from "../remi/flight";
import { BoardTitle, Plate, W, ink } from "../ui/parts";
import { Cam, breathe, type Move } from "../ui/motion";

/**
 * 42 to 50 s. The table from above. The camera drops onto the laptop with the
 * ring of voices, then swings to each bad placement as Remi points it out.
 * Straight from the companion page's "How to get clear audio".
 */

const CX = 1010;
const CY = 600;
const TW = 760;
const TH = 330;

const Seat: React.FC<{ x: number; y: number; k: number; f: number; i: number }> = ({ x, y, k, f, i }) => (
  <div
    style={{
      position: "absolute",
      left: x - 34,
      top: y - 34 + breathe(f + i * 30, 3, 110),
      width: 68,
      height: 68,
      borderRadius: "50%",
      background: "rgba(190,180,251,0.22)",
      boxShadow: "inset 0 0 0 2px rgba(190,180,251,0.6)",
      opacity: clamp(k),
      transform: `scale(${0.5 + 0.5 * clamp(k)})`,
    }}
  />
);

const Cross: React.FC<{ x: number; y: number; k: number; label: string }> = ({ x, y, k, label }) => (
  <div style={{ position: "absolute", left: x - 30, top: y - 30, opacity: clamp(k), transform: `scale(${0.4 + 0.6 * clamp(k)}) rotate(${(1 - clamp(k)) * -40}deg)` }}>
    <svg width={60} height={60} viewBox="0 0 60 60">
      <circle cx={30} cy={30} r={27} fill="rgba(255,59,48,0.14)" stroke={palette.live} strokeWidth={3} />
      <path d="M20 20 L40 40 M40 20 L20 40" stroke={palette.live} strokeWidth={5} strokeLinecap="round" />
    </svg>
    <div
      style={{
        position: "absolute",
        left: -120,
        top: 70,
        width: 300,
        textAlign: "center",
        fontFamily: INTER,
        fontWeight: 600,
        fontSize: 26,
        color: "rgba(255,255,255,0.9)",
        whiteSpace: "nowrap",
      }}
    >
      {label}
    </div>
  </div>
);

export const MicMap: React.FC = () => {
  const f = useCurrentFrame() + SCENES.micMap.from;
  const S = SCENES.micMap.from;
  const table = springAt(f, T.tableIn, { stiffness: 220, damping: 22 });
  const ring = tween(f, T.ringOut, T.ringOut + 26, 0, 1, expoOut);
  const seats: [number, number][] = [
    [CX - 230, CY - 230],
    [CX, CY - 240],
    [CX + 230, CY - 230],
    [CX - 230, CY + 230],
    [CX, CY + 240],
    [CX + 230, CY + 230],
  ];
  const keys: Move[] = [
    { f: S, x: CX, y: CY, z: 0.8 },
    { f: T.ringOut, x: CX, y: CY, z: 1.06, ease: expoOut },
    { f: T.crosses[0], x: CX + 250, y: CY + 40, z: 1.18 },
    { f: T.crosses[1], x: CX + 300, y: CY - 240, z: 1.14 },
    { f: T.crosses[2], x: CX - 380, y: CY + 260, z: 1.12 },
    { f: S + SCENES.micMap.dur, x: CX - 60, y: CY + 30, z: 0.95 },
  ];
  const plan: FlightPlan = {
    path: [
      { f: S - 8, x: CX - 760, y: CY - 260 },
      { f: T.tableIn + 14, x: CX - 170, y: CY - 120, ease: expoOut },
      { f: T.ringOut + 6, x: CX, y: CY - 120, arc: 60 },
      { f: T.crosses[0] - 6, x: CX + 330, y: CY - 10, arc: 80 },
      { f: T.crosses[1] - 6, x: CX + 390, y: CY - 250, arc: 70 },
      { f: T.crosses[2] - 6, x: CX - 300, y: CY + 230, arc: 180, ease: expoOut },
      { f: S + SCENES.micMap.dur, x: CX - 420, y: CY + 150, arc: 50 },
    ],
    faces: [
      [S - 8, "curious"],
      [T.ringOut, "happy"],
      [T.crosses[0], "worried"],
      [T.crosses[2] + 10, "shrug"],
    ],
    stunts: [point(T.crosses[0] - 4, T.crosses[1], 150), point(T.crosses[1] - 4, T.crosses[2], 120), squish(T.ringOut, 0.2)],
  };
  const remi = remiAt(plan, f);
  return (
    <AbsoluteFill>
      <Plate />
      <Cam f={f} keys={keys} id="micmap">
        <BoardTitle f={f} at={S} text="Put it in the middle" />

        <svg style={{ position: "absolute", left: 0, top: 0, width: W, height: 1080, overflow: "visible" }}>
          <circle
            cx={CX}
            cy={CY}
            r={70 + ring * 290}
            fill="none"
            stroke={palette.lavender}
            strokeWidth={3}
            opacity={(1 - ring * 0.45) * clamp(table)}
            strokeDasharray="10 12"
            strokeDashoffset={-f * 0.6}
          />
          <circle cx={CX} cy={CY} r={40 + ring * 200} fill="rgba(112,99,190,0.1)" opacity={clamp(table) * 0.9} />
        </svg>

        <div
          style={{
            position: "absolute",
            left: CX - TW / 2,
            top: CY - TH / 2,
            width: TW,
            height: TH,
            borderRadius: 90,
            background: "rgba(255,255,255,0.06)",
            boxShadow: `inset 0 0 0 2px ${ink.line}`,
            opacity: clamp(table),
            transform: `scale(${0.85 + 0.15 * clamp(table)})`,
          }}
        />
        {seats.map(([x, y], i) => (
          <Seat key={i} x={x} y={y} k={tween(f, T.tableIn + 6 + i * 2, T.tableIn + 16 + i * 2)} f={f} i={i} />
        ))}

        <div style={{ position: "absolute", left: CX - 76, top: CY - 52 + breathe(f, 2, 90), width: 152, height: 104, opacity: clamp(table) }}>
          <div style={{ position: "absolute", inset: 0, borderRadius: 10, background: "#d7d6de", boxShadow: "0 12px 30px rgba(0,0,0,0.5)" }} />
          <div style={{ position: "absolute", left: 16, right: 16, top: 12, height: 58, borderRadius: 6, background: "#15151b" }} />
          <div style={{ position: "absolute", left: 0, right: 0, bottom: 10, textAlign: "center", fontFamily: INTER, fontSize: 17, fontWeight: 600, color: "#2b2b33" }}>Mac</div>
        </div>

        <Cross x={CX + TW / 2 + 30} y={CY} k={springAt(f, T.crosses[0], { stiffness: 340, damping: 18 })} label="Not at the far end" />
        <Cross x={CX + 430} y={CY - 320} k={springAt(f, T.crosses[1], { stiffness: 340, damping: 18 })} label="Not by the fan" />
        <Cross x={CX - 470} y={CY + 300} k={springAt(f, T.crosses[2], { stiffness: 340, damping: 18 })} label="Not in a pocket" />

        <div
          style={{
            position: "absolute",
            left: 120,
            top: 250,
            width: 370,
            fontFamily: INTER,
            fontSize: 28,
            lineHeight: 1.45,
            color: ink.mid,
            opacity: tween(f, T.tableIn + 10, T.tableIn + 24),
            transform: `translateX(${(1 - tween(f, T.tableIn + 10, T.tableIn + 28, 0, 1, expoOut)) * -40}px)`,
          }}
        >
          <div style={{ fontWeight: 700, fontSize: 36, color: ink.hi, marginBottom: 16 }}>Lid open.</div>
          Nothing on the keyboard, and don't type on the one that's recording.
          <div style={{ marginTop: 20, color: ink.lo }}>Big room: use an external mic.</div>
        </div>

        <Trail f={f} pos={(g) => remiAt(plan, g)} from={S - 8} len={10} width={13} opacity={0.8} />
        <Remi s={remi} size={118} id="remi-map" glow={0.45} />
      </Cam>
    </AbsoluteFill>
  );
};
