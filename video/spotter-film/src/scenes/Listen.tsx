import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { clamp, expoInOut, expoOut, per, tween, useFmt, type Fmt } from "../lib";
import { World, boost, camSpeed, track, type CamKey } from "../fx/Camera";
import { Flash, TitleSlam, Trail } from "../fx/fx";
import { Bezel, Desktop } from "../mac/Desktop";
import { CallWindow } from "../mac/Call";
import { Keycap } from "../mac/Keycap";
import { ListenBar } from "../mac/SpotterMore";
import { Remi } from "../remi/Remi";
import { listen, look, remiAt, squish, type FlightPlan, type RemiState } from "../remi/flight";

/**
 * Listen, 14 to 18 s. Spotter hears nothing until you press Listen. The
 * keycap slams, the red dot lights, and the two sides come up one at a time:
 * Me is your microphone, Them is this Mac's sound.
 */

const cams = (fmt: Fmt): CamKey[] => [
  { f: T.listenKey, cam: { x: 766, y: 0, z: per(fmt, 0.76, 0.82) } },
  { f: T.meFrom, cam: { x: 766, y: 0, z: per(fmt, 0.83, 0.88) }, ease: expoOut },
  { f: SCENES.open.from, cam: { x: 766, y: 0, z: per(fmt, 0.9, 0.95) }, ease: expoInOut },
];

export const Listen: React.FC = () => {
  const fmt = useFmt();
  const f = useCurrentFrame() + SCENES.listen.from;
  const keys = boost(cams(fmt), per(fmt, 1, 1.12));
  const camOf = track(fmt, keys);
  const cam = camOf(f);
  // Only sideways motion blurs: the vertical clamp drifts as the zoom changes,
  // and a pure push-in must stay sharp.
  const sp = { dx: camSpeed(fmt, keys, f).dx, dy: 0 };

  const dot = tween(f, T.dot, T.dot + 5);
  // Each side swells on its own beat, then both stay alive.
  const me = tween(f, T.meFrom, T.meFrom + 8) * (0.55 + 0.45 * Math.abs(Math.cos((f - T.meFrom) / 11)));
  const them = tween(f, T.themFrom, T.themFrom + 8) * (0.5 + 0.5 * Math.abs(Math.cos((f - T.themFrom) / 9)));

  const plan: FlightPlan = {
    path: [
      { f: T.listenKey - 8, x: fmt.W * 0.28, y: fmt.H * per(fmt, 0.33, 0.29) },
      { f: T.dot + 6, x: fmt.W * 0.24, y: fmt.H * per(fmt, 0.4, 0.37), arc: 30, ease: expoOut },
      { f: T.meFrom, x: fmt.W * 0.2, y: fmt.H * per(fmt, 0.48, 0.45) },
      { f: T.themFrom, x: fmt.W * 0.8, y: fmt.H * per(fmt, 0.48, 0.45), arc: -60, ease: expoInOut },
      { f: SCENES.open.from, x: fmt.W * 0.78, y: fmt.H * per(fmt, 0.47, 0.44) },
    ],
    faces: [
      [T.listenKey - 8, "curious"],
      [T.dot, "wow"],
      [T.meFrom, "listening"],
      [T.themFrom, "listening"],
      [T.titleHears + 6, "happy"],
    ],
    stunts: [
      squish(T.listenKey, 0.2),
      listen(T.meFrom, SCENES.open.from),
      look(T.meFrom, -0.6, 0, T.themFrom),
      look(T.themFrom + 6, 0.6, 0, SCENES.open.from),
    ],
  };
  const remiOf = (g: number): RemiState => remiAt(plan, g);
  const remi = remiOf(f);
  const keyS = per(fmt, 250, 200);

  return (
    <AbsoluteFill>
      <World cam={cam} blur={sp} id="listen">
        <Bezel />
        <Desktop app="Zoom" radius={14}>
          <CallWindow speaking={clamp(them) > 0.3 ? 0 : -1} />
          <ListenBar f={f} dot={dot} me={clamp(me)} them={clamp(them)} />
        </Desktop>
      </World>
      <Keycap f={f} at={T.listenKey} x={fmt.W / 2} y={per(fmt, 1000, 680)} size={keyS * 1.1} label="⌘⇧\" sub="listen" out={T.meFrom - 8} tilt={-6} />
      <Trail f={f} pos={remiOf} len={10} width={per(fmt, 18, 14)} from={T.listenKey} opacity={0.8} />
      <Remi s={remi} size={fmt.remi * 0.85} id="remi-listen" />
      <Flash f={f} at={T.listenKey} peak={0.2} dur={7} />
      <TitleSlam f={f} out={T.titleHears - 5} words={[{ text: "Press", at: T.titleListen }, { text: "Listen.", at: T.titleListen + 5, accent: true }]} />
      <TitleSlam
        f={f}
        out={SCENES.open.from - 5}
        words={[
          { text: "Hears", at: T.titleHears },
          { text: "both", at: T.titleHears + 5 },
          { text: "sides.", at: T.titleHears + 10, accent: true },
        ]}
      />
    </AbsoluteFill>
  );
};
