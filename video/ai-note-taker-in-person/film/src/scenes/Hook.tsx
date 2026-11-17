import React from "react";
import { AbsoluteFill, Img, staticFile, useCurrentFrame } from "remotion";
import { T } from "../timing";
import { INTER, clamp, expoOut, palette, springAt, tween } from "../lib";
import { Flash, Shatter, SpeedLines, TitleSlam, Trail } from "../fx/fx";
import { Remi } from "../remi/Remi";
import { remiAt, roll360, squish, type FlightPlan } from "../remi/flight";
import { H, W, ink } from "../ui/parts";
import { Cam, type Move } from "../ui/motion";

/**
 * 0 to 4 s. Black. Remi wakes. A generic video-call window drops in, the
 * camera pushes at it as Remi charges, and on bar 1 it shatters: behind it is
 * the room, which has no link to join. "No link? No problem."
 */

const CallBox: React.FC<{ k: number; f: number }> = ({ k, f }) => (
  <div
    style={{
      position: "absolute",
      left: W / 2 - 430,
      top: H / 2 - 290 - (1 - k) * 260,
      width: 860,
      height: 540,
      borderRadius: 22,
      background: "linear-gradient(180deg, #23232b, #15151b)",
      boxShadow: "0 50px 120px rgba(0,0,0,0.6), inset 0 0 0 1px rgba(255,255,255,0.08)",
      opacity: k,
      transform: `rotate(${(1 - k) * -3}deg) scale(${0.9 + 0.1 * k})`,
      fontFamily: INTER,
      overflow: "hidden",
    }}
  >
    <div style={{ height: 52, background: "rgba(255,255,255,0.05)", display: "flex", alignItems: "center", paddingLeft: 20, gap: 9 }}>
      {["#ff5f57", "#febc2e", "#28c840"].map((c) => (
        <span key={c} style={{ width: 13, height: 13, borderRadius: 7, background: c, opacity: 0.85 }} />
      ))}
      <span style={{ marginLeft: 18, fontSize: 19, fontWeight: 500, color: "rgba(255,255,255,0.72)" }}>Zoom Meeting</span>
    </div>
    <div style={{ position: "absolute", left: 0, right: 0, top: 52, bottom: 0, display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14, padding: 22 }}>
      {[0, 1, 2, 3].map((i) => (
        <div key={i} style={{ borderRadius: 14, background: "rgba(255,255,255,0.07)", display: "flex", alignItems: "center", justifyContent: "center" }}>
          <div style={{ width: 74, height: 74, borderRadius: "50%", background: `rgba(255,255,255,${0.12 + 0.05 * Math.sin((f + i * 20) / 11)})` }} />
        </div>
      ))}
    </div>
  </div>
);

export const Hook: React.FC = () => {
  const f = useCurrentFrame();
  const plan: FlightPlan = {
    path: [
      { f: 0, x: W / 2, y: H / 2 + 40 },
      { f: T.windowIn, x: W / 2 - 360, y: H / 2 + 120, ease: expoOut },
      { f: T.charge, x: W / 2 - 300, y: H / 2 + 40 },
      { f: T.shatter, x: W / 2 + 320, y: H / 2 - 30, ease: (t) => t * t * t },
      { f: T.shatter + 14, x: W / 2 + 820, y: H / 2 - 190 },
      { f: T.shatter + 44, x: W - 360, y: H / 2 + 60, arc: 120, ease: expoOut },
    ],
    faces: [
      [0, "sleepy"],
      [T.eyesOpen, "curious"],
      [T.charge, "wow"],
      [T.shatter + 16, "happy"],
    ],
    stunts: [squish(T.shatter, 0.34), roll360(T.shatter + 4, 16)],
  };
  const remi = remiAt(plan, f);
  const wake = tween(f, T.eyesOpen - 6, T.eyesOpen + 6);
  const boxK = tween(f, T.windowIn, T.windowIn + 16, 0, 1, expoOut);
  const charge = tween(f, T.charge, T.shatter) * (1 - tween(f, T.shatter, T.shatter + 10));
  const roomK = tween(f, T.shatter, T.shatter + 10);
  const lock = springAt(f, T.shatter, { stiffness: 300, damping: 18 });

  // The camera leans at the window, punches back on the break, then pushes in.
  const keys: Move[] = [
    { f: 0, x: W / 2, y: H / 2, z: 1.08 },
    { f: T.charge, x: W / 2 - 40, y: H / 2 + 10, z: 1.14 },
    { f: T.shatter - 1, x: W / 2 + 30, y: H / 2, z: 1.46, ease: (t) => t * t },
    { f: T.shatter + 8, x: W / 2, y: H / 2, z: 0.94, ease: expoOut },
    { f: T.shatter + 60, x: W / 2 + 40, y: H / 2 - 16, z: 1.04, ease: (t) => t },
  ];

  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Cam f={f} keys={keys} id="hook">
        {f >= T.shatter - 2 ? (
          <AbsoluteFill style={{ opacity: roomK }}>
            <Img
              src={staticFile("plate-dusk.jpg")}
              style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", opacity: 0.5, filter: "saturate(0.7) brightness(0.52)" }}
            />
            <AbsoluteFill style={{ background: "linear-gradient(180deg, rgba(10,10,14,0.35), rgba(10,10,14,0.85))" }} />
            <div style={{ position: "absolute", left: 120, top: 140, fontFamily: INTER, fontWeight: 600, fontSize: 22, letterSpacing: "0.2em", color: ink.accent, opacity: 0.85 * clamp(lock) }}>
              B-ROLL: THE ROOM, LOCKED WIDE
            </div>
          </AbsoluteFill>
        ) : null}

        <Shatter f={f} at={T.shatter} cols={7} rows={5} dur={16}>
          <AbsoluteFill>
            <AbsoluteFill style={{ background: "#000", opacity: 1 - roomK * 0.9 }} />
            <CallBox k={boxK} f={f} />
          </AbsoluteFill>
        </Shatter>

        <SpeedLines k={charge * 0.8} cx={W / 2} cy={H / 2} seed="hook" />
        <Trail f={f} pos={(g) => remiAt(plan, g)} from={T.charge} len={12} width={16} opacity={clamp(charge + roomK)} />
        <Remi s={{ ...remi, opacity: remi.opacity * clamp(wake + 0.12) }} size={180} id="remi-hook" glow={0.55 * clamp(wake)} />
      </Cam>
      <Flash f={f} at={T.shatter} peak={0.5} dur={9} color={palette.violetTint} />
      <TitleSlam
        f={f}
        words={[
          { text: "No", at: T.title1[0] },
          { text: "link?", at: T.title1[0] + 3, accent: true },
          { text: "No", at: T.title1[1], br: true },
          { text: "problem.", at: T.title1[1] + 3 },
        ]}
        y={H / 2 + 100}
        scale={1.5}
      />
    </AbsoluteFill>
  );
};
