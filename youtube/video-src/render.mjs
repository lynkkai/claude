// usage: node render.mjs v1 stills 1,5,12   |  node render.mjs v1 video out.mp4 [fps]
import { chromium } from 'playwright-core';
import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const dir = path.dirname(fileURLToPath(import.meta.url));
const [v, mode, arg, fpsArg] = process.argv.slice(2);
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--allow-file-access-from-files'] });
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
page.on('pageerror', e => console.error('PAGE ERROR', e.message));
await page.goto('file://' + path.join(dir, 'engine.html') + '?v=' + v);
await page.evaluate(() => document.fonts.ready);
await page.evaluate(() => { window.renderFrame(0); return document.fonts.ready; });
const total = await page.evaluate(() => window.TOTAL);
const stage = await page.$('#stage');
if (mode === 'stills') {
  for (const t of arg.split(',').map(Number)) {
    await page.evaluate(t => window.renderFrame(t), t);
    await stage.screenshot({ path: path.join(dir, `still-${v}-${t}.png`) });
  }
  console.log('total', total);
} else {
  const fps = Number(fpsArg || 30), n = Math.ceil(total * fps);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'mjpeg', '-i', '-',
    '-f', 'lavfi', '-i', 'anullsrc=r=48000:cl=stereo', '-shortest',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', '-c:a', 'aac', '-b:a', '128k', '-movflags', '+faststart', arg], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let i = 0; i < n; i++) {
    await page.evaluate(t => window.renderFrame(t), i / fps);
    const buf = await stage.screenshot({ type: 'jpeg', quality: 92 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 300 === 0) console.log(`frame ${i}/${n}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  console.log('done', arg, total.toFixed(1) + 's');
}
await browser.close();
