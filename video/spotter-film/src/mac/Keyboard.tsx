import React from "react";
import { INTER, clamp, expoOut, palette, tween } from "../lib";

/**
 * The Mac keyboard, close up, drawn in screen px and seen at a low angle: the
 * right-hand side of the deck, so Return sits on the right edge and Command
 * beside the space bar. The film opens here, lit only by the screen above it,
 * and the two keys of Spotter's shortcut go down on the beat.
 *
 * Not a photograph of any machine: a drawn deck, Apple's key legends only
 * (the glyphs on a keyboard), no logos.
 */

type Key = { label: string; w?: number; id?: string; sub?: string };

/** Right-aligned rows, in key units. Row 3 is the bottom row (space, command). */
const ROWS: Key[][] = [
  [{ label: "O" }, { label: "P" }, { label: "{" }, { label: "}" }, { label: "|", w: 1.5 }],
  [{ label: "L" }, { label: ":" }, { label: '"' }, { label: "return", w: 1.9, id: "ret", sub: "↩" }],
  [{ label: "." }, { label: "/" }, { label: "shift", w: 2.4, sub: "⇧" }],
  [{ label: "space", w: 4.2 }, { label: "command", w: 1.5, id: "cmd", sub: "⌘" }, { label: "option", w: 1.1, sub: "⌥" }],
];

/** 0..1: how far a key is down on frame f, given the frame it was pressed. */
export const pressed = (f: number, at: number | undefined) => {
  if (at === undefined || f < at) return 0;
  const t = f - at;
  return t < 3 ? 1 : Math.max(0, 1 - (t - 3) / 7);
};

const Cap: React.FC<{ k: Key; u: number; down: number; glow: number }> = ({ k, u, down, glow }) => {
  const w = (k.w ?? 1) * u - u * 0.1;
  const h = u - u * 0.1;
  const r = u * 0.16;
  const lit = clamp(glow);
  return (
    <div style={{ position: "relative", width: w, height: h, transform: `translateY(${down * u * 0.12}px)` }}>
      <div
        style={{
          position: "absolute",
          inset: 0,
          borderRadius: r,
          background: `linear-gradient(180deg, rgba(86,86,96,${0.5 + lit * 0.5}), #16161a 85%)`,
          boxShadow: `inset 0 ${u * 0.03}px 0 rgba(255,255,255,${0.1 + lit * 0.22}), 0 ${u * 0.07 * (1 - down)}px ${u * 0.1}px rgba(0,0,0,0.7)`,
        }}
      />
      {down > 0.02 ? (
        <div style={{ position: "absolute", inset: -u * 0.06, borderRadius: r * 1.4, background: palette.lavender, opacity: down * 0.5, filter: `blur(${u * 0.12}px)` }} />
      ) : null}
      <div
        style={{
          position: "absolute",
          inset: 0,
          borderRadius: r,
          display: "grid",
          placeItems: "center",
          fontFamily: INTER,
          fontWeight: 500,
          fontSize: k.sub ? u * 0.3 : u * 0.34,
          color: `rgba(236,236,245,${0.45 + lit * 0.5 + down * 0.3})`,
          letterSpacing: "-0.01em",
        }}
      >
        {k.sub ? (
          <div style={{ display: "grid", justifyItems: "center", gap: u * 0.02 }}>
            <span style={{ fontSize: u * 0.34 }}>{k.sub}</span>
            <span style={{ fontSize: u * 0.17, opacity: 0.8 }}>{k.label}</span>
          </div>
        ) : (
          k.label
        )}
      </div>
    </div>
  );
};

/**
 * `presses` maps a key id to the frame it goes down. `glow` is the screen's
 * light on the deck, `tiltBack` the viewing angle in degrees.
 */
export const Keyboard: React.FC<{
  f: number;
  w: number;
  cx: number;
  cy: number;
  glow?: number;
  presses?: Partial<Record<string, number>>;
  tiltBack?: number;
}> = ({ f, w, cx, cy, glow = 1, presses = {}, tiltBack = 50 }) => {
  const u = w / 9.2; // key unit
  const gap = u * 0.1;
  return (
    <div style={{ position: "absolute", left: 0, top: 0, width: "100%", height: "100%", perspective: w * 1.5, perspectiveOrigin: `${cx}px ${cy - w * 0.5}px` }}>
      <div
        style={{
          position: "absolute",
          left: cx - w / 2,
          top: cy,
          width: w,
          transform: `rotateX(${tiltBack}deg)`,
          transformOrigin: "50% 0%",
          transformStyle: "preserve-3d",
        }}
      >
        {/* the deck */}
        <div
          style={{
            position: "absolute",
            left: -u * 0.9,
            top: -u * 0.9,
            width: w + u * 1.8,
            height: u * 11,
            borderRadius: u * 0.3,
            background: `linear-gradient(180deg, rgba(60,60,68,${0.55 * glow}), #0d0d10 70%)`,
            boxShadow: `inset 0 1px 0 rgba(255,255,255,${0.12 * glow})`,
          }}
        />
        <div style={{ position: "relative", display: "grid", gap, paddingRight: u * 0.55 }}>
          {ROWS.map((row, r) => (
            <div key={r} style={{ display: "flex", gap, justifyContent: "flex-end" }}>
              {row.map((k, i) => (
                <Cap key={`${r}-${i}`} k={k} u={u} down={pressed(f, k.id ? presses[k.id] : undefined)} glow={glow * (1 - r * 0.08)} />
              ))}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

/** The screen's light washing down over the keys as the Mac wakes. */
export const DeckLight: React.FC<{ k: number; cx: number; cy: number; w: number }> = ({ k, cx, cy, w }) =>
  k <= 0.01 ? null : (
    <div
      style={{
        position: "absolute",
        left: cx - w,
        top: cy - w * 1.1,
        width: w * 2,
        height: w * 1.6,
        background: `radial-gradient(50% 60% at 50% 0%, rgba(190,180,251,${0.3 * k}), rgba(112,99,190,${0.12 * k}) 45%, rgba(0,0,0,0) 72%)`,
        pointerEvents: "none",
      }}
    />
  );

/** Streaks rushing down the frame while the camera leaves the keyboard. */
export const Rush: React.FC<{ f: number; at: number; until: number; W: number; H: number }> = ({ f, at, until, W, H }) => {
  const k = tween(f, at, at + 8) * (1 - tween(f, until - 6, until + 2));
  if (k <= 0.01) return null;
  return (
    <svg style={{ position: "absolute", inset: 0, width: W, height: H, pointerEvents: "none" }}>
      {Array.from({ length: 24 }, (_, i) => {
        const x = ((i * 433) % W) + 24;
        const len = 200 + ((i * 157) % 320);
        const y = (((f - at) * 150 + i * 251) % (H + len)) - len;
        return <line key={i} x1={x} y1={y} x2={x} y2={y + len} stroke={palette.lavender} strokeWidth={2 + (i % 3)} opacity={k * 0.32} strokeLinecap="round" />;
      })}
    </svg>
  );
};

/** The keyboard sinking out of frame as the camera lifts to the screen. */
export const liftOut = (f: number, at: number, dur = 20) => {
  const t = tween(f, at, at + dur, 0, 1, expoOut);
  return { dy: t * 900, scale: 1 + t * 0.6, opacity: 1 - t };
};
