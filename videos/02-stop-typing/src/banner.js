// Renders the banner in each social size: node src/banner.js
const { chromium } = require('playwright');
const path = require('path');
const SIZES = [
  { name: 'banner-1200x628.png', w: 1200, h: 628, q: '' },                         // LinkedIn, Facebook, X link posts
  { name: 'banner-1280x720.png', w: 1280, h: 720, q: '?h=675&scale=1.0666667' },   // YouTube thumbnail
  { name: 'banner-1080x1350.png', w: 1080, h: 1350, q: '?layout=portrait' },        // Instagram feed
  { name: 'reel-cover-1080x1920.png', w: 1080, h: 1920, q: '?layout=reel' },        // Reels / Shorts cover
];
(async () => {
  const browser = await chromium.launch();
  for (const s of SIZES) {
    const page = await browser.newPage({ viewport: { width: s.w, height: s.h } });
    await page.goto('file://' + path.join(__dirname, 'banner.html') + s.q);
    await page.evaluate(() => window.ready);
    await page.screenshot({ path: path.join(__dirname, '..', 'banners', s.name) });
    console.log('wrote', s.name);
  }
  await browser.close();
})();
