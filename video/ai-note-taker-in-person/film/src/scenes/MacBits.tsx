import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { INTER, IRIS, SCREEN, clamp, expoOut, palette, springAt, tween } from "../lib";
import { Sphere } from "../mac/Desktop";
import { COLUMN, RecordColumn } from "../mac/Call";
import { Remi } from "../remi/Remi";
import { point, remiAt, squish, type FlightPlan } from "../remi/flight";
import { Plate, W, ink } from "../ui/parts";
import { TitleSlam, Trail } from "../fx/fx";
import { Cam, breathe, type Move } from "../ui/motion";

/**
 * The three Mac moments. The camera is pushing in through all of them, and
 * Remi does the work on screen: it bonks Record now, flies the column, and
 * lands on the action item.
 */

export const RecordNow: React.FC = () => {
  const f = useCurrentFrame() + SCENES.record.from;
  const S = SCENES.record.from;
  const open = springAt(f, T.menuOpen, { stiffness: 300, damping: 20 });
  const press = f >= T.click ? Math.exp(-(f - T.click) / 5) : 0;
  const rec = tween(f, T.recOn, T.recOn + 8);
  const bar = 76;
  const panelX = 700;
  const hotY = 150 + bar + 14 + 16 + 34; // middle of the Record now row

  const keys: Move[] = [
    { f: S, x: 1300, y: 300, z: 0.86 },
    { f: T.menuOpen, x: 1050, y: 360, z: 1.04, ease: expoOut },
    { f: T.click, x: panelX + 230, y: hotY + 20, z: 1.34 },
    { f: S + SCENES.record.dur, x: panelX + 250, y: hotY + 70, z: 1.26, ease: (t) => t },
  ];
  const plan: FlightPlan = {
    path: [
      { f: S - 6, x: 1850, y: 120 },
      { f: T.menuOpen, x: 1330, y: 210, ease: expoOut },
      { f: T.click - 7, x: panelX + 430, y: hotY - 96, arc: 60 },
      { f: T.click, x: panelX + 430, y: hotY - 46, ease: (t) => t * t },
      { f: T.recOn + 6, x: panelX + 560, y: hotY - 120, arc: 70, ease: expoOut },
      { f: S + SCENES.record.dur, x: panelX + 620, y: hotY - 60 },
    ],
    faces: [
      [S - 6, "curious"],
      [T.click, "happy"],
    ],
    stunts: [squish(T.click, 0.34), point(T.menuOpen, T.click - 8, 200)],
  };
  const remi = remiAt(plan, f);

  return (
    <AbsoluteFill>
      <Plate />
      <Cam f={f} keys={keys} id="rec">
        <div
          style={{
            position: "absolute",
            left: 0,
            top: 150,
            width: W,
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
            <div style={{ position: "absolute", inset: -16, borderRadius: "50%", background: `radial-gradient(closest-side, ${IRIS}bb, ${IRIS}00)`, opacity: 0.4 + 0.6 * clamp(open) }} />
            <Sphere size={34} color={rec > 0.5 ? palette.live : palette.white} />
          </div>
        </div>

        <div
          style={{
            position: "absolute",
            left: panelX,
            top: 150 + bar + 14,
            width: 560,
            borderRadius: 20,
            background: "rgba(22,22,26,0.94)",
            boxShadow: "0 40px 90px rgba(0,0,0,0.55), inset 0 0 0 1px rgba(255,255,255,0.12)",
            padding: "16px 0",
            transformOrigin: "80% 0%",
            transform: `scale(${0.82 + 0.18 * open}) rotate(${(1 - open) * -2}deg)`,
            opacity: clamp(open * 1.6),
            fontFamily: INTER,
          }}
        >
          {[{ label: "Record now", hot: true }, { label: "Open Lynkk" }, { label: "Dictation" }, { label: "Settings" }].map((r) => (
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
                background: r.hot ? `rgba(110,107,240,${0.5 + press * 0.5})` : "transparent",
                transform: r.hot ? `scale(${1 - press * 0.03})` : undefined,
              }}
            >
              {r.hot ? <span style={{ width: 14, height: 14, borderRadius: 8, background: rec > 0.5 ? palette.live : "#fff" }} /> : <span style={{ width: 14 }} />}
              {r.label}
            </div>
          ))}
        </div>

        <Trail f={f} pos={(g) => remiAt(plan, g)} from={S - 6} len={9} width={12} opacity={0.8} />
        <Remi s={remi} size={110} id="remi-rec" glow={0.45} />
      </Cam>

      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 980,
          textAlign: "center",
          fontFamily: INTER,
          fontSize: 30,
          color: ink.lo,
          opacity: tween(f, T.recOn, T.recOn + 10),
        }}
      >
        No invite. No link. Nothing joins.
      </div>
      <TitleSlam f={f} words={[{ text: "Record", at: T.click }, { text: "now.", at: T.click + 4, accent: true }]} y={830} />
    </AbsoluteFill>
  );
};

/** The recording column on the right edge, the app's own strings. */
export const Column: React.FC = () => {
  const f = useCurrentFrame() + SCENES.column.from;
  const S = SCENES.column.from;
  const k = springAt(f, T.columnIn, { stiffness: 230, damping: 23 });
  const turns = [
    { who: "You", you: true, text: "So the pilot starts with one team.", at: T.liveWords[0] },
    { who: "Speaker A", text: "And IT reviews it before we widen it.", at: T.liveWords[1] },
    { who: "Speaker B", text: "We can get the security overview to you.", at: T.liveWords[2] },
  ];
  const keys: Move[] = [
    { f: S, x: 820, y: 560, z: 0.92 },
    { f: T.liveWords[0], x: 1080, y: 500, z: 1.02, ease: expoOut },
    { f: T.liveWords[2], x: 1330, y: 400, z: 1.14 },
    { f: S + SCENES.column.dur, x: 1360, y: 430, z: 1.2, ease: (t) => t },
  ];
  const plan: FlightPlan = {
    path: [
      { f: S - 6, x: 320, y: 820 },
      { f: T.liveWords[0], x: 1120, y: 620, ease: expoOut },
      { f: T.liveWords[1], x: 1200, y: 420, arc: 60 },
      { f: T.liveWords[2], x: 1240, y: 330, arc: 40 },
      { f: S + SCENES.column.dur, x: 1180, y: 520, arc: 80 },
    ],
    faces: [
      [S - 6, "curious"],
      [T.liveWords[1], "listening"],
    ],
    stunts: [point(T.liveWords[0], S + SCENES.column.dur, 10)],
  };
  const remi = remiAt(plan, f);
  return (
    <AbsoluteFill>
      <Plate />
      <Cam f={f} keys={keys} id="col">
        <div
          style={{
            position: "absolute",
            left: 1230,
            top: 70 + breathe(f, 3, 120),
            width: COLUMN.w * 1.6,
            height: 980,
            overflow: "hidden",
            borderRadius: 29,
            transform: `translateX(${(1 - clamp(k)) * 560}px)`,
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
          <div
            style={{
              fontSize: 64,
              fontWeight: 700,
              letterSpacing: "-0.04em",
              color: ink.hi,
              opacity: tween(f, T.columnIn + 4, T.columnIn + 16),
              transform: `translateX(${(1 - tween(f, T.columnIn + 4, T.columnIn + 20, 0, 1, expoOut)) * -60}px)`,
            }}
          >
            You can see it hearing <span style={{ color: palette.lavender }}>the far end.</span>
          </div>
          <div style={{ marginTop: 28, fontSize: 30, lineHeight: 1.45, color: ink.mid, opacity: tween(f, T.columnIn + 14, T.columnIn + 28) }}>
            The clock, a pause and a stop, and the words as they come in.
          </div>
        </div>
        <Trail f={f} pos={(g) => remiAt(plan, g)} from={S - 6} len={10} width={12} opacity={0.75} />
        <Remi s={remi} size={110} id="remi-col" glow={0.45} />
      </Cam>
    </AbsoluteFill>
  );
};

// ------------------------------------------------------------------ the note

const Label: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div style={{ fontSize: 19, fontWeight: 600, color: "rgba(17,17,17,0.45)", marginBottom: 10 }}>{children}</div>
);

const stampStyle = (f: number, at: number) => ({
  opacity: clamp((f - at + 1) / 2),
  transform: `scale(${1.4 - 0.4 * tween(f, at, at + 7, 0, 1, expoOut)}) rotate(${(1 - tween(f, at, at + 8, 0, 1, expoOut)) * -3}deg)`,
  transformOrigin: "0 50%",
});

/**
 * The note Lynkk writes from the recording. Same shape as the Mac teaser's
 * note, but this one was made in a room, so it says so. The people and the
 * action item are the site's own worked example.
 */
export const NoteIn: React.FC = () => {
  const f = useCurrentFrame() + SCENES.note.from;
  const S = SCENES.note.from;
  const k = springAt(f, T.noteIn, { stiffness: 230, damping: 24 });
  const cardX = 300;
  const cardY = 160;
  const cardW = 1080;
  const keys: Move[] = [
    { f: S, x: 840, y: 240, z: 1.12 },
    { f: T.stamps[0], x: 840, y: 360, z: 1.04, ease: expoOut },
    { f: T.stamps[2], x: 880, y: 620, z: 1.14 },
    { f: T.land + 16, x: 900, y: 690, z: 1.24 },
    { f: S + SCENES.note.dur, x: 880, y: 600, z: 1.06, ease: (t) => t },
  ];
  const plan: FlightPlan = {
    path: [
      { f: S - 8, x: 2000, y: 300 },
      { f: T.stamps[0], x: cardX + cardW + 60, y: 330, ease: expoOut },
      { f: T.stamps[2], x: cardX + cardW - 60, y: 560, arc: 70 },
      { f: T.land, x: cardX + cardW - 150, y: 742, ease: (t) => t * t },
      { f: S + SCENES.note.dur, x: cardX + cardW - 150, y: 742 },
    ],
    faces: [
      [S - 8, "curious"],
      [T.stamps[1], "wow"],
      [T.land, "happy"],
    ],
    stunts: [squish(T.land, 0.3), point(T.stamps[0], T.stamps[2], 170)],
  };
  const remi = remiAt(plan, f);
  return (
    <AbsoluteFill>
      <Plate />
      <Cam f={f} keys={keys} id="note">
        <div
          style={{
            position: "absolute",
            left: cardX,
            top: cardY + breathe(f, 4, 150),
            width: cardW,
            borderRadius: 26,
            background: "#fff",
            boxShadow: "0 50px 110px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(0,0,0,0.06)",
            fontFamily: INTER,
            color: "#111",
            padding: "36px 44px 44px",
            boxSizing: "border-box",
            opacity: clamp(k * 1.6),
            transform: `translateY(${(1 - k) * 70}px) rotate(${(1 - k) * 1.4}deg)`,
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
        <Trail f={f} pos={(g) => remiAt(plan, g)} from={S - 8} len={10} width={12} opacity={0.7} />
        <Remi s={remi} size={110} id="remi-note" glow={0.4} />
      </Cam>
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 980,
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
