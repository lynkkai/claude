/* Timeline player for Lynkk videos built from post-kit slides.
   Load after kit/post.js and build/timeline.js, with the page's config first:

     <script>window.VIDEO = { cursor: { sceneId: [ {at, x, y} | {at, sel, click} ... ] } };</script>
     <script src="../pipeline/player.js"></script>

   Every <section class="post"> whose id matches a scene in script.json is one
   scene. Elements inside are animated from attributes:
     data-at="i2+0.4"      fade and rise in when line i2 starts, +0.4 s
     data-at="i2$-0.3"     ...relative to the END of line i2
     data-at="start+0.5"   ...relative to the scene start ("end" works too)
     data-out="b3$"        fade out at that time
     data-type="b2+1|2.2"  type the element's text over 2.2 s
     data-on="a2+1"        add class "on" (checkboxes)
     data-clock="b3$|0"    a mm:ss clock running from that time
     data-press="a1+2"     a button press (and a click sound)
     data-level="0"        an animated audio level (.m-level)
     data-sfx="pop"        a soft pop when the element appears
   Optional page elements: #narr (narrator levels), #cursor + #ripple,
   #veil (fade to the band at the end), #cap (burned-in captions; a section
   with data-nocap hides them).
   Exposes renderFrame(t), getSfx() and renderThumb() (shows #thumb). */
(() => {
  const TL = window.TIMELINE;
  const CFG = window.VIDEO || {};
  const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  const lerp = (a, b, k) => a + (b - a) * k;
  const easeOut = x => 1 - Math.pow(1 - x, 3);
  const easeInOut = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
  const P = (t, a, d = .55, e = easeOut) => e(clamp((t - a) / d));
  const $ = id => document.getElementById(id);

  const LINE = {}, SCN = {};
  TL.scenes.forEach(s => { SCN[s.id] = s; s.lines.forEach(l => { LINE[l.id] = l; }); });

  function T(expr, sid) {
    const m = expr.trim().match(/^([A-Za-z0-9]+)(\$)?([+-][\d.]+)?$/);
    if (!m) throw new Error('bad time: ' + expr);
    let base;
    if (m[1] === 'start') base = SCN[sid].start;
    else if (m[1] === 'end') base = SCN[sid].end;
    else { const l = LINE[m[1]]; if (!l) throw new Error('unknown cue: ' + m[1]); base = m[2] ? l.end : l.start; }
    return base + (m[3] ? parseFloat(m[3]) : 0);
  }

  const SCENES = TL.scenes.map((s, i) => {
    const el = $(s.id);
    if (!el) throw new Error('missing section #' + s.id);
    const items = [...el.querySelectorAll('[data-at],[data-out],[data-type],[data-on],[data-clock],[data-press],[data-level]')].map(n => {
      const d = n.dataset, it = { n };
      if (d.at) it.at = T(d.at, s.id);
      if (d.out) it.out = T(d.out, s.id);
      if (d.on) it.on = T(d.on, s.id);
      if (d.press) it.press = T(d.press, s.id);
      if (d.type) { const [a, dur] = d.type.split('|'); it.type = T(a, s.id); it.typeDur = parseFloat(dur); it.full = n.textContent; }
      if (d.clock) { const [a, from] = d.clock.split('|'); it.clock = T(a, s.id); it.clockFrom = parseFloat(from); }
      if (d.level !== undefined) it.level = parseInt(d.level, 10);
      return it;
    });
    return { ...s, el, items, idx: i, nocap: el.hasAttribute('data-nocap') };
  });

  const CURSOR = CFG.cursor || {};
  for (const [sid, keys] of Object.entries(CURSOR)) keys.forEach(k => { k.t = T(k.at, sid); k.sid = sid; });

  // Split a line into the fewest readable chunks: similar lengths, breaks after
  // punctuation where possible, never ending on a small word ("a", "the", "to").
  const SMALL = new Set(['a', 'an', 'the', 'to', 'from', 'in', 'on', 'of', 'and', 'or', 'with', 'at', 'for', 'your', 'my', 'press', 'click']);
  function splitCaption(text, max) {
    const words = text.split(/\s+/);
    const best = { cost: Infinity, cuts: null };
    const minN = Math.max(1, Math.ceil(text.length / max));
    for (let n = minN; n <= Math.min(minN + 1, words.length); n++) {
      const target = text.length / n;
      const walk = (start, left, cuts) => {
        if (left === 1) {
          const all = [...cuts, words.length];
          let cost = n * 40, from = 0;
          for (const end of all) {
            const chunk = words.slice(from, end).join(' ');
            if (chunk.length > max + 6) return;
            cost += Math.pow(chunk.length - target, 2) / target;
            const last = words[end - 1].toLowerCase().replace(/[^a-z']/g, '');
            if (end < words.length) {
              if (!/[.,:;?]$/.test(words[end - 1])) cost += 6;
              if (SMALL.has(last)) cost += 60;
            }
            from = end;
          }
          if (cost < best.cost) { best.cost = cost; best.cuts = all; }
          return;
        }
        for (let c = start + 1; c < words.length; c++) walk(c, left - 1, [...cuts, c]);
      };
      walk(0, n, []);
    }
    const out = [];
    let from = 0;
    for (const end of best.cuts || [words.length]) { out.push(words.slice(from, end).join(' ')); from = end; }
    return out;
  }

  // Captions: each line split into short chunks, timed by length.
  const CAPS = [];
  const capEl = $('cap');
  if (capEl) {
    const max = CFG.captionChars || 34;
    TL.scenes.forEach(s => s.lines.forEach(l => {
      const chunks = splitCaption(l.text, max);
      const total = chunks.reduce((n, c) => n + c.length, 0);
      let t = l.start;
      chunks.forEach(c => {
        const d = (l.end - l.start) * c.length / total;
        CAPS.push({ text: c, start: t, end: t + d, sid: s.id });
        t += d;
      });
    }));
  }

  function pointOf(k) {
    if (k.sel) {
      const r = document.querySelector(`#${k.sid} ${k.sel}`).getBoundingClientRect();
      return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
    }
    return { x: k.x, y: k.y };
  }
  function cursorAt(t) {
    for (const keys of Object.values(CURSOR)) {
      const first = keys[0], last = keys[keys.length - 1];
      if (t < first.t - .35 || t > last.t + .7) continue;
      let p = pointOf(first);
      if (t >= last.t) p = pointOf(last);
      else for (let i = 0; i < keys.length - 1; i++) {
        const a = keys[i], b = keys[i + 1];
        if (t >= a.t && t < b.t) { const k = easeInOut((t - a.t) / (b.t - a.t)); const pa = pointOf(a), pb = pointOf(b); p = { x: lerp(pa.x, pb.x, k), y: lerp(pa.y, pb.y, k) }; break; }
      }
      const op = Math.min(clamp((t - (first.t - .35)) / .35), 1 - clamp((t - (last.t + .3)) / .4));
      let press = 0, ripple = null;
      keys.forEach(k => { if (!k.click) return; const d = t - k.t; if (d > -.1 && d < .15) press = 1 - Math.abs(d) / .15; if (d >= 0 && d < .5) ripple = { ...pointOf(k), k: d / .5 }; });
      return { ...p, op, press, ripple };
    }
    return null;
  }

  const mmss = s => { s = Math.max(0, Math.floor(s)); return String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'); };
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');

  function renderItem(it, t) {
    const n = it.n;
    let op = 1, ty = 0, sc = 1;
    if (it.at !== undefined) { const k = P(t, it.at); op *= k; ty = (1 - k) * 14; }
    if (it.out !== undefined) op *= 1 - P(t, it.out, .35);
    if (it.press !== undefined) { const d = Math.abs(t - it.press); if (d < .15) sc = 1 - .06 * (1 - d / .15); }
    if (it.at !== undefined || it.out !== undefined) { n.style.opacity = op; n.style.visibility = op < .002 ? 'hidden' : ''; }
    n.style.transform = (ty > .01 || sc !== 1) ? `translateY(${ty}px) scale(${sc})` : '';
    if (it.on !== undefined) n.classList.toggle('on', t >= it.on);
    if (it.type !== undefined) {
      const k = clamp((t - it.type) / it.typeDur);
      const c = Math.round(it.full.length * k);
      n.innerHTML = esc(it.full.slice(0, c)) + (k > 0 && k < 1 ? '|' : '');
    }
    if (it.clock !== undefined) n.textContent = mmss(it.clockFrom + (t - it.clock));
    if (it.level !== undefined) {
      const v = 22 + 60 * Math.abs(Math.sin(t * (6.3 + it.level * 2.1) + it.level)) * (.5 + .5 * Math.abs(Math.sin(t * 1.7 + it.level * 3)));
      n.style.setProperty('--v', v.toFixed(1) + '%');
    }
  }

  function renderFrame(t) {
    document.documentElement.classList.add('video');
    let cur = 0;
    SCENES.forEach((s, i) => { if (t >= s.start - .3) cur = i; });
    SCENES.forEach((s, i) => {
      const next = SCENES[i + 1];
      const visible = t >= s.start - .3 && (!next || t < next.start + .35) && i <= cur;
      if (!visible) { s.el.style.display = 'none'; return; }
      s.el.style.display = '';
      s.el.style.zIndex = i + 1;
      s.el.style.opacity = i === 0 ? 1 : P(t, s.start - .3, .5, easeInOut);
      s.items.forEach(it => renderItem(it, t));
    });

    const fi = Math.min(TL.mouth.length - 1, Math.round(t * TL.fps));
    const amp = TL.mouth[fi] || 0;
    const narr = $('narr');
    if (narr) {
      narr.querySelectorAll('.bars b').forEach((b, i) => {
        b.style.height = (4 + 18 * amp * (.45 + .55 * Math.abs(Math.sin(t * 12 + i * 1.9)))) + 'px';
      });
      narr.style.opacity = P(t, .3, .6);
    }

    if (capEl) {
      const scene = SCENES[cur];
      const c = CAPS.find((c, i) => t >= c.start && t < (CAPS[i + 1] && CAPS[i + 1].sid === c.sid ? CAPS[i + 1].start : c.end + .35));
      if (c && !scene.nocap && c.sid === scene.id) {
        if (capEl.dataset.text !== c.text) { capEl.textContent = c.text; capEl.dataset.text = c.text; }
        const k = P(t, c.start, .15);
        capEl.style.opacity = k;
        capEl.style.transform = `translate(-50%, ${(1 - k) * 8}px)`;
      } else capEl.style.opacity = 0;
    }

    const c = cursorAt(t), cEl = $('cursor'), rEl = $('ripple');
    if (cEl) {
      if (c) {
        cEl.style.visibility = 'visible'; cEl.style.opacity = c.op;
        cEl.style.transform = `translate(${c.x - 5}px, ${c.y - 3}px) scale(${1 - c.press * .15})`;
        if (c.ripple) { rEl.style.visibility = 'visible'; rEl.style.opacity = (1 - c.ripple.k) * .9; rEl.style.transform = `translate(${c.ripple.x}px, ${c.ripple.y}px) scale(${.3 + c.ripple.k})`; }
        else rEl.style.visibility = 'hidden';
      } else { cEl.style.visibility = 'hidden'; rEl.style.visibility = 'hidden'; }
    }

    if ($('veil')) $('veil').style.opacity = P(t, TL.duration - 1.2, 1.2, easeInOut);
  }

  function getSfx() {
    const out = [];
    SCENES.forEach(s => s.items.forEach(it => {
      if (it.press !== undefined) out.push({ t: it.press, type: 'click' });
      if (it.on !== undefined) out.push({ t: it.on, type: 'tick' });
      if (it.n.dataset.sfx === 'pop' && it.at !== undefined) out.push({ t: it.at, type: 'pop' });
    }));
    return out.sort((a, b) => a.t - b.t);
  }

  function renderThumb() {
    document.documentElement.classList.add('video');
    SCENES.forEach(s => { s.el.style.display = 'none'; });
    const th = $('thumb');
    th.style.display = 'grid'; th.style.zIndex = 50;
    ['narr', 'cursor', 'ripple', 'veil', 'cap'].forEach(id => { if ($(id)) $(id).style.display = 'none'; });
  }

  window.renderFrame = renderFrame;
  window.getSfx = getSfx;
  window.renderThumb = renderThumb;
  const qs = new URLSearchParams(location.search);
  if (qs.has('t')) renderFrame(parseFloat(qs.get('t')));
})();
