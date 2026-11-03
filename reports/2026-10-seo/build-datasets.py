import csv, os, re
RAW='/tmp/claude-0/-home-user-claude/5b2b58fa-7bff-56a9-8d62-efa9e36c7f2a/scratchpad/gsc_raw/'
OUT='/tmp/claude-0/-home-user-claude/5b2b58fa-7bff-56a9-8d62-efa9e36c7f2a/scratchpad/data/'
def load(f): return list(csv.DictReader(open(RAW+f)))
def pct(s): return round(float(s.replace('%',''))/100,6)
def w(name, cols, rows):
    with open(OUT+name,'w',newline='') as fh:
        wr=csv.writer(fh); wr.writerow(cols); wr.writerows(rows)
    print(name, len(rows),'rows', os.path.getsize(OUT+name),'bytes')

# 1. daily
ch=load('Chart.csv')
w('daily.csv',['day','clicks','impressions','ctr','position'],
  [[r['Date'],int(r['Clicks']),int(r['Impressions']),pct(r['CTR']),float(r['Position'])] for r in ch])

# 2. queries with theme + type
THEMES=[
 ('Brand',['lynkk']),
 ('Google Meet',['google meet','gmeet','meet transcript','meet recording']),
 ('Zoom',['zoom']),
 ('Microsoft Teams',['microsoft teams','ms teams','teams ai','teams meeting','copilot','teams note','teams transcript']),
 ('Action items & tasks',['action item','action list','action plan','follow up email','follow-up email']),
 ('Dictation & voice-to-text',['voice to text','voice-to-text','dictation','dictate','speech to text','speech-to-text','voice memo','voice note','voice typing','talk to text']),
 ('Transcription services',['transcription','transcribe','transcript']),
 ('Competitors & alternatives',['otter','fireflies','granola','fathom','gong','circleback','avoma','notta','read ai','plaud','meetgeek','clari','alternative',' vs ','tldv','sembly','grain','chorus','leexi']),
 ('Pricing & cost',['pricing','price','cost','cheap','free ']),
 ('Meeting templates & process',['template','agenda','minutes','standup','stand up','stand-up','one on one','one-on-one','board meeting','meeting notes','meeting summary','retrospective','qbr','business review']),
 ('Note taker (generic)',['note taker','notetaker','note-taker','ai notes','meeting bot','note taking']),
 ('Sales & revenue',['spin selling','bant','meddic','forecast','lead qualification','conversation intelligence','revenue operations','sales enablement','account plan','discovery call']),
]
def theme(q):
    ql=' '+q.lower()+' '
    for name,pats in THEMES:
        if any(p in ql for p in pats): return name
    return 'Other'
q=load('Queries.csv')
rows=[]
for r in q:
    text=' '.join(r['Top queries'].split())
    words=len(text.split())
    if 'lynkk' in text.lower(): t='Brand'
    elif words>=10: t='Conversational / AI-style'
    elif words>=4: t='Long-tail'
    else: t='Head & mid-tail'
    rows.append([text,int(r['Clicks']),int(r['Impressions']),pct(r['CTR']),float(r['Position']),theme(text),t,words])
rows.sort(key=lambda x:(-x[2],-x[1]))
w('queries.csv',['query','clicks','impressions','ctr','position','theme','query_type','word_count'],rows)

# 3. pages with section
def section(u):
    p=u.replace('https://lynkk.ai','').split('#')[0]
    if p in ('','/'): return 'Homepage'
    seg=p.strip('/').split('/')[0]
    return {'blog':'Blog','articles':'Blog','features':'Features','compare':'Comparison','use-cases':'Use cases','integrations':'Integrations'}.get(seg,'Other site pages')
pg=load('Pages.csv')
prows=[[r['Top pages'].replace('https://lynkk.ai','') or '/',int(r['Clicks']),int(r['Impressions']),pct(r['CTR']),float(r['Position']),section(r['Top pages']),r['Top pages']] for r in pg]
prows.sort(key=lambda x:(-x[2],-x[1]))
w('pages.csv',['path','clicks','impressions','ctr','position','section','url'],prows)

# 4. countries
co=load('Countries.csv')
w('countries.csv',['country','clicks','impressions','ctr','position'],
  [[r['Country'],int(r['Clicks']),int(r['Impressions']),pct(r['CTR']),float(r['Position'])] for r in co])

# 5. devices
dv=load('Devices.csv')
w('devices.csv',['device','clicks','impressions','ctr','position'],
  [[r['Device'],int(r['Clicks']),int(r['Impressions']),pct(r['CTR']),float(r['Position'])] for r in dv])
