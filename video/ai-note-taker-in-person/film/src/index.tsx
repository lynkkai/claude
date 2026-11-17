import React from "react";
import { Composition, registerRoot } from "remotion";
import { Teaser } from "./Teaser";
import { DURATION, FPS } from "./timing";

/** One 16:9 YouTube frame. The 9:16 Short is cut from the same timeline later. */
const Root: React.FC = () => (
  <Composition id="Wide" component={Teaser} defaultProps={{ fmt: "wide" as const }} durationInFrames={DURATION} fps={FPS} width={1920} height={1080} />
);

registerRoot(Root);
