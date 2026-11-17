import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { INTER, IRIS, clamp, expoOut, palette, springAt, tween } from "../lib";
import { BoardTitle, H, Plate, W, ink } from "../ui/parts";

/**
 * 72 to 82 s. One mic, four people. The transcript is split by speaker, the
 * labels light as each person talks, and one is renamed, which is what the
 * companion page says you do once.
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

export const Labels: React.FC = () => {
  const f = useCurrentFrame() + SCENES.labels.from;
  const panel = springAt(f, T.transcriptIn, { stiffness: 230, damping: 24 });
  const renamed = tween(f, T.rename, T.rename + 8, 0, 1, expoOut);
  return (
    <AbsoluteFill>
      <Plate />
      <BoardTitle f={f} at={SCENES.labels.from} text="One mic, four people" />
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
          transform: `translateY(${(1 - panel) * 40}px)`,
        }}
      >
        <div style={{ fontSize: 20, fontWeight: 600, letterSpacing: "0.16em", color: ink.lo, marginBottom: 26 }}>TRANSCRIPT</div>
        {LINES.map((l, i) => {
          const at = T.speakers[i];
          const k = tween(f, at, at + 8, 0, 1, expoOut);
          const live = f >= at && f < at + 34;
          const name = l.rename && renamed > 0.5 ? l.rename : l.who;
          return (
            <div key={i} style={{ display: "flex", gap: 22, marginBottom: 26, opacity: 0.25 + 0.75 * k }}>
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
                  color: l.you ? "#fff" : live ? "#fff" : ink.mid,
                  background: l.you ? `rgba(110,107,240,0.75)` : live ? "rgba(190,180,251,0.3)" : "rgba(255,255,255,0.06)",
                  boxShadow: l.rename && renamed > 0 ? `inset 0 0 0 ${1 + renamed * 2}px ${IRIS}` : `inset 0 0 0 1px ${ink.line}`,
                  transform: l.rename ? `scale(${1 + Math.sin(Math.PI * renamed) * 0.06})` : undefined,
                }}
              >
                {name}
              </div>
              <div style={{ fontSize: 30, lineHeight: 1.4, color: live ? ink.hi : ink.mid, paddingTop: 6 }}>{l.text}</div>
            </div>
          );
        })}
      </div>

      <div style={{ position: "absolute", right: 120, top: 300, width: 420, fontFamily: INTER }}>
        <div style={{ fontSize: 44, fontWeight: 700, letterSpacing: "-0.04em", color: ink.hi, opacity: tween(f, T.speakers[0], T.speakers[0] + 10) }}>
          Split by <span style={{ color: palette.lavender }}>speaker.</span>
        </div>
        <div style={{ marginTop: 22, fontSize: 28, lineHeight: 1.45, color: ink.mid, opacity: tween(f, T.speakers[1], T.speakers[1] + 10) }}>
          The AI separates voices into Speaker 1, Speaker 2, and you rename them once.
        </div>
        <div style={{ marginTop: 26, fontSize: 28, fontWeight: 600, color: palette.lavender, opacity: tween(f, T.rename, T.rename + 10) }}>17 languages, Hinglish included.</div>
      </div>

      <div
        style={{
          position: "absolute",
          left: 120,
          top: H - 136,
          fontFamily: INTER,
          fontSize: 22,
          color: ink.lo,
          opacity: 0.8 * clamp(panel),
        }}
      >
        Stand-in transcript: swap in the real one from the room test.
      </div>
    </AbsoluteFill>
  );
};
