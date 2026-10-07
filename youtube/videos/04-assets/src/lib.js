// Shared helpers: every animated page exposes window.render(t) for deterministic frame capture.
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const easeOut = (x) => 1 - Math.pow(1 - clamp(x), 3);
const easeInOut = (x) => { x = clamp(x); return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
// progress of t inside [start, start+dur], eased
const p = (t, start, dur, ease = easeOut) => ease((t - start) / dur);
// fade in at a, fade out at b (each over d seconds)
const inOut = (t, a, b, d = 0.4) => Math.min(p(t, a, d), 1 - p(t, b, d, easeInOut));
const $ = (s) => document.querySelector(s);
const $$ = (s) => [...document.querySelectorAll(s)];
