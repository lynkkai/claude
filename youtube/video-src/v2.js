// Video 2: Voice typing in Google Docs on Mac (+ fixes, + dictate anywhere)
const leftText=(t,eyebrow,h1,lead,extra='',top=300,w=780)=>`<div class="abs col" style="left:140px;top:${top}px;width:${w}px;gap:28px">
 ${eyebrow?`<div class="eyebrow" style="${A(ap(t,.15))}">${eyebrow}</div>`:''}
 <h1 class="h1" style="${A(ap(t,.3))}">${h1}</h1>
 ${lead?`<p class="lead" style="${A(ap(t,.6))}">${lead}</p>`:''}${extra}</div>`;

function micWidget(t,state){ // state: 'off' | 'on'
 const on=state==='on';const ring=on?(.5+.5*Math.sin(t*5)):0;
 return `<div class="row" style="justify-content:center;width:76px;height:76px;border-radius:50%;background:${on?'var(--rec)':'#fff'};border:1px solid ${on?'var(--rec)':'var(--line2)'};box-shadow:0 0 0 ${(on?6+8*ring:0).toFixed(1)}px rgba(194,65,45,${(on?.18:0).toFixed(2)}),0 6px 18px rgba(22,24,29,.10)">${I.mic(on?'#fff':'var(--muted)',34)}</div>`;
}
function browser(t,{text='',mic=null,menu=0,hi=-1,toast=0,w=820,h=620,cursorAt=null}={}){
 const items=['Spelling and grammar','Word count','Voice typing','Dictionary'];
 return `<div class="card" style="position:relative;width:${w}px;height:${h}px;overflow:hidden;border-radius:18px">
  <div class="row" style="height:56px;gap:10px;padding:0 20px;border-bottom:1px solid var(--line);background:#fbfaf7">
   ${['#e4e2da','#e4e2da','#e4e2da'].map(c=>`<div style="width:14px;height:14px;border-radius:50%;background:${c}"></div>`).join('')}
   <div style="margin-left:16px;flex:1;height:34px;border-radius:999px;background:#f2f1ec;display:flex;align-items:center;padding:0 18px;font-size:18px;color:var(--muted)">docs.google.com/document/…</div></div>
  <div class="row" style="height:50px;gap:26px;padding:0 28px;font-size:19px;color:var(--body);border-bottom:1px solid var(--line)">${['File','Edit','View','Insert','Format','Tools','Extensions','Help'].map(m=>`<span style="${m==='Tools'&&menu>0?'background:var(--soft);color:var(--accent);border-radius:8px;padding:4px 8px;margin:0 -8px':''}">${m}</span>`).join('')}</div>
  <div style="position:absolute;left:0;right:0;top:106px;bottom:0;background:#f2f1ec">
   <div style="position:absolute;left:70px;right:70px;top:30px;bottom:0;background:#fff;border:1px solid var(--line);padding:56px 60px;font-size:27px;line-height:1.55;color:var(--ink)">${text}</div>
   ${mic?`<div class="abs" style="right:28px;top:56px">${micWidget(t,mic)}</div>`:''}
  </div>
  ${menu>0?`<div class="abs card col" style="left:330px;top:100px;width:420px;padding:10px;border-radius:14px;${A(menu,-10)}">${items.map((x,k)=>`<div class="row" style="justify-content:space-between;padding:14px 16px;border-radius:10px;font-size:21px;${k===2&&hi>0?`background:var(--soft);color:var(--accent);font-weight:600`:'color:var(--body)'}">${x}${k===2?`<span style="font-size:18px;color:${hi>0?'var(--accent)':'var(--muted)'}">⌘ Shift S</span>`:''}</div>`).join('')}</div>`:''}
  ${toast>0?`<div class="abs row" style="left:50%;bottom:36px;transform:translateX(-50%) translateY(${((1-toast)*20).toFixed(1)}px);opacity:${toast.toFixed(2)};gap:12px;background:var(--ink);color:#fff;border-radius:12px;padding:14px 22px;font-size:21px;font-weight:500;white-space:nowrap">${I.x('#fff',22)} Voice typing stopped</div>`:''}
  ${cursorAt?`<div class="abs" style="left:${cursorAt[0]}px;top:${cursorAt[1]}px">${I.cursor('var(--ink)',38)}</div>`:''}
 </div>`;
}
const stepsList=(t,steps,active)=>`<div class="col" style="gap:22px;margin-top:8px">${steps.map((s,k)=>{const on=k===active;return `<div class="row" style="gap:20px;${A(ap(t,.9+k*.35),16)}"><div class="row" style="justify-content:center;flex:0 0 52px;height:52px;border-radius:50%;font-weight:600;font-size:24px;${on?'background:var(--accent);color:#fff':'background:#fff;border:1px solid var(--line2);color:var(--muted)'}">${k+1}</div><div style="font-size:30px;line-height:1.35;color:${on?'var(--ink)':'var(--muted)'};font-weight:${on?600:400}">${s}</div></div>`}).join('')}</div>`;

const FIXES=[
 {ic:I.browser,t:'Use Chrome',d:'Voice typing is built for Chrome. In Safari the menu option may not appear.'},
 {ic:I.gear,t:'Allow the mic on your Mac',d:'System Settings › Privacy & Security › Microphone › turn on Chrome.'},
 {ic:I.mic,t:'Allow the mic in Chrome',d:'Click the icon left of the address bar › Microphone › Allow.'},
 {ic:I.sound,t:'Pick the right input',d:'System Settings › Sound › Input. Choose the mic you speak into.'},
 {ic:I.click,t:'Don’t click away',d:'It stops when you click outside the doc. Click back in and tap the mic.'},
 {ic:I.globe,t:'Check language and Wi-Fi',d:'Match the language above the mic. Voice typing needs internet.'},
];
const WIN=[
 {name:'Google Docs',txt:'Here’s the plan for the Q3 launch.',x:0,y:0},
 {name:'Gmail',txt:'Hi Priya, thanks for today. Notes are attached.',x:70,y:200},
 {name:'Slack',txt:'Beta ships Friday. Can someone review the copy?',x:140,y:400},
];
function appWin(t,w,k,active,start){
 return `<div class="abs card" style="left:${w.x}px;top:${w.y}px;width:640px;height:230px;border-radius:16px;overflow:hidden;${active?'border:2px solid var(--accent);z-index:3':'opacity:.9'}">
  <div class="row" style="height:48px;padding:0 18px;gap:8px;background:#fbfaf7;border-bottom:1px solid var(--line)">${[0,1,2].map(()=>`<div style="width:12px;height:12px;border-radius:50%;background:#e4e2da"></div>`).join('')}<div style="margin-left:12px;font-size:18px;font-weight:600;color:var(--muted)">${w.name}</div></div>
  <div style="padding:26px 28px;font-size:25px;line-height:1.5;color:var(--ink)">${typed(w.txt,t,start,24,active)}</div></div>`;
}

setScenes([
 // 1. HOOK: the issue
 {d:5.2,r:(t)=>{const off=t>2.7;const txt=typed('The Q3 launch plan is ready for rev',t,.3,14,!off);
  return leftText(t,'Google Docs on Mac','Voice typing keeps stopping?','Words go missing, the mic shuts off, or the option isn’t even there.')+
  `<div class="abs" style="left:1000px;top:220px;${A(ap(t,.1),30)}">${browser(t,{text:txt,mic:off?'off':'on',toast:ap(t,2.8,.35)})}</div>`}},
 // 2. HOOK: the solution
 {d:5.8,r:(t)=>leftText(t,'The fix','Set it up right. Fix it fast. Or dictate anywhere.','')+
  `<div class="abs col" style="left:1060px;top:280px;gap:26px">${[['Set it up','20 seconds in Chrome'],['Fix it','The 6 usual problems'],['Dictate anywhere','Every app on your Mac']].map(([a,b],k)=>`<div class="card row" style="width:640px;padding:28px 32px;gap:24px;box-sizing:border-box;${A(ap(t,.6+k*.45),24,40)}"><div class="row" style="justify-content:center;flex:0 0 60px;height:60px;border-radius:50%;background:var(--soft);color:var(--accent);font-family:Fraunces;font-weight:600;font-size:30px">${k+1}</div><div class="col" style="gap:4px"><div style="font-size:30px;font-weight:600">${a}</div><div style="font-size:22px;color:var(--muted)">${b}</div></div></div>`).join('')}</div>`},
 // 3. SET UP
 {d:13,step:'Part 1 · Set up',r:(t)=>{
  const active=t<3?0:t<7.5?1:2;const menu=t>3.6&&t<6.2?ap(t,3.6,.3):0;const hi=t>4.6?1:0;
  const mic=t>6.3?(t>7.9?'on':'off'):null;
  const text=t>8.3?typed('Meeting notes for Thursday. Launch moves to March 12.',t,8.4,17):'';
  let cur=null;
  if(t>2.8&&t<3.7){const p=ap(t,2.8,.8);cur=[400-(1-p)*120,80+(1-p)*160]}
  else if(t>=3.7&&t<6.2){const p=ap(t,3.8,.7);cur=[400+p*60,80+p*165]}
  else if(t>7&&t<8.1){const p=ap(t,7,.8);cur=[742-(1-p)*160,196+(1-p)*160]}
  return leftText(t,'Set up in 20 seconds','Turn on voice typing.','',stepsList(t,['Open your doc in Chrome','Tools › Voice typing<br><span style="font-size:24px;color:var(--muted);font-weight:400">or ⌘ + Shift + S</span>','Click the mic and start talking'],active),260)+
  `<div class="abs" style="left:1000px;top:200px">${browser(t,{text,mic,menu,hi,cursorAt:cur})}</div>`}},
 // 4. PUNCTUATION
 {d:11,step:'Part 1 · Set up',r:(t)=>leftText(t,'Pro tip','Say your punctuation.','Voice typing won’t add it for you. Say it out loud.',
  `<div class="row" style="gap:12px;flex-wrap:wrap;margin-top:6px">${['period','comma','question mark','new line','new paragraph'].map((c,k)=>`<span class="chip" style="background:#fff;border:1px solid var(--line);font-size:24px;padding:10px 18px;${A(ap(t,1.2+k*.25),10)}">“${c}”</span>`).join('')}</div>`,280)+
  `<div class="abs col" style="left:1040px;top:240px;gap:26px">
   <div class="card col" style="width:720px;padding:32px;gap:14px;box-sizing:border-box;${A(ap(t,.5),24)}"><div class="row" style="gap:12px;font-size:20px;font-weight:600;color:var(--muted)">${I.mic('var(--muted)',22)} YOU SAY</div><div style="font-size:28px;line-height:1.5;color:var(--body);font-style:italic">${typed('hi team comma new line the launch moved to friday period',t,1,16,false)}</div></div>
   <div class="row" style="justify-content:center;${A(ap(t,4.6),10)}"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M6 13l6 6 6-6"/></svg></div>
   <div class="card col" style="width:720px;padding:32px;gap:14px;box-sizing:border-box;border:2px solid var(--accent);${A(ap(t,5),24)}"><div class="row" style="gap:12px;font-size:20px;font-weight:600;color:var(--accent)">${I.check('var(--accent)',22)} YOU GET</div><div style="font-family:Plex;font-size:32px;line-height:1.5">Hi team,<br>The launch moved to Friday.</div></div></div>`},
 // 5. FIXES
 {d:28.5,step:'Part 2 · Fix it',r:(t)=>`<div class="abs col" style="left:140px;top:150px;gap:14px"><div class="eyebrow" style="${A(ap(t,.1))}">Voice typing not working?</div><h2 class="h2" style="${A(ap(t,.25))}">Check these 6 things.</h2></div>
  <div class="abs" style="left:140px;top:360px;display:grid;grid-template-columns:repeat(3,520px);gap:36px">${FIXES.map((f,k)=>{const st=.9+k*4.4;const on=t>=st&&t<st+4.4;const seen=t>=st;return `<div class="card col" style="height:270px;padding:32px;gap:16px;box-sizing:border-box;${seen?'':'opacity:.0;'}${on?'border:2px solid var(--accent);':''}${A(ap(t,st,.5),24)};${!on&&seen&&t>st+4.4?'opacity:.72':''}">
   <div class="row" style="gap:16px"><div class="row" style="justify-content:center;flex:0 0 52px;height:52px;border-radius:14px;background:${on?'var(--accent)':'var(--soft)'}">${f.ic(on?'#fff':'var(--accent)',28)}</div><div style="font-size:20px;font-weight:600;color:var(--muted)">FIX ${k+1}</div></div>
   <div style="font-size:30px;font-weight:600;line-height:1.2">${f.t}</div><div style="font-size:23px;line-height:1.45;color:var(--body)">${f.d}</div></div>`}).join('')}</div>`},
 // 6. LIMITS
 {d:8.5,r:(t)=>leftText(t,'Good to know','It works. With limits.','',
  `<div class="col" style="gap:20px;margin-top:6px">${['Only inside Google Docs and Slides speaker notes','Built for Chrome only','Stops when you click away','Not in Gmail, Slack or your other apps'].map((x,k)=>`<div class="row" style="gap:16px;font-size:30px;${A(ap(t,.9+k*.45),14)}"><div class="row" style="justify-content:center;flex:0 0 44px;height:44px;border-radius:50%;background:#f6e7dc">${I.x('var(--clay)',22)}</div>${x}</div>`).join('')}</div>`,250,1000)+
  `<div class="abs" style="left:1180px;top:330px;${A(ap(t,.3),24)}"><div style="transform:scale(.72);transform-origin:top left">${browser(t,{text:'Here’s the update for',mic:'off',toast:1})}</div></div>`},
 // 7. LYNKK: dictate anywhere
 {d:14,step:'Part 3 · Dictate anywhere',r:(t)=>{const act=t<4.8?0:t<8.8?1:2;const starts=[1.2,5,9];
  const w=WIN[act];const listen=`<div class="abs row" style="left:${w.x+330}px;top:${w.y+196}px;z-index:5;gap:12px;background:var(--ink);color:#fff;border-radius:999px;padding:10px 18px 10px 14px;box-shadow:0 10px 26px rgba(22,24,29,.25)"><div class="row" style="justify-content:center;width:34px;height:34px;border-radius:50%;background:var(--accent)">${I.mic('#fff',20)}</div><span style="font-size:19px;font-weight:600">Lynkk · Listening</span>${wave(t,10,22,'#fff')}</div>`;
  return leftText(t,'Dictate anywhere','Talk wherever your cursor is.','Lynkk’s Mac app types your words into Google Docs, Gmail, Slack, Notion, Word and every other app.',
  `<div class="row" style="gap:12px;flex-wrap:wrap;${A(ap(t,1.4))}">${['Any app','Any browser','Same app as your meeting notes'].map(c=>`<span class="pill" style="background:#fff;border:1px solid var(--line);font-size:22px">${I.check('var(--accent)',22)} ${c}</span>`).join('')}</div>`,250,800)+
  `<div class="abs" style="left:1040px;top:200px;width:800px;height:660px;${A(ap(t,.3),30)}">${WIN.map((x,k)=>appWin(t,x,k,k===act,starts[k])).join('')}${listen}</div>`}},
 // 8. CTA
 {d:8,bg:'var(--soft)',noMark:1,r:(t)=>`<div class="abs col" style="left:0;right:0;top:250px;align-items:center;gap:36px;text-align:center"><div style="font-family:Fraunces;font-weight:600;font-size:64px;${A(ap(t,.1))}">Lynkk</div><h1 class="h1" style="max-width:1400px;${A(ap(t,.3))}">Talk instead of typing, in every app.</h1><p class="lead" style="${A(ap(t,.6))}">Dictation and AI meeting notes in one Mac app.</p><div style="margin-top:16px;${A(ap(t,1),20,0,.1)}">${cta('Start free at lynkk.ai')}</div></div>`},
]);
