// Claude Code PostToolUse hook: runs the copy and claims check on any Lynkk
// design or video file right after it is written, so a false claim, a
// competitor name or an em dash is caught before it ships.
// Wired up in .claude/settings.json. Reads the hook payload on stdin.
// Exit 2 sends the errors back to Claude; 0 means clean or not a Lynkk file.
import fs from "node:fs";
import path from "node:path";
import { lint } from "./check.mjs";

const WATCHED = [/(^|\/)youtube\/videos\//, /(^|\/)lynkk-post-kit\/posts\//];
const EXTS = new Set([".html", ".md", ".srt", ".txt"]);

let payload = "";
for await (const chunk of process.stdin) payload += chunk;
let file;
try { file = JSON.parse(payload)?.tool_input?.file_path; } catch { process.exit(0); }
if (!file || !EXTS.has(path.extname(file)) || !WATCHED.some((re) => re.test(file)) || !fs.existsSync(file)) process.exit(0);

const { errors, warnings } = lint(fs.readFileSync(file, "utf8"));
if (!errors.length) {
  if (warnings.length) console.log(`Lynkk copy check: ${warnings.length} warning(s) in ${file}. Review them.`);
  process.exit(0);
}
console.error(`Lynkk guardrail: ${file} breaks lynkk-post-kit/docs/TRUTHS.md or COPY.md. Fix before continuing:`);
for (const e of errors) console.error(`  ERROR ${e}`);
for (const w of warnings) console.error(`  warn  ${w}`);
process.exit(2);
