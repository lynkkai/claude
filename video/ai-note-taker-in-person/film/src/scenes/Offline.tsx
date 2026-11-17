import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { INTER, clamp, expoOut, palette, springAt, tween } from "../lib";
import { Plate, W, ink } from "../ui/parts";

/**
 * 88 to 100 s. Wi-Fi off mid-recording: the clock keeps running and the audio
 * goes to disk from the first second. Then it comes back and the upload
 * resumes. Both claims are the Mac app's own behaviour.
 */

const WifiGlyph: React.FC<{ off: number; size?: number }> = ({ off, size = 120 }) => (
  <svg width={size} height={size} viewBox="0 0 48 48">
    {[1, 2, 3].map((i) => (
      <path
        key={i}
        d={`M ${24 - i * 7.5} ${30 - i * 4.4} A ${i * 10} ${i * 10} 0 0 1 ${24 + i * 7.5} ${30 - i * 4.4}`}
        fill="none"
        stroke={off > 0.5 ? "rgba(255,255,255,0.22)" : palette.lavender}
        strokeWidth={4}
        strokeLinecap="round"
      />
    ))}
    <circle cx={24} cy={34} r={3.6} fill={off > 0.5 ? "rgba(255,255,255,0.22)" : palette.lavender} />
    {off > 0 ? <path d="M9 9 L39 39" stroke={palette.live} strokeWidth={4} strokeLinecap="round" strokeDasharray={42} strokeDashoffset={42 * (1 - off)} /> : null}
  </svg>
);

const Chip: React.FC<{ k: number; dot: string; text: string; top: number }> = ({ k, dot, text, top }) => (
  <div
    style={{
      position: "absolute",
      left: W / 2 - 250,
      top,
      width: 500,
      height: 86,
      borderRadius: 43,
      background: "rgba(22,22,26,0.92)",
      boxShadow: `inset 0 0 0 1px rgba(255,255,255,0.14), 0 24px 60px rgba(0,0,0,0.5)`,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      gap: 16,
      fontFamily: INTER,
      fontSize: 34,
      fontWeight: 600,
      color: "#fff",
      opacity: clamp(k * 1.5),
      transform: `translateY(${(1 - k) * 26}px) scale(${0.94 + 0.06 * clamp(k)})`,
    }}
  >
    <span style={{ width: 16, height: 16, borderRadius: 9, background: dot }} />
    {text}
  </div>
);

export const Offline: React.FC = () => {
  const f = useCurrentFrame() + SCENES.offline.from;
  const off = tween(f, T.wifiOff, T.wifiOff + 10, 0, 1, expoOut);
  const disk = tween(f, T.diskFrom, T.diskTo);
  const secs = 38 + Math.floor((f - SCENES.offline.from) / 30);
  return (
    <AbsoluteFill>
      <Plate />
      <div style={{ position: "absolute", left: 0, right: 0, top: 180, display: "flex", justifyContent: "center" }}>
        <WifiGlyph off={off} size={150} />
      </div>
      <Chip k={springAt(f, T.wifiOff + 6, { stiffness: 300, damping: 20 })} dot={palette.live} text={`Still recording · ${Math.floor(secs / 60)}:${String(secs % 60).padStart(2, "0")}`} top={380} />

      {/* the disk filling, because the audio is written from the first second */}
      <div style={{ position: "absolute", left: W / 2 - 320, top: 540, width: 640, fontFamily: INTER, opacity: tween(f, T.diskFrom - 6, T.diskFrom + 6) }}>
        <div style={{ display: "flex", justifyContent: "space-between", fontSize: 24, color: ink.lo, marginBottom: 14 }}>
          <span>WRITTEN TO THIS MAC</span>
          <span>{Math.round(disk * 100)}%</span>
        </div>
        <div style={{ height: 18, borderRadius: 9, background: "rgba(255,255,255,0.08)", overflow: "hidden" }}>
          <div style={{ width: `${disk * 100}%`, height: "100%", borderRadius: 9, background: `linear-gradient(90deg, ${palette.violet}, ${palette.lavender})` }} />
        </div>
      </div>

      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 700,
          textAlign: "center",
          fontFamily: INTER,
          fontWeight: 700,
          fontSize: 64,
          letterSpacing: "-0.04em",
          color: ink.hi,
          opacity: tween(f, T.wifiOff + 14, T.wifiOff + 26),
        }}
      >
        Nothing waits on the <span style={{ color: palette.lavender }}>network.</span>
      </div>
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 800,
          textAlign: "center",
          fontFamily: INTER,
          fontSize: 30,
          color: ink.mid,
          opacity: tween(f, T.diskTo - 20, T.diskTo - 8),
        }}
      >
        Lynkk is offline-first. So is Plaud.
      </div>
    </AbsoluteFill>
  );
};

/** 96 to 100 s: back online, the upload picks up where it stopped. */
export const Online: React.FC = () => {
  const f = useCurrentFrame() + SCENES.online.from;
  const on = tween(f, T.wifiOn, T.wifiOn + 10, 0, 1, expoOut);
  const up = tween(f, T.wifiOn + 4, T.uploaded);
  const done = springAt(f, T.uploaded, { stiffness: 300, damping: 18 });
  return (
    <AbsoluteFill>
      <Plate />
      <div style={{ position: "absolute", left: 0, right: 0, top: 200, display: "flex", justifyContent: "center" }}>
        <WifiGlyph off={1 - on} size={150} />
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
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 600,
          textAlign: "center",
          fontFamily: INTER,
          fontWeight: 700,
          fontSize: 60,
          letterSpacing: "-0.04em",
          color: ink.hi,
          opacity: clamp(done * 1.5),
          transform: `scale(${0.94 + 0.06 * clamp(done)})`,
        }}
      >
        It picks up where it <span style={{ color: palette.lavender }}>stopped.</span>
      </div>
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: 720,
          textAlign: "center",
          fontFamily: INTER,
          fontSize: 30,
          color: ink.mid,
          opacity: clamp(done),
        }}
      >
        One recording runs up to two hours.
      </div>
    </AbsoluteFill>
  );
};
