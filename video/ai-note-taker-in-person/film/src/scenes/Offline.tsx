import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { INTER, clamp, expoOut, palette, springAt, tween } from "../lib";
import { Trail } from "../fx/fx";
import { Remi } from "../remi/Remi";
import { hop, point, remiAt, squish, type FlightPlan } from "../remi/flight";
import { Plate, W, ink } from "../ui/parts";
import { Cam, breathe, type Move } from "../ui/motion";

/**
 * 88 to 100 s. Wi-Fi off mid-recording: the clock keeps running and the audio
 * goes to disk from the first second. Then it comes back and the upload
 * resumes. The camera rides from the dead Wi-Fi down to the disk filling, and
 * Remi reacts: worried at the cut, pleased when it keeps going.
 */

const WifiGlyph: React.FC<{ off: number; size?: number; f: number }> = ({ off, size = 150, f }) => {
  const jitter = off > 0 && off < 1 ? Math.sin(f * 2.3) * 3 * (1 - off) : 0;
  return (
    <svg width={size} height={size} viewBox="0 0 48 48" style={{ transform: `translateX(${jitter}px)` }}>
      {[1, 2, 3].map((i) => (
        <path
          key={i}
          d={`M ${24 - i * 7.5} ${30 - i * 4.4} A ${i * 10} ${i * 10} 0 0 1 ${24 + i * 7.5} ${30 - i * 4.4}`}
          fill="none"
          stroke={off > 0.5 ? "rgba(255,255,255,0.22)" : palette.lavender}
          strokeWidth={4}
          strokeLinecap="round"
          opacity={off > 0.5 ? 1 : 0.55 + 0.45 * Math.sin((f - i * 6) / 7)}
        />
      ))}
      <circle cx={24} cy={34} r={3.6} fill={off > 0.5 ? "rgba(255,255,255,0.22)" : palette.lavender} />
      {off > 0 ? <path d="M9 9 L39 39" stroke={palette.live} strokeWidth={4} strokeLinecap="round" strokeDasharray={42} strokeDashoffset={42 * (1 - off)} /> : null}
    </svg>
  );
};

const Chip: React.FC<{ k: number; dot: string; text: string; top: number; f: number }> = ({ k, dot, text, top, f }) => (
  <div
    style={{
      position: "absolute",
      left: W / 2 - 250,
      top: top + breathe(f, 3, 110),
      width: 500,
      height: 86,
      borderRadius: 43,
      background: "rgba(22,22,26,0.92)",
      boxShadow: "inset 0 0 0 1px rgba(255,255,255,0.14), 0 24px 60px rgba(0,0,0,0.5)",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      gap: 16,
      fontFamily: INTER,
      fontSize: 34,
      fontWeight: 600,
      color: "#fff",
      opacity: clamp(k * 1.5),
      transform: `translateY(${(1 - clamp(k)) * 30}px) scale(${0.92 + 0.08 * clamp(k)})`,
    }}
  >
    <span style={{ width: 16, height: 16, borderRadius: 9, background: dot, opacity: 0.55 + 0.45 * Math.sin(f / 6) }} />
    {text}
  </div>
);

export const Offline: React.FC = () => {
  const f = useCurrentFrame() + SCENES.offline.from;
  const S = SCENES.offline.from;
  const off = tween(f, T.wifiOff, T.wifiOff + 10, 0, 1, expoOut);
  const disk = tween(f, T.diskFrom, T.diskTo);
  const secs = 38 + Math.floor((f - S) / 30);
  const keys: Move[] = [
    { f: S, x: W / 2, y: 300, z: 1.26 },
    { f: T.wifiOff + 10, x: W / 2, y: 340, z: 1.12, ease: expoOut },
    { f: T.diskFrom + 20, x: W / 2, y: 520, z: 1.02 },
    { f: T.diskTo, x: W / 2 + 20, y: 600, z: 1.06 },
    { f: S + SCENES.offline.dur, x: W / 2, y: 580, z: 1.12, ease: (t) => t },
  ];
  const plan: FlightPlan = {
    path: [
      { f: S - 6, x: W / 2 + 420, y: 170 },
      { f: T.wifiOff, x: W / 2 + 190, y: 250, ease: expoOut },
      { f: T.wifiOff + 16, x: W / 2 + 250, y: 400, arc: 50 },
      { f: T.diskFrom + 24, x: W / 2 + 380, y: 560, arc: 70 },
      { f: T.diskTo, x: W / 2 + 390, y: 600 },
      { f: S + SCENES.offline.dur, x: W / 2 + 330, y: 640, arc: 40 },
    ],
    faces: [
      [S - 6, "curious"],
      [T.wifiOff, "worried"],
      [T.diskFrom + 20, "happy"],
    ],
    stunts: [squish(T.wifiOff, 0.26), point(T.diskFrom, T.diskTo, 185), hop(T.diskTo - 20, 28, 12)],
  };
  const remi = remiAt(plan, f);
  return (
    <AbsoluteFill>
      <Plate />
      <Cam f={f} keys={keys} id="offline">
        <div style={{ position: "absolute", left: 0, top: 180, width: W, display: "flex", justifyContent: "center" }}>
          <WifiGlyph off={off} f={f} />
        </div>
        <Chip f={f} k={springAt(f, T.wifiOff + 6, { stiffness: 300, damping: 20 })} dot={palette.live} text={`Still recording · ${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, "0")}`} top={380} />

        <div style={{ position: "absolute", left: W / 2 - 320, top: 540, width: 640, fontFamily: INTER, opacity: tween(f, T.diskFrom - 6, T.diskFrom + 6) }}>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: 24, color: ink.lo, marginBottom: 14 }}>
            <span>WRITTEN TO THIS MAC</span>
            <span>{Math.round(disk * 100)}%</span>
          </div>
          <div style={{ height: 18, borderRadius: 9, background: "rgba(255,255,255,0.08)", overflow: "hidden" }}>
            <div style={{ width: `${disk * 100}%`, height: "100%", borderRadius: 9, background: `linear-gradient(90deg, ${palette.violet}, ${palette.lavender})` }} />
          </div>
        </div>
        <Trail f={f} pos={(g) => remiAt(plan, g)} from={S - 6} len={10} width={12} opacity={0.75} />
        <Remi s={remi} size={108} id="remi-off" glow={0.45} />
      </Cam>

      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 760,
          textAlign: "center",
          fontFamily: INTER,
          fontWeight: 700,
          fontSize: 64,
          letterSpacing: "-0.04em",
          color: ink.hi,
          opacity: tween(f, T.wifiOff + 14, T.wifiOff + 26),
          transform: `translateY(${(1 - tween(f, T.wifiOff + 14, T.wifiOff + 30, 0, 1, expoOut)) * 30}px)`,
        }}
      >
        Nothing waits on the <span style={{ color: palette.lavender }}>network.</span>
      </div>
      <div style={{ position: "absolute", left: 0, right: 0, top: 866, textAlign: "center", fontFamily: INTER, fontSize: 30, color: ink.mid, opacity: tween(f, T.diskTo - 20, T.diskTo - 8) }}>
        Lynkk is offline-first. So is Plaud.
      </div>
    </AbsoluteFill>
  );
};

/** 96 to 100 s: back online, the upload picks up where it stopped. */
export const Online: React.FC = () => {
  const f = useCurrentFrame() + SCENES.online.from;
  const S = SCENES.online.from;
  const on = tween(f, T.wifiOn, T.wifiOn + 10, 0, 1, expoOut);
  const up = tween(f, T.wifiOn + 4, T.uploaded);
  const done = springAt(f, T.uploaded, { stiffness: 300, damping: 18 });
  const keys: Move[] = [
    { f: S, x: W / 2, y: 360, z: 1.2 },
    { f: T.wifiOn + 10, x: W / 2, y: 430, z: 1.06, ease: expoOut },
    { f: S + SCENES.online.dur, x: W / 2, y: 500, z: 1.14, ease: (t) => t },
  ];
  const plan: FlightPlan = {
    path: [
      { f: S - 6, x: W / 2 - 520, y: 600 },
      { f: T.wifiOn, x: W / 2 - 230, y: 300, ease: expoOut, arc: 70 },
      { f: T.uploaded, x: W / 2 + 300, y: 440, arc: 120 },
      { f: S + SCENES.online.dur, x: W / 2 + 360, y: 520, arc: 50 },
    ],
    faces: [
      [S - 6, "curious"],
      [T.uploaded, "happy"],
    ],
    stunts: [hop(T.uploaded, 34, 12)],
  };
  const remi = remiAt(plan, f);
  return (
    <AbsoluteFill>
      <Plate />
      <Cam f={f} keys={keys} id="online">
        <div style={{ position: "absolute", left: 0, top: 200, width: W, display: "flex", justifyContent: "center" }}>
          <WifiGlyph off={1 - on} f={f} />
        </div>
        <div style={{ position: "absolute", left: W / 2 - 320, top: 440, width: 640, fontFamily: INTER }}>
          <div style={{ display: "flex", justifyContent: "space-between", fontSize: 24, color: ink.lo, marginBottom: 14 }}>
            <span>UPLOADING</span>
            <span>{Math.round(up * 100)}%</span>
          </div>
          <div style={{ height: 18, borderRadius: 9, background: "rgba(255,255,255,0.08)", overflow: "hidden" }}>
            <div style={{ width: `${up * 100}%`, height: "100%", borderRadius: 9, background: `linear-gradient(90deg, ${palette.violet}, ${palette.lavender})` }} />
          </div>
        </div>
        <Trail f={f} pos={(g) => remiAt(plan, g)} from={S - 6} len={10} width={12} opacity={0.75} />
        <Remi s={remi} size={108} id="remi-on" glow={0.45} />
      </Cam>
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 640,
          textAlign: "center",
          fontFamily: INTER,
          fontWeight: 700,
          fontSize: 60,
          letterSpacing: "-0.04em",
          color: ink.hi,
          opacity: clamp(done * 1.5),
          transform: `scale(${0.92 + 0.08 * clamp(done)})`,
        }}
      >
        It picks up where it <span style={{ color: palette.lavender }}>stopped.</span>
      </div>
      <div style={{ position: "absolute", left: 0, right: 0, top: 752, textAlign: "center", fontFamily: INTER, fontSize: 30, color: ink.mid, opacity: clamp(done) }}>
        One recording runs up to two hours.
      </div>
    </AbsoluteFill>
  );
};
