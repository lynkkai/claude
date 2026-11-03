import React from "react";
import { INTER, IRIS, SCREEN, clamp, palette } from "../lib";
import { Sphere, Window } from "./Desktop";

/**
 * Spotter at the top of the screen: the bar and the answer card, drawn after
 * components/landing/spotter/spotter.css and Features/Spotter/SpotterView.swift
 * ("Reading your screen" is the app's own working line). The pilot doc it
 * reads is open on screen; Spotter never answers from past calls.
 */

export const SPOT = { x: SCREEN.w / 2 - 270, y: 44, w: 540 } as const;
export const DOC = { x: 790, y: 270, w: 250, h: 320 } as const;

const glass: React.CSSProperties = {
  background: "linear-gradient(rgba(255,255,255,0.09), rgba(255,255,255,0.02) 38%, rgba(255,255,255,0)), rgba(0,0,0,0.72)",
  boxShadow: "inset 0 0 0 1px rgba(255,255,255,0.14), 0 20px 50px rgba(0,0,0,0.45)",
  backdropFilter: "blur(26px) saturate(1.6)",
};

export const SpotterPanel: React.FC<{ f: number; working: number; answer: string; listening?: boolean }> = ({ f, working, answer, listening = true }) => (
  <div style={{ position: "absolute", left: SPOT.x, top: SPOT.y, width: SPOT.w, display: "grid", gap: 8, fontFamily: INTER, color: "white", letterSpacing: 0 }}>
    <div style={{ ...glass, height: 52, borderRadius: 26, display: "flex", alignItems: "center", gap: 10, padding: "0 10px 0 14px" }}>
      <Sphere size={20} />
      <span style={{ fontSize: 13.5 }}>Sales ▾</span>
      <div style={{ flex: 1 }} />
      {listening ? <div style={{ width: 7, height: 7, borderRadius: 4, background: palette.live, opacity: 0.6 + 0.4 * Math.cos(f / 6) }} /> : null}
      <div style={{ height: 28, minWidth: 64, padding: "0 12px", borderRadius: 8, display: "grid", placeItems: "center", fontSize: 12.5, background: listening ? IRIS : "rgba(255,255,255,0.1)" }}>Listen</div>
      <div style={{ height: 28, minWidth: 64, padding: "0 12px", borderRadius: 8, display: "grid", placeItems: "center", fontSize: 12.5, background: "white", color: "#111", fontWeight: 600 }}>
        Ask ⌘↩
      </div>
    </div>
    <div style={{ ...glass, borderRadius: 20, padding: 18, minHeight: 120, boxSizing: "border-box" }}>
      {working > 0 ? (
        <div style={{ display: "flex", alignItems: "center", gap: 10, fontSize: 14, color: "rgba(255,255,255,0.6)", opacity: working }}>
          <div
            style={{
              width: 20,
              height: 20,
              borderRadius: 10,
              background: `conic-gradient(from ${f * 10}deg, ${IRIS}, #beb4fb, #8ab4f8, ${IRIS})`,
              WebkitMask: "radial-gradient(circle, transparent 6px, #000 6.5px)",
            }}
          />
          Reading your screen
        </div>
      ) : null}
      {answer ? (
        <div>
          <div style={{ fontSize: 24, lineHeight: 1.4, fontWeight: 500 }}>{answer}</div>
        </div>
      ) : null}
    </div>
  </div>
);

/** The pilot plan open on screen: what Spotter reads. */
export const PilotDoc: React.FC<{ glow?: number }> = ({ glow = 0 }) => (
  <Window x={DOC.x} y={DOC.y} w={DOC.w} h={DOC.h} title="Pilot plan" style={{ boxShadow: `0 30px 70px rgba(0,0,0,0.45), 0 0 0 ${glow * 3}px ${IRIS}` }}>
    <div style={{ padding: "18px 20px", color: "#111" }}>
      <div style={{ fontSize: 12, color: "rgba(17,17,17,0.5)" }}>Corvane Logistics</div>
      <div style={{ fontSize: 22, fontWeight: 600, letterSpacing: "-0.02em", margin: "4px 0 14px" }}>The pilot</div>
      {["One team", "Up to 20 seats", "30 days", "Security review first"].map((t, i) => (
        <div key={t} style={{ display: "flex", gap: 10, alignItems: "center", fontSize: 16, padding: "9px 0", borderTop: "1px solid rgba(0,0,0,0.07)", background: i < 3 && glow > 0 ? `rgba(110,107,240,${0.1 * clamp(glow)})` : undefined }}>
          <span style={{ width: 6, height: 6, borderRadius: 3, background: "rgba(17,17,17,0.4)" }} />
          {t}
        </div>
      ))}
    </div>
  </Window>
);
