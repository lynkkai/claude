const { chromium } = require('playwright');
(async () => {
  const [,, html, out, scale] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1500, height: 500 }, deviceScaleFactor: +scale });
  await p.goto('file://' + html);
  await p.waitForSelector('body[data-ready="1"]');
  await p.evaluate(() => document.fonts.ready);
  await p.locator('#b').screenshot({ path: out });
  await b.close();
})();
