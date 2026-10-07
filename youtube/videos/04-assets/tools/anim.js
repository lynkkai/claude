// Easing helpers for window.render(t). Animations only move opacity and
// transform, or toggle kit state classes (.is-off); styling stays the kit's.
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const ease = (x) => 1 - Math.pow(1 - clamp(x), 3);
const p = (t, start, dur) => ease((t - start) / dur);
const rise = (el, k, dy = 24) => { el.style.opacity = k; el.style.transform = `translateY(${(1 - k) * dy}px)`; };
