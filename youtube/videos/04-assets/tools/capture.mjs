// Frame capture for kit-built video graphics.
//   node tools/capture.mjs <page.html> <framesDir> <seconds> [fps=30]
// Each page holds one wide (1600x900) <section class="post"> and defines
// window.render(t). Frames are captured at 1.2x, which gives 1920x1080.
// Encode afterwards with ffmpeg (see README.md).
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
const require = createRequire(path.resolve("../../../lynkk-post-kit/package.json"));
let chromium;
try { ({ chromium } = require("playwright")); } catch { ({ chromium } = createRequire(import.meta.url)("playwright")); }

const [page_, outDir, secs, fps = 30] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1800, height: 1100 }, deviceScaleFactor: 1.2 });
await page.goto("file://" + path.resolve(page_), { waitUntil: "networkidle" });
await page.waitForFunction(() => document.documentElement.dataset.ready === "1", null, { timeout: 5000 });
await page.evaluate(() => document.fonts.ready);
const board = page.locator("section.post").first();
const n = Math.round(+secs * +fps);
for (let i = 0; i < n; i++) {
  await page.evaluate((t) => window.render(t), i / +fps);
  await board.screenshot({ path: `${outDir}/f${String(i).padStart(4, "0")}.png` });
}
await browser.close();
console.log(`${n} frames -> ${outDir}`);
