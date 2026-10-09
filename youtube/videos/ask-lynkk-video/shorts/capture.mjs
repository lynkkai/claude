// Render scenes of video.html, timed by out/timing.json.
//   node capture.mjs video <outDir> s1 s2 ...     one MP4 per scene (1080x1920, 30 fps)
//   node capture.mjs stills <outDir> s1 s2 ...    one PNG per scene, after its last reveal
// Story boards (1080x1920) at 1x, for YouTube Shorts.
import { createRequire } from "node:module";
import { spawn } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
const require = createRequire(path.resolve("../../../../lynkk-post-kit/package.json"));
let chromium;
try { ({ chromium } = require("playwright")); } catch { ({ chromium } = createRequire(import.meta.url)("playwright")); }

const [mode, root, ...ids] = process.argv.slice(2);
const timing = JSON.parse(fs.readFileSync("out/timing.json", "utf8"));

const FPS = 30;
fs.mkdirSync(root, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 1 });
await page.goto("file://" + path.resolve("short.html"), { waitUntil: "networkidle" });
await page.waitForFunction(() => document.documentElement.dataset.ready === "1");
await page.evaluate(() => document.fonts.ready);
for (const id of ids) {
  await page.evaluate((id) => document.querySelectorAll("section.post").forEach((s) => (s.style.display = s.id === id ? "" : "none")), id);
  const board = page.locator(`#${id}`);
  const tm = timing[id];
  if (mode === "stills") {
    await page.evaluate(([id, t, tm]) => window.render(id, t, tm), [id, tm.duration - 0.5, tm]);
    await board.screenshot({ path: path.join(root, `${id}.png`) });
    continue;
  }
  const ff = spawn("ffmpeg", ["-loglevel", "error", "-y", "-f", "image2pipe", "-framerate", String(FPS), "-c:v", "mjpeg", "-i", "-",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", "-r", String(FPS), path.join(root, `${id}.mp4`)], { stdio: ["pipe", "inherit", "inherit"] });
  const n = Math.round(tm.duration * FPS);
  for (let i = 0; i < n; i++) {
    await page.evaluate(([id, t, tm]) => window.render(id, t, tm), [id, i / FPS, tm]);
    const buf = await board.screenshot({ type: "jpeg", quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once("drain", r));
  }
  ff.stdin.end();
  await new Promise((r) => ff.on("close", r));
  console.log(`${id}: ${n} frames`);
}
await browser.close();
