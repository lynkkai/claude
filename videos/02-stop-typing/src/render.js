// Renders src/index.html frame by frame into a silent video, or stills for review.
//   node src/render.js                      -> work/video.mp4 (silent)
//   node src/render.js --stills 1,6.2,13    -> work/stills/t-<time>.png
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const work = path.join(root, 'work');
const TL = JSON.parse(fs.readFileSync(path.join(__dirname, 'timeline.json'), 'utf8'));

(async () => {
  const args = process.argv.slice(2);
  const stillsArg = args.indexOf('--stills');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(__dirname, 'index.html'));
  await page.evaluate(() => window.ready);

  if (stillsArg >= 0) {
    const dir = path.join(work, 'stills');
    fs.mkdirSync(dir, { recursive: true });
    for (const t of args[stillsArg + 1].split(',').map(Number)) {
      await page.evaluate(t => window.render(t), t);
      await page.screenshot({ path: path.join(dir, `t-${t.toFixed(2)}.png`) });
    }
    await browser.close();
    return;
  }

  fs.mkdirSync(work, { recursive: true });
  const out = path.join(work, 'video.mp4');
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(TL.fps), '-c:v', 'png', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const n = Math.round(TL.duration * TL.fps);
  for (let f = 0; f < n; f++) {
    await page.evaluate(t => window.render(t), f / TL.fps);
    const buf = await page.screenshot({ type: 'png' });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (f % 150 === 0) console.log(`frame ${f}/${n}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log('wrote', out);
})();
