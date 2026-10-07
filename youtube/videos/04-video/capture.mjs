// Render scenes of video.html to PNG frames, timed by out/timing.json.
//   node capture.mjs <framesRoot> s1 s2 ...
// Wide boards (1600x900) at 1.2x = 1920x1080, 30 fps.
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
const require = createRequire(path.resolve("../../../lynkk-post-kit/package.json"));
let chromium;
try { ({ chromium } = require("playwright")); } catch { ({ chromium } = createRequire(import.meta.url)("playwright")); }

const [root, ...ids] = process.argv.slice(2);
const timing = JSON.parse(fs.readFileSync("out/timing.json", "utf8"));
const FPS = 30;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1800, height: 1100 }, deviceScaleFactor: 1.2 });
await page.goto("file://" + path.resolve("video.html"), { waitUntil: "networkidle" });
await page.waitForFunction(() => document.documentElement.dataset.ready === "1");
await page.evaluate(() => document.fonts.ready);
for (const id of ids) {
  const dir = path.join(root, id);
  fs.mkdirSync(dir, { recursive: true });
  await page.evaluate((id) => document.querySelectorAll("section.post").forEach((s) => (s.style.display = s.id === id ? "" : "none")), id);
  const board = page.locator(`#${id}`);
  const n = Math.round(timing[id].duration * FPS);
  for (let i = 0; i < n; i++) {
    await page.evaluate(([id, t, tm]) => window.render(id, t, tm), [id, i / FPS, timing[id]]);
    await board.screenshot({ path: `${dir}/f${String(i).padStart(5, "0")}.png` });
  }
  console.log(`${id}: ${n} frames`);
}
await browser.close();
