// Render the kit boards of a video page, timed by timing.json (from tts.py). Adapted from
// ask-lynkk-video/capture.mjs.
//   node capture.mjs video  <page.html> <timing.json> <out.mp4>    every scene in order, one silent MP4
//   node capture.mjs stills <page.html> <timing.json> <outDir>     one PNG per scene, after its last reveal
// Wide boards (1600x900) are captured at 1.2x = 1920x1080; story boards (1080x1920) at 1x.
import { createRequire } from "node:module";
import { spawn } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.resolve(here, "../../../lynkk-post-kit/package.json"));
const { chromium } = require("playwright");

const [mode, pageFile, timingFile, out] = process.argv.slice(2); // argv[6]: "mid" for stills
const timing = JSON.parse(fs.readFileSync(timingFile, "utf8"));
const FPS = 30;
const browser = await chromium.launch({ executablePath: process.env.CHROME || undefined });

let page;
async function open() {
  if (page) await page.close().catch(() => {});
  const probe = fs.readFileSync(pageFile, "utf8");
  const story = /data-size="story"/.test(probe);
  page = await browser.newPage(story
    ? { viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 1 }
    : { viewport: { width: 1800, height: 1100 }, deviceScaleFactor: 1.2 });
  await page.goto("file://" + path.resolve(pageFile), { waitUntil: "networkidle" });
  await page.waitForFunction(() => document.documentElement.dataset.ready === "1");
  await page.evaluate(() => document.fonts.ready);
}
await open();

// One frame. A hung page is replaced and the frame retried, so a long capture can't stall.
async function frame(id, t, opts) {
  for (let attempt = 0; ; attempt++) {
    try {
      await page.evaluate(([id, t, tm]) => {
        document.querySelectorAll("section.post").forEach((s) => (s.style.display = s.id === id ? "" : "none"));
        window.render(id, t, tm);
      }, [id, t, timing[id]]);
      return await page.locator(`#${id}`).screenshot({ timeout: 30000, ...opts });
    } catch (e) {
      if (attempt >= 3) throw e;
      console.log(`retrying ${id} at ${t.toFixed(2)}s: ${e.message.split("\n")[0]}`);
      await open();
    }
  }
}

const ids = timing._order;
if (mode === "stills") {
  fs.mkdirSync(out, { recursive: true });
  // "mid" (5th arg): halfway through the last line, so the Shorts caption shows
  const mid = process.argv[6] === "mid";
  for (const id of ids) {
    const tm = timing[id], last = tm.starts.length - 1;
    const t = mid ? (tm.starts[last] + tm.ends[last]) / 2 : tm.duration - 0.4;
    await frame(id, t, { path: path.join(out, `${id}.png`) });
  }
} else {
  const ff = spawn("ffmpeg", ["-loglevel", "error", "-y", "-f", "image2pipe", "-framerate", String(FPS), "-c:v", "mjpeg", "-i", "-",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium", "-r", String(FPS), out], { stdio: ["pipe", "inherit", "inherit"] });
  const closed = new Promise((r) => ff.on("close", r));
  for (const id of ids) {
    const n = Math.round(timing[id].duration * FPS);
    for (let i = 0; i < n; i++) {
      const buf = await frame(id, i / FPS, { type: "jpeg", quality: 95 });
      if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once("drain", r));
    }
    console.log(`${id}: ${n} frames`);
  }
  ff.stdin.end();
  await closed;
}
await browser.close();
