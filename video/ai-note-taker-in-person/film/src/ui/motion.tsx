import React from "react";
import { clamp, expoOut, expoInOut, inOut, lerp, tween } from "../lib";
import { H, W } from "./parts";

/**
 * The camera for the screen-space scenes, and the transitions between them.
 *
 * The rule from the kit's craft notes: never still. Every scene has a camera
 * that is always moving, and every cut carries motion across it, so nothing
 * ever reads as "it stopped".
 */

/** A camera key: the point that sits in the middle of the frame, and the zoom. */
export type Move = { f: number; x?: number; y?: number; z: number; ease?: (t: number) => number };

const at = (keys: Move[], f: number) => {
  const k0 = keys[0];
  const fill = (k: Move) => ({ x: k.x ?? W / 2, y: k.y ?? H / 2, z: k.z });
  if (f <= k0.f) return fill(k0);
  for (let i = 1; i < keys.length; i++) {
    const a = fill(keys[i - 1]);
    const b = fill(keys[i]);
    if (f <= keys[i].f) {
      const t = (keys[i].ease ?? inOut)(clamp((f - keys[i - 1].f) / Math.max(1, keys[i].f - keys[i - 1].f)));
      // Zoom in log space, so a push-in feels even the whole way.
      return { x: lerp(a.x, b.x, t), y: lerp(a.y, b.y, t), z: Math.exp(lerp(Math.log(a.z), Math.log(b.z), t)) };
    }
  }
  return fill(keys[keys.length - 1]);
};

/** Where a world point lands on screen under this camera, for placing Remi. */
export const onScreen = (keys: Move[], f: number, x: number, y: number) => {
  const c = at(keys, f);
  return { x: W / 2 + (x - c.x) * c.z, y: H / 2 + (y - c.y) * c.z };
};

/**
 * Moves its children under the camera, and blurs them along the move when it
 * is fast (a pan blurs, a pure push-in does not).
 */
export const Cam: React.FC<{ f: number; keys: Move[]; id: string; children: React.ReactNode }> = ({ f, keys, id, children }) => {
  const c = at(keys, f);
  const p = at(keys, f - 1);
  const dx = (p.x - c.x) * c.z;
  const dy = (p.y - c.y) * c.z;
  const blur = Math.min(15, Math.hypot(dx, dy) * 0.26);
  const on = blur > 1.2;
  return (
    <>
      {on ? (
        <svg width={0} height={0} style={{ position: "absolute" }}>
          <filter id={`${id}-cam`} x="-15%" y="-15%" width="130%" height="130%">
            <feGaussianBlur stdDeviation={`${(Math.abs(dx) * 0.3).toFixed(2)} ${(Math.abs(dy) * 0.3).toFixed(2)}`} />
          </filter>
        </svg>
      ) : null}
      <div
        style={{
          position: "absolute",
          left: 0,
          top: 0,
          width: W,
          height: H,
          transformOrigin: "0 0",
          transform: `translate(${(W / 2 - c.x * c.z).toFixed(2)}px, ${(H / 2 - c.y * c.z).toFixed(2)}px) scale(${c.z.toFixed(4)})`,
          filter: on ? `url(#${id}-cam)` : undefined,
        }}
      >
        {children}
      </div>
    </>
  );
};

/** A push-in across a scene: the default move when nothing else is happening. */
export const push = (from: number, dur: number, z0 = 1, z1 = 1.1, drift: [number, number] = [0, 0]): Move[] => [
  { f: from, x: W / 2, y: H / 2, z: z0 },
  { f: from + dur, x: W / 2 + drift[0], y: H / 2 + drift[1], z: z1, ease: (t) => t },
];

export type TransKind = "whipL" | "whipR" | "ramp" | "drop" | "rise" | "none";

/**
 * What a scene does on its way in and on its way out. Every cut in the film
 * is one of these, so no cut lands on a frame that is standing still.
 */
export const Trans: React.FC<{
  f: number;
  from: number;
  dur: number;
  into?: TransKind;
  out?: TransKind;
  id: string;
  children: React.ReactNode;
}> = ({ f, from, dur, into = "whipL", out = "whipL", id, children }) => {
  const end = from + dur;
  const IN = 9;
  const OUT = 7;
  let tx = 0;
  let ty = 0;
  let sc = 1;
  let op = 1;

  // arriving
  const ki = tween(f, from, from + IN, 0, 1, expoOut);
  if (into === "whipL") tx += (1 - ki) * W * 1.05;
  if (into === "whipR") tx -= (1 - ki) * W * 1.05;
  if (into === "ramp") {
    sc *= lerp(1.9, 1, ki);
    op *= clamp(ki * 2.2);
  }
  if (into === "drop") ty -= (1 - ki) * H * 0.9;
  if (into === "rise") ty += (1 - ki) * H * 0.9;

  // leaving
  const ko = tween(f, end - OUT, end, 0, 1, (t) => t * t * t);
  if (out === "whipL") tx -= ko * W * 1.05;
  if (out === "whipR") tx += ko * W * 1.05;
  if (out === "ramp") {
    sc *= lerp(1, 0.55, ko);
    op *= 1 - ko;
  }
  if (out === "drop") ty += ko * H * 0.9;
  if (out === "rise") ty -= ko * H * 0.9;

  // blur along whatever it is doing
  const prev = (() => {
    const g = f - 1;
    let x = 0;
    const kin = tween(g, from, from + IN, 0, 1, expoOut);
    if (into === "whipL") x += (1 - kin) * W * 1.05;
    if (into === "whipR") x -= (1 - kin) * W * 1.05;
    const kout = tween(g, end - OUT, end, 0, 1, (t) => t * t * t);
    if (out === "whipL") x -= kout * W * 1.05;
    if (out === "whipR") x += kout * W * 1.05;
    return x;
  })();
  const v = Math.abs(tx - prev);
  const blur = Math.min(54, v * 0.34);

  return (
    <>
      {blur > 1 ? (
        <svg width={0} height={0} style={{ position: "absolute" }}>
          <filter id={`${id}-tr`} x="-25%" y="-10%" width="150%" height="120%">
            <feGaussianBlur stdDeviation={`${blur.toFixed(1)} 0`} />
          </filter>
        </svg>
      ) : null}
      <div
        style={{
          position: "absolute",
          inset: 0,
          opacity: op,
          transformOrigin: "50% 50%",
          transform: `translate(${tx.toFixed(1)}px, ${ty.toFixed(1)}px) scale(${sc.toFixed(4)})`,
          filter: blur > 1 ? `url(#${id}-tr)` : undefined,
        }}
      >
        {children}
      </div>
    </>
  );
};

/** An eased 0..1 that never quite settles, so a held frame still breathes. */
export const breathe = (f: number, amp = 4, period = 150) => Math.sin((f / period) * Math.PI * 2) * amp;

export { expoInOut };
