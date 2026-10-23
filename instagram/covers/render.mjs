// Renders Instagram Reel covers (1080x1920 PNG) from covers.json.
// Usage: node render.mjs [--guides] [id ...]
//   --guides  draw the 3:4 grid crop (cyan) and 4:5 feed crop (yellow) for checking layout
//   id ...    only render these cover ids (default: all)
import { readFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
let chromium;
try {
  ({ chromium } = require('playwright'));
} catch {
  ({ chromium } = require('/opt/node-tools/node_modules/playwright'));
}

const here = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const guides = args.includes('--guides');
const only = args.filter((a) => !a.startsWith('--'));

const covers = JSON.parse(readFileSync(join(here, 'covers.json'), 'utf8'))
  .filter((c) => only.length === 0 || only.includes(c.id));
const logo = readFileSync(join(here, 'logo-mark.svg'), 'utf8');
const outDir = join(here, guides ? 'out/guides' : 'out');
mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });

for (const cover of covers) {
  await page.goto(pathToFileURL(join(here, 'template.html')).href);
  await page.evaluate(({ cover, logo, guides }) => {
    const esc = (s) => s.replace(/[&<>"]/g, (ch) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[ch]);
    // *word* in the title is drawn in the accent color
    const title = esc(cover.title).replace(/\*([^*]+)\*/g, '<em>$1</em>');
    const accent = cover.accent === 'violet' ? 'violet-ink' : (cover.accent || 'lavender');
    document.documentElement.style.setProperty('--accent', `var(--${accent})`);
    document.getElementById('logo').innerHTML = logo;
    document.getElementById('eyebrow').textContent = cover.eyebrow || '';
    document.getElementById('title').innerHTML = title;
    document.getElementById('sub').textContent = cover.sub || '';
    if (cover.live) document.getElementById('dot').classList.add('live');
    if (guides) document.getElementById('guides').classList.add('on');
  }, { cover, logo, guides });
  await page.evaluate(() => document.fonts.ready);
  const file = join(outDir, `${cover.id}.png`);
  await page.screenshot({ path: file });
  console.log(file);
}

await browser.close();
