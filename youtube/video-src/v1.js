// Video 1: Record and summarize in-person meetings (no device needed)
const PEOPLE=[
 {i:'M',n:'Maya',x:60,y:250,bg:'#e8eafb',c:'#3346d3'},
 {i:'D',n:'Dev',x:250,y:60,bg:'#dff1ee',c:'#0f766e'},
 {i:'S',n:'Sam',x:470,y:60,bg:'#f6e7dc',c:'#b4541f'},
 {i:'A',n:'Ana',x:660,y:250,bg:'#ececef',c:'#16181d'},
 {i:'J',n:'Jo',x:360,y:470,bg:'#e8eafb',c:'#2b3bb8'},
];
function room(t,{rec=0,bubbles=0,laptopIn=1,range=0}={}){
 let s=`<div style="position:relative;width:800px;height:600px">`;
 if(range>0){const r=1+.06*Math.sin(t*3);s+=`<div class="abs" style="left:${400-230*r}px;top:${300-200*r}px;width:${460*r}px;height:${400*r}px;border-radius:50%;border:3px dashed rgba(51,70,211,${(.45*range).toFixed(2)})"></div>`}
 s+=`<div class="abs" style="left:170px;top:170px;width:460px;height:260px;border-radius:130px;background:#ebe8df;border:2px solid var(--line2)"></div>`;
 PEOPLE.forEach((p,k)=>{
  s+=`<div class="abs col" style="left:${p.x}px;top:${p.y}px;width:84px;align-items:center;gap:6px"><div class="row" style="justify-content:center;width:84px;height:84px;border-radius:50%;background:${p.bg};color:${p.c};font-family:Fraunces;font-weight:600;font-size:34px;border:3px solid #fff;box-shadow:0 4px 14px rgba(22,24,29,.08)">${p.i}</div><div style="font-size:18px;color:var(--muted);font-weight:500">${p.n}</div></div>`;
  if(bubbles){const ph=(t*1.1+k*.7)%3; const on=ph<1.6?eo(ph/.3):0;
   s+=`<div class="abs card" style="left:${p.x+54}px;top:${p.y-44}px;padding:8px 14px;border-radius:14px;font-size:22px;color:var(--muted);${A(on,8,0,.2)}">• • •</div>`}
 });
 // laptop
 const glow=rec?(10+6*Math.sin(t*4)):0;
 s+=`<div class="abs" style="left:330px;top:250px;width:140px;height:96px;border-radius:12px;background:#16181d;${A(laptopIn,40)};box-shadow:0 0 0 ${glow.toFixed(1)}px rgba(51,70,211,${(.22*rec).toFixed(2)})"><div style="margin:8px;height:80px;border-radius:6px;background:#262a33;display:flex;align-items:center;justify-content:center;gap:8px">${rec?`<div style="width:12px;height:12px;border-radius:50%;background:var(--rec);opacity:${(.6+.4*Math.sin(t*6)).toFixed(2)}"></div><div style="color:#fff;font-weight:600;font-size:18px;letter-spacing:.06em">REC</div>`:''}</div></div>`;
 return s+`</div>`;
}
const leftText=(t,eyebrow,h1,lead,extra='',top=300)=>`<div class="abs col" style="left:140px;top:${top}px;width:780px;gap:28px">
 ${eyebrow?`<div class="eyebrow" style="${A(ap(t,.15))}">${eyebrow}</div>`:''}
 <h1 class="h1" style="${A(ap(t,.3))}">${h1}</h1>
 ${lead?`<p class="lead" style="${A(ap(t,.6))}">${lead}</p>`:''}${extra}</div>`;
const bullets=(t,items,start,gap=.5,icon=I.check('var(--accent)'))=>`<div class="col" style="gap:18px;margin-top:8px">${items.map((x,k)=>`<div class="row" style="gap:16px;font-size:28px;color:var(--ink);${A(ap(t,start+k*gap),16)}"><div class="row" style="justify-content:center;width:40px;height:40px;border-radius:50%;background:var(--soft);flex:0 0 40px">${icon}</div>${x}</div>`).join('')}</div>`;
const recPill=(t,secs)=>{const m=String(Math.floor(secs/60)).padStart(2,'0'),s=String(Math.floor(secs%60)).padStart(2,'0');return `<span class="pill" style="background:#fff;border:1px solid var(--line);font-size:22px;color:var(--ink)"><span style="width:12px;height:12px;border-radius:50%;background:var(--rec);opacity:${(.6+.4*Math.sin(t*6)).toFixed(2)}"></span>Recording · ${m}:${s}</span>`};

const TRANS=[
 {p:0,txt:'Let’s move the launch to March 12.',tag:'Decision',tc:'#3346d3',tb:'#e8eafb'},
 {p:1,txt:'I’ll update the landing page by Friday.',tag:'Task',tc:'#0f766e',tb:'#dff1ee'},
 {p:2,txt:'I can brief the sales team next week.',tag:'Task',tc:'#0f766e',tb:'#dff1ee'},
 {p:3,txt:'Can we keep the beta price for early users?',tag:'Open question',tc:'#b4541f',tb:'#f6e7dc'},
];
const avatar=(p,s=48)=>`<div class="row" style="justify-content:center;flex:0 0 ${s}px;width:${s}px;height:${s}px;border-radius:50%;background:${p.bg};color:${p.c};font-family:Fraunces;font-weight:600;font-size:${s*.42}px">${p.i}</div>`;

function notesCard(t,start,{compact=false}={}){
 const sec=(k)=>A(ap(t,start+k*.55),18);
 return `<div class="card col" style="width:${compact?620:780}px;padding:${compact?28:40}px;gap:${compact?16:24}px;box-sizing:border-box">
 <div class="row" style="justify-content:space-between;${sec(0)}"><div class="col" style="gap:6px"><div style="font-family:Fraunces;font-weight:600;font-size:${compact?28:36}px">Launch planning</div><div style="font-size:20px;color:var(--muted)">In person · Conference room · 18 min</div></div><span class="chip" style="background:var(--soft);color:var(--accent)">${I.check('var(--accent)',20)} Notes ready</span></div>
 <div class="col" style="gap:8px;${sec(1)}"><div class="eyebrow" style="font-size:16px">Summary</div><div style="font-size:${compact?21:24}px;line-height:1.5;color:var(--body)">Launch moves to March 12. The landing page and a sales briefing are the open items before launch.</div></div>
 ${compact?'':`<div class="col" style="gap:8px;${sec(2)}"><div class="eyebrow" style="font-size:16px">Decision</div><div style="font-size:24px;color:var(--ink)">Launch date: March 12</div></div>`}
 <div class="col" style="gap:12px;${sec(compact?2:3)}"><div class="eyebrow" style="font-size:16px">Action items</div>
  ${[['Update the landing page','Dev','Fri'],['Brief the sales team','Sam','Next week']].map(([a,o,d])=>`<div class="row" style="gap:14px;font-size:${compact?21:24}px"><div style="width:24px;height:24px;border-radius:7px;border:2px solid var(--line2)"></div><div style="flex:1">${a}</div><span class="chip" style="background:#f2f1ec;color:var(--body);font-size:18px">${o}</span><span style="font-size:18px;color:var(--muted);width:100px;text-align:right">${d}</span></div>`).join('')}
 </div></div>`;
}

setScenes([
 // 1. HOOK: the issue
 {d:4.8,r:(t)=>leftText(t,'In-person meetings','Your most important meetings happen in a room.','')+
  `<div class="abs" style="left:1020px;top:220px;${A(ap(t,.2),30)}">${room(t,{bubbles:1,laptopIn:0})}</div>`+
  `<div class="abs card row" style="left:1260px;top:770px;padding:20px 26px;gap:18px;${A(ap(t,1.9),24)}"><div class="row" style="justify-content:center;width:52px;height:52px;border-radius:14px;background:#f2f1ec">${I.laptop('var(--muted)',30)}</div><div class="col" style="gap:4px"><div style="font-size:22px;font-weight:600">AI note taker bot</div><div style="font-size:20px;color:var(--muted)">Waiting for a meeting link${'.'.repeat(1+Math.floor(t*2)%3)}</div></div></div>`+
  `<div class="abs" style="left:140px;top:640px;${A(ap(t,2.3))}"><p class="lead" style="width:760px">But most AI note takers only join <b style="color:var(--ink)">video calls</b>. So nobody writes down what was decided.</p></div>`},
 // 2. HOOK: the solution
 {d:5.6,r:(t)=>leftText(t,'The fix','Record it on your laptop.','Lynkk turns the conversation into notes and action items about 30 seconds after you stop.')+
  `<div class="abs" style="left:1020px;top:220px">${room(t,{rec:ap(t,.4),laptopIn:1})}</div>`+
  `<div class="abs" style="left:1140px;top:620px;${A(ap(t,2.2),40,0,.06)}">${notesCard(t,2.3,{compact:true})}</div>`},
 // 3. STEP 1
 {d:10.5,step:'Step 1 of 4',r:(t)=>leftText(t,'Set up','Put your laptop in the middle of the table.','',bullets(t,['Lid open, mic facing the room','Away from fans and coffee machines','Big room? Add a USB conference mic'],1.4,.9),250)+
  `<div class="abs" style="left:1020px;top:220px">${room(t,{laptopIn:ap(t,.6,.8),range:ap(t,1.4,.8)})}</div>`+
  `<div class="abs" style="left:1240px;top:840px;${A(ap(t,2.2))}"><span class="pill" style="background:var(--soft);color:var(--accent);font-size:22px">${I.mic('var(--accent)',22)} Built-in mic covers 4 to 6 people</span></div>`},
 // 4. STEP 2
 {d:11,step:'Step 2 of 4',r:(t)=>{const recOn=t>5.2;const secs=recOn?(t-5.2)*1:0;
  return leftText(t,'Consent first','Tell everyone, then hit record.','',
  `<div class="col" style="gap:16px;margin-top:10px">
   <div class="card" style="align-self:flex-start;padding:18px 24px;border-radius:18px 18px 18px 6px;font-size:26px;max-width:640px;${A(ap(t,1.2),16)}">“Mind if I take AI notes so we don’t miss any action items?”</div>
   <div class="card" style="align-self:flex-end;margin-right:60px;padding:18px 24px;border-radius:18px 18px 6px 18px;font-size:26px;background:var(--soft);border-color:var(--soft);${A(ap(t,2.6),16)}">“Sure, send them to us after!”</div></div>`,250)+
  `<div class="abs card col" style="left:1080px;top:250px;width:680px;padding:40px;gap:30px;box-sizing:border-box;${A(ap(t,.4),30)}">
    <div class="row" style="justify-content:space-between"><div style="font-family:Fraunces;font-weight:600;font-size:34px">New meeting</div><span class="chip" style="background:#f2f1ec;color:var(--muted)">In person</span></div>
    <div class="col" style="gap:8px"><div style="font-size:20px;color:var(--muted)">Title</div><div style="font-size:28px;border:1px solid var(--line);border-radius:12px;padding:14px 18px">${typed('Launch planning',t,1,18,!recOn)}</div></div>
    <div class="row" style="height:64px;gap:20px">${recOn?recPill(t,secs)+wave(t,22,48):`<div style="font-size:22px;color:var(--muted)">Ready when you are</div>`}</div>
    <div class="row" style="justify-content:center;height:88px;border-radius:16px;font-size:30px;font-weight:600;gap:14px;${recOn?'background:#fff;border:2px solid var(--line2);color:var(--ink)':`background:var(--accent);color:#fff;transform:scale(${t>4.6&&t<5.2?.96:1})`}">${recOn?'<span style="width:22px;height:22px;border-radius:5px;background:var(--rec)"></span> Stop':I.mic('#fff',30)+' Start recording'}</div>
  </div>`+
  (t>3.8&&t<5.6?`<div class="abs" style="left:${1380+(1-ap(t,3.8,.8))*160}px;top:${640+(1-ap(t,3.8,.8))*140}px">${I.cursor('var(--ink)',40)}</div>`:'')}},
 // 5. STEP 3
 {d:14,step:'Step 3 of 4',r:(t)=>leftText(t,'Meet','Talk normally.','Make decisions. Assign tasks. Ask questions. Lynkk captures all of it.',
  `<div class="row" style="gap:16px;margin-top:6px;${A(ap(t,1))}"><span class="pill" style="background:#fff;border:1px solid var(--line);font-size:22px">${I.wifioff('var(--accent)',24)} Works offline</span><span class="pill" style="background:#fff;border:1px solid var(--line);font-size:22px">${I.globe('var(--accent)',24)} Multilingual</span></div>`,280)+
  `<div class="abs card col" style="left:1020px;top:200px;width:760px;padding:36px;gap:22px;box-sizing:border-box;${A(ap(t,.3),30)}">
   <div class="row" style="justify-content:space-between">${recPill(t,63+t)}${wave(t,16,40)}</div>
   <div style="height:1px;background:var(--line)"></div>
   ${TRANS.map((l,k)=>{const st=1+k*2.7;const p=PEOPLE[l.p];return `<div class="row" style="gap:18px;align-items:flex-start;${A(ap(t,st),16)}">${avatar(p)}<div class="col" style="gap:8px;flex:1"><div style="font-size:18px;font-weight:600;color:var(--muted)">${p.n}</div><div style="font-size:26px;line-height:1.4">${typed(l.txt,t,st+.1,34,false)}</div></div><span class="chip" style="background:${l.tb};color:${l.tc};${A(ap(t,st+1.3),0,0,.3)}">${l.tag}</span></div>`}).join('')}
  </div>`},
 // 6. STEP 4
 {d:14,step:'Step 4 of 4',r:(t)=>{const done=t>4.4;const pr=clamp((t-1.6)/2.6);
  return leftText(t,'Done','Stop. Your notes are ready.','Summary, decisions and action items with owners, about 30 seconds later. Searchable with all your other meetings.')+
  (done?`<div class="abs" style="left:1000px;top:150px">${notesCard(t,4.5)}</div>`:
  `<div class="abs card col" style="left:1060px;top:340px;width:660px;padding:44px;gap:26px;box-sizing:border-box;${A(ap(t,.3),30)}">
    <div class="row" style="gap:16px"><span class="chip" style="background:var(--soft);color:var(--accent)">About 30 seconds later</span></div>
    <div style="font-family:Fraunces;font-weight:600;font-size:36px">Writing your notes…</div>
    <div style="height:14px;border-radius:999px;background:#f2f1ec;overflow:hidden"><div style="height:100%;width:${(pr*100).toFixed(1)}%;background:var(--accent);border-radius:999px"></div></div>
    <div class="col" style="gap:12px;font-size:24px;color:var(--muted)">${['Summarizing the discussion','Finding decisions','Assigning action items'].map((x,k)=>`<div class="row" style="gap:12px;opacity:${pr>k*.33?1:.35}">${pr>(k+1)*.33?I.check('var(--accent)',24):'<span style="width:24px"></span>'}${x}</div>`).join('')}</div>
  </div>`)}},
 // 7. APP VS GADGET
 {d:11,r:(t)=>`<div class="abs col" style="left:0;right:0;top:150px;align-items:center;gap:20px;text-align:center"><div class="eyebrow" style="${A(ap(t,.1))}">No gadget needed</div><h1 class="h1" style="${A(ap(t,.25))}">Your laptop is already the recorder.</h1></div>
  <div class="abs row" style="left:200px;right:200px;top:420px;gap:40px;align-items:stretch">
   <div class="card col" style="flex:1;padding:44px;gap:24px;background:#fbfaf7;box-shadow:none;${A(ap(t,.9),30)}"><div style="font-size:30px;font-weight:600;color:var(--muted)">AI recorder gadget</div>
    ${['One more device to buy, carry and charge','Notes live in a separate app','Online calls need a different tool'].map((x,k)=>`<div class="row" style="gap:16px;font-size:27px;color:var(--body);${A(ap(t,1.5+k*.5),14)}">${I.x('var(--muted)',26)}${x}</div>`).join('')}</div>
   <div class="card col" style="flex:1;padding:44px;gap:24px;border:2px solid var(--accent);${A(ap(t,1.2),30)}"><div style="font-size:30px;font-weight:600;color:var(--accent)">Lynkk on your laptop</div>
    ${['Uses the laptop you already bring','In-person and online meetings in one place','Every meeting searchable later'].map((x,k)=>`<div class="row" style="gap:16px;font-size:27px;color:var(--ink);${A(ap(t,3+k*.5),14)}">${I.check('var(--accent)',26)}${x}</div>`).join('')}</div>
  </div>`},
 // 8. CONSENT REMINDER
 {d:6.5,r:(t)=>`<div class="abs col" style="left:0;right:0;top:330px;align-items:center;gap:30px;text-align:center"><div class="eyebrow" style="${A(ap(t,.1))}">One rule</div><h1 class="h1" style="max-width:1400px;${A(ap(t,.25))}">Always tell people you’re recording.</h1><p class="lead" style="max-width:1100px;${A(ap(t,.7))}">Some places require everyone’s consent. A quick “mind if I take AI notes?” works, and people love getting the summary afterwards.</p></div>`},
 // 9. CTA
 {d:8,bg:'var(--soft)',noMark:1,r:(t)=>`<div class="abs col" style="left:0;right:0;top:260px;align-items:center;gap:36px;text-align:center"><div style="font-family:Fraunces;font-weight:600;font-size:64px;${A(ap(t,.1))}">Lynkk</div><h1 class="h1" style="max-width:1300px;${A(ap(t,.3))}">Record your next in-person meeting.</h1><p class="lead" style="${A(ap(t,.6))}">Notes and action items in about 30 seconds. Online or in person.</p><div style="margin-top:16px;${A(ap(t,1),20,0,.1)}">${cta('Start free at lynkk.ai')}</div></div>`},
]);
