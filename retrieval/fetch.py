import json,sys,urllib.request,re,os
import xml.etree.ElementTree as ET
E='https://www.ebi.ac.uk/europepmc/webservices/rest'
def get(u): return urllib.request.urlopen(u,timeout=90).read()
def txt(e): return re.sub(r'\s+',' ',''.join(e.itertext())).strip()
meta={}
for pmid in sys.argv[1:]:
    r=json.loads(get(f"{E}/search?query=EXT_ID:{pmid}%20AND%20SRC:MED&format=json&resultType=core"))['resultList']['result']
    if not r: print(pmid,'notfound');continue
    r=r[0]; m=dict(pmid=pmid,doi=r.get('doi'),pmcid=r.get('pmcid'),title=r.get('title'),journal=r.get('journalInfo',{}).get('journal',{}).get('title'),year=r.get('pubYear'),abstract=r.get('abstractText',''))
    out=[f"[TITLE] {m['title']}",f"[ABSTRACT] {re.sub('<[^>]+>','',m['abstract'])}"]
    status='abstract_only'
    if m['pmcid']:
        try:
            x=get(f"{E}/{m['pmcid']}/fullTextXML"); open(f'xml/{pmid}.xml','wb').write(x)
            root=ET.fromstring(x)
            body=root.find('body')
            if body is not None:
                status='full_text'
                def walk(sec,path):
                    t=sec.find('title'); path=path+[txt(t)] if t is not None else path
                    for ch in sec:
                        if ch.tag=='p': out.append(f"[{' > '.join(path)}] {txt(ch)}")
                        elif ch.tag=='sec': walk(ch,path)
                walk(body,[])
            for f in root.iter('fig'):
                lab=f.find('label'); cap=f.find('caption')
                if cap is not None: out.append(f"[{txt(lab) if lab is not None else f.get('id')} legend] {txt(cap)}")
            for tw in root.iter('table-wrap'):
                lab=tw.find('label'); out.append(f"[{txt(lab) if lab is not None else 'Table'}] {txt(tw)}")
            for s in root.iter('supplementary-material'):
                out.append(f"[Supplement] {txt(s)}")
        except Exception as e: print(pmid,'err',e)
    m['status']=status
    open(f'sources/{pmid}.txt','w').write('\n'.join(out))
    meta[pmid]=m; print(pmid,status,m['pmcid'],m['year'],m['title'][:80])
old=json.load(open('meta.json')) if os.path.exists('meta.json') else {}
old.update(meta); json.dump(old,open('meta.json','w'),indent=1)
