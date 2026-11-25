import json,sys
sys.path.insert(0,'.')
exec(open('search.py').read().split('allr={}')[0])
A='(ABSTRACT:"APOE4" OR ABSTRACT:"apoE4" OR ABSTRACT:"APOE ε4" OR ABSTRACT:"APOE4/4" OR ABSTRACT:"E4/E4" OR TITLE:"APOE4" OR TITLE:"apoE4" OR ABSTRACT:"apolipoprotein E4" OR TITLE:"apolipoprotein E4" OR ABSTRACT:"ApoE ε4")'
L='(ABSTRACT:lysosom* OR ABSTRACT:"late endosom*" OR ABSTRACT:endolysosom* OR ABSTRACT:endosom* OR ABSTRACT:autophag* OR ABSTRACT:"lipid droplet*" OR ABSTRACT:cathepsin* OR ABSTRACT:"bis(monoacylglycero)phosphate")'
qs={'t1':f'{A} AND {L} AND (ABSTRACT:lipid* OR ABSTRACT:cholesterol OR ABSTRACT:triglyceride* OR ABSTRACT:"fatty acid*" OR ABSTRACT:sphingo* OR ABSTRACT:ceramide* OR ABSTRACT:lipidom*)',
    't2':f'{A} AND (ABSTRACT:"lipid droplet*" OR ABSTRACT:"cholesterol accumulat*" OR ABSTRACT:"cholesterol ester*" OR ABSTRACT:lipidom*) AND (ABSTRACT:iPSC OR ABSTRACT:hiPSC OR ABSTRACT:"induced pluripotent" OR ABSTRACT:isogenic OR ABSTRACT:astrocyte* OR ABSTRACT:microglia*)'}
out={}
for k,q in qs.items():
    r=search(q,1000); print(k,len(r))
    for x in r:
        if x['pmid']: out.setdefault(x['pmid'],{**x,'via':[]})['via'].append(k)
old=json.load(open('candidates.json'))
for p,x in old.items():
    if any(v.startswith('seed') for v in x['via']): out.setdefault(p,{**x,'via':[]})['via']+=x['via']
json.dump(out,open('cand2.json','w'),indent=1); print(len(out))
