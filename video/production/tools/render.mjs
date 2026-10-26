// Render a timeline to silent MP4: every frame is setTime(t) in player.html, captured
// by headless Chromium and piped straight into ffmpeg.
// usage: node render.mjs <video_dir> <out.mp4> [--fps 30] [--stills t1,t2,...] [--from s --to s]
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { spawn } from 'node:child_process';
import { readFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const [vdir, out] = process.argv.slice(2);
const arg = (k, d) => { const i = process.argv.indexOf(k); return i > 0 ? process.argv[i + 1] : d; };
const fps = +arg('--fps', 30);
const tl = JSON.parse(readFileSync(join(vdir, 'timeline.json'), 'utf8'));

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto(pathToFileURL(resolve(here, '..', 'player.html')).href);
await page.evaluate(tl => window.loadTimeline(tl), tl);

const stills = arg('--stills');
if (stills) {
  mkdirSync(out, { recursive: true });
  for (const t of stills.split(',').map(Number)) {
    await page.evaluate(t => window.setTime(t), t);
    await page.screenshot({ path: join(out, `still_${t.toFixed(2)}.png`) });
  }
  await browser.close();
  process.exit(0);
}

const from = +arg('--from', 0), to = +arg('--to', tl.duration);
const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
  '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', String(fps), out], { stdio: ['pipe', 'inherit', 'inherit'] });
const frames = Math.round((to - from) * fps);
const t0 = Date.now();
for (let f = 0; f < frames; f++) {
  await page.evaluate(t => window.setTime(t), from + f / fps);
  const buf = await page.screenshot({ type: 'jpeg', quality: 93 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (f % 600 === 0) console.log(`${tl.id}: frame ${f}/${frames} (${((Date.now() - t0) / 1000).toFixed(0)}s)`);
}
ff.stdin.end();
await new Promise(r => ff.on('close', r));
await browser.close();
console.log(`${tl.id}: wrote ${out} (${frames} frames)`);
