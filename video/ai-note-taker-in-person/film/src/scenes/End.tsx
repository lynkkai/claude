import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { SCENES, T } from "../timing";
import { INTER, MARK_PATHS, MARK_VIEWBOX, clamp, expoInOut, expoOut, palette, springAt, tween } from "../lib";
import { Flash, Trail } from "../fx/fx";
import { Remi } from "../remi/Remi";
import { hop, remiAt, squish, wave, type FlightPlan, type RemiState } from "../remi/flight";
import { W, ink } from "../ui/parts";
import { Cam, type Move } from "../ui/motion";

/**
 * 114 to 120 s. Remi's trail draws a circle that locks into the Lynkk sphere,
 * then the name, the CTA, the price and the fine print, one beat apart. Remi
 * lands on the button on 1:58, where the music's last chord is. The camera
 * keeps pushing the whole way, so the end never sits still.
 *
 * The CTA is "Get Lynkk Pro" and the price is on screen: there is no free
 * plan (website changes, section 1).
 */

const SPHERE = { y: 300, s: 190 };
const TITLE_Y = 470;
const BTN = { y: 650, w: 620, h: 112, fs: 44 };
const URL_Y = 790;
const FINE_Y = 910;

export const End: React.FC = () => {
  const f = useCurrentFrame() + SCENES.end.from;
  const S = SCENES.end.from;
  const cx = W / 2;
  const cy = SPHERE.y;
  const R = SPHERE.s * 0.62;

  const circ = (g: number) => {
    const t = tween(g, T.circleFrom, T.logo, 0, 1, expoInOut);
    const a = -Math.PI / 2 + t * Math.PI * 2;
    return { x: cx + Math.cos(a) * R, y: cy + Math.sin(a) * R };
  };
  const btnTop = BTN.y - BTN.h / 2;
  const perch = { x: cx + BTN.w / 2 - 50, y: btnTop - 46 };
  const rest = { x: cx + SPHERE.s * 1.15, y: cy - SPHERE.s * 0.2 };

  const plan: FlightPlan = {
    path: [
      { f: S - 20, x: W + 200, y: cy + R },
      { f: T.circleFrom, x: cx, y: cy - R, arc: 60, ease: expoOut },
    ],
    faces: [
      [S - 20, "wow"],
      [T.logo, "happy"],
      [T.perch + 4, "wave"],
    ],
    stunts: [squish(T.perch, 0.24), wave(T.perch + 5, 44), hop(T.perch + 48, 22, 10)],
  };
  const remiOf = (g: number): RemiState => {
    const s = remiAt(plan, g);
    if (g < T.circleFrom) return s;
    let p = circ(g);
    if (g > T.logo) {
      const k = tween(g, T.logo, T.logo + 12, 0, 1, expoOut);
      p = { x: p.x + (rest.x - p.x) * k, y: p.y + (rest.y - p.y) * k };
    }
    if (g > T.perch - 12) {
      const k = tween(g, T.perch - 12, T.perch, 0, 1, (t) => t * t);
      const lift = Math.sin(Math.PI * k) * 54;
      p = { x: p.x + (perch.x - p.x) * k, y: p.y + (perch.y - p.y) * k - lift };
    }
    const prev = g > T.circleFrom ? circ(g - 1) : p;
    const bank = g <= T.logo ? clamp((p.x - prev.x) * 0.6, -25, 25) : 0;
    return { ...s, x: p.x, y: p.y + (g > T.logo ? Math.sin(g / 9) * 3 : 0), rot: bank, rig: { ...s.rig, thrust: g >= T.perch ? 0.12 : g <= T.logo ? 1 : 0.45 } };
  };
  const remi = remiOf(f);

  const keys: Move[] = [
    { f: S, x: cx, y: cy + 40, z: 1.16 },
    { f: T.logo, x: cx, y: cy + 90, z: 1.06, ease: expoOut },
    { f: T.cta, x: cx, y: 520, z: 1.0 },
    { f: T.perch, x: cx, y: 560, z: 1.03 },
    { f: S + SCENES.end.dur, x: cx, y: 575, z: 1.09, ease: (t) => t },
  ];

  const ring = tween(f, T.circleFrom, T.logo, 0, 1, expoInOut);
  const ringOut = tween(f, T.logo, T.logo + 12);
  const lock = springAt(f, T.logo, { stiffness: 320, damping: 15 });
  const title = springAt(f, T.logo + 6, { stiffness: 300, damping: 20 });
  const button = springAt(f, T.cta, { stiffness: 300, damping: 16 });
  const price = tween(f, T.price, T.price + 8);
  const url = tween(f, T.price + 6, T.price + 14);
  const fine = tween(f, T.fine, T.fine + 10);
  const press = f >= T.perch ? Math.exp(-(f - T.perch) / 4) * 0.05 : 0;
  const C = 2 * Math.PI * R;

  return (
    <AbsoluteFill>
      <AbsoluteFill style={{ background: "radial-gradient(60% 50% at 50% 30%, #231e3c, #0b0a10 70%)" }} />
      <Cam f={f} keys={keys} id="end">
        {f >= T.circleFrom && ringOut < 1 ? (
          <svg style={{ position: "absolute", left: 0, top: 0, width: W, height: 1080, overflow: "visible" }}>
            <circle
              cx={cx}
              cy={cy}
              r={R}
              fill="none"
              stroke={palette.lavender}
              strokeWidth={10 * (1 - ringOut * 0.7)}
              strokeLinecap="round"
              strokeDasharray={`${C * ring} ${C}`}
              transform={`rotate(-90 ${cx} ${cy})`}
              opacity={1 - ringOut}
              style={{ filter: "drop-shadow(0 0 14px rgba(112,99,190,0.95))" }}
            />
          </svg>
        ) : null}

        {f >= T.logo - 1 ? (
          <div style={{ position: "absolute", left: cx - SPHERE.s / 2, top: cy - SPHERE.s / 2, width: SPHERE.s, height: SPHERE.s, transform: `scale(${0.7 + 0.3 * lock})` }}>
            <div style={{ position: "absolute", inset: "-40%", borderRadius: "50%", background: "radial-gradient(closest-side, rgba(112,99,190,0.55), rgba(112,99,190,0))", opacity: lock }} />
            <svg viewBox={MARK_VIEWBOX} width={SPHERE.s} height={SPHERE.s} style={{ position: "relative", overflow: "visible" }}>
              {MARK_PATHS.map((d, j) => {
                const k = tween(f, T.logo + j * 0.6, T.logo + 4 + j * 0.6, 0, 1, expoOut);
                return <path key={j} d={d} fill={palette.white} opacity={k} transform={`translate(${(1 - k) * (j % 2 ? 26 : -26)} 0)`} />;
              })}
            </svg>
          </div>
        ) : null}

        <div
          style={{
            position: "absolute",
            left: 0,
            width: W,
            top: TITLE_Y,
            transform: `translateY(-50%) translateY(${(1 - title) * 34}px)`,
            opacity: clamp(title * 2),
            textAlign: "center",
            fontFamily: INTER,
            fontWeight: 600,
            fontSize: 86,
            letterSpacing: "-0.045em",
            color: palette.white,
          }}
        >
          Lynkk
        </div>

        {f >= T.cta ? (
          <div
            style={{
              position: "absolute",
              left: cx - BTN.w / 2,
              top: btnTop,
              width: BTN.w,
              height: BTN.h,
              borderRadius: BTN.h / 2,
              background: palette.white,
              color: palette.black,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              fontFamily: INTER,
              fontWeight: 600,
              fontSize: BTN.fs,
              letterSpacing: "-0.02em",
              transform: `scale(${(0.6 + 0.4 * button) * (1 - press)})`,
              opacity: clamp(button * 2),
              boxShadow: `0 20px 60px rgba(112,99,190,${0.45 * button})`,
            }}
          >
            Get Lynkk Pro
          </div>
        ) : null}

        <div
          style={{
            position: "absolute",
            left: 0,
            width: W,
            top: URL_Y,
            transform: `translateY(-50%) translateY(${(1 - price) * 18}px)`,
            textAlign: "center",
            fontFamily: INTER,
            fontWeight: 600,
            fontSize: 38,
            color: palette.lavender,
            opacity: price,
            letterSpacing: "-0.02em",
          }}
        >
          $4 a month · ₹250 in India
        </div>
        <div
          style={{
            position: "absolute",
            left: 0,
            width: W,
            top: URL_Y + 66,
            transform: "translateY(-50%)",
            textAlign: "center",
            fontFamily: INTER,
            fontWeight: 500,
            fontSize: 34,
            color: "rgba(255,255,255,0.75)",
            opacity: url,
          }}
        >
          lynkk.ai
        </div>
        <div
          style={{
            position: "absolute",
            left: 0,
            width: W,
            top: FINE_Y,
            transform: "translateY(-50%)",
            textAlign: "center",
            fontFamily: INTER,
            fontSize: 24,
            color: ink.lo,
            opacity: fine,
          }}
        >
          Apple silicon · macOS 14.2 or later
        </div>

        <Trail f={f} pos={remiOf} from={T.circleFrom - 6} len={9} width={16} opacity={1 - ringOut} />
        <Remi s={remi} size={118} id="remi-end" glow={0.6} />
      </Cam>
      <Flash f={f} at={T.logo} peak={0.35} dur={10} color={palette.violetTint} />
    </AbsoluteFill>
  );
};
