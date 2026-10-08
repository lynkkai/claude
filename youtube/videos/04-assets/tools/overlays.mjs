// Render every [data-id] overlay in overlays.html to a transparent 1920x1080 PNG.
//   node tools/overlays.mjs   (run from 04-assets/)
import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
const require = createRequire(path.resolve("../../../lynkk-post-kit/package.json"));
let chromium;
try { ({ chromium } = require("playwright")); } catch { ({ chromium } = createRequire(import.meta.url)("playwright")); }

fs.mkdirSync("out/overlays", { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
await page.goto("file://" + path.resolve("overlays.html"), { waitUntil: "networkidle" });
await page.waitForFunction(() => document.documentElement.dataset.ready === "1");
await page.evaluate(() => document.fonts.ready);
const ids = await page.$$eval(".ov", (els) => els.map((e) => e.dataset.id));
for (const id of ids) {
  await page.evaluate((id) => document.querySelectorAll(".ov").forEach((e) => e.classList.toggle("show", e.dataset.id === id)), id);
  await page.screenshot({ path: `out/overlays/${id}.png`, omitBackground: true });
  console.log(`wrote out/overlays/${id}.png`);
}
await browser.close();
