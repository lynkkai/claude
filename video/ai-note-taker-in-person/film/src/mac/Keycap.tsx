import React from "react";
import { INTER, clamp, expoIn, tween } from "../lib";

/**
 * A giant Mac keycap that drops from above and slams down on `at`: it falls
 * for `fall` frames, hits, travels down a few px (the press) and springs back.
 * Drawn in screen px. `label` is the key face; `sub` the small corner glyph.
 */
export const Keycap: React.FC<{
  f: number;
  at: number;
  x: number;
  y: number;
  size: number;
  label: React.ReactNode;
  sub?: React.ReactNode;
  fall?: number;
  out?: number;
  tilt?: number;
}> = ({ f, at, x, y, size, label, sub, fall = 8, out = 1e9, tilt = 0 }) => {
  if (f < at - fall) return null;
  const drop = tween(f, at - fall, at, 0, 1, expoIn);
  const after = f - at;
  const press = after >= 0 ? Math.exp(-after / 3.5) * Math.cos(after * 0.9) : 0;
  const depth = size * 0.11;
  const gone = tween(f, out, out + 6);
  if (gone >= 1) return null;
  const dy = (1 - drop) * -900 + Math.max(0, press) * depth * 0.8 + gone * 80;
  const sq = after >= 0 ? 1 + press * 0.05 : 1;
  return (
    <div
      style={{
        position: "absolute",
        left: x - size / 2,
        top: y - size / 2,
        width: size,
        height: size,
        transform: `translateY(${dy}px) rotate(${(1 - drop) * tilt}deg) scale(${sq}, ${2 - sq})`,
        opacity: clamp(drop * 3) * (1 - gone),
      }}
    >
      {/* the key's side */}
      <div style={{ position: "absolute", left: 0, right: 0, top: depth, height: size, borderRadius: size * 0.16, background: "linear-gradient(#9c9ca4, #5b5b63)" }} />
      {/* the shadow on the ground, tighter as it lands */}
      <div style={{ position: "absolute", left: "8%", right: "8%", bottom: -depth * 1.6, height: depth * 1.5, borderRadius: "50%", background: "rgba(0,0,0,0.45)", filter: "blur(14px)", opacity: drop }} />
      {/* the top */}
      <div
        style={{
          position: "absolute",
          inset: 0,
          borderRadius: size * 0.16,
          background: "linear-gradient(160deg, #ffffff, #e9e9ee 60%, #dcdce3)",
          boxShadow: "inset 0 2px 0 rgba(255,255,255,0.9), inset 0 -3px 6px rgba(0,0,0,0.08)",
          display: "grid",
          placeItems: "center",
          fontFamily: INTER,
          fontWeight: 500,
          color: "#1b1b1f",
          fontSize: size * 0.36,
          letterSpacing: "-0.02em",
        }}
      >
        {label}
        {sub ? <div style={{ position: "absolute", left: size * 0.12, bottom: size * 0.1, fontSize: size * 0.16, opacity: 0.7 }}>{sub}</div> : null}
      </div>
    </div>
  );
};

/** The globe glyph on the fn key. */
export const Globe: React.FC<{ size: number }> = ({ size }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={1.6}>
    <circle cx={12} cy={12} r={9} />
    <ellipse cx={12} cy={12} rx={4} ry={9} />
    <path d="M3 12h18" />
  </svg>
);
