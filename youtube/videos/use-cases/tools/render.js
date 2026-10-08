// Deterministic frames for the use-case videos: render(id, t, timing) sets every
// element of board `id` for time t (seconds). Same model as ask-lynkk-video:
//   data-s="n"   reveal when narration line n of the scene starts (out/timing.json)
//   data-d="x"   shift that by x seconds
//   data-out="n" hide again when line n starts (data-od shifts it)
//   data-type    type the element's text over data-dur seconds (dictation)
//   data-e="x"   reveal at x seconds (boards without narration)
const clamp = (v) => Math.min(1, Math.max(0, v));
const ease = (x) => 1 - Math.pow(1 - clamp(x), 3);
const p = (t, start, dur) => ease((t - start) / dur);
window.render = (id, t, timing) => {
  const sec = document.getElementById(id);
  const { starts, duration } = timing;
  const at = (i) => starts[Math.min(+i, starts.length - 1)];
  for (const el of sec.querySelectorAll("[data-s]")) {
    const t0 = at(el.dataset.s) + +(el.dataset.d || 0);
    if (el.dataset.type !== undefined) {
      el.dataset.full ??= el.textContent;
      const full = el.dataset.full;
      const k = clamp((t - t0) / +(el.dataset.dur || 3));
      el.textContent = full.slice(0, Math.round(full.length * k));
      el.classList.toggle("is-typing", k > 0 && k < 1);
      continue;
    }
    let k = p(t, t0 - 0.1, 0.6);
    if (el.dataset.out !== undefined) k *= 1 - p(t, at(el.dataset.out) + +(el.dataset.od || 0) - 0.25, 0.35);
    el.style.opacity = k;
    el.style.transform = `translateY(${(1 - k) * 22}px)`;
  }
  for (const el of sec.querySelectorAll("[data-e]")) {
    const k = p(t, +el.dataset.e, 0.8);
    el.style.opacity = k;
    el.style.transform = `translateY(${(1 - k) * 22}px)`;
  }
  const last = sec.hasAttribute("data-last");
  const body = sec.querySelector(".post-body");
  body.style.opacity = Math.min(p(t, 0, 0.3), last ? 1 : 1 - p(t, duration - 0.35, 0.35));
};
document.documentElement.dataset.ready = "1";
