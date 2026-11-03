import React from "react";
import { AbsoluteFill, Img, Sequence, staticFile, useCurrentFrame } from "remotion";
import { SCENES, T } from "./timing";
import { FORMATS, FmtContext, type FmtName } from "./lib";
import { shakeAt } from "./fx/fx";
import { Hook } from "./scenes/Hook";
import { ASK_FROM, Ask } from "./scenes/Ask";
import { Screen } from "./scenes/Screen";
import { Listen } from "./scenes/Listen";
import { Open } from "./scenes/Open";
import { Recap } from "./scenes/Recap";
import { END_FROM, EndCard } from "./scenes/EndCard";

/** Every impact the camera feels, with how hard. */
const HITS = [
  { f: T.cmdDown, amp: 0.6 },
  { f: T.retDown, amp: 0.7 },
  { f: T.deskHit, amp: 1 },
  { f: T.answerHit, amp: 0.45 },
  { f: T.picDrop, amp: 0.3 },
  { f: T.listenKey, amp: 1 },
  ...T.tiles.map((f, i) => ({ f, amp: 0.3 + i * 0.05 })),
  { f: T.smash, amp: 0.9 },
  ...T.recap.map((f, i) => ({ f, amp: 0.55 + i * 0.15 })),
  { f: T.logo, amp: 0.7 },
];

/** The dark plate everything sits on when the camera pulls back past the screen. */
const Backdrop: React.FC = () => (
  <AbsoluteFill style={{ background: "#0b0a10" }}>
    <Img src={staticFile("plate-night.jpg")} style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover", opacity: 0.16, filter: "blur(40px)" }} />
    <AbsoluteFill style={{ background: "radial-gradient(70% 55% at 50% 40%, rgba(112,99,190,0.18), rgba(0,0,0,0) 70%)" }} />
  </AbsoluteFill>
);

/**
 * The film: one timeline, scene starts from bar numbers (timing.ts). The
 * shake wraps everything, so every impact moves the whole frame.
 */
export const Teaser: React.FC<{ fmt: FmtName }> = ({ fmt }) => {
  const f = useCurrentFrame();
  return (
    <FmtContext.Provider value={FORMATS[fmt]}>
      <AbsoluteFill style={{ background: "#000", overflow: "hidden" }}>
        <AbsoluteFill style={{ transform: `${shakeAt(f, HITS)} scale(1.03)` }}>
          <Backdrop />
          <Sequence from={SCENES.hook.from} durationInFrames={SCENES.hook.dur} name="Hook">
            <Hook />
          </Sequence>
          <Sequence from={ASK_FROM} durationInFrames={SCENES.ask.from + SCENES.ask.dur - ASK_FROM} name="Ask">
            <Ask />
          </Sequence>
          <Sequence from={SCENES.screen.from} durationInFrames={SCENES.screen.dur} name="Screen">
            <Screen />
          </Sequence>
          <Sequence from={SCENES.listen.from} durationInFrames={SCENES.listen.dur} name="Listen">
            <Listen />
          </Sequence>
          <Sequence from={SCENES.open.from} durationInFrames={SCENES.open.dur} name="Open">
            <Open />
          </Sequence>
          <Sequence from={SCENES.recap.from} durationInFrames={SCENES.recap.dur} name="Recap">
            <Recap />
          </Sequence>
          <Sequence from={END_FROM} durationInFrames={SCENES.end.from + SCENES.end.dur - END_FROM} name="End card">
            <EndCard />
          </Sequence>
        </AbsoluteFill>
      </AbsoluteFill>
    </FmtContext.Provider>
  );
};
