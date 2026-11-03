import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { T } from "../timing";
import { INTER, MARK_PATHS, MARK_VIEWBOX, clamp, expoInOut, expoOut, palette, per, springAt, tween, useFmt, type Fmt } from "../lib";
import { Flash, Trail } from "../fx/fx";
import { Remi } from "../remi/Remi";
import { hop, remiAt, squish, wave, type FlightPlan, type RemiState } from "../remi/flight";

/**
 * The end card, 28 to 32 s. Everything clears to the dark plate. Remi flies
 * one fast circle and its trail draws the Lynkk sphere, which locks on the
 * logo hit. Spotter, the Request early access button, the page's address and
 * the fine print. Remi perches on the button and waves.
 *
 * This scene starts a little before bar 14 (Teaser.tsx) so the circle can
 * finish on the logo frame.
 */

export const END_FROM = T.clear - 8;
const CIRCLE_FROM = T.clear + 1;

const layout = (fmt: Fmt) =>
  per(
    fmt,
    { sphere: { y: 590, s: 300 }, title: 815, size: 112, button: { y: 1135, w: 720, h: 124, fs: 44 }, url: 1262, fine: 1345 },
    { sphere: { y: 390, s: 230 }, title: 625, size: 96, button: { y: 850, w: 650, h: 112, fs: 40 }, url: 975, fine: 1060 },
  );

export const EndCard: React.FC = () => {
  const fmt = useFmt();
  const f = useCurrentFrame() + END_FROM;
  const L = layout(fmt);
  const cx = fmt.W / 2;
  const cy = L.sphere.y;
  const R = L.sphere.s * 0.56;

  // The circle: from the top, clockwise, finishing on the logo frame.
  const circ = (g: number) => {
    const t = tween(g, CIRCLE_FROM, T.logo, 0, 1, expoInOut);
    const a = -Math.PI / 2 + t * Math.PI * 2;
    return { x: cx + Math.cos(a) * R, y: cy + Math.sin(a) * R };
  };
  const btnTop = L.button.y - L.button.h / 2;
  const perch = { x: cx + L.button.w / 2 - 60, y: btnTop - fmt.remi * 0.36 };
  const rest = { x: cx + L.sphere.s * 0.95, y: cy - L.sphere.s * 0.25 };
  const plan: FlightPlan = {
    path: [
      { f: END_FROM, x: fmt.W + 200, y: cy + R * 1.4 },
      { f: CIRCLE_FROM, x: cx, y: cy - R, arc: 80, ease: expoOut },
    ],
    faces: [
      [END_FROM, "wow"],
      [T.logo, "happy"],
      [T.perch + 4, "wave"],
    ],
    stunts: [squish(T.perch, 0.22), wave(T.perch + 4, 52), hop(T.perch + 60, 26, 10)],
  };
  const remiOf = (g: number): RemiState => {
    const s = remiAt(plan, g);
    if (g < CIRCLE_FROM) return s;
    // On the circle, then out to rest beside the sphere, then down onto the button.
    let p = circ(g);
    if (g > T.logo) {
      const k = tween(g, T.logo, T.logo + 14, 0, 1, expoOut);
      p = { x: p.x + (rest.x - p.x) * k, y: p.y + (rest.y - p.y) * k };
    }
    if (g > T.perch - 12) {
      const k = tween(g, T.perch - 12, T.perch, 0, 1, (t) => t * t);
      const lift = Math.sin(Math.PI * k) * 60;
      p = { x: p.x + (perch.x - p.x) * k, y: p.y + (perch.y - p.y) * k - lift };
    }
    const prev = g > CIRCLE_FROM ? circ(g - 1) : p;
    const bank = g <= T.logo ? clamp((p.x - prev.x) * 0.6, -25, 25) : 0;
    return { ...s, x: p.x, y: p.y + (g > T.logo ? Math.sin(g / 9) * 4 : 0), rot: bank, rig: { ...s.rig, thrust: g >= T.perch ? 0.12 : g <= T.logo ? 1 : 0.45 } };
  };
  const remi = remiOf(f);

  const plate = tween(f, END_FROM, T.clear + 6);
  const ring = tween(f, CIRCLE_FROM, T.logo, 0, 1, expoInOut);
  const ringOut = tween(f, T.logo, T.logo + 12);
  const lock = springAt(f, T.logo, { stiffness: 320, damping: 15 });
  const title = springAt(f, T.name, { stiffness: 300, damping: 20 });
  const button = springAt(f, T.button, { stiffness: 300, damping: 16 });
  const url = tween(f, T.url, T.url + 8);
  const fine = tween(f, T.fine, T.fine + 10);
  const press = f >= T.perch ? Math.exp(-(f - T.perch) / 4) * 0.05 : 0;
  const circumference = 2 * Math.PI * R;

  return (
    <AbsoluteFill>
      <AbsoluteFill style={{ opacity: plate, background: "radial-gradient(65% 45% at 50% 38%, #221d3a, #0b0a10 72%)" }} />
      {/* the trail's ring */}
      {f >= CIRCLE_FROM && ringOut < 1 ? (
        <svg style={{ position: "absolute", inset: 0, width: fmt.W, height: fmt.H }}>
          <circle
            cx={cx}
            cy={cy}
            r={R}
            fill="none"
            stroke={palette.lavender}
            strokeWidth={per(fmt, 12, 10) * (1 - ringOut * 0.7)}
            strokeLinecap="round"
            strokeDasharray={`${circumference * ring} ${circumference}`}
            transform={`rotate(-90 ${cx} ${cy})`}
            opacity={1 - ringOut}
            style={{ filter: "drop-shadow(0 0 14px rgba(112,99,190,0.95))" }}
          />
        </svg>
      ) : null}
      {/* the sphere, stripe by stripe on the hit */}
      {f >= T.logo - 1 ? (
        <div style={{ position: "absolute", left: cx - L.sphere.s / 2, top: cy - L.sphere.s / 2, width: L.sphere.s, height: L.sphere.s, transform: `scale(${0.7 + 0.3 * lock})` }}>
          <div style={{ position: "absolute", inset: "-40%", borderRadius: "50%", background: "radial-gradient(closest-side, rgba(112,99,190,0.55), rgba(112,99,190,0))", opacity: lock }} />
          <svg viewBox={MARK_VIEWBOX} width={L.sphere.s} height={L.sphere.s} style={{ position: "relative", overflow: "visible" }}>
            {MARK_PATHS.map((d, j) => {
              const k = tween(f, T.logo + j * 0.6, T.logo + 4 + j * 0.6, 0, 1, expoOut);
              return <path key={j} d={d} fill={palette.white} opacity={k} transform={`translate(${(1 - k) * (j % 2 ? 30 : -30)} 0)`} />;
            })}
          </svg>
        </div>
      ) : null}
      <div
        style={{
          position: "absolute",
          left: 0,
          right: 0,
          top: L.title,
          transform: `translateY(-50%) translateY(${(1 - title) * 40}px)`,
          opacity: clamp(title * 2),
          textAlign: "center",
          fontFamily: INTER,
          fontWeight: 600,
          fontSize: L.size,
          letterSpacing: "-0.045em",
          color: palette.white,
        }}
      >
        Spotter
      </div>
      {f >= T.button ? (
        <div
          style={{
            position: "absolute",
            left: cx - L.button.w / 2,
            top: btnTop,
            width: L.button.w,
            height: L.button.h,
            borderRadius: L.button.h / 2,
            background: palette.white,
            color: palette.black,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            gap: L.button.fs * 0.4,
            fontFamily: INTER,
            fontWeight: 600,
            fontSize: L.button.fs,
            letterSpacing: "-0.02em",
            transform: `scale(${(0.6 + 0.4 * button) * (1 - press)})`,
            opacity: clamp(button * 2),
            boxShadow: `0 20px 60px rgba(112,99,190,${0.45 * button})`,
          }}
        >
          Request early access
        </div>
      ) : null}
      <div style={{ position: "absolute", left: 0, right: 0, top: L.url, transform: "translateY(-50%)", textAlign: "center", fontFamily: INTER, fontWeight: 500, fontSize: L.size * 0.36, color: "rgba(255,255,255,0.75)", opacity: url, letterSpacing: "-0.01em" }}>
        lynkk.ai/features/spotter
      </div>
      <div style={{ position: "absolute", left: 40, right: 40, top: L.fine, transform: "translateY(-50%)", textAlign: "center", fontFamily: INTER, fontSize: per(fmt, 27, 24), color: "rgba(255,255,255,0.5)", opacity: fine }}>
        Apple silicon · macOS 14.2 or later · Lynkk Pro · Spotter in early access
      </div>
      <Trail f={f} pos={remiOf} from={CIRCLE_FROM - 6} len={9} width={per(fmt, 20, 16)} opacity={1 - ringOut} />
      <Remi s={remi} size={fmt.remi * 0.85} id="remi-end" glow={0.6} />
      <Flash f={f} at={T.logo} peak={0.35} dur={10} color="#e2e0f2" />
    </AbsoluteFill>
  );
};
