// Render scenes.html frame by frame with headless Chromium and pipe to ffmpeg.
// Usage: node render.mjs <startFrame> <endFrame> <out.mp4>
//        node render.mjs --stills <t1,t2,...> <outDir>
import { createRequire } from 'module';
import { spawn } from 'child_process';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const require = createRequire(import.meta.url);
let chromium;
try { ({ chromium } = require('playwright')); }
catch { ({ chromium } = require('/opt/node-tools/node_modules/playwright')); }

const here = path.dirname(fileURLToPath(import.meta.url));
const timeline = JSON.parse(fs.readFileSync(path.join(here, 'build/timeline.json'), 'utf8'));

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
await page.goto('file://' + path.join(here, 'scenes.html'));
await page.evaluate(async (tl) => { await document.fonts.ready; window.init(tl); }, timeline);
await page.evaluate(() => Promise.all([...document.fonts].map(f => f.load())));

if (process.argv[2] === '--stills') {
  const times = process.argv[3].split(',').map(Number);
  const out = process.argv[4];
  fs.mkdirSync(out, { recursive: true });
  for (const t of times) {
    await page.evaluate((t) => window.renderAt(t), t);
    await page.screenshot({ path: path.join(out, `still_${t.toFixed(1).padStart(6, '0')}.png`) });
  }
} else {
  const [start, end] = [Number(process.argv[2]), Number(process.argv[3])];
  const out = process.argv[4];
  const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(timeline.fps), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-pix_fmt', 'yuv420p', '-r', String(timeline.fps), out], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let f = start; f < end; f++) {
    await page.evaluate((t) => window.renderAt(t), f / timeline.fps);
    const buf = await page.screenshot({ type: 'jpeg', quality: 94 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if ((f - start) % 300 === 0) console.log(`${out}: frame ${f} / ${end}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
}
await browser.close();
