import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { ANSWER, SCENES, T } from "../timing";
import { INTER, IRIS, clamp, expoInOut, expoOut, palette, per, tween, useFmt, type Fmt } from "../lib";
import { World, boost, camSpeed, track, type CamKey } from "../fx/Camera";
import { Flash, TitleSlam, Trail, Whip } from "../fx/fx";
import { Bezel, Desktop } from "../mac/Desktop";
import { CallWindow } from "../mac/Call";
import { DOC, PilotDoc, SPOT, SpotterPanel } from "../mac/Spotter";
import { Remi } from "../remi/Remi";
import { look, remiAt, type FlightPlan, type RemiState } from "../remi/flight";

/**
 * Screen, 10 to 14 s. What "reads your screen" means: a band of light runs
 * down the pilot plan, the lines it crosses turn into plain words, the words
 * fly up into the bar, and the picture of the window is dropped. Only the
 * words go, with your question.
 */

const LINES = ["One team", "Up to 20 seats", "30 days", "Security review first"] as const;

const cams = (fmt: Fmt): CamKey[] => [
  { f: T.whip, cam: { x: 840, y: 0, z: per(fmt, 0.86, 0.92) } },
  { f: T.lift1, cam: { x: 810, y: 0, z: per(fmt, 0.82, 0.88) }, ease: expoInOut },
  { f: SCENES.listen.from, cam: { x: 790, y: 0, z: per(fmt, 0.78, 0.84) }, ease: expoInOut },
];

export const Screen: React.FC = () => {
  const fmt = useFmt();
  const f = useCurrentFrame() + SCENES.screen.from;
  const keys = boost(cams(fmt), per(fmt, 1, 1.18));
  const camOf = track(fmt, keys);
  const cam = camOf(f);
  // Only sideways motion blurs: the vertical clamp drifts as the zoom changes,
  // and a pure push-in must stay sharp.
  const sp = { dx: camSpeed(fmt, keys, f).dx, dy: 0 };

  // The band: from the top of the doc to the bottom, over the second bar.
  const sweep = tween(f, T.sweepFrom, T.sweepTo, 0, 1, (t) => t);
  const bandY = DOC.y + sweep * DOC.h;
  // Each line turns to words as the band passes it.
  const lineY = (i: number) => DOC.y + 96 + i * 42;
  const words = LINES.map((t, i) => {
    const read = clamp((bandY - lineY(i)) / 18);
    const flight = tween(f, T.lift1 + i * 4, T.lift1 + 22 + i * 4, 0, 1, expoOut);
    return { t, read, flight, y: lineY(i) };
  });
  const picture = 1 - tween(f, T.picDrop, T.picDrop + 12, 0, 1, expoOut);

  const plan: FlightPlan = {
    path: [
      { f: T.whip, x: fmt.W + 220, y: fmt.H * 0.44 },
      { f: T.whip + 14, x: fmt.W * 0.24, y: fmt.H * per(fmt, 0.62, 0.66), arc: -50, ease: expoOut },
      { f: T.lift1, x: fmt.W * 0.22, y: fmt.H * per(fmt, 0.6, 0.64) },
      { f: T.lift1 + 20, x: fmt.W * 0.17, y: fmt.H * per(fmt, 0.4, 0.37), arc: 60, ease: expoOut },
      { f: SCENES.listen.from, x: fmt.W * 0.16, y: fmt.H * per(fmt, 0.39, 0.36) },
    ],
    faces: [
      [T.whip, "curious"],
      [T.sweepFrom, "thinking"],
      [T.lift1, "wow"],
      [T.picDrop, "happy"],
    ],
    stunts: [look(T.sweepFrom, 0.8, 0.4, T.lift1), look(T.lift1 + 10, 0.5, -0.4, SCENES.listen.from)],
  };
  const remiOf = (g: number): RemiState => remiAt(plan, g);
  const remi = remiOf(f);

  return (
    <AbsoluteFill>
      <Whip f={f} into={[T.whip, T.whip + 10]} id="screen">
        <World cam={cam} blur={sp} id="screen">
          <Bezel />
          <Desktop app="Zoom" radius={14}>
            <CallWindow speaking={-1} />
            <div style={{ opacity: picture, transform: `scale(${0.96 + 0.04 * picture})`, transformOrigin: `${DOC.x + DOC.w / 2}px ${DOC.y + DOC.h / 2}px`, filter: `grayscale(${(1 - picture) * 0.9})` }}>
              <PilotDoc glow={clamp(sweep * 2) * picture} />
            </div>
            {/* the band of light */}
            {sweep > 0 && sweep < 1 ? (
              <div
                style={{
                  position: "absolute",
                  left: DOC.x - 6,
                  top: bandY - 26,
                  width: DOC.w + 12,
                  height: 64,
                  background: `linear-gradient(rgba(190,180,251,0), #ffffff 45%, ${IRIS} 55%, rgba(190,180,251,0))`,
                  opacity: 0.95,
                  filter: "blur(1.5px)",
                  boxShadow: `0 0 40px 10px rgba(110,107,240,0.55)`,
                }}
              />
            ) : null}
            {/* the words, lifting off the doc and into the bar */}
            {words.map((w, i) =>
              w.read > 0.01 ? (
                <div
                  key={w.t}
                  style={{
                    position: "absolute",
                    left: DOC.x + 22 + (SPOT.x + 60 - (DOC.x + 22)) * w.flight,
                    top: w.y - (w.y - (SPOT.y + 104)) * w.flight,
                    fontFamily: INTER,
                    fontSize: 17 + 5 * w.flight,
                    fontWeight: 500,
                    color: palette.white,
                    opacity: w.read * (1 - tween(f, T.picDrop + 4 + i * 2, T.picDrop + 14 + i * 2)),
                    textShadow: "0 2px 18px rgba(112,99,190,0.9)",
                    whiteSpace: "nowrap",
                  }}
                >
                  {w.t}
                </div>
              ) : null,
            )}
            <SpotterPanel f={f} working={1 - clamp(tween(f, T.lift1 + 18, T.picDrop))} answer={f > T.lift1 + 18 ? ANSWER : ""} />
          </Desktop>
        </World>
      </Whip>
      <Trail f={f} pos={remiOf} len={10} width={per(fmt, 18, 14)} from={T.whip} opacity={0.8} />
      <Remi s={remi} size={fmt.remi * 0.85} id="remi-screen" />
      <Flash f={f} at={T.picDrop} peak={0.14} dur={8} color="#beb4fb" />
      <TitleSlam
        f={f}
        out={T.titleWords - 5}
        words={[
          { text: "Your", at: T.titleText },
          { text: "screen,", at: T.titleText + 4 },
          { text: "as", at: T.titleText + 10 },
          { text: "text.", at: T.titleText + 14, accent: true },
        ]}
      />
      <TitleSlam
        f={f}
        out={SCENES.listen.from - 5}
        words={[
          { text: "Only", at: T.titleWords },
          { text: "the", at: T.titleWords + 4 },
          { text: "words", at: T.titleWords + 8, accent: true },
          { text: "go.", at: T.titleWords + 13 },
        ]}
      />
    </AbsoluteFill>
  );
};
