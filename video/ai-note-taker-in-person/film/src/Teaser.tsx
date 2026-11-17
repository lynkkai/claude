import React from "react";
import { AbsoluteFill, Sequence, useCurrentFrame } from "remotion";
import { HITS, SCENES } from "./timing";
import { FORMATS, FmtContext, type FmtName } from "./lib";
import { shakeAt } from "./fx/fx";
import { ChapterCard, Slate } from "./ui/parts";
import { Trans, type TransKind } from "./ui/motion";
import { Hook } from "./scenes/Hook";
import { DeviceBoard, PicksBoard } from "./scenes/Boards";
import { MicMap } from "./scenes/MicMap";
import { Column, NoteIn, RecordNow } from "./scenes/MacBits";
import { Labels } from "./scenes/Labels";
import { Offline, Online } from "./scenes/Offline";
import { End } from "./scenes/End";

/**
 * The 2:00 timeline. Every scene arrives and leaves on a move (a whip, a
 * punch-in, a slam down), so no cut lands on a frame that is standing still,
 * and every scene has its own camera running underneath.
 *
 * Remi's graphics are rendered here; the footage the team films is held by a
 * slate that says what the shot is and the line said over it.
 */

const S = SCENES;

/** One piece of the timeline, with the move it makes on the way in and out. */
const Beat: React.FC<{
  from: number;
  dur: number;
  name: string;
  into?: TransKind;
  out?: TransKind;
  children: React.ReactNode;
}> = ({ from, dur, name, into, out, children }) => (
  <Sequence from={from} durationInFrames={dur} name={name}>
    <Inner from={from} dur={dur} into={into} out={out} id={name.replace(/\W+/g, "-")}>
      {children}
    </Inner>
  </Sequence>
);

const Inner: React.FC<{ from: number; dur: number; into?: TransKind; out?: TransKind; id: string; children: React.ReactNode }> = ({ from, dur, into, out, id, children }) => {
  const f = useCurrentFrame() + from;
  return (
    <Trans f={f} from={from} dur={dur} into={into} out={out} id={id}>
      {children}
    </Trans>
  );
};

const Card: React.FC<{ n: number; title: string; accent?: string }> = ({ n, title, accent }) => {
  const f = useCurrentFrame();
  return <ChapterCard f={f} at={0} n={n} title={title} accent={accent} />;
};

const Shot: React.FC<Omit<React.ComponentProps<typeof Slate>, "f">> = (p) => {
  const f = useCurrentFrame();
  return <Slate {...p} f={f} />;
};

export const Teaser: React.FC<{ fmt: FmtName }> = ({ fmt }) => {
  const f = useCurrentFrame();
  return (
    <FmtContext.Provider value={FORMATS[fmt]}>
      <AbsoluteFill style={{ background: "#000", overflow: "hidden" }}>
        <AbsoluteFill style={{ transform: `${shakeAt(f, HITS)} scale(1.02)` }}>
          <Beat from={S.hook.from} dur={S.hook.dur} name="G1 cold open" into="none" out="whipL">
            <Hook />
          </Beat>

          <Beat from={S.shotIntro.from} dur={S.shotIntro.dur} name="Shot the problem" into="whipL" out="whipL">
            <Shot
              kind="A-ROLL + SCREEN"
              what="Presenter at the head of the table, then the rooms: a glass-walled office, a client visit, a site visit."
              vo="Most AI note takers need a Zoom link. Your best conversations don't have one. Here's how to get the same notes from a room, in two minutes. Online, a bot hears everyone cleanly. In a room, one mic fights the fan and the echo."
              from="0:04"
              to="0:20"
            />
          </Beat>

          <Beat from={S.card1.from} dur={S.card1.dur} name="Card 1" into="drop" out="whipL">
            <Card n={1} title="Phone, laptop or recorder?" accent="recorder?" />
          </Beat>
          <Beat from={S.shotDevices.from} dur={S.shotDevices.dur} name="Shot three devices" into="whipL" out="whipL">
            <Shot
              kind="A-ROLL"
              what="The three on the table: a MacBook, a phone, a small recorder. Disclosure to camera."
              vo="Three ways to get a room into an AI note taker. Disclosure: I work on Lynkk."
              from="0:22"
              to="0:28"
            />
          </Beat>
          <Beat from={S.board.from} dur={S.board.dur} name="G3 device board" into="ramp" out="whipL">
            <DeviceBoard />
          </Beat>
          <Beat from={S.shotNoPhone.from} dur={S.shotNoPhone.dur} name="Shot no phone app" into="whipL" out="whipL">
            <Shot kind="A-ROLL" what="Presenter taps the MacBook." vo="Lynkk has no phone app." from="0:38" to="0:40" />
          </Beat>

          <Beat from={S.card2.from} dur={S.card2.dur} name="Card 2" into="drop" out="whipL">
            <Card n={2} title="Record the room." accent="room." />
          </Beat>
          <Beat from={S.micMap.from} dur={S.micMap.dur} name="G4 mic map" into="rise" out="whipL">
            <MicMap />
          </Beat>
          <Beat from={S.shotConsent.from} dur={S.shotConsent.dur} name="Shot ask first" into="whipL" out="whipL">
            <Shot kind="A-ROLL" what="Presenter asks the room, on camera, before recording." vo="And ask first. Everyone here agreed on camera." from="0:50" to="0:54" />
          </Beat>
          <Beat from={S.record.from} dur={S.record.dur} name="G5a Record now" into="ramp" out="whipL">
            <RecordNow />
          </Beat>
          <Beat from={S.column.from} dur={S.column.dur} name="G5b recording column" into="whipL" out="whipL">
            <Column />
          </Beat>
          <Beat from={S.note.from} dur={S.note.dur} name="G5c the note" into="rise" out="ramp">
            <NoteIn />
          </Beat>

          <Beat from={S.card3.from} dur={S.card3.dur} name="Card 3" into="drop" out="whipL">
            <Card n={3} title="Who said what?" accent="what?" />
          </Beat>
          <Beat from={S.labels.from} dur={S.labels.dur} name="G6 speaker labels" into="whipL" out="whipL">
            <Labels />
          </Beat>
          <Beat from={S.shotTips.from} dur={S.shotTips.dur} name="Shot label tips" into="whipL" out="whipL">
            <Shot kind="A-ROLL" what="Presenter, to camera." vo="One at a time, and say names. Over to you, Priya." from="1:22" to="1:26" />
          </Beat>

          <Beat from={S.card4.from} dur={S.card4.dur} name="Card 4" into="drop" out="whipL">
            <Card n={4} title="No Wi-Fi?" accent="Wi-Fi?" />
          </Beat>
          <Beat from={S.offline.from} dur={S.offline.dur} name="G7 offline" into="ramp" out="whipL">
            <Offline />
          </Beat>
          <Beat from={S.online.from} dur={S.online.dur} name="G7b back online" into="whipL" out="ramp">
            <Online />
          </Beat>

          <Beat from={S.card5.from} dur={S.card5.dur} name="Card 5" into="drop" out="whipL">
            <Card n={5} title="My picks." accent="picks." />
          </Beat>
          <Beat from={S.picks.from} dur={S.picks.dur} name="G8 picks board" into="whipL" out="ramp">
            <PicksBoard />
          </Beat>
          <Beat from={S.end.from} dur={S.end.dur} name="G9 end card" into="ramp" out="none">
            <End />
          </Beat>
        </AbsoluteFill>
      </AbsoluteFill>
    </FmtContext.Provider>
  );
};
