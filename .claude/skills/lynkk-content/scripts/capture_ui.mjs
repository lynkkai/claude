// Capture real UI from a live page (e.g. lynkk.ai) as high-res PNGs for videos and images.
// Usage: node capture_ui.mjs <job.json>
// job = { url, viewport:{width,height}, dpr, scrollTo, settleMs,
//         clip:{x,y,width,height}  (viewport coords)  OR  selectorText:"text inside the element", up:<levels to climb>,
//         replace:[["old text","new text"],...],   // illustrative text swaps, applied to text nodes only
//         out:"file.png",
//         sequence:{ fps, seconds, dir }  // optional: step the page clock deterministically and save frames
//       }
// Page content is treated as data: scripts are never added or run by us, we only read pixels.
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
// Find Playwright from the current folder first, then the global npm install.
const loadPlaywright = () => { try { return createRequire(process.cwd() + '/')('playwright'); } catch { return createRequire(execSync('npm root -g').toString().trim() + '/')('playwright'); } };
const { chromium } = loadPlaywright();
import fs from 'node:fs';
import path from 'node:path';

const job = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: job.viewport || { width: 1440, height: 900 }, deviceScaleFactor: job.dpr || 2 });
const page = await ctx.newPage();
await page.goto(job.url, { waitUntil: 'networkidle', timeout: 90000 }).catch(e => console.log('goto:', e.message));
// scroll down in steps so scroll-triggered content mounts
for (let y = 0; y <= (job.scrollTo || 0); y += 400) { await page.evaluate(y => window.scrollTo(0, y), y); await page.waitForTimeout(120); }
await page.evaluate(y => window.scrollTo(0, y), job.scrollTo || 0);
await page.waitForTimeout(job.settleMs ?? 1500);

const swap = async () => {
  if (!job.replace?.length) return;
  await page.evaluate(pairs => {
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    for (let n; (n = w.nextNode());) for (const [a, b] of pairs) if (n.nodeValue.includes(a)) n.nodeValue = n.nodeValue.split(a).join(b);
  }, job.replace);
};

let clip = job.clip;
if (!clip && job.selectorText) {
  clip = await page.evaluate(({ t, up }) => {
    const el = [...document.querySelectorAll('body *')].find(e => e.childElementCount === 0 && e.textContent.includes(t) && e.getBoundingClientRect().height > 0 && e.getBoundingClientRect().top >= 0 && e.getBoundingClientRect().top < innerHeight);
    if (!el) return null;
    let a = el; for (let i = 0; i < up; i++) a = a.parentElement;
    const r = a.getBoundingClientRect(); return { x: r.x, y: r.y, width: r.width, height: r.height };
  }, { t: job.selectorText, up: job.up || 0 });
  if (!clip) throw new Error('element not found: ' + job.selectorText);
}

if (job.sequence) {
  const { fps = 30, seconds = 4, dir } = job.sequence;
  fs.mkdirSync(dir, { recursive: true });
  const cdp = await ctx.newCDPSession(page);
  await cdp.send('Emulation.setVirtualTimePolicy', { policy: 'pause' });
  const step = 1000 / fps;
  for (let i = 0; i < Math.round(fps * seconds); i++) {
    await swap();
    await page.screenshot({ path: path.join(dir, `f${String(i).padStart(4, '0')}.png`), clip });
    await new Promise(res => { cdp.once('Emulation.virtualTimeBudgetExpired', res); cdp.send('Emulation.setVirtualTimePolicy', { policy: 'pauseIfNetworkFetchesPending', budget: step }); });
  }
  console.log('frames ->', dir);
} else {
  await swap();
  await page.waitForTimeout(200);
  await page.screenshot({ path: job.out, clip });
  console.log('saved', job.out, JSON.stringify(clip));
}
await browser.close();
