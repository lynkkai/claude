import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { INTER, IRIS, clamp, expoOut, palette, springAt, tween } from "../lib";
import { Trail } from "../fx/fx";
import { Remi } from "../remi/Remi";
import { listen, point, remiAt, squish, type FlightPlan } from "../remi/flight";
import { BoardTitle, H, Plate, ink } from "../ui/parts";
import { Cam, breathe, type Move } from "../ui/motion";

/**
 * 72 to 82 s. One mic, four people. The camera rides down the transcript as
 * each label lights, Remi listens along, then knocks one label into its real
 * name, which is what the companion page says you do once.
 *
 * The lines here are a stand-in: replace them with the real transcript from
 * the test recording before this renders for the final cut.
 */

type Line = { who: string; text: string; you?: boolean; rename?: string };
const LINES: Line[] = [
  { who: "You", text: "So we'd start with one team and widen it after the review.", you: true },
  { who: "Speaker 1", text: "That works. IT will want the security overview first.", rename: "Priya" },
  { who: "Speaker 2", text: "How long does the pilot run?" },
  { who: "Speaker 3", text: "Thirty days, then we decide together." },
];

const ROW_Y = (i: number) => 330 + i * 106;

export const Labels: React.FC = () => {
  const f = useCurrentFrame() + SCENES.labels.from;
  const S = SCENES.labels.from;
  const panel = springAt(f, T.transcriptIn, { stiffness: 230, damping: 24 });
  const renamed = springAt(f, T.rename, { stiffness: 330, damping: 17 });
  const keys: Move[] = [
    { f: S, x: 700, y: 330, z: 1.2 },
    { f: T.speakers[0], x: 740, y: 380, z: 1.1, ease: expoOut },
    { f: T.speakers[2], x: 780, y: 520, z: 1.0 },
    { f: T.rename, x: 560, y: ROW_Y(1) + 30, z: 1.3, ease: expoOut },
    { f: T.rename + 24, x: 640, y: ROW_Y(1) + 40, z: 1.22 },
    { f: S + SCENES.labels.dur, x: 820, y: 520, z: 0.98, ease: (t) => t },
  ];
  const plan: FlightPlan = {
    path: [
      { f: S - 8, x: -200, y: 300 },
      { f: T.speakers[0], x: 1340, y: ROW_Y(0) + 20, ease: expoOut },
      { f: T.speakers[1], x: 1360, y: ROW_Y(1) + 20, arc: 34 },
      { f: T.speakers[2], x: 1360, y: ROW_Y(2) + 20, arc: 30 },
      { f: T.speakers[3], x: 1360, y: ROW_Y(3) + 20, arc: 30 },
      { f: T.rename - 6, x: 420, y: ROW_Y(1) - 40, arc: 160, ease: expoOut },
      { f: T.rename, x: 350, y: ROW_Y(1) + 16, ease: (t) => t * t },
      { f: S + SCENES.labels.dur, x: 560, y: ROW_Y(3) + 90, arc: 120 },
    ],
    faces: [
      [S - 8, "curious"],
      [T.speakers[0], "listening"],
      [T.rename, "happy"],
    ],
    stunts: [listen(T.speakers[0], T.speakers[3] + 20), squish(T.rename, 0.3), point(T.speakers[1], T.rename - 10, 10)],
  };
  const remi = remiAt(plan, f);
  return (
    <AbsoluteFill>
      <Plate />
      <Cam f={f} keys={keys} id="labels">
        <BoardTitle f={f} at={S} text="One mic, four people" />
        <div
          style={{
            position: "absolute",
            left: 120,
            top: 250,
            width: 1180,
            borderRadius: 24,
            background: "rgba(255,255,255,0.045)",
            boxShadow: `inset 0 0 0 1px ${ink.line}`,
            padding: "34px 40px",
            boxSizing: "border-box",
            fontFamily: INTER,
            opacity: clamp(panel * 1.5),
            transform: `translateY(${(1 - panel) * 50}px)`,
          }}
        >
          <div style={{ fontSize: 20, fontWeight: 600, letterSpacing: "0.16em", color: ink.lo, marginBottom: 26 }}>TRANSCRIPT</div>
          {LINES.map((l, i) => {
            const at = T.speakers[i];
            const k = springAt(f, at, { stiffness: 380, damping: 22 });
            const live = f >= at && f < at + 34;
            const name = l.rename && renamed > 0.5 ? l.rename : l.who;
            return (
              <div
                key={i}
                style={{
                  display: "flex",
                  gap: 22,
                  marginBottom: 26,
                  opacity: 0.22 + 0.78 * clamp(k),
                  transform: `translateX(${(1 - clamp(k)) * 30}px)`,
                }}
              >
                <div
                  style={{
                    flex: "none",
                    minWidth: 168,
                    height: 48,
                    padding: "0 18px",
                    borderRadius: 12,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    fontSize: 24,
                    fontWeight: 600,
                    color: l.you || live ? "#fff" : ink.mid,
                    background: l.you ? "rgba(110,107,240,0.75)" : live ? "rgba(190,180,251,0.3)" : "rgba(255,255,255,0.06)",
                    boxShadow: l.rename && renamed > 0 ? `inset 0 0 0 ${1 + Math.min(1, renamed) * 2}px ${IRIS}` : `inset 0 0 0 1px ${ink.line}`,
                    transform: l.rename ? `scale(${1 + Math.sin(Math.PI * clamp(renamed)) * 0.12}) rotate(${Math.sin(Math.PI * clamp(renamed)) * -3}deg)` : undefined,
                  }}
                >
                  {name}
                </div>
                <div style={{ fontSize: 30, lineHeight: 1.4, color: live ? ink.hi : ink.mid, paddingTop: 6 }}>{l.text}</div>
              </div>
            );
          })}
        </div>

        <div style={{ position: "absolute", left: 1420, top: 300 + breathe(f, 4, 160), width: 400, fontFamily: INTER }}>
          <div style={{ fontSize: 44, fontWeight: 700, letterSpacing: "-0.04em", color: ink.hi, opacity: tween(f, T.speakers[0], T.speakers[0] + 10) }}>
            Split by <span style={{ color: palette.lavender }}>speaker.</span>
          </div>
          <div style={{ marginTop: 22, fontSize: 28, lineHeight: 1.45, color: ink.mid, opacity: tween(f, T.speakers[1], T.speakers[1] + 10) }}>
            The AI separates voices into Speaker 1, Speaker 2, and you rename them once.
          </div>
          <div style={{ marginTop: 26, fontSize: 28, fontWeight: 600, color: palette.lavender, opacity: tween(f, T.rename, T.rename + 10) }}>17 languages, Hinglish included.</div>
        </div>

        <Trail f={f} pos={(g) => remiAt(plan, g)} from={S - 8} len={10} width={12} opacity={0.75} />
        <Remi s={remi} size={110} id="remi-labels" glow={0.45} />
      </Cam>
      <div style={{ position: "absolute", left: 120, top: H - 120, fontFamily: INTER, fontSize: 22, color: ink.lo, opacity: 0.75 * clamp(panel) }}>
        Stand-in transcript: swap in the real one from the room test.
      </div>
    </AbsoluteFill>
  );
};
