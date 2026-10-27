// Every frame is a pure function of time: window.render(t).
const T = window.TIMING;
const $ = id => document.getElementById(id);
const clamp = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
const lerp = (a, b, k) => a + (b - a) * k;
const E = {
  out: x => 1 - Math.pow(1 - x, 4),
  out3: x => 1 - Math.pow(1 - x, 3),
  back: x => { const c1 = 1.5, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); },
  inout: x => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2),
  in: x => x * x * x,
  lin: x => x,
};
const P = (t, s, d, e = E.out) => e(clamp((t - s) / d));
const wt = (line, i) => T.lines[line].start + T.lines[line].words[i].s;
function rnd(seed) { let a = seed >>> 0; return () => { a |= 0; a = (a + 0x6d2b79f5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }

function st(el, o) {
  const s = el.style;
  if (o.o !== undefined) s.opacity = o.o;
  s.transform = `translate(${o.x || 0}px,${o.y || 0}px) scale(${o.s ?? 1}) rotate(${o.r || 0}deg)`;
  s.filter = o.b > 0.05 ? `blur(${o.b}px)` : 'none';
}
// rise-in / fall-out helper: k in [0,1] in, q in [0,1] out
function inout(el, k, q = 0, { dy = 36, blur = 10, s0 = 1, dyOut = -24 } = {}) {
  st(el, { o: k * (1 - q), y: (1 - k) * dy + q * dyOut, s: lerp(s0, 1, k), b: (1 - k) * blur + q * 8 });
}

// split text into word spans, keeping inline wrappers
function splitWords(el) {
  const out = [];
  const walk = node => {
    [...node.childNodes].forEach(ch => {
      if (ch.nodeType === 3) {
        const parts = ch.textContent.split(/([ \n\t]+)/);
        const frag = document.createDocumentFragment();
        parts.forEach(p => {
          if (!p) return;
          if (/^[ \n\t]+$/.test(p)) { frag.appendChild(document.createTextNode(' ')); return; }
          const sp = document.createElement('span'); sp.className = 'wd'; sp.textContent = p.replace(/ /g, ' ');
          frag.appendChild(sp); out.push(sp);
        });
        node.replaceChild(frag, ch);
      } else if (ch.nodeType === 1) walk(ch);
    });
  };
  walk(el);
  return out;
}
function words(ws, times, t, dur = 0.45, dy = 34) {
  ws.forEach((w, i) => { const k = P(t, times[Math.min(i, times.length - 1)], dur); st(w, { o: k, y: (1 - k) * dy, b: (1 - k) * 8 }); });
}
const stagger = (t0, n, gap) => Array.from({ length: n }, (_, i) => t0 + i * gap);
const sceneOn = (id, t) => {
  const [a, b] = T.scenes[id]; const on = t >= a - 0.001 && t <= b + 0.001; const el = $(id);
  el.style.display = on ? 'block' : 'none';
  if (on) el.style.transform = `scale(${1 + 0.03 * clamp((t - a) / (b - a))})`; // slow push-in per scene
  return on;
};
const mmss = s => `${String(Math.floor(s / 60)).padStart(2, '0')}:${String(Math.floor(s % 60)).padStart(2, '0')}`;

// ---------------------------------------------------------------- init
let H1A, H1B, STOP, S2L, S3H, S4H, S5Q, S6Q, S7H, O1, O2, FV5, FV3, KEYS = [], GRAPH, HELLO = [];
function init() {
  document.querySelectorAll('.logo').forEach(e => (e.innerHTML = window.LOGO));
  H1A = splitWords($('h1a')); H1B = splitWords($('h1b'));
  STOP = splitWords($('stop')); S2L = splitWords($('s2line'));
  S3H = splitWords($('s3h')); S4H = splitWords($('s4h'));
  S5Q = splitWords($('s5q')); S6Q = splitWords($('s6q')); S7H = splitWords($('s7h'));
  O1 = splitWords($('o1')); O2 = splitWords($('o2'));
  FV5 = splitWords($('flip').children[0]); FV3 = splitWords($('flip').children[1]);

  // underline under "sales conversation"
  const ul = document.createElement('span'); ul.className = 'uline'; ul.id = 'uline';
  document.querySelector('#s2line .hl').appendChild(ul);

  // buyer voice bars + waves
  const bars = $('buyerbars'); for (let i = 0; i < 9; i++) bars.appendChild(document.createElement('i'));
  ['wave2', 'wave4'].forEach(id => { for (let i = 0; i < 34; i++) $(id).appendChild(document.createElement('i')); });

  // keycaps for every 3rd keystroke
  const r = rnd(7), kc = $('keycaps');
  T.keys.forEach((kt, i) => {
    if (i % 3) return;
    let ch = T.pad[i]; if (!ch || /\s/.test(ch)) ch = '⌫';
    const d = document.createElement('div'); d.className = 'key'; d.textContent = ch.toUpperCase();
    const k = { el: d, t: kt, x: 1060 + r() * 700, y: 900 + r() * 80, dx: (r() - 0.5) * 160, dy: -(180 + r() * 220), r0: (r() - 0.5) * 50, r1: (r() - 0.5) * 70 };
    kc.appendChild(d); KEYS.push(k);
  });

  // greetings
  const hellos = ['Hello', 'नमस्ते', 'Hola', 'Bonjour', 'こんにちは', 'Hallo', '안녕하세요', 'Olá', 'مرحبا', 'Ciao'];
  hellos.forEach(h => { const s = document.createElement('span'); s.textContent = h; $('hello').appendChild(s); HELLO.push(s); });

  buildGraph(); buildWires(); buildGrain();
  // answer text
  $('aska').innerHTML = 'A <span class="mark">15-person pilot</span><span class="cite">1</span>, and the <span class="mark">security overview</span> before the proposal<span class="cite">2</span>. Jamie sends it by Friday<span class="cite">3</span>.';
  ASK = splitWords($('aska'));
  ASKC = [...$('aska').querySelectorAll('.cite')];
  SUMTXT = 'Corvane wants to give its sales team a single source of customer context. Priya confirmed budget and a phased rollout, pending IT approval.';
}
let ASK, ASKC, SUMTXT;

// knowledge-graph constellation behind the logo reveal
function buildGraph() {
  const svg = $('graph'), NS = 'http://www.w3.org/2000/svg';
  const labels = ['Discovery · Oct 06', '$30K → $50K', 'IT review', '15-person pilot', 'Security overview', 'Priya Shah', 'Demo · Oct 13', 'Follow-up sent', 'Commercials · Oct 20', 'Jira · HW-218'];
  const cx = 960, cy = 380, r = rnd(3);
  GRAPH = labels.map((lb, i) => {
    const a = (i / labels.length) * Math.PI * 2 + 0.3;
    const R = 470 + r() * 130;
    const x = clamp(cx + Math.cos(a) * R * 1.35, 110, 1600), y = clamp(cy + Math.sin(a) * R * 0.78, 60, 1010);
    const line = document.createElementNS(NS, 'line');
    line.setAttribute('x1', cx); line.setAttribute('y1', cy); line.setAttribute('x2', x); line.setAttribute('y2', y);
    line.setAttribute('stroke', 'rgba(190,180,251,.22)'); line.setAttribute('stroke-width', '1.5');
    const len = Math.hypot(x - cx, y - cy); line.setAttribute('stroke-dasharray', len); line.setAttribute('stroke-dashoffset', len);
    const g = document.createElementNS(NS, 'g');
    const c = document.createElementNS(NS, 'circle'); c.setAttribute('r', 7); c.setAttribute('fill', i % 3 ? '#beb4fb' : '#f57b3a');
    const tx = document.createElementNS(NS, 'text'); tx.textContent = lb; tx.setAttribute('x', 16); tx.setAttribute('y', 6);
    tx.setAttribute('fill', 'rgba(255,255,255,.42)'); tx.setAttribute('font-family', 'JetBrains Mono'); tx.setAttribute('font-size', '19');
    g.appendChild(c); g.appendChild(tx);
    svg.appendChild(line); svg.appendChild(g);
    return { line, g, len, x, y, ph: r() * 6.28 };
  });
}

// wires for hand-off scene
let WIRES = [];
function buildWires() {
  const svg = $('wires'), NS = 'http://www.w3.org/2000/svg';
  const x0 = 730, ys = [560, 620, 680], dests = [[1180, 420], [1180, 630], [1180, 830]];
  WIRES = dests.map(([x1, y1], i) => {
    const y0 = ys[i];
    const d = `M${x0},${y0} C${x0 + 230},${y0} ${x1 - 230},${y1} ${x1},${y1}`;
    const p = document.createElementNS(NS, 'path'); p.setAttribute('d', d); p.setAttribute('fill', 'none');
    p.setAttribute('stroke', ['#4c8dff', '#beb4fb', '#f57b3a'][i]); p.setAttribute('stroke-width', '3'); p.setAttribute('stroke-linecap', 'round');
    svg.appendChild(p);
    const len = p.getTotalLength(); p.setAttribute('stroke-dasharray', len); p.setAttribute('stroke-dashoffset', len);
    const dot = document.createElementNS(NS, 'circle'); dot.setAttribute('r', 9); dot.setAttribute('fill', '#fff');
    dot.style.filter = 'drop-shadow(0 0 10px rgba(255,255,255,.9))'; svg.appendChild(dot);
    return { p, len, dot };
  });
}

function buildGrain() {
  const c = document.createElement('canvas'); c.width = c.height = 256; const g = c.getContext('2d');
  const im = g.createImageData(256, 256), r = rnd(99);
  for (let i = 0; i < im.data.length; i += 4) { const v = r() * 255; im.data[i] = im.data[i + 1] = im.data[i + 2] = v; im.data[i + 3] = 255; }
  g.putImageData(im, 0, 0); $('grain').style.backgroundImage = `url(${c.toDataURL()})`;
}

// ---------------------------------------------------------------- scenes
function bg(t) {
  const g1 = document.querySelector('.g1'), g2 = document.querySelector('.g2');
  // warm glow drifts; brighter after the reveal
  const warm = t < 4 ? 0.10 : 0.22;
  g1.style.opacity = warm; g2.style.opacity = t < 4 ? 0.06 : 0.16;
  g1.style.transform = `translate(${-200 + Math.sin(t * 0.21) * 160 + t * 18}px,${300 + Math.cos(t * 0.17) * 120}px)`;
  g2.style.transform = `translate(${1300 - t * 10 + Math.cos(t * 0.19) * 160}px,${-200 + Math.sin(t * 0.23) * 120}px)`;
  const f = Math.floor(t * T.fps);
  $('grain').style.backgroundPosition = `${(f * 73) % 256}px ${(f * 151) % 256}px`;
}

function s1(t) {
  if (!sceneOn('s1', t)) return;
  const L = T.lines.l1, w = i => L.start + L.words[i].s;
  const out = P(t, 3.95, 0.3, E.inout), wout = P(t, 4.0, 0.4, E.inout);
  // headline words synced to the voice
  words(H1A, [w(0), w(1), w(2), w(3), w(4), w(5)], t);
  words(H1B, [w(6), w(7), w(8), w(9), w(10), w(11), w(12)], t);
  st($('h1a'), { o: 1 - out, y: -out * 40, b: out * 10 });
  st($('h1b'), { o: 1 - out, y: -out * 40, b: out * 10 });
  // "not listening" pulse
  const red = document.querySelector('#h1b .red'); red.style.textShadow = `0 0 ${30 * P(t, w(11), .4) * (1 - P(t, w(12) + .5, .6))}px rgba(255,59,48,.8)`;

  const win = $('callwin');
  const kin = P(t, -0.25, 0.6);
  st(win, { o: kin * (1 - wout), x: (1 - kin) * 60 + wout * 140, s: 1 - wout * 0.06, b: wout * 14 });
  $('calltime').textContent = mmss(12 * 60 + 4 + t);
  // buyer speaking until she notices
  const talk = 1 - P(t, 2.0, 0.4);
  [...$('buyerbars').children].forEach((b, i) => {
    const a = 0.5 + 0.5 * Math.sin(t * 13 + i * 1.7) * Math.sin(t * 5.3 + i);
    b.style.height = `${8 + talk * 30 * Math.abs(a)}px`; b.style.opacity = 0.4 + talk * 0.6;
  });
  $('buyerring').style.opacity = talk;
  const bub = P(t, 2.55, 0.45, E.back);
  st($('bubble'), { o: P(t, 2.55, 0.2), y: (1 - bub) * 20, s: lerp(0.7, 1, bub) });
  // typing pad
  let n = T.keys.filter(k => k <= t).length;
  const blink = Math.floor(t * 3) % 2 === 0 || t < 3.9;
  $('pad').innerHTML = T.pad.slice(0, n).replace(/</g, '&lt;') + `<span class="cur" style="opacity:${blink ? 1 : 0}"></span>`;
  const tp = $('typingpill'); tp.style.display = 'flex';
  tp.style.opacity = t < 4.1 ? (0.6 + 0.4 * Math.sin(t * 10)) : 0;
  // keycaps
  KEYS.forEach(k => {
    const a = t - k.t;
    if (a < 0 || a > 1.4) { k.el.style.opacity = 0; return; }
    const pop = E.back(clamp(a / 0.22)); const fly = E.out3(clamp(a / 1.3));
    let x = k.x + k.dx * fly, y = k.y + k.dy * fly, r = lerp(k.r0, k.r1, fly), o = clamp(1 - (a - 0.7) / 0.6);
    st(k.el, { o, x, y, s: pop, r });
    k.el.style.left = '0px'; k.el.style.top = '0px';
  });
}

function s2(t) {
  if (!sceneOn('s2', t)) return;
  const tl = wt('l2', 3) - 0.08; // the brand name
  // "So stop typing."
  words(STOP, [wt('l2', 0), wt('l2', 1), wt('l2', 2)], t, 0.35);
  const so = P(t, tl - 0.3, 0.3, E.in);
  st($('stop'), { o: 1 - so, s: 1 + so * 0.08, b: so * 16 });
  // logo + wordmark
  const lk = P(t, tl, 0.7, E.back), lo = P(t, tl, 0.25);
  const ex = P(t, 7.7, 0.3, E.in);
  st($('biglogo'), { o: lo, s: lerp(0.3, 1, lk), r: lerp(-140, 0, P(t, tl, 0.9)) });
  const wm = P(t, tl + 0.12, 0.55);
  st($('wordmark'), { o: wm, x: (1 - wm) * -40, b: (1 - wm) * 12 });
  st($('lockup'), { o: 1 - ex, s: 1 + ex * 0.05, b: ex * 10, y: (1 - P(t, tl, .8)) * 40 });
  // eyebrow + line
  const eb = P(t, wt('l2', 4) - 0.15, 0.4);
  inout($('s2eyebrow'), eb, ex);
  const lt = [wt('l2', 4) - 0.1, wt('l2', 4), wt('l2', 5), wt('l2', 6), wt('l2', 7), wt('l2', 8), wt('l2', 9)];
  words(S2L, lt, t);
  st($('s2line'), { o: 1 - ex, b: ex * 10 });
  $('uline').style.transform = `scaleX(${P(t, wt('l2', 7) + 0.25, 0.6, E.inout)})`;
  $('uline').style.width = '100%';
  // constellation
  GRAPH.forEach((n, i) => {
    const k = P(t, tl + 0.2 + i * 0.12, 0.8, E.out3);
    n.line.setAttribute('stroke-dashoffset', n.len * (1 - k));
    const pk = P(t, tl + 0.5 + i * 0.12, 0.5, E.back);
    const dx = Math.sin(t * 0.6 + n.ph) * 10, dy = Math.cos(t * 0.5 + n.ph) * 8;
    n.g.setAttribute('transform', `translate(${n.x + dx},${n.y + dy}) scale(${pk})`);
    n.g.style.opacity = P(t, tl + 0.5 + i * 0.12, 0.3) * (1 - ex);
    n.line.style.opacity = 1 - ex;
  });
}

function s3(t) {
  if (!sceneOn('s3', t)) return;
  const [a, b] = T.scenes.s3; const ex = P(t, b - 0.3, 0.3, E.in);
  inout($('s3eyebrow'), P(t, a + 0.05, 0.4), ex);
  words(S3H, stagger(a + 0.15, S3H.length, 0.09), t);
  st($('s3h'), { o: 1 - ex, b: ex * 8 });
  const bed = P(t, a, 0.6);
  st($('s3bed'), { o: bed * (1 - ex), x: (1 - bed) * 120 + ex * 60, b: ex * 8 });
  const ct = [wt('l3', 1), wt('l3', 2), wt('l3', 3), wt('l3', 7)];
  ['cap1', 'cap2', 'cap3', 'cap4'].forEach((id, i) => {
    const k = P(t, ct[i] - 0.08, 0.5, E.back), o = P(t, ct[i] - 0.08, 0.2);
    st($(id), { o, y: (1 - k) * 50, s: lerp(0.86, 1, k) });
  });
  $('cap2t').textContent = mmss(24 + (t - a));
  $('cap4t').textContent = mmss(8 * 60 + 12 + (t - a));
  ['wave2', 'wave4'].forEach((id, j) => {
    [...$(id).children].forEach((bar, i) => {
      const v = Math.abs(Math.sin(t * 7.3 + i * 0.9 + j) * Math.sin(t * 2.1 + i * 0.37)) * 0.85 + 0.12;
      bar.style.height = `${v * 64}px`;
    });
  });
  $('wave2').style.color = '#151514'; $('wave4').style.color = '#f6b25c';
  const rb = P(t, ct[2] + 0.5, 0.25); $('recbtn').style.boxShadow = `0 0 0 ${rb * 6}px rgba(21,21,20,${0.25 * (1 - P(t, ct[2] + .75, .5))})`;
  // languages
  const lt = wt('l3', 8) - 0.25;
  inout($('lang'), P(t, lt, 0.45), ex);
  $('langnum').textContent = String(Math.max(1, Math.round(17 * P(t, lt, 0.8, E.out3))));
  HELLO.forEach((h, i) => {
    const s = lt + 0.15 + i * 0.26, k = P(t, s, 0.22), q = i === HELLO.length - 1 ? 0 : P(t, s + 0.26, 0.2);
    st(h, { o: k * (1 - q), y: (1 - k) * 30 - q * 30 });
  });
  inout($('s3chips').children[0], P(t, lt + 0.5, 0.4), ex);
  const off = P(t, wt('l3', 10) - 0.05, 0.4);
  inout($('offchip'), off, ex);
  $('offchip').style.borderColor = off > 0.5 ? 'rgba(245,123,58,.7)' : '#3a3a3e';
  const ob = P(t, wt('l3', 11), 0.3);
  $('offbadge').style.background = `rgba(245,123,58,${0.12 + ob * 0.8})`; $('offbadge').style.color = ob > .5 ? '#fff' : '#cfcfd2';
}

function s4(t) {
  if (!sceneOn('s4', t)) return;
  const [a, b] = T.scenes.s4; const ex = P(t, b - 0.3, 0.3, E.in);
  words(S4H, [wt('l4', 0), wt('l4', 1), wt('l4', 2), wt('l4', 4), wt('l4', 5), wt('l4', 6), wt('l4', 7), wt('l4', 8)], t);
  // highlight the three outcomes as they are named
  const hs = [wt('l4', 4), wt('l4', 5), wt('l4', 7)];
  [...$('s4h').querySelectorAll('.w')].forEach((sp, i) => { sp.style.color = t >= hs[i] ? ['#fff', '#beb4fb', '#f5a46c'][i] : '#fff'; });
  st($('s4h'), { o: 1 - ex, b: ex * 8 });
  const bed = P(t, a, 0.7);
  const push = P(t, a, b - a, E.lin);
  st($('s4bed'), { o: bed * (1 - ex), y: (1 - bed) * 90, s: 1 + push * 0.02 - ex * 0.02, b: ex * 8 });
  const ap = P(t, a + 0.15, 0.7);
  st($('app'), { o: ap, y: (1 - ap) * 80 });
  const cap = P(t, a + 0.6, 0.4, E.back);
  st($('captured'), { o: P(t, a + 0.6, .2), s: lerp(0.6, 1, cap) });
  // summary streams in on "notes"
  const sk = P(t, wt('l4', 4) - 0.1, 1.1, E.lin);
  const n = Math.round(SUMTXT.length * sk);
  $('sum').innerHTML = SUMTXT.slice(0, n) + (sk > 0 && sk < 1 ? '<span class="caret" style="height:22px;width:2px"></span>' : '');
  const k1 = P(t, wt('l4', 5) - 0.05, 0.5, E.back), k2 = P(t, wt('l4', 7) - 0.05, 0.5, E.back);
  st($('kc1'), { o: P(t, wt('l4', 5) - .05, .2), y: (1 - k1) * 40, s: lerp(.9, 1, k1) });
  st($('kc2'), { o: P(t, wt('l4', 7) - .05, .2), y: (1 - k2) * 40, s: lerp(.9, 1, k2) });
  $('taskcount').textContent = String(Math.round(3 * P(t, wt('l4', 8), .5, E.lin)));
  const t1 = P(t, wt('l4', 8) + 0.25, 0.5, E.back), t2 = P(t, wt('l4', 8) + 0.85, 0.5, E.back);
  st($('toast1'), { o: P(t, wt('l4', 8) + .25, .2), x: (1 - t1) * -60, s: lerp(.85, 1, t1) });
  st($('toast2'), { o: P(t, wt('l4', 8) + .85, .2), x: (1 - t2) * 60, s: lerp(.85, 1, t2) });
}

function s5(t) {
  if (!sceneOn('s5', t)) return;
  const [a, b] = T.scenes.s5; const ex = P(t, b - 0.3, 0.3, E.in);
  inout($('s5eb'), P(t, a + 0.05, 0.4), ex);
  words(S5Q, stagger(a + 0.25, S5Q.length, 0.1), t);
  st($('s5q'), { o: (1 - ex) * lerp(1, 0.45, P(t, wt('l5', 11), 0.5)), b: ex * 8 });
  inout($('s5w'), P(t, wt('l5', 13), 0.5), ex);
  const bed = P(t, a, 0.6);
  st($('s5bed'), { o: bed * (1 - ex), x: (1 - bed) * 120 + ex * 60, b: ex * 8 });
  const ap = P(t, a + 0.2, 0.6); st($('askpanel'), { o: ap, y: (1 - ap) * 60 });
  // question typing
  const n = T.qkeys.filter(k => k <= t).length;
  $('askqt').textContent = T.question.slice(0, n);
  st($('askq'), { o: P(t, T.qkeys[0] - 0.15, 0.2) });
  $('askcaret').style.opacity = n < T.question.length ? 1 : 0;
  const g0 = T.qkeys[T.qkeys.length - 1] + 0.15;
  const gk = P(t, g0, 0.3);
  st($('ground'), { o: gk * (0.6 + 0.4 * Math.abs(Math.sin((t - g0) * 4))) });
  // answer streams word by word
  const a0 = wt('l5', 11) - 0.05;
  words(ASK, stagger(a0, ASK.length, 0.07), t, 0.3, 12);
  ASKC.forEach((c, i) => { const k = P(t, a0 + [0.35, 0.8, 1.15][i], 0.35, E.back); c.style.transform = `scale(${k})`; });
  ['src1', 'src2', 'src3'].forEach((id, i) => { const k = P(t, wt('l5', 15) + i * 0.16, 0.45, E.back); st($(id), { o: P(t, wt('l5', 15) + i * 0.16, .2), x: (1 - k) * 40 }); });
}

let CUR0 = null;
function s6(t) {
  if (!sceneOn('s6', t)) return;
  const [a, b] = T.scenes.s6; const ex = P(t, b - 0.3, 0.3, E.in);
  inout($('s6eb'), P(t, a + 0.05, 0.4), ex);
  words(S6Q, stagger(a + 0.25, S6Q.length, 0.09), t);
  st($('s6q'), { o: (1 - ex) * lerp(1, 0.4, P(t, wt('l6', 9) - 0.3, 0.5)), b: ex * 8 });
  words(FV5, [wt('l6', 9), wt('l6', 10), wt('l6', 11), wt('l6', 12), wt('l6', 13)], t);
  words(FV3, [wt('l6', 14), wt('l6', 15), wt('l6', 16)], t);
  $('fv3').style.setProperty('--k', P(t, wt('l6', 16) + 0.25, 0.4, E.inout));
  st($('flip'), { o: 1 - ex, b: ex * 8 });
  const bed = P(t, a, 0.6);
  st($('s6bed'), { o: bed * (1 - ex), x: (1 - bed) * 120 + ex * 60, b: ex * 8 });
  const mp = P(t, a + 0.15, 0.6); st($('mail'), { o: mp, y: (1 - mp) * 60 });
  ['p1', 'p2'].forEach((id, i) => inout($(id), P(t, a + 0.7 + i * 0.15, 0.4), 0, { dy: 16, blur: 4 }));
  const d0 = wt('l6', 7) - 0.15;
  ['tk1', 'tk2', 'tk3'].forEach((id, i) => {
    const k = P(t, d0 + i * 0.2, 0.35); st($(id), { o: k, x: (1 - k) * -20 });
    $(id).style.clipPath = `inset(0 ${100 - P(t, d0 + i * 0.2, 0.45, E.out3) * 100}% 0 0)`;
  });
  // cursor glides to "Send to 2" and clicks
  const btn = $('sendbtn');
  if (!CUR0) { let x = 0, y = 0, e = btn; while (e && e.id !== 's6bed') { x += e.offsetLeft; y += e.offsetTop; e = e.offsetParent; } CUR0 = { x: x + btn.offsetWidth * 0.55, y: y + btn.offsetHeight * 0.55 }; }
  const c0 = wt('l6', 8) + 0.1, click = c0 + 0.75;
  const m = P(t, c0, 0.7, E.inout);
  const cx = lerp(CUR0.x + 260, CUR0.x, m), cy = lerp(CUR0.y + 220, CUR0.y, m);
  const press = P(t, click, 0.08) * (1 - P(t, click + 0.1, 0.15));
  const cur = $('cursor'); cur.style.left = cx + 'px'; cur.style.top = cy + 'px';
  st(cur, { o: P(t, c0, 0.2) * (1 - P(t, click + 1.2, 0.3)), s: 1 - press * 0.15 });
  st(btn, { s: 1 - press * 0.08 });
  btn.style.boxShadow = `0 0 0 ${P(t, click, 0.5) * 18}px rgba(21,21,20,${0.3 * (1 - P(t, click, 0.5))})`;
  btn.textContent = t > click + 0.05 ? 'Sent ✓' : 'Send to 2';
  const tk = P(t, click + 0.2, 0.5, E.back);
  st($('toast3'), { o: P(t, click + 0.2, 0.2), y: (1 - tk) * 30, s: lerp(.85, 1, tk) });
}

function s7(t) {
  if (!sceneOn('s7', t)) return;
  const [a, b] = T.scenes.s7; const ex = P(t, b - 0.3, 0.3, E.in);
  inout($('s7eb'), P(t, a + 0.05, 0.4), ex);
  words(S7H, stagger(a + 0.15, S7H.length, 0.08), t);
  st($('s7h'), { o: 1 - ex, b: ex * 8 });
  const sn = P(t, a + 0.2, 0.6);
  st($('srcnote'), { o: sn * (1 - ex), x: (1 - sn) * -100, b: ex * 8 });
  const lands = [wt('l7', 4), wt('l7', 7), wt('l7', 10)];
  ['ai1', 'ai2', 'ai3'].forEach((id, i) => {
    inout($(id), P(t, a + 0.5 + i * 0.12, 0.4), 0, { dy: 14, blur: 3 });
    const done = t >= lands[[0, 0, 2][i]] + (i === 1 ? 0.2 : 0);
    const cb = $(id).querySelector('.cb');
    cb.style.background = done ? '#2f7a4a' : 'transparent'; cb.style.borderColor = done ? '#2f7a4a' : '#c9c9cf';
    cb.innerHTML = done ? '<svg viewBox="0 0 20 20" width="18" height="18"><path d="M4 10l4 4 8-9" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round"/></svg>' : '';
  });
  WIRES.forEach((w, i) => {
    const s = lands[i] - 0.55, k = P(t, s, 0.55, E.inout);
    w.p.setAttribute('stroke-dashoffset', w.len * (1 - k)); w.p.style.opacity = 0.9 * (1 - ex);
    const pt = w.p.getPointAtLength(w.len * k); w.dot.setAttribute('cx', pt.x); w.dot.setAttribute('cy', pt.y);
    w.dot.style.opacity = (k > 0 && k < 1 ? 1 : 0) * (1 - ex);
    const d = P(t, lands[i] - 0.05, 0.5, E.back);
    st($('d' + (i + 1)), { o: P(t, lands[i] - .05, .2) * (1 - ex), x: (1 - d) * 50, s: lerp(.9, 1, d), b: ex * 8 });
  });
  const tk = P(t, wt('l7', 5) - 0.2, 0.5, E.back);
  st($('toast4'), { o: P(t, wt('l7', 5) - .2, .2) * (1 - ex), y: (1 - tk) * 30, s: lerp(.85, 1, tk) });
}

function s8(t) {
  if (!sceneOn('s8', t)) return;
  words(O1, [wt('l8', 0), wt('l8', 1), wt('l8', 2)], t, 0.4);
  words(O2, [wt('l8', 3), wt('l8', 4), wt('l8', 5)], t, 0.4);
  const tl = wt('l8', 6) - 0.1;
  const go = P(t, tl - 0.35, 0.35, E.in);
  st($('o1'), { o: 1 - go, y: -go * 60, b: go * 12 });
  st($('o2'), { o: 1 - go, y: -go * 60, b: go * 12 });
  const lk = P(t, tl, 0.7, E.back);
  st($('endlogo'), { o: P(t, tl, .2), s: lerp(0.3, 1, lk), r: lerp(-140, 0, P(t, tl, 0.9)) });
  const wm = P(t, tl + 0.12, 0.55);
  st($('endlock').querySelector('.wordmark'), { o: wm, x: (1 - wm) * -40, b: (1 - wm) * 12 });
  st($('endlock'), { o: P(t, tl, .2), y: (1 - P(t, tl, .8)) * 40 });
  inout($('endsub'), P(t, tl + 0.45, 0.5));
  const c = P(t, wt('l8', 7) - 0.05, 0.55, E.back);
  st($('cta'), { o: P(t, wt('l8', 7) - .05, .2), y: (1 - c) * 30, s: lerp(.9, 1, c) });
  const u = $('cta').querySelector('.url'); u.style.color = t > wt('l8', 10) ? '#f6b25c' : '#fff';
  [...$('trust').children].forEach((sp, i) => inout(sp, P(t, wt('l8', 10) + 0.3 + i * 0.15, 0.4), 0, { dy: 16, blur: 4 }));
  // gentle breathing glow on the button at the end
  const btn = $('cta').querySelector('.btn'); btn.style.boxShadow = `0 0 ${40 + 20 * Math.sin(t * 3)}px rgba(246,178,92,${0.35 * P(t, wt('l8', 7), 0.6)})`;
}

function camera(t) {
  // slow push-in per scene, reset at each cut
  const id = Object.keys(T.scenes).filter(k => t >= T.scenes[k][0]).pop();
  const [a, b] = T.scenes[id];
  const k = clamp((t - a) / (b - a));
  $('cam').style.transform = `scale(${1 + 0.03 * k})`;
}

window.render = function (t) {
  bg(t);
  s1(t); s2(t); s3(t); s4(t); s5(t); s6(t); s7(t); s8(t);
};
window.ready = (async () => {
  await document.fonts.ready;
  await Promise.all(['500 20px "Schibsted Grotesk"', '600 20px "Schibsted Grotesk"', '400 20px Inter', '500 20px Inter', '600 20px Inter', '400 20px "JetBrains Mono"',
    '500 20px "Noto Sans Devanagari"', '500 20px "Noto Sans JP"', '500 20px "Noto Sans KR"', '500 20px "Noto Sans Arabic"'].map(f => document.fonts.load(f, 'नमस्ते こんにちは 안녕하세요 مرحبا Aa')));
  init(); window.render(0); return true;
})();
