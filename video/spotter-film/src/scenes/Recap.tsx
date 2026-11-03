import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { ANSWER, SCENES, T } from "../timing";
import { INTER, SCREEN, clamp, expoOut, palette, per, springAt, tween, useFmt } from "../lib";
import { Flash } from "../fx/fx";
import { SPOT, SpotterPanel } from "../mac/Spotter";
import { ListenBar } from "../mac/SpotterMore";

/**
 * The recap, 26 to 28 s, on the music's drop: Reads. Hears. Answers. One word
 * per beat, stacking, each with the bar in that state flashing big behind it.
 * Clears on the last beat for the end card.
 */

/** Shows a box of the Mac screen (in points) centred at (cx, cy), `scale` px per point. */
const Showcase: React.FC<{ box: { x: number; y: number; w: number; h: number }; cx: number; cy: number; scale: number; children: React.ReactNode; style?: React.CSSProperties }> = ({
  box,
  cx,
  cy,
  scale,
  children,
  style,
}) => (
  <div
    style={{
      position: "absolute",
      left: cx - (box.w * scale) / 2,
      top: cy - (box.h * scale) / 2,
      width: box.w,
      height: box.h,
      transformOrigin: "0 0",
      transform: `scale(${scale})`,
      ...style,
    }}
  >
    <div style={{ position: "absolute", left: -box.x, top: -box.y, width: SCREEN.w, height: SCREEN.h }}>{children}</div>
  </div>
);

const WORDS = ["Reads.", "Hears.", "Answers."];

export const Recap: React.FC = () => {
  const fmt = useFmt();
  const f = useCurrentFrame() + SCENES.recap.from;
  const clear = tween(f, T.clear, T.clear + 6, 0, 1, expoOut);
  const active = T.recap.reduce((a, at, i) => (f >= at ? i : a), 0);
  const size = per(fmt, 150, 118);
  const lineH = size * 1.08;
  const midY = per(fmt, 1010, 690);
  const uiY = per(fmt, 480, 270);
  const box = { x: SPOT.x - 10, y: SPOT.y - 10, w: SPOT.w + 20, h: 215 };

  const flashUI = (i: number) => {
    const at = T.recap[i];
    if (f < at || (i < 2 && f >= T.recap[i + 1] + 3)) return null;
    const k = tween(f, at, at + 10, 0, 1, expoOut);
    const out = i < 2 ? tween(f, T.recap[i + 1], T.recap[i + 1] + 3) : clear;
    const style: React.CSSProperties = { opacity: (0.4 + 0.6 * (1 - k * 0.3)) * (1 - out), filter: `blur(${(1 - k) * 10}px)` };
    const sc = per(fmt, 1.75, 1.6) * (1.2 - 0.2 * k);
    return (
      <Showcase key={i} box={box} cx={fmt.W / 2} cy={uiY} scale={sc} style={style}>
        {i === 0 ? (
          <SpotterPanel f={f} working={1} answer="" />
        ) : i === 1 ? (
          <ListenBar f={f} dot={1} me={0.9} them={0.6} />
        ) : (
          <SpotterPanel f={f} working={0} answer={ANSWER} />
        )}
      </Showcase>
    );
  };

  return (
    <AbsoluteFill style={{ opacity: 1 - clear, transform: `scale(${1 + clear * 0.15})` }}>
      <AbsoluteFill style={{ background: "radial-gradient(60% 45% at 50% 40%, rgba(112,99,190,0.35), rgba(10,9,14,0.96) 70%)" }} />
      {[0, 1, 2].map(flashUI)}
      <div style={{ position: "absolute", left: 0, right: 0, top: midY - lineH * 1.5 }}>
        {WORDS.map((w, i) => {
          const at = T.recap[i];
          if (f < at) return <div key={w} style={{ height: lineH }} />;
          const k = springAt(f, at, { stiffness: 420, damping: 20, mass: 0.7 });
          return (
            <div
              key={w}
              style={{
                height: lineH,
                textAlign: "center",
                fontFamily: INTER,
                fontWeight: 700,
                fontSize: size,
                lineHeight: `${lineH}px`,
                letterSpacing: "-0.05em",
                color: i === active ? palette.white : "rgba(255,255,255,0.4)",
                transform: `scale(${1 + (1 - k) * 0.7})`,
                opacity: clamp((f - at + 1) / 2),
                textShadow: "0 10px 40px rgba(0,0,0,0.5)",
              }}
            >
              {w}
            </div>
          );
        })}
      </div>
      {T.recap.map((at) => (
        <Flash key={at} f={f} at={at} peak={at === T.drop ? 0.5 : 0.22} dur={7} color={at === T.drop ? "#fff" : "#beb4fb"} />
      ))}
    </AbsoluteFill>
  );
};
