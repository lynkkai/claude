// Run the post kit's copy and claims checker on the voiceover script.
//   node check_script.mjs
import fs from "node:fs";
import { lint, report } from "../../lynkk-post-kit/scripts/check.mjs";

const script = JSON.parse(fs.readFileSync(new URL("script.json", import.meta.url)));
const text = script.scenes.flatMap((s) => [s.chapter, ...s.lines.map((l) => l.text)]).join("\n");
const result = lint(`<p>${text}</p>`);
report("script.json", result);
process.exit(result.errors.length ? 1 : 0);
