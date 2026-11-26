"""Build the APOE4 knowledge-graph page from the H5 submission workbook.

Usage: python3 docs/viz/build.py h5_submission.xlsx [meta.json] [commit]
Writes docs/viz/kg_data.json and docs/index.html.
Concept tags, link directions and cell-type groups below were assigned by hand
from each finding's summary for this view; they are not columns of the sheet.
"""
import json,re,sys,os,datetime,openpyxl
XLSX=sys.argv[1]; META=sys.argv[2] if len(sys.argv)>2 else None; SHA=sys.argv[3] if len(sys.argv)>3 else 'unknown'
HERE=os.path.dirname(os.path.abspath(__file__))
def extract(path):
  wb=openpyxl.load_workbook(path,read_only=True)
  rows=list(wb['Submission'].iter_rows(values_only=True));h=rows[0];papers=[];finds=[]
  for r in rows[2:]:
    d=dict(zip(h,r));i=d['Paper/Finding ID']
    if i and '.' not in str(i): papers.append({'id':i,'doi':d['DOI'],'pmid':d['PubMed ID'],'type':d['Paper/source type']})
    elif i: finds.append({k:(str(d[k]) if d[k] is not None else None) for k in h[4:]})
  return {'papers':papers,'findings':finds}
d=extract(XLSX)
S={}
def a(node,ids):
  for i in ids.split(): S[i]=node
a('chol','P3.F6 P1.F1 P2.F4 P2.F8 P3.F2 P4.F4 P4.F7 P12.F1 P6.F3')
a('lysochol','P1.F2 P3.F1 P4.F5 P8.F3 P9.F5')
a('ld','P8.F6 P10.F5 P11.F4 P4.F6 P7.F1 P7.F4 P11.F1 P11.F2 P11.F3')
a('efflux','P3.F5 P10.F3')
a('rescue','P1.F8 P1.F9 P1.F10 P1.F11 P2.F5 P2.F6 P2.F7 P5.F5')
a('load','P8.F1 P8.F2 P8.F4 P9.F6 P10.F1 P10.F2 P10.F4')
a('degr','P2.F9 P8.F7 P1.F5 P2.F1 P2.F2 P4.F1 P5.F2 P6.F1 P8.F5 P9.F1 P9.F2 P9.F3 P12.F2')
a('acid','P1.F13 P6.F7 P8.F8 P1.F3 P1.F4 P2.F3 P3.F3 P4.F2 P4.F3 P5.F1 P5.F3 P9.F4 P13.F1')
a('auto','P1.F12 P1.F6 P1.F7 P6.F4 P7.F2 P7.F3')
a('prot','P6.F6 P3.F4 P5.F4 P5.F6 P6.F2 P6.F5 P13.F2')
def cell(f):
  s=f['Experimental system'].lower();i=f['Paper/Finding ID']
  if i.startswith('P13') or i.startswith('P5.') and i!='P5.F6' or i in('P8.F4','P8.F7','P8.F8'): return 'lines'
  if i.startswith('P9') or i in('P10.F1','P10.F2','P10.F3'): return 'mixed'
  if 'microglia' in s and 'astrocyte' not in s: return 'microglia'
  if 'neuron' in s: return 'neurons'
  return 'astro'
P={'P1':('Lee 2023','Cell Reports'),'P2':('Mesentier-Louro 2026','Cell Stem Cell'),'P3':('TCW 2022','Cell'),'P4':('de Leeuw 2022','Stem Cell Reports'),'P5':('Krogsaeter 2025','Autophagy'),'P6':('Hellén 2025','J Neuroinflammation'),'P7':('Cuní-López 2026','Nature Communications'),'P8':('Guo 2024','Cell'),'P9':('Nyberg 2025','J Biol Chem'),'P10':('PNAS Nexus 2026','PNAS Nexus'),'P11':('Sienski 2021','Sci Transl Med'),'P12':('Lin 2018','Neuron'),'P13':('Fote 2022','J Cell Sci')}
meta=json.load(open(META)) if META else {}
papers=[]
for p in d['papers']:
  m=meta.get(str(p['pmid']),{})
  papers.append({'id':p['id'],'short':P[p['id']][0],'journal':P[p['id']][1],'doi':p['doi'],'pmid':p['pmid'],'title':re.sub('<[^>]+>|&lt;/?i&gt;','',m.get('title',''))})
out=[]
for f in d['findings']:
  i=f['Paper/Finding ID']
  out.append({'id':i,'p':i.split('.')[0],'node':S[i],'cell':cell(f),'con':'CONTRADICTS' in (f['Finding summary']+f['Finding description']),
   'desc':f['Finding description'],'quote':f['Finding quote'],'sum':f['Finding summary'],'rel':f['Finding relevance'],'sys':f['Experimental system'],'loc':f['Data location'],
   'es':f['Effect size'],'esp':f['Effect size provenance'],'pv':f['P value'],'pvp':f['P value provenance'],'n':f['Sample size'],'np':f['Sample size provenance'],'cls':int(f['Directness class']),'str':f['Directness strength']})
assert len(S)==79==len(out)
D={'papers':papers,'findings':out}

d=D
A='APOE4'
E='''P1.F1 A chol up
P1.F2 A lyschol up
P1.F3 A size up
P1.F4 A size up
P1.F5 A cath up
P1.F6 A auto down
P1.F7 A auto down
P1.F8 mbcd size rescue
P1.F9 statin lyschol rescue;statin size rescue
P1.F10 mbcd auto rescue
P1.F11 A auto down
P1.F12 A mito down
P1.F13 A ph up
P2.F1 A degr down
P2.F2 A degr down
P2.F3 A lamp down
P2.F4 A chol up
P2.F5 mbcd degr rescue;statin degr none
P2.F6 mbcd degr rescue
P2.F7 mbcd ph rescue
P2.F8 A chol up;mbcd chol down
P2.F9 A asyn up;A degr down
P3.F1 A lyschol up
P3.F2 A chol up
P3.F3 A lamp down;lamp lyschol up
P3.F4 A lgenes down
P3.F5 A efflux down
P3.F6 A chol up
P4.F1 A degr none
P4.F2 A size none
P4.F3 A lamp down
P4.F4 A chol up
P4.F5 A lyschol none
P4.F6 A tag up
P4.F7 A chol down;A efflux down
P5.F1 A ph down
P5.F2 A cath down
P5.F3 A ph down
P5.F4 A lprot change
P5.F5 tmed5 ph rescue
P5.F6 A lprot change
P6.F1 A degr down
P6.F2 A lmp down;abeta lmp down
P6.F3 A chol none
P6.F4 A auto none
P6.F5 A lprot down
P6.F6 A cath down
P6.F7 A lamp none
P7.F1 A ld up
P7.F2 A lipophagy down
P7.F3 A lipophagy change
P7.F4 A ld up
P8.F1 A lipofuscin up
P8.F2 A lipofuscin up
P8.F3 A lipofuscin up
P8.F4 pufa lipofuscin up
P8.F5 A tau up
P8.F6 A tag up
P8.F7 A cath none
P8.F8 A size none
P9.F1 A degr none
P9.F2 A degr down
P9.F3 A ph down
P9.F4 A size none
P9.F5 A lyschol up
P9.F6 A degr none;load degr down
P10.F1 A ld up
P10.F2 A neurite up
P10.F3 A efflux down
P10.F4 A lyschol none
P10.F5 A ld none
P11.F1 A ld up
P11.F2 A tag up
P11.F3 choline ld rescue
P11.F4 A tag up
P12.F1 A chol up
P12.F2 A degr down;A abeta up
P13.F1 A size up;A auto change;A ld change
P13.F2 A lprot change;A mito down'''
fx={}
for line in E.splitlines():
  i,rest=line.split(' ',1)
  fx[i]=[dict(zip(('s','t','e'),x.split())) for x in rest.split(';')]
for v in fx.values():
  for e in v:
    if e['s']=='A': e['s']=A
ids={f['id'] for f in d['findings']}
assert set(fx)==ids,(ids^set(fx))
for f in d['findings']: f['edges']=fx[f['id']]
d['design']=[['mbcd','chol','removes'],['statin','chol','lowers synthesis'],['load','chol','adds'],['npc1','lyschol','traps'],['choline','ld','reverses'],['pufa','tag','supplies'],['tmed5','lprot','is part of']]
# NPC1 used as context in P10


json.dump(d,open(os.path.join(HERE,'kg_data.json'),'w'),ensure_ascii=False,indent=0)
t=open(os.path.join(HERE,'kg_template.html')).read()
s=json.dumps(d,ensure_ascii=False).replace('</','<\\/')
t=t.replace('__DATA__',s).replace('__SHA__',SHA[:7]).replace('__TIME__',datetime.datetime.fromtimestamp(os.path.getmtime(XLSX),datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')).replace('__NF__',str(len(d['findings'])))
t=t.replace('<meta name="claude:viewport-fit-sides" content="cover">','')
page='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'+t.replace('<style>','<style>\nimg{max-width:100%}[hidden]{display:none!important}\n',1)
page=page.replace('\n<div class="band">','\n</head>\n<body>\n<div class="band">',1)+'\n</body>\n</html>\n'
open(os.path.join(HERE,'..','index.html'),'w').write(page)
open(os.path.join(HERE,'..','..','index.html'),'w').write(page)  # repo root, for the short Pages URL
print('built',len(d['findings']),'findings')
