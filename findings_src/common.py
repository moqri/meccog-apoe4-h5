import json
S={1:"1 very strong",2:"2 strong",3:"3 moderate",4:"4 weak",5:"5 very weak"}
K=["description","quote","summary","relevance","system","location","effect_size","effect_size_prov","p_value","p_value_prov","sample_size","sample_size_prov","directness","strength"]
def F(*a):
    d=dict(zip(K,a)); d["strength"]=S[d["strength"]]; return d
def save(name,doi,pmid,src,findings):
    json.dump(dict(doi=doi,pmid=pmid,source_type=src,findings=findings),open(f"{name}.json","w"),indent=1)
