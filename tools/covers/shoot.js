const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 2 });
  for (const f of fs.readdirSync('out').filter(f => f.endsWith('.html'))) {
    const slug = f.replace(/\.html$/, '');
    await page.goto('file://' + path.resolve('out', f));
    try { await page.evaluate(() => document.fonts.ready); } catch (e) {}
    await page.waitForTimeout(1800);
    await page.screenshot({ path: `out/${slug}.png` });
    console.log('shot', slug);
  }
  await browser.close();
})();
