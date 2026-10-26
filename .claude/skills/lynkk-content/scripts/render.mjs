// Render a built scene page (see build.py) to stills or video. Every frame is a pure function of time:
// the page exposes window.ready (fonts + images loaded) and window.render(t).
// Usage:
//   node render.mjs preview <page.html> <sheet.png> t1 t2 ...      contact sheet of stills (check every scene + mid-animation)
//   node render.mjs still   <page.html> <out.png|jpg> <t> [width=1080] [height=1920]   one frame (posters, social images)
//   node render.mjs video   <page.html> <out.mp4> [fps=30] [seconds=20] [width=1080] [height=1920]
// Needs Playwright (Chromium, found locally or globally) and ffmpeg.
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
// Find Playwright from the current folder first, then the global npm install.
const loadPlaywright = () => { try { return createRequire(process.cwd() + '/')('playwright'); } catch { return createRequire(execSync('npm root -g').toString().trim() + '/')('playwright'); } };
const { chromium } = loadPlaywright();
import { spawn } from 'node:child_process';
import path from 'node:path';

const [mode, pagePath, out, ...rest] = process.argv.slice(2);
const sizeArgs = mode === 'video' ? rest.slice(2, 4) : mode === 'still' ? rest.slice(1, 3) : [];
const width = Number(sizeArgs[0] || 1080), height = Number(sizeArgs[1] || 1920);
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.log('[pageerror]', e.message));
await page.goto('file://' + path.resolve(pagePath));
await page.evaluate(() => window.ready);

if (mode === 'preview') {
  const times = rest.map(Number), shots = [];
  for (const t of times) {
    await page.evaluate(t => window.render(t), t);
    shots.push((await page.screenshot({ type: 'png' })).toString('base64'));
  }
  const sheet = await browser.newPage({ viewport: { width: 1600, height: 1400 } });
  const cols = Math.min(4, times.length);
  await sheet.setContent(`<body style="margin:0;background:#888;display:grid;grid-template-columns:repeat(${cols},1fr);gap:6px">${shots.map((s, i) => `<div style="position:relative"><img style="width:100%;display:block" src="data:image/png;base64,${s}"><b style="position:absolute;left:6px;top:6px;background:#000;color:#fff;font:14px sans-serif;padding:2px 6px">${times[i]}s</b></div>`).join('')}</body>`);
  await sheet.screenshot({ path: out, fullPage: true });
} else if (mode === 'still') {
  await page.evaluate(t => window.render(t), Number(rest[0] || 0));
  await page.screenshot({ path: out, type: out.endsWith('.png') ? 'png' : 'jpeg', ...(out.endsWith('.png') ? {} : { quality: 95 }) });
} else {
  const fps = Number(rest[0] || 30), dur = Number(rest[1] || 20);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', String(fps), out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const n = Math.round(fps * dur);
  for (let i = 0; i < n; i++) {
    await page.evaluate(t => window.render(t), i / fps);
    const buf = await page.screenshot({ type: 'jpeg', quality: 94 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 150 === 0) console.log(`frame ${i}/${n}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
}
await browser.close();
