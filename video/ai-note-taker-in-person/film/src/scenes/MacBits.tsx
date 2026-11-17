import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { INTER, IRIS, clamp, expoOut, palette, springAt, tween } from "../lib";
import { Sphere } from "../mac/Desktop";
import { COLUMN, RecordColumn } from "../mac/Call";
import { SCREEN } from "../lib";
import { Remi } from "../remi/Remi";
import { remiAt, squish, type FlightPlan } from "../remi/flight";
import { H, Plate, W, ink } from "../ui/parts";
import { TitleSlam } from "../fx/fx";

/** A close-up of the menu bar: the Lynkk sphere, open, with Record now. */
export const RecordNow: React.FC = () => {
  const f = useCurrentFrame() + SCENES.record.from;
  const open = springAt(f, T.menuOpen, { stiffness: 300, damping: 20 });
  const press = f >= T.click ? Math.exp(-(f - T.click) / 5) : 0;
  const rec = tween(f, T.recOn, T.recOn + 8);
  const cursor = tween(f, SCENES.record.from + 6, T.click, 0, 1, expoOut);
  const bar = 76;
  const panelX = W / 2 - 230;
  return (
    <AbsoluteFill>
      <Plate />
      {/* the menu bar, blown up so it reads on a phone */}
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 150,
          height: bar,
          background: "rgba(16,16,22,0.72)",
          boxShadow: `inset 0 -1px 0 ${ink.line}`,
          display: "flex",
          alignItems: "center",
          justifyContent: "flex-end",
          paddingRight: 150,
          gap: 46,
          fontFamily: INTER,
          fontSize: 26,
          color: "rgba(255,255,255,0.75)",
        }}
      >
        <span>100%</span>
        <span>Wed 10:04</span>
        <div style={{ position: "relative", width: 40, height: 40, display: "grid", placeItems: "center" }}>
          <div style={{ position: "absolute", inset: -16, borderRadius: "50%", background: `radial-gradient(closest-side, ${IRIS}bb, ${IRIS}00)`, opacity: 0.5 + 0.5 * clamp(open) }} />
          <Sphere size={34} color={rec > 0.5 ? palette.live : palette.white} />
        </div>
      </div>

      {/* the menu that drops out of it */}
      <div
        style={{
          position: "absolute",
          left: panelX,
          top: 150 + bar + 14,
          width: 560,
          borderRadius: 20,
          background: "rgba(22,22,26,0.94)",
          boxShadow: `0 40px 90px rgba(0,0,0,0.55), inset 0 0 0 1px rgba(255,255,255,0.12)`,
          padding: "16px 0",
          transformOrigin: "80% 0%",
          transform: `scale(${0.86 + 0.14 * open})`,
          opacity: clamp(open * 1.6),
          fontFamily: INTER,
        }}
      >
        {[
          { label: "Record now", hot: true },
          { label: "Open Lynkk" },
          { label: "Dictation" },
          { label: "Settings" },
        ].map((r) => (
          <div
            key={r.label}
            style={{
              display: "flex",
              alignItems: "center",
              gap: 18,
              padding: "18px 28px",
              margin: "0 10px",
              borderRadius: 12,
              fontSize: 34,
              fontWeight: r.hot ? 600 : 500,
              color: r.hot ? "#fff" : "rgba(255,255,255,0.62)",
              background: r.hot ? `rgba(110,107,240,${0.55 + press * 0.45})` : "transparent",
            }}
          >
            {r.hot ? <span style={{ width: 14, height: 14, borderRadius: 8, background: rec > 0.5 ? palette.live : "#fff" }} /> : <span style={{ width: 14 }} />}
            {r.label}
          </div>
        ))}
      </div>

      {/* the pointer */}
      <svg
        style={{
          position: "absolute",
          left: panelX + 150 + (1 - cursor) * 240,
          top: 150 + bar + 60 + (1 - cursor) * 170,
          width: 44,
          height: 44,
          transform: `scale(${1 - press * 0.12})`,
        }}
        viewBox="0 0 24 24"
      >
        <path d="M5 2 L5 20 L10 15.5 L13 22 L16 20.5 L13 14.5 L19 14 Z" fill="#fff" stroke="#111" strokeWidth={1.2} strokeLinejoin="round" />
      </svg>

      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 470,
          textAlign: "center",
          fontFamily: INTER,
          fontSize: 30,
          color: ink.lo,
          opacity: tween(f, T.recOn, T.recOn + 10),
        }}
      >
        No invite. No link. Nothing joins.
      </div>
      <TitleSlam f={f} words={[{ text: "Record", at: SCENES.record.from + 8 }, { text: "now.", at: SCENES.record.from + 14, accent: true }]} y={760} />
    </AbsoluteFill>
  );
};

/** The recording column on the right edge, the app's own strings. */
export const Column: React.FC = () => {
  const f = useCurrentFrame() + SCENES.column.from;
  const k = springAt(f, T.columnIn, { stiffness: 240, damping: 24 });
  const turns = [
    { who: "You", you: true, text: "So the pilot starts with one team.", at: T.liveWords[0] },
    { who: "Speaker A", text: "And IT reviews it before we widen it.", at: T.liveWords[1] },
    { who: "Speaker B", text: "We can get the security overview to you.", at: T.liveWords[2] },
  ];
  return (
    <AbsoluteFill>
      <Plate />
      <div
        style={{
          position: "absolute",
          left: 1230,
          top: 70,
          width: COLUMN.w * 1.6,
          height: 980,
          overflow: "hidden",
          borderRadius: 29,
          transform: `translateX(${(1 - clamp(k)) * 520}px)`,
          opacity: clamp(k * 1.4),
        }}
      >
        <div style={{ position: "absolute", left: 0, top: 0, transformOrigin: "0 0", transform: "scale(1.6)" }}>
          <div style={{ position: "absolute", left: -COLUMN.x, top: -COLUMN.y, width: SCREEN.w, height: SCREEN.h }}>
            <RecordColumn f={f} seconds={Math.max(0, Math.floor((f - T.columnIn) / 30) + 38)} turns={turns} />
          </div>
        </div>
      </div>
      <div style={{ position: "absolute", left: 140, top: 330, width: 1000, fontFamily: INTER }}>
        <div style={{ fontSize: 64, fontWeight: 700, letterSpacing: "-0.04em", color: ink.hi, opacity: tween(f, T.columnIn + 4, T.columnIn + 16) }}>
          You can see it hearing <span style={{ color: palette.lavender }}>the far end.</span>
        </div>
        <div style={{ marginTop: 28, fontSize: 30, lineHeight: 1.45, color: ink.mid, opacity: tween(f, T.columnIn + 12, T.columnIn + 26) }}>
          The clock, a pause and a stop, and the words as they come in.
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------------ the note

const Label: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div style={{ fontSize: 19, fontWeight: 600, color: "rgba(17,17,17,0.45)", marginBottom: 10 }}>{children}</div>
);

const stampStyle = (f: number, at: number) => ({
  opacity: clamp((f - at + 1) / 2),
  transform: `scale(${1.35 - 0.35 * tween(f, at, at + 7, 0, 1, expoOut)})`,
  transformOrigin: "0 50%",
});

/**
 * The note Lynkk writes from the recording. Same shape as the Mac teaser's
 * note (summary, decision, action item with owner and due), but this one was
 * made in a room, so it says so. The people and the action item are the
 * site's own worked example.
 */
export const NoteIn: React.FC = () => {
  const f = useCurrentFrame() + SCENES.note.from;
  const k = springAt(f, T.noteIn, { stiffness: 230, damping: 24 });
  const cardX = 300;
  const cardY = 160;
  const cardW = 1080;
  const plan: FlightPlan = {
    path: [
      { f: SCENES.note.from, x: W + 180, y: 420 },
      { f: T.land - 10, x: cardX + cardW - 120, y: 300, ease: expoOut },
      { f: T.land, x: cardX + cardW - 150, y: 724, ease: (t) => t * t },
      { f: SCENES.note.from + SCENES.note.dur, x: cardX + cardW - 150, y: 724 },
    ],
    faces: [
      [SCENES.note.from, "curious"],
      [T.land, "happy"],
    ],
    stunts: [squish(T.land, 0.26)],
  };
  const remi = remiAt(plan, f);
  return (
    <AbsoluteFill>
      <Plate />
      <div
        style={{
          position: "absolute",
          left: cardX,
          top: cardY,
          width: cardW,
          borderRadius: 26,
          background: "#fff",
          boxShadow: "0 50px 110px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(0,0,0,0.06)",
          fontFamily: INTER,
          color: "#111",
          padding: "36px 44px 44px",
          boxSizing: "border-box",
          opacity: clamp(k * 1.6),
          transform: `translateY(${(1 - k) * 50}px)`,
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: 12, fontSize: 20, color: "rgba(17,17,17,0.5)" }}>
          <span style={{ width: 10, height: 10, borderRadius: 6, background: IRIS }} />
          In person · 38 min · Today
        </div>
        <div style={{ fontSize: 50, fontWeight: 600, letterSpacing: "-0.03em", margin: "12px 0 30px", lineHeight: 1.1 }}>Corvane pilot, on site</div>

        <div style={{ ...stampStyle(f, T.stamps[0]), marginBottom: 28 }}>
          <Label>Summary</Label>
          <div style={{ fontSize: 28, lineHeight: 1.4, color: "rgba(17,17,17,0.82)" }}>Corvane wants to try Lynkk with one team before the IT review.</div>
        </div>

        <div style={{ ...stampStyle(f, T.stamps[1]), marginBottom: 28 }}>
          <Label>Key decision</Label>
          <div style={{ display: "inline-flex", alignItems: "center", gap: 12, fontSize: 28, padding: "12px 20px", borderRadius: 14, background: "#f1f0fb" }}>
            <span style={{ fontWeight: 600, color: IRIS }}>✓</span> Start with a 30-day pilot
          </div>
        </div>

        <div style={stampStyle(f, T.stamps[2])}>
          <Label>Action items</Label>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              gap: 16,
              padding: "18px 22px",
              borderRadius: 16,
              background: "#f6f6f8",
              boxShadow: `inset 0 0 0 ${1 + tween(f, T.land, T.land + 6) * 2}px ${f >= T.land ? IRIS : "rgba(0,0,0,0.06)"}`,
            }}
          >
            <div style={{ width: 28, height: 28, borderRadius: 8, border: "2px solid rgba(17,17,17,0.3)", flex: "none" }} />
            <div style={{ flex: 1, fontSize: 29, fontWeight: 500 }}>Send the security overview by Friday</div>
          </div>
          <div style={{ display: "flex", gap: 12, marginTop: 12, paddingLeft: 66, fontSize: 20, color: "rgba(17,17,17,0.5)" }}>
            <span>Priya Shah</span>·<span>Due Fri</span>·<span>High</span>
          </div>
        </div>
      </div>
      <Remi s={remi} size={120} id="remi-note" glow={0.4} />
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 960,
          textAlign: "center",
          fontFamily: INTER,
          fontWeight: 600,
          fontSize: 38,
          letterSpacing: "-0.03em",
          color: ink.hi,
          opacity: tween(f, T.stamps[2] + 6, T.stamps[2] + 18),
        }}
      >
        The same note you get from a <span style={{ color: palette.lavender }}>Zoom call.</span>
      </div>
    </AbsoluteFill>
  );
};
