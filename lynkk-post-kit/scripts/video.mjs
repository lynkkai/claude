// Render a video post (one board whose page defines window.__seek(t)) to MP4.
//   node scripts/video.mjs posts/my-video                       (reads posts/my-video/post.html)
//   node scripts/video.mjs posts/my-video --audio posts/my-video/out/mix.wav
//   node scripts/video.mjs posts/my-video --stills 2,9.5,11.6   (PNGs at those seconds, no video)
//   --fps 30      frames per second (default 30)
//   --scale 1     render scale; 2 renders at 2x and downsamples to the board size (smoother edges)
//   --force       render even if the copy check finds errors
//
// Output: <folder>/out/video.mp4 (H.264, plus AAC audio when --audio is given)
// and <folder>/out/still-<t>.png for --stills. Needs ffmpeg on PATH.
import fs from "node:fs";
import path from "node:path";
import { spawn } from "node:child_process";
import { chromium } from "playwright";
import { lint, report } from "./check.mjs";

const args = process.argv.slice(2);
const flag = (name) => args.includes(`--${name}`);
const opt = (name) => { const i = args.indexOf(`--${name}`); return i >= 0 ? args[i + 1] : undefined; };
const valued = ["--audio", "--fps", "--scale", "--stills"];
const target = args.find((a, i) => !a.startsWith("--") && !valued.includes(args[i - 1]));
if (!target) {
  console.log("usage: node scripts/video.mjs posts/<name> [--audio file.wav] [--stills 1,2.5] [--fps 30] [--scale 1] [--force]");
  process.exit(2);
}
const file = path.resolve(fs.statSync(target).isDirectory() ? path.join(target, "post.html") : target);
const outDir = path.join(path.dirname(file), "out");
const fps = Number(opt("fps") ?? 30);
const scale = Number(opt("scale") ?? 1);
const audio = opt("audio");
const stills = opt("stills")?.split(",").map(Number);

console.log(`\n${path.relative(process.cwd(), file)}`);
const copy = lint(fs.readFileSync(file, "utf8"));
report(file, copy);
if (copy.errors.length && !flag("force")) {
  console.log("\nCopy check failed. Fix the errors above (or pass --force to render anyway).");
  process.exit(1);
}

// Cloud sessions ship Chromium in /opt/pw-browsers; use it when Playwright's own build is missing.
const launch = async () => {
  try { return await chromium.launch(); }
  catch (e) {
    const exe = "/opt/pw-browsers/chromium";
    if (!fs.existsSync(exe)) throw e;
    return chromium.launch({ executablePath: exe });
  }
};

const browser = await launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: scale });
const pageWarnings = [];
page.on("console", (m) => { if (["warning", "error"].includes(m.type())) pageWarnings.push(m.text()); });
page.on("pageerror", (e) => pageWarnings.push(String(e)));
page.on("requestfailed", (r) => pageWarnings.push(`failed to load ${r.url()}`));

await page.goto(`file://${file}?still`, { waitUntil: "networkidle" });
await page.waitForFunction(() => document.documentElement.dataset.ready === "1" && typeof window.__seek === "function", null, { timeout: 5000 });
await page.addStyleTag({ content: "html, body { background: none !important } body { display: block !important; padding: 0 !important }" });
await page.evaluate(() => document.fonts.ready);
const duration = await page.evaluate(() => window.__duration);
const board = page.locator("section.post").first();
const box = await board.boundingBox();
await page.setViewportSize({ width: Math.round(box.width), height: Math.round(box.height) });
const clip = { x: 0, y: 0, width: Math.round(box.width), height: Math.round(box.height) };
const pose = async (t) => { await page.evaluate((t) => window.__seek(t), t); };

fs.mkdirSync(outDir, { recursive: true });

if (stills) {
  for (const t of stills) {
    await pose(t);
    await page.waitForTimeout(30);
    const png = path.join(outDir, `still-${String(t).replace(".", "_")}.png`);
    await page.screenshot({ path: png, clip });
    console.log(`  wrote ${path.relative(process.cwd(), png)}`);
  }
} else {
  const mp4 = path.join(outDir, "video.mp4");
  const ff = [
    "-y", "-loglevel", "error",
    "-f", "image2pipe", "-framerate", String(fps), "-i", "-",
    ...(audio ? ["-i", audio] : []),
    "-vf", `scale=${clip.width}:-2:flags=lanczos,format=yuv420p`,
    "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-tune", "animation", "-movflags", "+faststart",
    ...(audio ? ["-c:a", "aac", "-b:a", "192k", "-shortest"] : []),
    mp4,
  ];
  const enc = spawn("ffmpeg", ff, { stdio: ["pipe", "inherit", "inherit"] });
  const frames = Math.round(duration * fps);
  const started = Date.now();
  for (let i = 0; i < frames; i++) {
    await pose(i / fps);
    const buf = await page.screenshot({ clip, type: "png" });
    if (!enc.stdin.write(buf)) await new Promise((r) => enc.stdin.once("drain", r));
    if (i % fps === 0) process.stdout.write(`\r  frame ${i}/${frames}  (${((Date.now() - started) / 1000).toFixed(0)} s)`);
  }
  enc.stdin.end();
  const code = await new Promise((r) => enc.on("close", r));
  process.stdout.write("\n");
  if (code !== 0) { console.log("  ffmpeg failed"); process.exit(1); }
  console.log(`  wrote ${path.relative(process.cwd(), mp4)}  (${frames} frames, ${fps} fps, ${clip.width}x${clip.height}${audio ? ", with audio" : ""})`);
}
for (const w of new Set(pageWarnings)) console.log(`  \x1b[33mpage\x1b[0m  ${w}`);
await browser.close();
