import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { ANSWER, SCENES, T } from "../timing";
import { INTER, SCREEN, clamp, expoInOut, expoOut, palette, per, springAt, tween, useFmt, type Fmt } from "../lib";
import { World, boost, camSpeed, track, type CamKey } from "../fx/Camera";
import { Flash, TitleSlam, Trail } from "../fx/fx";
import { Bezel, Desktop } from "../mac/Desktop";
import { CallWindow } from "../mac/Call";
import { SPOT, SpotterPanel } from "../mac/Spotter";
import { ASKS, KeepSwitch, ShareTile } from "../mac/SpotterMore";
import { Remi } from "../remi/Remi";
import { look, remiAt, type FlightPlan, type RemiState } from "../remi/flight";

/**
 * Open, 18 to 26 s. Two things that are true at once: Spotter is in every
 * screen share, on purpose, and it keeps nothing. The screen multiplies into
 * four attendee views with the bar plainly in each, then comes back to one,
 * where the session's asks blow away and the only switch that would keep
 * them is off.
 */

/** The part of the shared screen an attendee tile shows: the bar, and the call under it. */
const CROP = { x: 376, y: 0, w: 760, h: 428 } as const;

/** The shared screen, as the other people on the call see it. */
const MiniScreen: React.FC<{ f: number; w: number }> = ({ f, w }) => {
  const s = w / CROP.w;
  return (
    <div style={{ position: "absolute", left: 0, top: 0, width: CROP.w, height: CROP.h, overflow: "hidden" }}>
      <div style={{ position: "absolute", left: -CROP.x * s, top: -CROP.y * s, width: SCREEN.w * s, height: SCREEN.h * s }}>
        <div style={{ position: "absolute", left: 0, top: 0, width: SCREEN.w, height: SCREEN.h, transformOrigin: "0 0", transform: `scale(${s})` }}>
          <Desktop app="Zoom">
            <CallWindow speaking={-1} />
            <SpotterPanel f={f} working={0} answer={ANSWER} />
          </Desktop>
        </div>
      </div>
    </div>
  );
};

const cams = (fmt: Fmt): CamKey[] => [
  { f: T.smash, cam: { x: 756, y: 0, z: per(fmt, 1.06, 1.1) } },
  { f: T.keep, cam: { x: 756, y: 0, z: per(fmt, 1.14, 1.18) }, ease: expoInOut },
  { f: SCENES.recap.from, cam: { x: 756, y: 0, z: per(fmt, 1.2, 1.24) } },
];

export const Open: React.FC = () => {
  const fmt = useFmt();
  const f = useCurrentFrame() + SCENES.open.from;
  const keys = boost(cams(fmt), per(fmt, 1, 1.1));
  const camOf = track(fmt, keys);
  const cam = camOf(f);
  // Only sideways motion blurs: the vertical clamp drifts as the zoom changes,
  // and a pure push-in must stay sharp.
  const sp = { dx: camSpeed(fmt, keys, f).dx, dy: 0 };

  // ---- the grid of attendee views, bars 9 and 10
  const tileW = per(fmt, 470, 500);
  const tileH = (tileW * CROP.h) / CROP.w;
  const gap = per(fmt, 26, 24);
  const gridY = per(fmt, 820, 560);
  const names = ["Priya Shah", "Sam Carter", "Neha Rao", "You"];
  const gridOut = tween(f, T.smash - 3, T.smash, 0, 1, expoOut);
  const drift = tween(f, T.share, T.smash, -1, 1, (t) => t);
  // Bar 10 pushes into one attendee's view, where the bar is readable.
  const into = tween(f, T.cross - 28, T.cross + 6, 0, 1, expoInOut);
  const gridW = tileW * 2 + gap;
  const gridH = tileH * 2 + gap;
  const ox = (fmt.W - gridW) / 2 + tileW / 2;
  const oy = gridY - gridH / 2 + tileH / 2;
  const intoScale = 1 + into * (per(fmt, 1060, 1000) / tileW - 1);
  const intoX = (fmt.W / 2 - ox) * into;
  const intoY = (fmt.H * per(fmt, 0.45, 0.46) - oy) * into;

  // ---- back to one screen, bars 11 and 12
  const slam = springAt(f, T.smash, { stiffness: 220, damping: 22 });
  const blow = tween(f, T.empty, T.empty + 16, 0, 1, expoOut);
  const pull = tween(f, T.pull, T.pull + 6) * (1 - tween(f, SCENES.recap.from - 2, SCENES.recap.from));

  const plan: FlightPlan = {
    path: [
      { f: SCENES.open.from, x: fmt.W * 0.78, y: fmt.H * per(fmt, 0.47, 0.44) },
      { f: T.cross - 10, x: fmt.W + 200, y: gridY, ease: expoInOut },
      { f: T.cross + 10, x: -200, y: gridY + 30, ease: (t) => t },
      { f: T.smash - 8, x: fmt.W * 0.22, y: fmt.H * per(fmt, 0.3, 0.27), arc: -70, ease: expoOut },
      { f: T.keep, x: fmt.W * 0.2, y: fmt.H * per(fmt, 0.3, 0.27) },
      { f: SCENES.recap.from, x: fmt.W * 0.2, y: fmt.H * per(fmt, 0.31, 0.28) },
    ],
    faces: [
      [SCENES.open.from, "happy"],
      [T.tiles[1], "wow"],
      [T.cross - 12, "curious"],
      [T.smash, "wow"],
      [T.empty + 6, "shrug"],
      [T.keep + 10, "happy"],
    ],
    stunts: [look(T.smash, 0.2, 0.6, T.empty), look(T.keep, 0.3, 0.4, SCENES.recap.from)],
  };
  const remiOf = (g: number): RemiState => remiAt(plan, g);
  const remi = remiOf(f);

  return (
    <AbsoluteFill>
      {/* bars 9 to 10: every attendee sees it */}
      {f < T.smash ? (
        <AbsoluteFill style={{ opacity: 1 - gridOut, transform: `scale(${1 + gridOut * 0.5})` }}>
          <AbsoluteFill style={{ background: "radial-gradient(60% 45% at 50% 42%, rgba(112,99,190,0.26), rgba(10,9,14,0.98) 72%)" }} />
          <div
            style={{
              position: "absolute",
              left: (fmt.W - gridW) / 2,
              top: gridY - gridH / 2,
              width: gridW,
              height: gridH,
              transformOrigin: `${ox - (fmt.W - gridW) / 2}px ${tileH / 2}px`,
              transform: `translate(${intoX + drift * per(fmt, 14, 12)}px, ${intoY}px) scale(${intoScale})`,
            }}
          >
            <div style={{ display: "grid", gridTemplateColumns: `repeat(2, ${tileW}px)`, gap }}>
              {names.map((n, i) => (
                <ShareTile key={n} name={n} w={tileW} h={tileH} k={springAt(f, T.tiles[i], { stiffness: 260, damping: 20 })}>
                  <MiniScreen f={f} w={tileW} />
                </ShareTile>
              ))}
            </div>
          </div>
        </AbsoluteFill>
      ) : null}

      {/* bars 11 to 12: and it keeps nothing */}
      {f >= T.smash - 2 ? (
        <AbsoluteFill style={{ opacity: clamp(slam * 3), transform: `scale(${1 + (1 - slam) * 0.16})` }}>
          <World cam={cam} blur={sp} id="open">
            <Bezel />
            <Desktop app="Zoom" radius={14} dim={pull * 0.25}>
              <CallWindow speaking={-1} />
              <SpotterPanel f={f} working={0} answer={blow > 0.5 ? "" : ANSWER} />
              {/* what it was holding, until it is not */}
              {ASKS.map((t, i) => {
                const at = T.smash + 2 + i * 6;
                const k = tween(f, at, at + 8, 0, 1, expoOut);
                const go = clamp(blow * 1.2 - i * 0.12);
                return (
                  <div
                    key={t}
                    style={{
                      position: "absolute",
                      left: SPOT.x + 40,
                      top: SPOT.y + 136 + i * 54 - go * (180 + i * 40),
                      width: SPOT.w - 80,
                      boxSizing: "border-box",
                      borderRadius: 14,
                      padding: "13px 16px",
                      background: "linear-gradient(rgba(255,255,255,0.09), rgba(255,255,255,0.02) 38%, rgba(255,255,255,0)), rgba(0,0,0,0.72)",
                      boxShadow: "inset 0 0 0 1px rgba(255,255,255,0.14), 0 20px 50px rgba(0,0,0,0.45)",
                      color: "rgba(255,255,255,0.92)",
                      fontFamily: INTER,
                      fontSize: 17,
                      letterSpacing: 0,
                      display: "flex",
                      gap: 10,
                      alignItems: "center",
                      opacity: k * (1 - go),
                      transform: `translateY(${(1 - k) * 16}px) rotate(${go * (i % 2 ? 7 : -6)}deg) scale(${1 - go * 0.25})`,
                      filter: go > 0.05 ? `blur(${go * 7}px)` : undefined,
                    }}
                  >
                    <span style={{ fontSize: 13, color: "rgba(255,255,255,0.45)" }}>⌘↩</span>
                    {t}
                  </div>
                );
              })}
              <KeepSwitch f={f} at={T.keep} />
            </Desktop>
          </World>
        </AbsoluteFill>
      ) : null}

      <Trail f={f} pos={remiOf} len={10} width={per(fmt, 18, 14)} from={SCENES.open.from} opacity={0.8} />
      <Remi s={remi} size={fmt.remi * 0.85} id="remi-open" />
      <Flash f={f} at={T.smash} peak={0.3} dur={8} />
      <TitleSlam
        f={f}
        out={T.smash - 6}
        words={[
          { text: "In", at: T.titleShare },
          { text: "every", at: T.titleShare + 4 },
          { text: "screen", at: T.titleShare + 9, br: true },
          { text: "share.", at: T.titleShare + 13, accent: true },
        ]}
      />
      <TitleSlam
        f={f}
        out={SCENES.recap.from - 4}
        words={[
          { text: "Nothing", at: T.titleKept },
          { text: "kept.", at: T.titleKept + 5, accent: true },
        ]}
      />
    </AbsoluteFill>
  );
};
