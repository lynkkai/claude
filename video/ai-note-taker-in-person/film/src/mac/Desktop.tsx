import React from "react";
import { Img, staticFile } from "remotion";
import { INTER, IRIS, MARK_PATHS, MARK_VIEWBOX, SCREEN, palette } from "../lib";

/**
 * The Mac screen, in Mac points (1512 x 982): a photo plate as wallpaper, the
 * menu bar with the Lynkk sphere in it, the notch. Windows go in `children`.
 * Drawn after the mockups in design-lab/explorations/desktop-v2-* and the
 * Mac brief: generic app windows, no copied app UI, no Apple logo.
 */

export const MENU_H = 32;
export const NOTCH = { x: SCREEN.w / 2 - 92, w: 184, h: 32 } as const;
/** Where the Lynkk sphere sits in the menu bar. */
export const MENU_SPHERE = { x: 1262, y: MENU_H / 2 } as const;

export const Sphere: React.FC<{ size: number; color?: string; stripe?: (j: number) => number; style?: React.CSSProperties }> = ({
  size,
  color = palette.white,
  stripe,
  style,
}) => (
  <svg viewBox={MARK_VIEWBOX} width={size} height={size} style={{ display: "block", overflow: "visible", ...style }}>
    {MARK_PATHS.map((d, j) => (
      <path key={j} d={d} fill={color} opacity={stripe ? stripe(j) : 1} />
    ))}
  </svg>
);

const Glyph: React.FC<{ d: string; w?: number }> = ({ d, w = 16 }) => (
  <svg width={w} height={w} viewBox="0 0 16 16" style={{ display: "block" }}>
    <path d={d} fill="none" stroke="white" strokeWidth={1.5} strokeLinecap="round" strokeLinejoin="round" />
  </svg>
);

/** The menu bar: the front app's menus left, status icons right, the notch in the middle. */
export const MenuBar: React.FC<{ app?: string; sphereLit?: number; sphereRec?: number }> = ({ app = "Finder", sphereLit = 1, sphereRec = 0 }) => (
  <div
    style={{
      position: "absolute",
      left: 0,
      top: 0,
      width: SCREEN.w,
      height: MENU_H,
      background: "rgba(16,16,22,0.38)",
      backdropFilter: "blur(30px)",
      display: "flex",
      alignItems: "center",
      fontFamily: INTER,
      fontSize: 13.5,
      color: "white",
      letterSpacing: 0,
    }}
  >
    <div style={{ display: "flex", gap: 20, paddingLeft: 22, alignItems: "center" }}>
      <span style={{ fontWeight: 700 }}>{app}</span>
      {["File", "Edit", "View", "Window", "Help"].map((m) => (
        <span key={m} style={{ fontWeight: 500, opacity: 0.92 }}>
          {m}
        </span>
      ))}
    </div>
    <div style={{ position: "absolute", right: 18, display: "flex", gap: 18, alignItems: "center", height: MENU_H }}>
      <div style={{ position: "relative", width: 18, height: 18 }}>
        <div
          style={{
            position: "absolute",
            inset: -10,
            borderRadius: "50%",
            background: `radial-gradient(closest-side, ${IRIS}cc, ${IRIS}00)`,
            opacity: sphereLit > 0 ? (1 - Math.abs(sphereLit - 0.5) * 2) * 0.9 + sphereRec * 0.6 : 0,
          }}
        />
        <Sphere size={18} color="white" style={{ position: "relative", opacity: 0.35 + 0.65 * Math.min(1, sphereLit) }} />
        {sphereRec > 0 ? (
          <div style={{ position: "absolute", right: -3, top: -2, width: 7, height: 7, borderRadius: 4, background: palette.live, opacity: sphereRec }} />
        ) : null}
      </div>
      <Glyph d="M2 6.5a9 9 0 0 1 12 0M4.4 9a5.5 5.5 0 0 1 7.2 0M7 11.5a1.6 1.6 0 0 1 2 0" />
      <svg width={26} height={13} viewBox="0 0 26 13">
        <rect x={0.75} y={0.75} width={21} height={11.5} rx={3.2} fill="none" stroke="white" strokeOpacity={0.55} strokeWidth={1.2} />
        <rect x={2.5} y={2.5} width={15} height={8} rx={1.8} fill="white" />
        <rect x={23} y={4.2} width={2} height={4.6} rx={1} fill="white" fillOpacity={0.55} />
      </svg>
      <Glyph d="M3 5h10M3 11h10M5 3v4M11 9v4" />
      <span style={{ fontWeight: 500 }}>Wed 10:42</span>
    </div>
  </div>
);

/** The notch: pure black, rounded at the bottom. */
export const Notch: React.FC<{ w?: number; h?: number }> = ({ w = NOTCH.w, h = NOTCH.h }) => (
  <div
    style={{
      position: "absolute",
      left: SCREEN.w / 2 - w / 2,
      top: 0,
      width: w,
      height: h,
      background: "#000",
      borderRadius: `0 0 ${Math.min(14, h / 2)}px ${Math.min(14, h / 2)}px`,
    }}
  />
);

export type Plate = "dusk" | "sky" | "meadow" | "night" | "ember" | "field";

/** The whole screen: wallpaper, windows, menu bar, notch, in that order. */
export const Desktop: React.FC<{
  plate?: Plate;
  app?: string;
  sphereLit?: number;
  sphereRec?: number;
  dim?: number;
  children?: React.ReactNode;
  over?: React.ReactNode;
  radius?: number;
}> = ({ plate = "meadow", app, sphereLit, sphereRec, dim = 0, children, over, radius = 0 }) => (
  <div style={{ position: "absolute", left: 0, top: 0, width: SCREEN.w, height: SCREEN.h, overflow: "hidden", borderRadius: radius, background: "#111" }}>
    <Img src={staticFile(`plate-${plate}.jpg`)} style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "cover" }} />
    {dim > 0 ? <div style={{ position: "absolute", inset: 0, background: "#000", opacity: dim }} /> : null}
    {children}
    <MenuBar app={app} sphereLit={sphereLit} sphereRec={sphereRec} />
    <Notch />
    {over}
  </div>
);

/** A Liquid Glass-ish window frame with traffic lights and a centred title. */
export const Window: React.FC<{
  x: number;
  y: number;
  w: number;
  h: number;
  title?: string;
  dark?: boolean;
  style?: React.CSSProperties;
  children?: React.ReactNode;
  barH?: number;
}> = ({ x, y, w, h, title, dark = false, style, children, barH = 38 }) => (
  <div
    style={{
      position: "absolute",
      left: x,
      top: y,
      width: w,
      height: h,
      borderRadius: 16,
      overflow: "hidden",
      background: dark ? "#1b1b1d" : "#fbfbfc",
      boxShadow: "0 30px 70px rgba(0,0,0,0.45), 0 0 0 0.5px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255,255,255,0.12)",
      fontFamily: INTER,
      letterSpacing: 0,
      ...style,
    }}
  >
    <div
      style={{
        height: barH,
        display: "flex",
        alignItems: "center",
        padding: "0 14px",
        background: dark ? "#232326" : "#f1f1f3",
        borderBottom: dark ? "1px solid rgba(255,255,255,0.06)" : "1px solid rgba(0,0,0,0.07)",
        position: "relative",
      }}
    >
      <div style={{ display: "flex", gap: 8 }}>
        {["#ff5f57", "#febc2e", "#28c840"].map((c) => (
          <div key={c} style={{ width: 12, height: 12, borderRadius: 6, background: c }} />
        ))}
      </div>
      {title ? (
        <div style={{ position: "absolute", left: 0, right: 0, textAlign: "center", fontSize: 13.5, fontWeight: 600, color: dark ? "rgba(255,255,255,0.75)" : "rgba(0,0,0,0.7)" }}>
          {title}
        </div>
      ) : null}
    </div>
    <div style={{ position: "absolute", left: 0, right: 0, top: barH, bottom: 0 }}>{children}</div>
  </div>
);

/** A small app tile for the island and the dock-like rows: a colour and a letter, never a real logo. */
export const AppTile: React.FC<{ name: string; size?: number }> = ({ name, size = 22 }) => {
  const look: Record<string, [string, string]> = {
    Slack: ["#4a154b", "#"],
    Mail: ["#2f7cf6", "@"],
    Notion: ["#ffffff", "N"],
    Chrome: ["#e8eaed", "◎"],
    Zoom: ["#2d8cff", "Z"],
  };
  const [bg, ch] = look[name] ?? ["#444", name[0]];
  const dark = bg === "#ffffff" || bg === "#e8eaed";
  return (
    <div
      style={{
        width: size,
        height: size,
        borderRadius: size * 0.24,
        background: bg,
        display: "grid",
        placeItems: "center",
        color: dark ? "#111" : "white",
        fontFamily: INTER,
        fontWeight: 700,
        fontSize: size * 0.58,
        lineHeight: 1,
        boxShadow: "inset 0 0 0 1px rgba(0,0,0,0.15)",
      }}
    >
      {ch}
    </div>
  );
};

/** The display's black bezel around the screen, seen when the camera is pulled back. */
export const Bezel: React.FC<{ pad?: number }> = ({ pad = 22 }) => (
  <div
    style={{
      position: "absolute",
      left: -pad,
      top: -pad,
      width: SCREEN.w + pad * 2,
      height: SCREEN.h + pad * 2,
      borderRadius: 30 + pad,
      background: "#08080a",
      boxShadow: "0 60px 140px rgba(0,0,0,0.6), inset 0 0 0 1.5px rgba(255,255,255,0.10)",
    }}
  />
);
