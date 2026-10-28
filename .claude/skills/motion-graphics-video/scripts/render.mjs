#!/usr/bin/env node
/**
 * Render a deterministic HTML timeline to MP4, frame by frame.
 *
 * The page must expose window.renderFrame(t) (t in seconds) and may declare
 * window.FPS, window.DURATION, window.WIDTH, window.HEIGHT. See
 * references/motion-studio-rules.md for the full render contract.
 *
 * Usage:
 *   node render.mjs --html out/index.html --out out/film.mp4
 *   node render.mjs --html out/index.html --out out/preview.mp4 --range 0:3 --scale 0.5
 *   node render.mjs --html out/index.html --out out/film.mp4 --audio out/mix.wav
 *
 * Flags:
 *   --html <path>      timeline page (required)
 *   --out <path>       output mp4 (default: alongside the html, film.mp4)
 *   --fps <n>          overrides window.FPS
 *   --duration <s>     overrides window.DURATION
 *   --width/--height   overrides window.WIDTH / window.HEIGHT
 *   --scale <f>        render at a fraction of size, for fast look checks
 *   --range <a:b>      render only seconds a to b
 *   --audio <path>     mux this audio track into the result
 *   --crf <n>          x264 quality, default 18
 *   --frames <dir>     where to write PNGs (default: a temp dir next to --out)
 *   --keep-frames      do not delete the PNG frames
 */

import { spawn } from 'node:child_process';
import { createRequire } from 'node:module';
import { mkdir, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';

// Playwright is often installed globally rather than in the project, and a bare ESM
// import only looks in node_modules next to this file. CommonJS resolution finds the
// global install, so go through createRequire and fall back to known global roots.
const require_ = createRequire(import.meta.url);
function loadChromium() {
  const candidates = [
    'playwright',
    'playwright-core',
    '/opt/node-tools/node_modules/playwright',
    '/usr/local/lib/node_modules_global/playwright',
    '/usr/lib/node_modules/playwright',
    '/usr/local/lib/node_modules/playwright',
  ];
  for (const id of candidates) {
    try {
      return require_(id).chromium;
    } catch {}
  }
  throw new Error(
    'Could not load Playwright. It is preinstalled in most environments; do not run ' +
    '"playwright install" (a fresh copy will not find the existing browser). If a ' +
    'project pins its own @playwright/test, launch with executablePath: ' +
    '"/opt/pw-browsers/chromium".'
  );
}
const chromium = loadChromium();

function parseArgs(argv) {
  const args = {};
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (!a.startsWith('--')) continue;
    const key = a.slice(2);
    const next = argv[i + 1];
    if (next === undefined || next.startsWith('--')) {
      args[key] = true;
    } else {
      args[key] = next;
      i++;
    }
  }
  return args;
}

function run(cmd, cmdArgs) {
  return new Promise((resolve, reject) => {
    const child = spawn(cmd, cmdArgs, { stdio: 'inherit' });
    child.on('error', reject);
    child.on('close', (code) =>
      code === 0 ? resolve() : reject(new Error(`${cmd} exited with ${code}`))
    );
  });
}

const args = parseArgs(process.argv.slice(2));

if (!args.html || args.html === true) {
  console.error('render.mjs: --html <path to timeline page> is required');
  process.exit(1);
}

const htmlPath = path.resolve(String(args.html));
const outPath = path.resolve(
  String(args.out && args.out !== true ? args.out : path.join(path.dirname(htmlPath), 'film.mp4'))
);
const framesDir = path.resolve(
  String(args.frames && args.frames !== true
    ? args.frames
    : path.join(path.dirname(outPath), `.frames-${path.basename(outPath, '.mp4')}`))
);

await mkdir(path.dirname(outPath), { recursive: true });
await rm(framesDir, { recursive: true, force: true });
await mkdir(framesDir, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage();

const pageErrors = [];
page.on('pageerror', (err) => pageErrors.push(String(err)));
page.on('console', (msg) => {
  if (msg.type() === 'error') pageErrors.push(msg.text());
});

await page.goto('file://' + htmlPath, { waitUntil: 'load' });

// Wait for the contract to be in place rather than assuming it is.
await page.waitForFunction('typeof window.renderFrame === "function"', null, { timeout: 15000 })
  .catch(() => {
    throw new Error(
      'The page never defined window.renderFrame(t). See the render contract in ' +
      'references/motion-studio-rules.md.'
    );
  });

const meta = await page.evaluate(() => ({
  fps: window.FPS,
  duration: window.DURATION,
  width: window.WIDTH,
  height: window.HEIGHT,
}));

const fps = Number(args.fps && args.fps !== true ? args.fps : meta.fps || 30);
const duration = Number(args.duration && args.duration !== true ? args.duration : meta.duration);
const scale = Number(args.scale && args.scale !== true ? args.scale : 1);
const baseWidth = Number(args.width && args.width !== true ? args.width : meta.width || 1920);
const baseHeight = Number(args.height && args.height !== true ? args.height : meta.height || 1080);

if (!duration || Number.isNaN(duration)) {
  await browser.close();
  throw new Error('No duration: declare window.DURATION in the page or pass --duration.');
}

// Keep dimensions even, since yuv420p requires it.
const width = Math.round((baseWidth * scale) / 2) * 2;
const height = Math.round((baseHeight * scale) / 2) * 2;

await page.setViewportSize({ width, height });
// Tell the page its real output size, so layout can branch on aspect ratio.
await page.evaluate(([w, h]) => {
  window.WIDTH = w;
  window.HEIGHT = h;
  if (typeof window.onResize === 'function') window.onResize(w, h);
}, [baseWidth, baseHeight]);

let startT = 0;
let endT = duration;
if (args.range && args.range !== true) {
  const [a, b] = String(args.range).split(':').map(Number);
  if (!Number.isNaN(a)) startT = a;
  if (!Number.isNaN(b)) endT = b;
}

const startFrame = Math.round(startT * fps);
const endFrame = Math.round(endT * fps);
const total = Math.max(0, endFrame - startFrame);

console.log(
  `render: ${width}x${height} @ ${fps}fps, ${(endT - startT).toFixed(2)}s, ${total} frames`
);

for (let i = 0; i < total; i++) {
  const frame = startFrame + i;
  const t = frame / fps;
  await page.evaluate((time) => window.renderFrame(time), t);
  await page.screenshot({
    path: path.join(framesDir, String(i).padStart(6, '0') + '.png'),
    animations: 'disabled',
  });
  if (i % fps === 0 || i === total - 1) {
    process.stdout.write(`\r  frame ${i + 1}/${total} (t=${t.toFixed(2)}s)   `);
  }
}
process.stdout.write('\n');

await browser.close();

if (pageErrors.length) {
  console.warn('page reported errors during render:');
  for (const e of [...new Set(pageErrors)].slice(0, 10)) console.warn('  ' + e);
}

const crf = String(args.crf && args.crf !== true ? args.crf : 18);
const ffmpegArgs = ['-y', '-framerate', String(fps), '-i', path.join(framesDir, '%06d.png')];

if (args.audio && args.audio !== true) {
  ffmpegArgs.push('-i', path.resolve(String(args.audio)));
}

ffmpegArgs.push(
  '-c:v', 'libx264',
  '-profile:v', 'high',
  '-crf', crf,
  '-pix_fmt', 'yuv420p',
  '-movflags', '+faststart'
);

if (args.audio && args.audio !== true) {
  ffmpegArgs.push('-c:a', 'aac', '-b:a', '192k', '-shortest');
}

ffmpegArgs.push(outPath);

await run('ffmpeg', ffmpegArgs);

// A small manifest makes later rounds and delivery notes easier to write.
await writeFile(
  outPath.replace(/\.mp4$/, '.render.json'),
  JSON.stringify(
    { html: htmlPath, out: outPath, fps, duration, width, height, startT, endT, frames: total,
      audio: args.audio && args.audio !== true ? path.resolve(String(args.audio)) : null,
      renderedAt: new Date().toISOString() },
    null,
    2
  ) + '\n'
);

if (!args['keep-frames']) {
  await rm(framesDir, { recursive: true, force: true });
}

console.log(`done: ${outPath}`);
