import json,sys,urllib.request,urllib.parse
E='https://www.ebi.ac.uk/europepmc/webservices/rest'
def get(u): return json.load(urllib.request.urlopen(u,timeout=60))
def search(q,maxn=300):
    out=[];cur='*'
    while len(out)<maxn:
        j=get(f"{E}/search?query={urllib.parse.quote(q)}&format=json&pageSize=100&cursorMark={urllib.parse.quote(cur)}&resultType=lite")
        res=j['resultList']['result']
        out+= [dict(pmid=r.get('pmid'),pmcid=r.get('pmcid'),doi=r.get('doi'),title=r.get('title'),year=r.get('pubYear'),oa=r.get('isOpenAccess'),src=r.get('source'),cited=r.get('citedByCount'),ptype=r.get('pubType','')) for r in res]
        if not res or j.get('nextCursorMark') in (None,cur): break
        cur=j['nextCursorMark']
    return out[:maxn]
def cites(pmid,kind):
    j=get(f"{E}/MED/{pmid}/{kind}?format=json&pageSize=1000")
    l=j.get('citationList',{}).get('citation',[]) if kind=='citations' else j.get('referenceList',{}).get('reference',[])
    return [dict(pmid=c.get('id'),title=c.get('title'),year=c.get('pubYear'),src=c.get('source')) for c in l]
allr={}
qs={
 'q1':'(APOE4 OR "ApoE4" OR "apoE4" OR "APOE ε4" OR "apolipoprotein E4") AND (lysosom* OR "late endosom*" OR endolysosom*) AND (lipid* OR cholesterol OR "lipid droplet*" OR triglyceride* OR "fatty acid*" OR sphingolipid* OR BMP OR "bis(monoacylglycero)phosphate") AND (iPSC OR "induced pluripotent" OR astrocyte* OR microglia OR neuron* OR "human brain")',
 'q2':'(APOE4 OR apoE4) AND (astrocyte* OR microglia*) AND ("lipid droplet*" OR cholesterol) AND (iPSC OR hiPSC OR "isogenic")',
 'q3':'(APOE4 OR apoE4) AND (lysosom* OR endolysosom* OR autophag*) AND (cholesterol) AND (astrocyte* OR microglia* OR neuron*)',
 'q4':'(APOE4 OR apoE4) AND ("lysosomal function" OR "lysosomal dysfunction" OR "endolysosomal" OR "cathepsin" OR "lysosomal pH" OR "LAMP1") AND (iPSC OR "stem cell")',
}
for k,q in qs.items():
    r=search(q,400); print(k,len(r),file=sys.stderr)
    for x in r:
        if x['pmid']: allr.setdefault(x['pmid'],{**x,'via':[]})['via'].append(k)
for kind in ('citations','references'):
    r=cites('37777962',kind); print(kind,len(r),file=sys.stderr)
    for x in r:
        if x['pmid']: allr.setdefault(x['pmid'],{**x,'via':[]})['via'].append('seed_'+kind)
json.dump(allr,open('candidates.json','w'),indent=1)
print(len(allr),file=sys.stderr)
