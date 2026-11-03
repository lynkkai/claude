import React from "react";
import { INTER, IRIS, clamp, palette } from "../lib";
import { Sphere, Window, AppTile } from "./Desktop";

/**
 * The call and Lynkk's capture UI around it: a generic video-call window
 * labelled "Zoom" (not Zoom's UI), the "Zoom call detected" card top right,
 * the recording column on the right edge. After
 * design-lab/explorations/desktop-v2-capture (01-detected, 03-column) and
 * Features/Meetings/CallPrompt.swift, Features/Capture/CaptureStore.swift.
 */

export const CALL = { x: 60, y: 64, w: 1100, h: 740 } as const;
export const CARD = { x: 1124, y: 44, w: 372, h: 82 } as const;
/** The Record button's centre, for Remi's tap. */
export const RECORD_BTN = { x: CARD.x + CARD.w - 12 - 42, y: CARD.y + 12 + 13 } as const;
export const COLUMN = { x: 1192, y: 44, w: 308, h: 926 } as const;
export const PEOPLE = { x: 994, y: 232, w: 192, h: 300 } as const;

const PEOPLE_LIST: [string, string, string][] = [
  ["Priya Shah", "PS", "#beb4fb"],
  ["Sam Carter", "SC", "#f7b7ef"],
  ["Neha Rao", "NR", "#93b45c"],
  ["You", "Y", "#f57b3a"],
];

const Tile: React.FC<{ name: string; initials: string; color: string; speaking?: boolean }> = ({ name, initials, color, speaking }) => (
  <div
    style={{
      position: "relative",
      borderRadius: 12,
      background: "#2c2c2e",
      display: "grid",
      placeItems: "center",
      boxShadow: speaking ? "inset 0 0 0 3px #3ccf6b" : undefined,
    }}
  >
    <div style={{ width: 96, height: 96, borderRadius: 48, background: color, display: "grid", placeItems: "center", color: "#111", fontSize: 32, fontWeight: 600 }}>
      {initials}
    </div>
    <div style={{ position: "absolute", left: 14, bottom: 12, fontSize: 15, color: "rgba(255,255,255,0.9)", fontWeight: 500 }}>{name}</div>
  </div>
);

/** The generic call window. `caption` shows a live caption over the tiles. */
export const CallWindow: React.FC<{ speaking?: number; caption?: { who: string; text: string; o: number } }> = ({ speaking = 0, caption }) => (
  <Window x={CALL.x} y={CALL.y} w={CALL.w} h={CALL.h} title="Zoom Meeting" dark>
    <div style={{ position: "absolute", inset: 0, padding: 14, display: "grid", gridTemplateRows: "1fr 64px", gap: 12, color: "white" }}>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gridTemplateRows: "1fr 1fr", gap: 10 }}>
        {PEOPLE_LIST.map(([n, i, c], k) => (
          <Tile key={n} name={n} initials={i} color={c} speaking={k === speaking} />
        ))}
      </div>
      <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 14 }}>
        {["Mute", "Stop Video", "Participants", "Share", "Chat"].map((l) => (
          <div key={l} style={{ display: "grid", justifyItems: "center", gap: 6, width: 92 }}>
            <div style={{ width: 30, height: 30, borderRadius: 15, background: "#3a3a3d" }} />
            <span style={{ fontSize: 12, color: "rgba(255,255,255,0.7)" }}>{l}</span>
          </div>
        ))}
        <div style={{ height: 34, padding: "0 18px", borderRadius: 10, background: "#e5484d", display: "grid", placeItems: "center", fontSize: 14, fontWeight: 600 }}>End</div>
      </div>
    </div>
    {caption && caption.o > 0 ? (
      <div
        style={{
          position: "absolute",
          left: "50%",
          bottom: 190,
          transform: `translateX(-50%) translateY(${(1 - caption.o) * 16}px)`,
          opacity: caption.o,
          padding: "12px 22px",
          borderRadius: 10,
          background: "rgba(0,0,0,0.72)",
          color: "white",
          textAlign: "center",
          whiteSpace: "nowrap",
        }}
      >
        <div style={{ fontSize: 13, color: "rgba(255,255,255,0.6)", marginBottom: 2 }}>{caption.who}</div>
        <div style={{ fontSize: 22, fontWeight: 500 }}>{caption.text}</div>
      </div>
    ) : null}
  </Window>
);

/** Zoom's participant list, generic: four people, nobody else. */
export const Participants: React.FC<{ glow?: number }> = ({ glow = 0 }) => (
  <div
    style={{
      position: "absolute",
      left: PEOPLE.x,
      top: PEOPLE.y,
      width: PEOPLE.w,
      height: PEOPLE.h,
      borderRadius: 14,
      background: "#252528",
      boxShadow: `0 20px 50px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.1), 0 0 0 ${glow * 3}px ${palette.lavender}`,
      fontFamily: INTER,
      color: "white",
      padding: 16,
      letterSpacing: 0,
    }}
  >
    <div style={{ fontSize: 15, fontWeight: 600, marginBottom: 14 }}>Participants (4)</div>
    {PEOPLE_LIST.map(([n, i, c]) => (
      <div key={n} style={{ display: "flex", alignItems: "center", gap: 10, height: 52 }}>
        <div style={{ width: 32, height: 32, borderRadius: 16, background: c, color: "#111", display: "grid", placeItems: "center", fontSize: 12, fontWeight: 600 }}>{i}</div>
        <span style={{ fontSize: 15 }}>{n}</span>
      </div>
    ))}
  </div>
);

/**
 * "Zoom call detected": the Lynkk mark with the app in its corner, Record and
 * Not now, and the line that drains over 30 seconds. `drain` 0..1.
 */
export const CallCard: React.FC<{ drain: number; pressed?: number }> = ({ drain, pressed = 0 }) => (
  <div
    style={{
      position: "absolute",
      left: CARD.x,
      top: CARD.y,
      width: CARD.w,
      height: CARD.h,
      borderRadius: 16,
      overflow: "hidden",
      display: "flex",
      alignItems: "center",
      gap: 12,
      padding: "12px 12px 12px 14px",
      background: "linear-gradient(rgba(255,255,255,0.06), rgba(255,255,255,0) 50%), rgba(22,22,25,0.96)",
      boxShadow: "0 10px 32px rgba(0,0,0,0.45), inset 0 0 0 1px rgba(255,255,255,0.12)",
      fontFamily: INTER,
      color: "white",
      letterSpacing: 0,
      boxSizing: "border-box",
    }}
  >
    <div style={{ position: "relative", width: 40, height: 40, borderRadius: 10, background: "#111", display: "grid", placeItems: "center", flex: "none" }}>
      <Sphere size={24} />
      <div style={{ position: "absolute", right: -6, bottom: -6, border: "2px solid #2a2a30", borderRadius: 6 }}>
        <AppTile name="Zoom" size={16} />
      </div>
    </div>
    <div style={{ flex: 1, minWidth: 0 }}>
      <div style={{ fontSize: 14, fontWeight: 600 }}>Zoom call detected</div>
      <div style={{ fontSize: 12, lineHeight: 1.35, color: "rgba(255,255,255,0.6)", marginTop: 3 }}>Both sides are recorded on this Mac. Stop any time.</div>
    </div>
    <div style={{ display: "flex", flexDirection: "column", gap: 6, flex: "none" }}>
      <div
        style={{
          height: 26,
          minWidth: 84,
          borderRadius: 7,
          background: IRIS,
          display: "grid",
          placeItems: "center",
          fontSize: 12.5,
          fontWeight: 600,
          transform: `scale(${1 - pressed * 0.08})`,
          filter: `brightness(${1 + pressed * 0.35})`,
        }}
      >
        Record
      </div>
      <div style={{ height: 26, minWidth: 84, borderRadius: 7, background: "rgba(255,255,255,0.12)", display: "grid", placeItems: "center", fontSize: 12.5 }}>Not now</div>
    </div>
    <div style={{ position: "absolute", left: 0, bottom: 0, height: 2, background: "rgba(255,255,255,0.85)", width: `${(1 - clamp(drain)) * 100}%` }} />
  </div>
);

/** A level meter: bars that move with a fake but steady voice. */
const Meter: React.FC<{ f: number; seed: number; active: number }> = ({ f, seed, active }) => (
  <div style={{ display: "flex", gap: 2.5, alignItems: "center", height: 16 }}>
    {Array.from({ length: 14 }, (_, i) => {
      const v = 0.25 + 0.75 * Math.abs(Math.sin(f * 0.37 + i * 0.9 + seed) * Math.sin(f * 0.11 + i * 0.4 + seed * 2));
      return <div key={i} style={{ width: 3, height: 3 + v * 13 * active, borderRadius: 2, background: i < 9 ? IRIS : "rgba(255,255,255,0.35)" }} />;
    })}
  </div>
);

export type Turn = { who: string; you?: boolean; text: string; at: number };

/**
 * The recording column: clock, source app, Pause and Stop, two levels (you,
 * others), the live words, the note field. `f` is local to the scene.
 */
export const RecordColumn: React.FC<{ f: number; seconds: number; turns: Turn[]; ended?: number; partial?: string }> = ({ f, seconds, turns, ended = 0, partial }) => {
  const mm = Math.floor(seconds / 60);
  const ss = Math.floor(seconds % 60);
  return (
    <div
      style={{
        position: "absolute",
        left: COLUMN.x,
        top: COLUMN.y,
        width: COLUMN.w,
        height: COLUMN.h,
        borderRadius: 18,
        overflow: "hidden",
        display: "flex",
        flexDirection: "column",
        background: "rgba(22,22,26,0.9)",
        boxShadow: "0 18px 40px rgba(0,0,0,0.45), inset 0 0 0 1px rgba(255,255,255,0.12)",
        fontFamily: INTER,
        color: "white",
        letterSpacing: 0,
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: 10, padding: "14px 16px 12px", fontSize: 14 }}>
        <div style={{ width: 9, height: 9, borderRadius: 5, background: IRIS, boxShadow: `0 0 0 3px ${IRIS}38, 0 0 10px ${IRIS}99` }} />
        <span style={{ fontVariantNumeric: "tabular-nums", fontWeight: 600 }}>
          {mm}:{String(ss).padStart(2, "0")}
        </span>
        <span style={{ color: "rgba(255,255,255,0.6)", fontWeight: 500 }}>Zoom</span>
        <div style={{ flex: 1 }} />
        <div style={{ height: 24, padding: "0 10px", borderRadius: 7, background: "rgba(255,255,255,0.1)", display: "grid", placeItems: "center", fontSize: 12 }}>Pause</div>
        <div style={{ height: 24, padding: "0 10px", borderRadius: 7, background: "rgba(255,255,255,0.92)", color: "#0b0b0d", display: "grid", placeItems: "center", fontSize: 12, fontWeight: 600 }}>Stop</div>
      </div>
      <div style={{ display: "flex", gap: 14, padding: "0 16px 12px", borderBottom: "1px solid rgba(255,255,255,0.08)" }}>
        {[
          ["You", 0.6],
          ["Others", 1],
        ].map(([l, a], i) => (
          <div key={l as string} style={{ flex: 1, display: "flex", gap: 8, alignItems: "center" }}>
            <span style={{ fontSize: 11.5, color: "rgba(255,255,255,0.5)", width: 42 }}>{l}</span>
            <Meter f={f} seed={i * 3.1} active={(a as number) * (1 - ended)} />
          </div>
        ))}
      </div>
      <div style={{ flex: 1, display: "flex", flexDirection: "column", justifyContent: "flex-start", gap: 14, padding: 16, overflow: "hidden" }}>
        {turns.map((t, i) => {
          const o = clamp((f - t.at) / 5);
          if (o <= 0) return null;
          return (
            <div key={i} style={{ opacity: o, transform: `translateY(${(1 - o) * 14}px)` }}>
              <div style={{ fontSize: 11.5, fontWeight: 600, color: t.you ? "rgba(255,255,255,0.7)" : "rgba(255,255,255,0.45)" }}>{t.who}</div>
              <div style={{ fontSize: 14.5, lineHeight: 1.5, marginTop: 3, color: t.you ? "white" : "rgba(255,255,255,0.78)" }}>{t.text}</div>
            </div>
          );
        })}
        {partial ? <div style={{ fontSize: 14.5, color: "rgba(255,255,255,0.4)" }}>{partial}</div> : null}
      </div>
      {ended > 0 ? (
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 8,
            padding: "12px 16px",
            background: "rgba(255,255,255,0.06)",
            borderTop: "1px solid rgba(255,255,255,0.08)",
            fontSize: 13,
            opacity: ended,
          }}
        >
          <span style={{ flex: 1, color: "rgba(255,255,255,0.85)" }}>The call ended. Saving in 10 s.</span>
          <span style={{ height: 24, padding: "0 10px", borderRadius: 7, background: "rgba(255,255,255,0.12)", display: "grid", placeItems: "center", fontSize: 12 }}>Keep recording</span>
        </div>
      ) : null}
      <div style={{ borderTop: "1px solid rgba(255,255,255,0.08)", padding: "12px 16px" }}>
        <div style={{ fontSize: 12.5, padding: "8px 10px", borderRadius: 8, background: "rgba(255,255,255,0.06)", color: "rgba(255,255,255,0.4)" }}>Add a note</div>
      </div>
    </div>
  );
};
