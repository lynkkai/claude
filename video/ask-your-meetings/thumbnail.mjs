// Build the YouTube thumbnail (1280x720) from the same design kit and avatar.
// Usage: node thumbnail.mjs <out.png>
import { createRequire } from 'module';
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
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 2 / 3 });
await page.goto('file://' + path.join(here, 'scenes.html'));
await page.evaluate(async (tl) => { await document.fonts.ready; window.init(tl); window.renderAt(52.3); }, timeline);
await page.evaluate(() => {
  document.querySelectorAll('.scene').forEach(s => s.style.display = 'none');
  document.getElementById('brand').style.display = 'none';
  const st = document.getElementById('stage');
  st.style.background = '#16181d';
  const av = document.getElementById('avatar');
  av.style.transform = 'translate(1240px, 250px) scale(1.55)';
  document.getElementById('avTag').style.display = 'none';
  document.getElementById('avRing').style.opacity = 0;
  const wrap = document.createElement('div');
  wrap.innerHTML = `
    <div style="position:absolute;left:96px;top:90px;font-family:Fraunces,serif;font-weight:600;font-size:64px;color:#fff">Lynkk</div>
    <div style="position:absolute;left:96px;top:250px;width:1150px;font-family:Fraunces,serif;font-weight:600;font-size:150px;line-height:.98;letter-spacing:-0.02em;color:#fff">Ask your meetings <span style="color:#aab4ff">anything.</span></div>
    <div style="position:absolute;left:96px;top:820px;padding:30px 40px;border-radius:30px 30px 30px 8px;background:#fff;color:#16181d;font-size:48px;font-weight:600;font-family:'IBM Plex Sans',sans-serif">"What did Acme say about pricing?"</div>`;
  st.appendChild(wrap);
});
await page.screenshot({ path: process.argv[2] });
await browser.close();
