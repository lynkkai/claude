// Usage: node capture.mjs <page.html> <outDir> <seconds> [fps] [width] [height]
// Renders window.render(t) frame by frame with a transparent background.
import { createRequire } from 'module';
const { chromium } = createRequire('/opt/node22/lib/node_modules/')('playwright');
import { mkdirSync } from 'fs';
import path from 'path';
const [page_, outDir, secs, fps = 30, w = 1920, h = 1080] = process.argv.slice(2);
mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: +w, height: +h } });
const [file, q = ''] = page_.split('?');
await page.goto('file://' + path.resolve(file) + (q ? '?' + q : ''));
await page.evaluate(() => document.fonts.ready);
const n = Math.round(+secs * +fps);
for (let i = 0; i < n; i++) {
  await page.evaluate((t) => window.render(t), i / +fps);
  await page.screenshot({ path: `${outDir}/f${String(i).padStart(4, '0')}.png`, omitBackground: true });
}
await browser.close();
console.log(`${n} frames -> ${outDir}`);
