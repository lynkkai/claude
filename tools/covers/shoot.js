const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 2 });
  for (const dir of ['out', 'out-light']) {
    if (!fs.existsSync(dir)) continue;
    for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.html'))) {
      const slug = f.replace(/\.html$/, '');
      await page.goto('file://' + path.resolve(dir, f));
      try { await page.evaluate(() => document.fonts.ready); } catch (e) {}
      await page.waitForTimeout(1500);
      await page.screenshot({ path: `${dir}/${slug}.png` });
    }
    console.log('shot', dir);
  }
  await browser.close();
})();
