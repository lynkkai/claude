import React from "react";
import { noise2D } from "@remotion/noise";
import { INTER, IRIS, clamp, palette, tween } from "../lib";
import { Sphere } from "./Desktop";
import { SPOT } from "./Spotter";

/**
 * The rest of Spotter's surfaces this film needs: the bar while it listens
 * (Me is your microphone, Them is the Mac's sound, with the red dot on), the
 * asks it holds in memory, and the one switch that would keep the session.
 * Strings are the app's and the feature page's own.
 */

const glass: React.CSSProperties = {
  background: "linear-gradient(rgba(255,255,255,0.09), rgba(255,255,255,0.02) 38%, rgba(255,255,255,0)), rgba(0,0,0,0.72)",
  boxShadow: "inset 0 0 0 1px rgba(255,255,255,0.14), 0 20px 50px rgba(0,0,0,0.45)",
  backdropFilter: "blur(26px) saturate(1.6)",
};

/** One side's live level: 28 bars, driven by noise, `k` 0..1 for how loud. */
const Level: React.FC<{ f: number; seed: string; k: number; color: string }> = ({ f, seed, k, color }) => (
  <div style={{ display: "flex", alignItems: "center", gap: 3, height: 26 }}>
    {Array.from({ length: 28 }, (_, i) => {
      const n = (noise2D(seed, i * 0.6, f * 0.14) + 1) / 2;
      const h = 3 + n * 23 * k;
      return <div key={i} style={{ width: 4, height: h, borderRadius: 2, background: color, opacity: 0.35 + 0.65 * k * n }} />;
    })}
  </div>
);

/** The bar, listening: the two sides it hears, each with its own level. */
export const ListenBar: React.FC<{ f: number; dot: number; me: number; them: number }> = ({ f, dot, me, them }) => (
  <div style={{ position: "absolute", left: SPOT.x, top: SPOT.y, width: SPOT.w, display: "grid", gap: 8, fontFamily: INTER, color: "white", letterSpacing: 0 }}>
    <div style={{ ...glass, height: 52, borderRadius: 26, display: "flex", alignItems: "center", gap: 10, padding: "0 10px 0 14px" }}>
      <Sphere size={20} />
      <span style={{ fontSize: 13.5 }}>Sales ▾</span>
      <div style={{ flex: 1 }} />
      <div style={{ width: 8, height: 8, borderRadius: 4, background: palette.live, opacity: dot * (0.55 + 0.45 * Math.cos(f / 5)), boxShadow: `0 0 ${10 * dot}px ${palette.live}` }} />
      <div
        style={{
          height: 28,
          minWidth: 64,
          padding: "0 12px",
          borderRadius: 8,
          display: "grid",
          placeItems: "center",
          fontSize: 12.5,
          background: dot > 0.5 ? IRIS : "rgba(255,255,255,0.1)",
          fontWeight: dot > 0.5 ? 600 : 400,
        }}
      >
        Listen
      </div>
      <div style={{ height: 28, minWidth: 64, padding: "0 12px", borderRadius: 8, display: "grid", placeItems: "center", fontSize: 12.5, background: "white", color: "#111", fontWeight: 600 }}>Ask ⌘↩</div>
    </div>
    <div style={{ ...glass, borderRadius: 20, padding: "16px 18px", display: "grid", gap: 12 }}>
      {([
        ["Me", "your microphone", me, palette.lavender, "lvl-me"],
        ["Them", "this Mac's sound", them, "#8ab4f8", "lvl-them"],
      ] as const).map(([who, what, k, color, seed]) => (
        <div key={who} style={{ display: "flex", alignItems: "center", gap: 14 }}>
          <div style={{ width: 62 }}>
            <div style={{ fontSize: 16, fontWeight: 600, opacity: 0.5 + 0.5 * clamp(k * 2) }}>{who}</div>
            <div style={{ fontSize: 10.5, color: "rgba(255,255,255,0.45)" }}>{what}</div>
          </div>
          <Level f={f} seed={seed} k={k} color={color} />
        </div>
      ))}
    </div>
  </div>
);

/** What Spotter is holding from this session, until it is not. */
export const ASKS = ["How would the pilot work?", "What budget did they mention?", "Who owns the security review?"] as const;

export const AskStack: React.FC<{ f: number; from: number; w?: number }> = ({ f, from, w = 470 }) => (
  <div style={{ position: "absolute", left: SPOT.x + (SPOT.w - w) / 2, top: SPOT.y + 128, width: w, display: "grid", gap: 10, fontFamily: INTER, letterSpacing: 0 }}>
    {ASKS.map((t, i) => {
      const at = from + i * 7;
      const k = tween(f, at, at + 8);
      return (
        <div
          key={t}
          style={{
            ...glass,
            borderRadius: 14,
            padding: "13px 16px",
            color: "rgba(255,255,255,0.92)",
            fontSize: 17,
            display: "flex",
            gap: 10,
            alignItems: "center",
            opacity: k,
            transform: `translateY(${(1 - k) * 18}px)`,
          }}
        >
          <span style={{ fontSize: 13, color: "rgba(255,255,255,0.45)" }}>⌘↩</span>
          {t}
        </div>
      );
    })}
  </div>
);

/** The one switch that would keep anything: off, as it ships. */
export const KeepSwitch: React.FC<{ f: number; at: number }> = ({ f, at }) => {
  const k = tween(f, at, at + 10);
  if (k <= 0.01) return null;
  return (
    <div
      style={{
        ...glass,
        position: "absolute",
        left: SPOT.x + 40,
        top: SPOT.y + 150,
        width: SPOT.w - 80,
        borderRadius: 16,
        padding: "16px 18px",
        display: "flex",
        alignItems: "center",
        gap: 14,
        fontFamily: INTER,
        color: "white",
        letterSpacing: 0,
        opacity: k,
        transform: `translateY(${(1 - k) * 14}px) scale(${0.96 + 0.04 * k})`,
      }}
    >
      <div style={{ flex: 1 }}>
        <div style={{ fontSize: 17, fontWeight: 500 }}>Keep the session as a note</div>
        <div style={{ fontSize: 12.5, color: "rgba(255,255,255,0.5)", marginTop: 2 }}>Off. Asks are not saved.</div>
      </div>
      <div style={{ width: 46, height: 27, borderRadius: 14, background: "rgba(255,255,255,0.16)", padding: 3, boxSizing: "border-box" }}>
        <div style={{ width: 21, height: 21, borderRadius: 11, background: "white", opacity: 0.85 }} />
      </div>
    </div>
  );
};

/**
 * What the other people on the call see: the shared screen as a tile, with
 * Spotter's bar plainly in it. `children` is the screen, already scaled.
 */
export const ShareTile: React.FC<{ name: string; w: number; h: number; k: number; children: React.ReactNode }> = ({ name, w, h, k, children }) => (
  <div
    style={{
      width: w,
      height: h,
      borderRadius: 14,
      overflow: "hidden",
      position: "relative",
      background: "#17171a",
      boxShadow: `0 24px 60px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,${0.1 + 0.1 * k})`,
      transform: `scale(${0.82 + 0.18 * k})`,
      opacity: clamp(k * 1.6),
      fontFamily: INTER,
    }}
  >
    {children}
    <div style={{ position: "absolute", left: 10, bottom: 8, fontSize: 15, color: "rgba(255,255,255,0.85)", fontWeight: 500, textShadow: "0 2px 8px rgba(0,0,0,0.8)" }}>{name}</div>
  </div>
);
