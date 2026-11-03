import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { clamp, per, tween, useFmt } from "../lib";
import { TitleSlam, Trail } from "../fx/fx";
import { DeckLight, Keyboard, Rush, liftOut } from "../mac/Keyboard";
import { Keycap } from "../mac/Keycap";
import { Remi } from "../remi/Remi";
import { hop, look, remiAt, squish, type FlightPlan } from "../remi/flight";

/**
 * The hook, 0 to 4 s. Black, then the Mac keyboard close up, lit only by the
 * screen above it. Remi is asleep over the keys and wakes. On 2.0 s Command
 * goes down, then Return: the shortcut that asks Spotter. The keyboard drops
 * away and the camera lifts to the screen, which the next scene brings in.
 */

export const Hook: React.FC = () => {
  const fmt = useFmt();
  const f = useCurrentFrame() + SCENES.hook.from;
  const kbW = per(fmt, 1010, 1040);
  const kbX = fmt.W / 2 - per(fmt, 10, 6);
  const kbY = per(fmt, 1010, 690);
  const glow = tween(f, T.glowOn, T.glowOn + 20);
  const out = liftOut(f, T.lift, 22);

  const over = { x: kbX - kbW * 0.36, y: kbY - per(fmt, 330, 250) };
  const plan: FlightPlan = {
    noBlink: true,
    path: [
      { f: 0, x: over.x, y: over.y + 10 },
      { f: T.cmdDown, x: over.x, y: over.y },
      { f: T.retDown, x: over.x - per(fmt, 70, 60), y: over.y - 24 },
      { f: T.lift, x: over.x - per(fmt, 70, 60), y: over.y - 34 },
      { f: T.lift + 16, x: fmt.W / 2, y: -per(fmt, 400, 340) },
    ],
    faces: [
      [0, "sleepy"],
      [T.eyesOpen + 4, "curious"],
      [T.cmdDown, "happy"],
      [T.lift, "wow"],
    ],
    stunts: [
      (g) => ({ blink: g < T.eyesOpen ? 0.05 : g < T.eyesOpen + 5 ? (g - T.eyesOpen) / 5 : 1 }),
      (g) => ({ dark: 1 - tween(g, T.glowOn, T.eyesOpen + 10) * 0.85 }),
      (g) => ({
        thrust: g < T.flameOn ? 0 : g < T.flameOn + 8 ? [0.45, 0.1, 0.55, 0.15, 0.5, 0.25, 0.45, 0.35][g - T.flameOn] : g < T.lift ? 0.4 : 1,
      }),
      look(T.eyesOpen + 6, -0.2, 0.75, T.cmdDown),
      squish(T.cmdDown, 0.18),
      hop(T.retDown, per(fmt, 40, 34), 12),
      (g) => ({ scale: 1 + 0.14 * tween(g, T.lift - 4, T.lift) }),
    ],
  };
  const remi = remiAt(plan, f);
  const keyS = per(fmt, 300, 240);
  const keyY = per(fmt, 640, 430);

  return (
    <AbsoluteFill>
      <AbsoluteFill style={{ background: "#07070a" }} />
      <AbsoluteFill style={{ transform: `translateY(${out.dy}px) scale(${out.scale})`, opacity: out.opacity, filter: out.dy > 8 ? `blur(${Math.min(14, out.dy / 40)}px)` : undefined }}>
        <DeckLight k={glow} cx={kbX} cy={kbY} w={kbW} />
        <Keyboard f={f} w={kbW} cx={kbX} cy={kbY} glow={glow} presses={{ cmd: T.cmdDown, ret: T.retDown }} />
      </AbsoluteFill>
      <Rush f={f} at={T.lift} until={SCENES.hook.from + SCENES.hook.dur} W={fmt.W} H={fmt.H} />
      <Trail f={f} from={T.lift} pos={(g) => remiAt(plan, g)} len={10} width={per(fmt, 24, 18)} opacity={clamp(tween(f, T.lift, T.lift + 4))} />
      <Remi s={remi} size={fmt.remi * per(fmt, 0.95, 0.9)} id="remi-hook" glow={0.3 + 0.35 * glow} />
      <Keycap f={f} at={T.cmdDown} x={fmt.W / 2 - keyS * 0.6} y={keyY} size={keyS} label="⌘" sub="command" out={T.lift + 2} tilt={-10} />
      <Keycap f={f} at={T.retDown} x={fmt.W / 2 + keyS * 0.6} y={keyY} size={keyS} label="↩" sub="return" out={T.lift + 2} tilt={8} />
      <TitleSlam
        f={f}
        out={T.cmdDown - 4}
        words={[
          { text: "Stuck", at: T.titleStuck[0] },
          { text: "on", at: T.titleStuck[1] },
          { text: "a", at: T.titleStuck[2] },
          { text: "call?", at: T.titleStuck[3], accent: true },
        ]}
      />
      <TitleSlam f={f} out={T.lift + 4} words={[{ text: "Press", at: T.titleKeys }, { text: "⌘↩.", at: T.retDown, accent: true }]} />
    </AbsoluteFill>
  );
};
