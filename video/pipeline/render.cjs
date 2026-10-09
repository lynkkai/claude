// Render video.html frame by frame with headless Chromium and encode with ffmpeg.
// Usage (<dir> holds video.html and build/timeline.json):
//   node render.cjs <dir>                      full render -> <dir>/build/video-silent.mp4 (+ sfx.json)
//   node render.cjs <dir> --stills 3,20,95     write <dir>/build/still-<t>.png for quick checks
//   node render.cjs <dir> --thumb 9.5 out.png  single still at a given time
//   node render.cjs <dir> --thumbnail out.png  YouTube thumbnail (video.html's renderThumb)
// The frame size comes from <meta name="board" content="1600x900@1.2"> in video.html:
// the CSS board size, then the device scale (1600x900 at 1.2 gives 1920x1080 frames).
const path = require('path');
const fs = require('fs');
const { spawn } = require('child_process');
let chromium;
try { ({ chromium } = require('playwright')); } catch { ({ chromium } = require('/opt/node22/lib/node_modules/playwright')); }

const argv = process.argv.slice(2);
const HERE = path.resolve(argv[0] && !argv[0].startsWith('--') ? argv.shift() : '.');
const BUILD = path.join(HERE, 'build');
const TL = JSON.parse(fs.readFileSync(path.join(BUILD, 'timeline.json'), 'utf8'));
const FPS = TL.fps;
const URL = 'file://' + path.join(HERE, 'video.html');
const WORKERS = parseInt(process.env.WORKERS || '4', 10);
const board = (fs.readFileSync(path.join(HERE, 'video.html'), 'utf8').match(/<meta name="board" content="(\d+)x(\d+)@([\d.]+)"/) || [0, 1600, 900, 1.2]).slice(1).map(Number);

async function openPage(browser) {
  const page = await browser.newPage({ viewport: { width: board[0], height: board[1] }, deviceScaleFactor: board[2] });
  page.on('pageerror', e => { console.error('PAGE ERROR', e.message); process.exitCode = 1; });
  page.on('console', m => { if (['warning', 'error'].includes(m.type())) console.error('PAGE', m.text()); });
  await page.goto(URL, { waitUntil: 'networkidle' });
  await page.waitForFunction(() => document.documentElement.dataset.ready === '1');
  await page.evaluate(() => document.fonts.ready);
  return page;
}

async function stills(times, outFor) {
  const browser = await chromium.launch();
  const page = await openPage(browser);
  for (const t of times) {
    await page.evaluate(t => window.renderFrame(t), t);
    const out = outFor(t);
    await page.screenshot({ path: out });
    console.log('wrote', out);
  }
  await browser.close();
}

async function renderRange(browser, from, to, out) {
  const page = await openPage(browser);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '17', '-pix_fmt', 'yuv420p', '-r', String(FPS), out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const done = new Promise((res, rej) => ff.on('close', c => c === 0 ? res() : rej(new Error('ffmpeg ' + c))));
  for (let f = from; f < to; f++) {
    await page.evaluate(t => window.renderFrame(t), f / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 94 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if ((f - from) % 300 === 0) console.log(`${path.basename(out)}: ${f - from}/${to - from}`);
  }
  ff.stdin.end();
  await done;
  await page.close();
}

async function full() {
  const total = Math.ceil(TL.duration * FPS);
  const browser = await chromium.launch();
  const p0 = await openPage(browser);
  fs.writeFileSync(path.join(BUILD, 'sfx.json'), JSON.stringify(await p0.evaluate(() => window.getSfx())));
  await p0.close();
  const per = Math.ceil(total / WORKERS);
  const segs = [];
  const jobs = [];
  for (let w = 0; w < WORKERS; w++) {
    const a = w * per, b = Math.min(total, (w + 1) * per);
    if (a >= b) break;
    const out = path.join(BUILD, `seg${w}.mp4`);
    segs.push(out);
    jobs.push(renderRange(browser, a, b, out));
  }
  await Promise.all(jobs);
  await browser.close();
  fs.writeFileSync(path.join(BUILD, 'segs.txt'), segs.map(s => `file '${s}'`).join('\n') + '\n');
  await new Promise((res, rej) => spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', path.join(BUILD, 'segs.txt'), '-c', 'copy', path.join(BUILD, 'video-silent.mp4')], { stdio: 'inherit' })
    .on('close', c => c === 0 ? res() : rej(new Error('concat ' + c))));
  console.log('wrote build/video-silent.mp4', total, 'frames');
}

(async () => {
  const args = argv;
  if (args[0] === '--stills') await stills(args[1].split(',').map(Number), t => path.join(BUILD, `still-${t}.png`));
  else if (args[0] === '--thumb') await stills([parseFloat(args[1])], () => path.resolve(args[2]));
  else if (args[0] === '--thumbnail') {
    const browser = await chromium.launch();
    const page = await openPage(browser);
    await page.evaluate(() => window.renderThumb());
    await page.screenshot({ path: path.resolve(args[1]) });
    await browser.close();
    console.log('wrote', args[1]);
  }
  else await full();
})().catch(e => { console.error(e); process.exit(1); });
