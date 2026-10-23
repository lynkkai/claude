// Usage (run build.py first): node render.mjs preview <out.png> t1 t2 ...   (contact sheet of stills)
//        node render.mjs video <out.mp4> [fps] [duration]
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const [mode, out, ...rest] = process.argv.slice(2);
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
page.on('console', m => console.log('[page]', m.text()));
page.on('pageerror', e => console.log('[pageerror]', e.message));
await page.goto('file://' + path.join(here, 'scene.html'));
await page.evaluate(() => window.ready);

if (mode === 'preview') {
  const times = rest.map(Number);
  const shots = [];
  for (const t of times) {
    await page.evaluate(t => window.render(t), t);
    shots.push((await page.screenshot({ type: 'png' })).toString('base64'));
  }
  const sheet = await browser.newPage({ viewport: { width: 1600, height: 1400 } });
  const cols = Math.min(4, times.length);
  await sheet.setContent(`<body style="margin:0;background:#888;display:grid;grid-template-columns:repeat(${cols},1fr);gap:6px">${shots.map((s, i) => `<div style="position:relative"><img style="width:100%;display:block" src="data:image/png;base64,${s}"><b style="position:absolute;left:6px;top:6px;background:#000;color:#fff;font:14px sans-serif;padding:2px 6px">${times[i]}s</b></div>`).join('')}</body>`);
  await sheet.screenshot({ path: out, fullPage: true });
} else {
  const fps = Number(rest[0] || 30), dur = Number(rest[1] || 50);
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
