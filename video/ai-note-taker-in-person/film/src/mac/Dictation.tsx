import React from "react";
import { INTER, IRIS, SCREEN, clamp, palette } from "../lib";
import { AppTile, NOTCH, Window } from "./Desktop";

/**
 * Dictation: the notch island (Features/Dictation/IslandViews.swift) and the
 * apps the words land in. The island springs out of the notch and opens a
 * band below the camera: where the words are going (the app's icon and name),
 * a hairline, then the Iris dot and what is happening to them.
 */

export const ISLAND_W = 380;

export const NotchIsland: React.FC<{
  /** 0 closed (just the notch) .. 1 open. */
  open: number;
  app: string;
  status: React.ReactNode;
  f: number;
  /** 0..1, the level meter. */
  level?: number;
  done?: boolean;
}> = ({ open, app, status, f, level = 0.8, done = false }) => {
  const w = NOTCH.w + (ISLAND_W - NOTCH.w) * open;
  const h = NOTCH.h + 44 * open;
  const r = 12 + 12 * open;
  return (
    <div
      style={{
        position: "absolute",
        left: SCREEN.w / 2 - w / 2,
        top: 0,
        width: w,
        height: h,
        background: "#000",
        borderRadius: `0 0 ${r}px ${r}px`,
        overflow: "hidden",
        fontFamily: INTER,
        letterSpacing: 0,
        color: "white",
        boxShadow: open > 0.1 ? `0 10px 30px rgba(0,0,0,0.35), 0 6px 22px -6px ${IRIS}${Math.round(open * 160).toString(16).padStart(2, "0")}` : undefined,
      }}
    >
      <div style={{ position: "absolute", left: 16, right: 16, top: NOTCH.h + 6, height: 32, display: "flex", alignItems: "center", gap: 10, opacity: clamp((open - 0.5) * 2) }}>
        <AppTile name={app} size={20} />
        <span style={{ fontSize: 13.5, fontWeight: 600 }}>{app}</span>
        <div style={{ width: 1, height: 16, background: "rgba(255,255,255,0.18)" }} />
        {done ? (
          <span style={{ color: IRIS, fontWeight: 700, fontSize: 15 }}>✓</span>
        ) : (
          <div style={{ position: "relative", width: 9, height: 9 }}>
            <div style={{ position: "absolute", inset: 0, borderRadius: 5, background: IRIS }} />
            <div
              style={{
                position: "absolute",
                inset: -4 - ((f % 24) / 24) * 5,
                borderRadius: 10,
                border: `1.5px solid ${IRIS}`,
                opacity: 1 - (f % 24) / 24,
              }}
            />
          </div>
        )}
        <div style={{ flex: 1, minWidth: 0, fontSize: 13.5, whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" }}>{status}</div>
        <div style={{ display: "flex", gap: 2, alignItems: "center" }}>
          {Array.from({ length: 7 }, (_, i) => (
            <div
              key={i}
              style={{
                width: 2.5,
                borderRadius: 2,
                background: "rgba(255,255,255,0.85)",
                height: 3 + level * 12 * Math.abs(Math.sin(f * 0.45 + i * 1.3) * Math.cos(f * 0.13 + i)),
              }}
            />
          ))}
        </div>
      </div>
      <div style={{ position: "absolute", left: 30, right: 30, bottom: 0, height: 2, background: `linear-gradient(90deg, ${IRIS}00, ${IRIS}, ${IRIS}00)`, opacity: open * level }} />
    </div>
  );
};

/** A blinking text caret. */
export const Caret: React.FC<{ f: number; h?: number; color?: string }> = ({ f, h = 20, color = "#111" }) => (
  <span style={{ display: "inline-block", width: 2, height: h, marginLeft: 1, verticalAlign: "-0.18em", background: color, opacity: Math.floor(f / 8) % 2 ? 0 : 1 }} />
);

export const SLACK = { x: 496, y: 110, w: 520, h: 390 } as const;
/** The compose box inside the Slack window, in screen points. */
export const COMPOSE = { x: SLACK.x + 16, y: SLACK.y + SLACK.h - 96, w: SLACK.w - 32, h: 80 } as const;

/** A generic team chat window titled Slack, with a message box at the bottom. */
export const SlackCompose: React.FC<{ f: number; text: string; caret?: boolean }> = ({ f, text, caret = true }) => (
  <Window x={SLACK.x} y={SLACK.y} w={SLACK.w} h={SLACK.h} title="Slack">
    <div style={{ position: "absolute", inset: 0, color: "#111" }}>
      <div style={{ padding: "16px 20px", borderBottom: "1px solid rgba(0,0,0,0.07)", fontSize: 17, fontWeight: 700 }}>Sam Carter</div>
      <div style={{ padding: "18px 20px", display: "grid", gap: 18 }}>
        {[
          ["Sam Carter", "Did Corvane get back to us?"],
          ["Sam Carter", "No rush, just want to plan the week."],
        ].map(([w, t], i) => (
          <div key={i} style={{ display: "flex", gap: 12 }}>
            <div style={{ width: 36, height: 36, borderRadius: 9, background: palette.pink, flex: "none" }} />
            <div>
              <div style={{ fontSize: 15, fontWeight: 700 }}>
                {w} <span style={{ fontWeight: 400, color: "rgba(0,0,0,0.45)", fontSize: 13 }}>10:3{i + 6}</span>
              </div>
              <div style={{ fontSize: 16, lineHeight: 1.45, marginTop: 2 }}>{t}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
    <div
      style={{
        position: "absolute",
        left: 16,
        right: 16,
        bottom: 16,
        height: COMPOSE.h,
        borderRadius: 12,
        border: "1.5px solid rgba(0,0,0,0.22)",
        padding: "14px 16px",
        boxSizing: "border-box",
        fontSize: 19,
        color: text ? "#111" : "rgba(0,0,0,0.4)",
      }}
    >
      {text || (caret ? "" : "Message Sam Carter")}
      {caret ? <Caret f={f} h={22} /> : null}
      {!text && caret ? <span style={{ color: "rgba(0,0,0,0.4)", marginLeft: 2 }}>Message Sam Carter</span> : null}
    </div>
  </Window>
);

/** The quick-fire apps under the island: generic windows, each with the line at the cursor. */
export const QuickApp: React.FC<{ app: "Mail" | "Notion" | "Chrome"; f: number }> = ({ app, f }) => {
  const box = { x: 496, y: 150, w: 520, h: 420 };
  if (app === "Mail")
    return (
      <Window {...box} title="New Message">
        <div style={{ padding: "6px 22px", fontSize: 16, color: "#111" }}>
          {[
            ["To:", "Sam Carter"],
            ["Subject:", "Corvane"],
          ].map(([k, v]) => (
            <div key={k} style={{ display: "flex", gap: 10, padding: "12px 0", borderBottom: "1px solid rgba(0,0,0,0.07)" }}>
              <span style={{ color: "rgba(0,0,0,0.45)" }}>{k}</span>
              {v}
            </div>
          ))}
          <div style={{ paddingTop: 18, fontSize: 20 }}>
            Hey Sam, just wanted to check in on Corvane.
            <Caret f={f} />
          </div>
        </div>
      </Window>
    );
  if (app === "Notion")
    return (
      <Window {...box} title="Notion">
        <div style={{ padding: "28px 40px", color: "#111" }}>
          <div style={{ fontSize: 34, fontWeight: 700, letterSpacing: "-0.02em" }}>Pilot plan</div>
          <div style={{ fontSize: 20, lineHeight: 1.6, marginTop: 16, color: "rgba(0,0,0,0.8)" }}>
            Start with one team and check in after two weeks.
            <Caret f={f} />
          </div>
        </div>
      </Window>
    );
  return (
    <Window {...box} title="Chrome">
      <div style={{ padding: 28, color: "#111" }}>
        <div style={{ height: 52, borderRadius: 26, border: "1.5px solid rgba(0,0,0,0.18)", display: "flex", alignItems: "center", padding: "0 22px", fontSize: 20 }}>
          security overview template for a pilot
          <Caret f={f} />
        </div>
        <div style={{ display: "grid", gap: 14, marginTop: 28 }}>
          {[0.9, 0.7, 0.8].map((w, i) => (
            <div key={i} style={{ height: 14, width: `${w * 100}%`, borderRadius: 7, background: "rgba(0,0,0,0.07)" }} />
          ))}
        </div>
      </div>
    </Window>
  );
};
