const { chromium } = require('playwright'); const http=require('http'),fs=require('fs'),path=require('path');
const ROOT=path.join(__dirname,'build'); const M={'.html':'text/html','.css':'text/css','.js':'application/javascript','.woff2':'font/woff2'};
const srv=http.createServer((q,r)=>{const f=path.join(ROOT,q.url.split('?')[0]);fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return}r.writeHead(200,{'Content-Type':M[path.extname(f)]||'application/octet-stream'});r.end(d)})});
(async()=>{await new Promise(r=>srv.listen(8766,r));const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:2700}});
await p.goto('http://localhost:8766/thumb.html',{waitUntil:'networkidle'});await p.evaluate(()=>window.ready);
const out=process.argv[2];await (await p.$('#yt')).screenshot({path:out+'/youtube-thumbnail.png'});await (await p.$('#ig')).screenshot({path:out+'/instagram-reel-cover.png'});
await b.close();srv.close();})();
