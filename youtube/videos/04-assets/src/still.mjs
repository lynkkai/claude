// Usage: node still.mjs <page.html?query> <out.png> [width] [height] [alpha]
import { createRequire } from 'module';
const { chromium } = createRequire('/opt/node22/lib/node_modules/')('playwright');
import path from 'path';
const [page_, out, w = 1920, h = 1080, alpha = '1'] = process.argv.slice(2);
const [file, q = ''] = page_.split('?');
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: +w, height: +h } });
await page.goto('file://' + path.resolve(file) + (q ? '?' + q : ''));
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: out, omitBackground: alpha === '1' });
await browser.close();
