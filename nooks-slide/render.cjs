const { chromium } = require('/opt/node22/lib/node_modules/playwright/node_modules/playwright-core');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--no-sandbox'] });
  const page = await browser.newPage({ viewport:{ width:1920, height:1080 }, deviceScaleFactor:2 });
  await page.goto('file://' + __dirname + '/nooks-slide.html');
  await page.waitForTimeout(400);
  await page.screenshot({ path: 'nooks-slide.png' });
  await browser.close();
  console.log('rendered');
})();
