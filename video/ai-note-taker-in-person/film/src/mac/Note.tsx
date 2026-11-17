import React from "react";
import { INTER, IRIS, backOut, clamp, tween } from "../lib";

/**
 * The note Lynkk writes from the call: the Meeting Brief's summary, a key
 * decision and an action item (owner, due). The Corvane example and its
 * action item are the site's own (dot/pages/home.ts).
 */

/** How a stamped row lands: drops from 1.5x, rotated, with a hard stop. */
const stamp = (f: number, at: number) => {
  const t = tween(f, at, at + 7, 0, 1, backOut);
  return {
    opacity: clamp((f - at + 1) / 2),
    transform: `scale(${1.5 - 0.5 * t}) rotate(${(1 - t) * -4}deg)`,
  };
};

const Label: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div style={{ fontSize: 15, fontWeight: 600, color: "rgba(17,17,17,0.45)", marginBottom: 10 }}>{children}</div>
);

export const NoteCard: React.FC<{ f: number; stamps: readonly number[]; width: number; glowAction?: number }> = ({ f, stamps, width, glowAction = 0 }) => (
  <div
    style={{
      width,
      borderRadius: 26,
      background: "#ffffff",
      boxShadow: "0 40px 90px rgba(0,0,0,0.45), inset 0 0 0 1px rgba(0,0,0,0.06)",
      fontFamily: INTER,
      letterSpacing: 0,
      color: "#111",
      padding: "34px 38px 38px",
      boxSizing: "border-box",
    }}
  >
    <div style={{ display: "flex", alignItems: "center", gap: 10, fontSize: 15, color: "rgba(17,17,17,0.5)" }}>
      <span style={{ width: 9, height: 9, borderRadius: 5, background: IRIS }} />
      Zoom · 47 min · Today
    </div>
    <div style={{ fontSize: 40, fontWeight: 600, letterSpacing: "-0.03em", margin: "10px 0 26px", lineHeight: 1.1 }}>Corvane Logistics, pilot call</div>

    <div style={{ ...stamp(f, stamps[0]), transformOrigin: "0 50%", marginBottom: 24 }}>
      <Label>Summary</Label>
      <div style={{ fontSize: 22, lineHeight: 1.45, color: "rgba(17,17,17,0.82)" }}>Corvane wants to try Lynkk with one team before the IT review.</div>
    </div>

    <div style={{ ...stamp(f, stamps[1]), transformOrigin: "0 50%", marginBottom: 24 }}>
      <Label>Key decision</Label>
      <div style={{ display: "inline-flex", alignItems: "center", gap: 10, fontSize: 22, padding: "10px 16px", borderRadius: 12, background: "#f1f0fb" }}>
        <span style={{ fontWeight: 600, color: IRIS }}>✓</span> Start with a 30-day pilot
      </div>
    </div>

    <div style={{ ...stamp(f, stamps[2]), transformOrigin: "0 50%" }}>
      <Label>Action items</Label>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: 14,
          padding: "16px 18px",
          borderRadius: 14,
          background: "#f6f6f8",
          boxShadow: `inset 0 0 0 ${1 + glowAction * 2}px ${glowAction > 0 ? IRIS : "rgba(0,0,0,0.06)"}`,
        }}
      >
        <div style={{ width: 24, height: 24, borderRadius: 7, border: "2px solid rgba(17,17,17,0.3)", flex: "none" }} />
        <div style={{ flex: 1, fontSize: 23, fontWeight: 500 }}>Send the security overview by Friday</div>
      </div>
      <div style={{ display: "flex", gap: 10, marginTop: 10, paddingLeft: 56, fontSize: 15, color: "rgba(17,17,17,0.5)" }}>
        <span>You</span>·<span>Due Fri</span>·<span>High</span>
      </div>
    </div>
  </div>
);
