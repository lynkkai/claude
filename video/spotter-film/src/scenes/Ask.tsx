import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { ANSWER, SCENES, T, answerChars } from "../timing";
import { INTER, clamp, expoInOut, expoOut, palette, per, pulse, springAt, tween, useFmt, type Fmt } from "../lib";
import { World, boost, camSpeed, track, type CamKey } from "../fx/Camera";
import { Flash, TitleSlam, Trail } from "../fx/fx";
import { Bezel, Desktop } from "../mac/Desktop";
import { CallWindow } from "../mac/Call";
import { PilotDoc, SPOT, SpotterPanel } from "../mac/Spotter";
import { Remi } from "../remi/Remi";
import { hop, look, remiAt, type FlightPlan, type RemiState } from "../remi/flight";

/**
 * Ask, 4 to 10 s. The Mac screen crashes into frame: a call, Priya mid
 * question, and the pilot plan open beside it. Spotter's bar drops from the
 * top, reads the screen and answers from what is on it. Early access.
 * The question and the answer are the site's own example.
 */

/** The scene starts before its bar so the screen can fall into the hit. */
export const ASK_FROM = T.lift;

const cams = (fmt: Fmt): CamKey[] => [
  { f: T.deskHit, cam: { x: 756, y: 0, z: per(fmt, 0.42, 0.56) } },
  { f: T.panel + 10, cam: { x: 766, y: 0, z: per(fmt, 0.66, 0.74) }, ease: expoOut },
  { f: T.answerHit, cam: { x: 766, y: 0, z: per(fmt, 0.8, 0.86) }, ease: expoInOut },
  { f: SCENES.ask.from + SCENES.ask.dur, cam: { x: 766, y: 0, z: per(fmt, 0.88, 0.94) } },
];

export const Ask: React.FC = () => {
  const fmt = useFmt();
  const f = useCurrentFrame() + ASK_FROM;
  const keys = boost(cams(fmt), per(fmt, 1, 1.22));
  const camOf = track(fmt, keys);
  const cam = camOf(f);
  // Only sideways motion blurs: the vertical clamp drifts as the zoom changes,
  // and a pure push-in must stay sharp.
  const sp = { dx: camSpeed(fmt, keys, f).dx, dy: 0 };

  // The screen falls from above and lands on the hit. It has to be in frame
  // from about f 100, or the lift leaves a hole with nothing in it.
  const fall = tween(f, T.lift + 2, T.deskHit, 0, 1, (t) => t * t);
  const deskY = (1 - fall) * -fmt.H * 1.15;
  const deskRot = (1 - fall) * -6;

  const working = f < T.panel + 4 ? 0 : 1 - tween(f, T.answerFrom - 3, T.answerFrom);
  const reading = tween(f, T.readGlow, T.readGlow + 8) * (1 - tween(f, T.answerHit, T.answerHit + 12));
  const caption = {
    who: "Priya Shah",
    text: "How would the pilot work?",
    o: tween(f, T.question, T.question + 6, 0, 1, expoOut) * (1 - tween(f, T.panel + 6, T.panel + 14)),
  };
  const drop = springAt(f, T.panel, { stiffness: 250, damping: 20 });
  const pill = springAt(f, T.pill, { stiffness: 300, damping: 18 });

  const plan: FlightPlan = {
    path: [
      { f: T.deskHit - 10, x: fmt.W / 2, y: -per(fmt, 400, 340) },
      { f: T.deskHit + 10, x: fmt.W * 0.3, y: fmt.H * per(fmt, 0.52, 0.56), arc: -70, ease: expoOut },
      { f: T.panel, x: fmt.W * 0.3, y: fmt.H * per(fmt, 0.5, 0.54) },
      { f: T.panel + 16, x: fmt.W * 0.15, y: fmt.H * per(fmt, 0.44, 0.42), arc: 40, ease: expoOut },
      { f: T.answerHit, x: fmt.W * 0.14, y: fmt.H * per(fmt, 0.43, 0.41) },
      { f: T.hops[0], x: fmt.W * 0.14, y: fmt.H * per(fmt, 0.43, 0.41) },
    ],
    faces: [
      [T.deskHit - 10, "wow"],
      [T.question + 6, "worried"],
      [T.panel + 4, "curious"],
      [T.answerFrom, "thinking"],
      [T.answerHit - 1, "happy"],
    ],
    stunts: [
      look(T.question + 4, -0.5, 0.3, T.panel),
      look(T.panel + 16, 0.6, -0.5, T.answerHit + 20),
      ...T.hops.map((at) => hop(at, per(fmt, 44, 36), 13)),
    ],
  };
  const remiOf = (g: number): RemiState => {
    const s = remiAt(plan, g);
    const t = tween(g, T.joy, T.joy + 22, 0, 1, expoInOut);
    const th = t * Math.PI * 2;
    const r = per(fmt, 140, 115);
    return { ...s, x: s.x + r * Math.sin(th), y: s.y - r * (1 - Math.cos(th)), rot: s.rot + (th * 180) / Math.PI };
  };
  const remi = remiOf(f);

  // The frame around the answer, flashing once as it lands.
  const ring = pulse(f, T.answerHit, 2, 16);

  return (
    <AbsoluteFill>
      <AbsoluteFill style={{ transform: `translateY(${deskY}px) rotate(${deskRot}deg)`, transformOrigin: "50% 0%" }}>
        <World cam={cam} blur={sp} id="ask">
          <Bezel />
          <Desktop app="Zoom" radius={14}>
            <CallWindow speaking={f < T.panel ? 0 : -1} caption={caption} />
            <PilotDoc glow={reading} />
            {f >= T.panel ? (
              <div style={{ position: "absolute", inset: 0, transform: `translateY(${(1 - drop) * -300}px)`, opacity: clamp(drop * 2.5) }}>
                <SpotterPanel f={f} working={working} answer={ANSWER.slice(0, answerChars(f))} />
                {ring > 0.01 ? (
                  <div
                    style={{
                      position: "absolute",
                      left: SPOT.x - 4,
                      top: SPOT.y + 56,
                      width: SPOT.w + 8,
                      height: 128,
                      borderRadius: 22,
                      boxShadow: `0 0 0 3px ${palette.violet}, 0 0 44px ${palette.violet}`,
                      opacity: ring,
                    }}
                  />
                ) : null}
              </div>
            ) : null}
          </Desktop>
        </World>
      </AbsoluteFill>
      <Trail f={f} pos={remiOf} len={10} width={per(fmt, 18, 14)} from={T.deskHit - 10} opacity={0.85} />
      <Remi s={remi} size={fmt.remi * 0.85} id="remi-ask" />
      <Flash f={f} at={T.deskHit} peak={0.42} dur={9} />
      <Flash f={f} at={T.answerHit} peak={0.2} dur={9} color="#beb4fb" />
      <TitleSlam
        f={f}
        out={SCENES.screen.from - 5}
        words={[
          { text: "Spotter", at: T.titleLive, accent: true },
          { text: "answers.", at: T.titleLive + 5 },
          { text: "Live.", at: T.titleLive + 14, br: true },
        ]}
      />
      {f >= T.pill ? (
        <div
          style={{
            position: "absolute",
            left: "50%",
            top: fmt.title.y - fmt.title.size * per(fmt, 1.42, 1.4),
            transform: `translate(-50%, -50%) scale(${0.7 + 0.3 * pill})`,
            opacity: clamp(pill * 2) * (1 - tween(f, SCENES.screen.from - 6, SCENES.screen.from - 2)),
            padding: "10px 24px",
            borderRadius: 999,
            background: palette.violet,
            color: "white",
            fontFamily: INTER,
            fontWeight: 600,
            fontSize: per(fmt, 34, 28),
            letterSpacing: "-0.01em",
            boxShadow: "0 10px 30px rgba(112,99,190,0.5)",
          }}
        >
          Early access
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
