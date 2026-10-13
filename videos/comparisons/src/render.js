// Render a video from stage.html + timeline.json + mix.wav.
// Usage:
//   node render.js <workdir>/<slug> <out.mp4>            full render
//   node render.js <workdir>/<slug> --stills 1.2,5,9     PNG stills for review
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const FPS = 30;

(async () => {
  const dir = process.argv[2];
  const meta = JSON.parse(fs.readFileSync(path.join(dir, 'timeline.json'), 'utf8'));
  const vertical = meta.format === 'vertical';
  const W = vertical ? 1080 : 1920, H = vertical ? 1920 : 1080;
  const browser = await chromium.launch({ executablePath: process.env.CHROME || undefined });
  let page, stage;
  const open = async () => {
    if (page) await page.close().catch(() => {});
    page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
    await page.goto('file://' + path.join(__dirname, 'stage', 'stage.html'));
    await page.evaluate((m) => window.__init(m), meta);
    await page.evaluate(() => document.fonts.ready);
    stage = await page.$('#stage');
  };
  await open();
  // one frame; a hung page is replaced and the frame retried, so a long render can't stall
  const frame = async (t, opts) => {
    for (let attempt = 0; ; attempt++) {
      try {
        await page.evaluate((t) => window.__set(t), t);
        return await stage.screenshot({ timeout: 30000, ...opts });
      } catch (e) {
        if (attempt >= 3) throw e;
        console.log(`${meta.slug}: retrying frame at ${t.toFixed(2)}s (${e.message.split('\n')[0]})`);
        await open();
      }
    }
  };

  if (process.argv[3] === '--stills') {
    const times = process.argv[4].split(',').map(Number);
    for (const t of times) {
      await frame(t, { path: path.join(dir, `still_${t.toFixed(2)}.png`) });
    }
    await browser.close();
    return;
  }

  const out = process.argv[3];
  const n = Math.ceil(meta.duration * FPS);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    // pad the audio so it never ends before the last frame (with -shortest, ffmpeg would stop reading frames and stall)
    '-i', path.join(dir, 'mix.wav'), '-map', '0:v', '-map', '1:a', '-af', 'apad',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-r', String(FPS),
    '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const t0 = Date.now();
  for (let i = 0; i < n; i++) {
    const buf = await frame(i / FPS, { type: 'jpeg', quality: 93 });
    if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once('drain', r));
    if (i % 300 === 0) console.log(`${meta.slug}: frame ${i}/${n} (${((Date.now() - t0) / 1000).toFixed(0)}s)`);
  }
  ff.stdin.end();
  await new Promise((r) => ff.on('close', r));
  await browser.close();
  console.log('done', out);
})();
