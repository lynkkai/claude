import React from "react";
import { INTER, clamp, expoOut, palette, springAt, tween } from "../lib";
import { Sphere } from "../mac/Desktop";

/**
 * The parts the 16:9 graphics are built from: the dark plate every insert
 * sits on, the chapter card, the board frame and its rows, and the slate that
 * stands in for footage the team has not shot yet.
 */

export const W = 1920;
export const H = 1080;
/** Nothing a viewer must read goes below this: YouTube's progress bar. */
export const SAFE_BOTTOM = H - 60;

export const ink = {
  hi: palette.white,
  mid: "rgba(255,255,255,0.68)",
  lo: "rgba(255,255,255,0.42)",
  line: "rgba(255,255,255,0.12)",
  accent: palette.lavender,
};

export const Plate: React.FC<{ o?: number }> = ({ o = 1 }) => (
  <div
    style={{
      position: "absolute",
      inset: 0,
      opacity: o,
      background: "radial-gradient(70% 60% at 50% 36%, #1d1932 0%, #0b0a10 68%)",
    }}
  />
);

/** A lavender hairline that draws itself left to right. */
export const Rule: React.FC<{ x: number; y: number; w: number; k: number; color?: string; thick?: number }> = ({
  x,
  y,
  w,
  k,
  color = ink.line,
  thick = 2,
}) => (
  <div style={{ position: "absolute", left: x, top: y, width: w * clamp(k), height: thick, background: color, borderRadius: thick }} />
);

/**
 * A chapter card: the number, the title, a rule under it. One bar long, so
 * everything is in and gone inside 60 frames.
 */
export const ChapterCard: React.FC<{ f: number; at: number; n: number; title: string; accent?: string }> = ({ f, at, n, title, accent }) => {
  const k = springAt(f, at, { stiffness: 330, damping: 19 });
  const num = springAt(f, at + 3, { stiffness: 380, damping: 20 });
  const out = tween(f, at + 46, at + 56, 0, 1, expoOut);
  const words = title.split(" ");
  return (
    <div style={{ position: "absolute", inset: 0, opacity: 1 - out, transform: `translateX(${-out * 160}px)` }}>
      <Plate o={0.98} />
      <div
        style={{
          position: "absolute",
          left: 190,
          top: H / 2 - 150,
          fontFamily: INTER,
          fontWeight: 700,
          fontSize: 120,
          letterSpacing: "-0.05em",
          color: ink.accent,
          opacity: clamp(num * 1.6),
          transform: `translateY(${(1 - num) * 40}px)`,
        }}
      >
        {n}
      </div>
      <Rule x={190} y={H / 2 - 10} w={520} k={tween(f, at + 6, at + 22, 0, 1, expoOut)} color={ink.accent} thick={4} />
      <div
        style={{
          position: "absolute",
          left: 190,
          top: H / 2 + 36,
          width: 1480,
          fontFamily: INTER,
          fontWeight: 700,
          fontSize: 104,
          lineHeight: 1.05,
          letterSpacing: "-0.045em",
          color: ink.hi,
        }}
      >
        {words.map((w2, i) => {
          const wk = springAt(f, at + 4 + i * 3, { stiffness: 420, damping: 22, mass: 0.7 });
          return (
            <span
              key={i}
              style={{
                display: "inline-block",
                marginRight: "0.26em",
                opacity: clamp(wk * 1.8),
                transform: `translateY(${(1 - wk) * 34}px)`,
                color: accent === w2 ? ink.accent : undefined,
              }}
            >
              {w2}
            </span>
          );
        })}
      </div>
      <div style={{ position: "absolute", left: 194, top: H / 2 - 212, fontFamily: INTER, fontWeight: 600, fontSize: 22, letterSpacing: "0.22em", color: ink.lo, opacity: clamp(k * 1.4) }}>
        CHAPTER
      </div>
    </div>
  );
};

/** A board's heading, top left, with its rule. */
export const BoardTitle: React.FC<{ f: number; at: number; text: string; note?: string }> = ({ f, at, text, note }) => {
  const k = springAt(f, at, { stiffness: 320, damping: 20 });
  return (
    <>
      <div
        style={{
          position: "absolute",
          left: 120,
          top: 92,
          fontFamily: INTER,
          fontWeight: 700,
          fontSize: 58,
          letterSpacing: "-0.04em",
          color: ink.hi,
          opacity: clamp(k * 1.6),
          transform: `translateY(${(1 - k) * 26}px)`,
        }}
      >
        {text}
      </div>
      {note ? (
        <div style={{ position: "absolute", right: 120, top: 112, fontFamily: INTER, fontWeight: 500, fontSize: 24, color: ink.lo, opacity: clamp(k * 1.2) }}>{note}</div>
      ) : null}
      <Rule x={120} y={178} w={1680} k={tween(f, at + 4, at + 20, 0, 1, expoOut)} />
    </>
  );
};

/** The small Lynkk sphere used to mark our own row. */
export const Pip: React.FC<{ size?: number; o?: number }> = ({ size = 26, o = 1 }) => (
  <div style={{ opacity: o, filter: "drop-shadow(0 0 10px rgba(190,180,251,0.5))" }}>
    <Sphere size={size} color={palette.lavender} />
  </div>
);

/**
 * The slate that stands in for footage: what the shot is, when it runs, and
 * the line the presenter says over it. It is deliberately plain, so nobody
 * mistakes it for a finished frame.
 */
export const Slate: React.FC<{ f: number; kind: "A-ROLL" | "B-ROLL" | "SCREEN" | "A-ROLL + SCREEN"; what: string; vo?: string; from: string; to: string }> = ({
  f,
  kind,
  what,
  vo,
  from,
  to,
}) => {
  const k = tween(f, 0, 3);
  return (
    <div style={{ position: "absolute", inset: 0, opacity: k }}>
      <div style={{ position: "absolute", inset: 0, background: "#0a0a0e" }} />
      <div
        style={{
          position: "absolute",
          left: 120,
          top: 150,
          right: 120,
          bottom: 190,
          border: `3px dashed rgba(255,255,255,0.16)`,
          borderRadius: 28,
        }}
      />
      <div style={{ position: "absolute", left: 180, top: 232, fontFamily: INTER, fontWeight: 700, fontSize: 24, letterSpacing: "0.24em", color: ink.accent }}>{kind}</div>
      <div style={{ position: "absolute", right: 180, top: 232, fontFamily: INTER, fontWeight: 600, fontSize: 24, letterSpacing: "0.1em", color: ink.lo }}>
        {from} to {to}
      </div>
      <div
        style={{
          position: "absolute",
          left: 180,
          right: 180,
          top: 330,
          fontFamily: INTER,
          fontWeight: 600,
          fontSize: 62,
          lineHeight: 1.15,
          letterSpacing: "-0.035em",
          color: ink.hi,
        }}
      >
        {what}
      </div>
      {vo ? (
        <div
          style={{
            position: "absolute",
            left: 180,
            right: 180,
            top: 600,
            fontFamily: INTER,
            fontWeight: 400,
            fontSize: 34,
            lineHeight: 1.4,
            color: ink.mid,
          }}
        >
          <span style={{ color: ink.lo, fontWeight: 600, fontSize: 22, letterSpacing: "0.18em", display: "block", marginBottom: 16 }}>VOICE-OVER</span>
          {vo}
        </div>
      ) : null}
    </div>
  );
};
