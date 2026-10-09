// Run the post kit's copy and claims checker on the voiceover script.
//   node check_script.mjs <video-dir>
import fs from "node:fs";
import path from "node:path";
import { lint, report } from "../../lynkk-post-kit/scripts/check.mjs";

const dir = path.resolve(process.argv[2] ?? ".");
const script = JSON.parse(fs.readFileSync(path.join(dir, "script.json"), "utf8"));
const text = script.scenes.flatMap((s) => [s.chapter, ...s.lines.map((l) => l.text)]).join("\n");
const result = lint(`<p>${text}</p>`);
report(path.join(dir, "script.json"), result);
process.exit(result.errors.length ? 1 : 0);
