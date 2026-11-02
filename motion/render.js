const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
(async()=>{
  const out=process.argv[3]; fs.mkdirSync(out,{recursive:true});
  const DUR=6800, FPS=60, N=Math.round(DUR/1000*FPS);
  const b=await chromium.launch({args:['--force-device-scale-factor=1','--hide-scrollbars']});
  const p=await b.newPage({viewport:{width:1920,height:1080},deviceScaleFactor:1});
  await p.goto('file://'+path.resolve(process.argv[2]));
  await p.waitForTimeout(600);
  for(let i=0;i<N;i++){
    await p.evaluate(t=>window.__seek(t), i*1000/FPS);
    await p.screenshot({path:`${out}/f_${String(i).padStart(4,'0')}.png`});
  }
  await b.close(); console.log('frames',N);
})();
