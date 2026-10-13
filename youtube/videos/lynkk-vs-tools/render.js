// Deterministic frames for kit boards, from ask-lynkk-video/video.html.
// render(id, t, timing) sets every element of scene `id` for time t (seconds into the scene).
//   data-s="n"   reveal when narration line n starts; data-d shifts it in seconds
//   data-out="n" hide again when line n starts
//   data-e="sec" reveal at a fixed time
//   data-cap     shows the narration line being spoken (Shorts, for sound-off viewing)
const clamp = (v) => Math.min(1, Math.max(0, v));
const ease = (x) => 1 - Math.pow(1 - clamp(x), 3);
const p = (t, start, dur) => ease((t - start) / dur);
window.render = (id, t, timing) => {
  const sec = document.getElementById(id);
  const { starts, ends, lines, duration } = timing;
  const at = (i) => starts[Math.min(+i, starts.length - 1)];
  for (const el of sec.querySelectorAll("[data-s]")) {
    let k = p(t, at(el.dataset.s) + +(el.dataset.d || 0) - 0.1, 0.6);
    if (el.dataset.out !== undefined) k *= 1 - p(t, at(el.dataset.out) - 0.25, 0.35);
    el.style.opacity = k;
    el.style.transform = `translateY(${(1 - k) * 22}px)`;
  }
  for (const el of sec.querySelectorAll("[data-e]")) {
    const k = p(t, +el.dataset.e, 0.8);
    el.style.opacity = k;
    el.style.transform = `translateY(${(1 - k) * 22}px)`;
  }
  for (const el of sec.querySelectorAll("[data-cap]")) {
    let i = -1;
    for (let j = 0; j < starts.length; j++) if (t >= starts[j] - 0.1) i = j;
    const live = i >= 0 && t <= ends[i] + 0.3;
    if (live && el.dataset.line !== String(i)) { el.textContent = lines[i]; el.dataset.line = String(i); }
    el.style.opacity = live ? Math.min(p(t, starts[i] - 0.1, 0.25), 1 - p(t, ends[i] + 0.1, 0.2)) : 0;
  }
  const body = sec.querySelector(".post-body");
  body.style.opacity = id === "end" ? Math.min(1, p(t, 0, 0.3)) : Math.min(p(t, 0, 0.3), 1 - p(t, duration - 0.35, 0.35));
};
