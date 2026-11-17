import React from "react";
import { AbsoluteFill, Sequence, useCurrentFrame } from "remotion";
import { HITS, SCENES } from "./timing";
import { FORMATS, FmtContext, type FmtName } from "./lib";
import { shakeAt } from "./fx/fx";
import { ChapterCard, Slate } from "./ui/parts";
import { Hook } from "./scenes/Hook";
import { DeviceBoard, PicksBoard } from "./scenes/Boards";
import { MicMap } from "./scenes/MicMap";
import { Column, NoteIn, RecordNow } from "./scenes/MacBits";
import { Labels } from "./scenes/Labels";
import { Offline, Online } from "./scenes/Offline";
import { End } from "./scenes/End";

/**
 * The 2:00 timeline. Remi's graphics are rendered here; the footage the team
 * films is held by a slate that says what the shot is and the line said over
 * it, so the whole two minutes can be watched against the soundtrack before
 * anybody books a room.
 */

const S = SCENES;

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
          <Sequence from={S.hook.from} durationInFrames={S.hook.dur} name="G1 cold open">
            <Hook />
          </Sequence>

          <Sequence from={S.shotIntro.from} durationInFrames={S.shotIntro.dur} name="Shot: the problem">
            <Shot
              kind="A-ROLL + SCREEN"
              what="Presenter at the head of the table, then the rooms: a glass-walled office, a client visit, a site visit."
              vo="Most AI note takers need a Zoom link. Your best conversations don't have one. Here's how to get the same notes from a room, in two minutes. Online, a bot hears everyone cleanly. In a room, one mic fights the fan and the echo."
              from="0:04"
              to="0:20"
            />
          </Sequence>

          <Sequence from={S.card1.from} durationInFrames={S.card1.dur} name="Card 1">
            <Card n={1} title="Phone, laptop or recorder?" accent="recorder?" />
          </Sequence>
          <Sequence from={S.shotDevices.from} durationInFrames={S.shotDevices.dur} name="Shot: three devices">
            <Shot
              kind="A-ROLL"
              what="The three on the table: a MacBook, a phone, a small recorder. Disclosure to camera."
              vo="Three ways to get a room into an AI note taker. Disclosure: I work on Lynkk."
              from="0:22"
              to="0:28"
            />
          </Sequence>
          <Sequence from={S.board.from} durationInFrames={S.board.dur} name="G3 device board">
            <DeviceBoard />
          </Sequence>
          <Sequence from={S.shotNoPhone.from} durationInFrames={S.shotNoPhone.dur} name="Shot: no phone app">
            <Shot kind="A-ROLL" what="Presenter taps the MacBook." vo="Lynkk has no phone app." from="0:38" to="0:40" />
          </Sequence>

          <Sequence from={S.card2.from} durationInFrames={S.card2.dur} name="Card 2">
            <Card n={2} title="Record the room." accent="room." />
          </Sequence>
          <Sequence from={S.micMap.from} durationInFrames={S.micMap.dur} name="G4 mic map">
            <MicMap />
          </Sequence>
          <Sequence from={S.shotConsent.from} durationInFrames={S.shotConsent.dur} name="Shot: ask first">
            <Shot kind="A-ROLL" what="Presenter asks the room, on camera, before recording." vo="And ask first. Everyone here agreed on camera." from="0:50" to="0:54" />
          </Sequence>
          <Sequence from={S.record.from} durationInFrames={S.record.dur} name="G5a Record now">
            <RecordNow />
          </Sequence>
          <Sequence from={S.column.from} durationInFrames={S.column.dur} name="G5b recording column">
            <Column />
          </Sequence>
          <Sequence from={S.note.from} durationInFrames={S.note.dur} name="G5c the note">
            <NoteIn />
          </Sequence>

          <Sequence from={S.card3.from} durationInFrames={S.card3.dur} name="Card 3">
            <Card n={3} title="Who said what?" accent="what?" />
          </Sequence>
          <Sequence from={S.labels.from} durationInFrames={S.labels.dur} name="G6 speaker labels">
            <Labels />
          </Sequence>
          <Sequence from={S.shotTips.from} durationInFrames={S.shotTips.dur} name="Shot: label tips">
            <Shot kind="A-ROLL" what="Presenter, to camera." vo="One at a time, and say names. Over to you, Priya." from="1:22" to="1:26" />
          </Sequence>

          <Sequence from={S.card4.from} durationInFrames={S.card4.dur} name="Card 4">
            <Card n={4} title="No Wi-Fi?" accent="Wi-Fi?" />
          </Sequence>
          <Sequence from={S.offline.from} durationInFrames={S.offline.dur} name="G7 offline">
            <Offline />
          </Sequence>
          <Sequence from={S.online.from} durationInFrames={S.online.dur} name="G7b back online">
            <Online />
          </Sequence>

          <Sequence from={S.card5.from} durationInFrames={S.card5.dur} name="Card 5">
            <Card n={5} title="My picks." accent="picks." />
          </Sequence>
          <Sequence from={S.picks.from} durationInFrames={S.picks.dur} name="G8 picks board">
            <PicksBoard />
          </Sequence>
          <Sequence from={S.end.from} durationInFrames={S.end.dur} name="G9 end card">
            <End />
          </Sequence>
        </AbsoluteFill>
      </AbsoluteFill>
    </FmtContext.Provider>
  );
};
