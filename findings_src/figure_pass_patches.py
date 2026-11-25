# (pmid, finding index 1-based, dict of updates)
PATCH = [
 ('35750033',2,dict(p_value='<0.01',p_value_prov='visual_only')),
 ('35750033',4,dict(p_value_prov='full_text_unavailable',effect_size_prov='full_text_unavailable')),
 ('35750033',5,dict(p_value='<0.001',p_value_prov='visual_only',sample_size='12',sample_size_prov='printed_in_text',effect_size='~11%',effect_size_prov='estimated_from_figure')),
]
V=lambda **k: dict(p_value='<0.05',p_value_prov='visual_only',**k)
PATCH += [
 ('41103078',1,V()),
 ('41103078',2,V(effect_size='~24%',effect_size_prov='estimated_from_figure')),
 ('41103078',3,V(effect_size='~57%',effect_size_prov='estimated_from_figure')),
 ('41103078',4,V()),
 ('41103078',5,V()),
 ('41103078',6,V()),
]
PATCH += [
 ('39532095',1,dict(p_value='<0.0001',p_value_prov='visual_only',effect_size='~1.8x',effect_size_prov='estimated_from_figure')),
 ('39532095',4,dict(p_value='<0.0001',p_value_prov='visual_only',sample_size='3',sample_size_prov='visual_only')),
 ('39532095',5,dict(p_value='<0.01',p_value_prov='visual_only')),
]
PATCH += [
 ('33658354',1,dict(p_value='<=0.0001',p_value_prov='printed_in_text',sample_size='7',sample_size_prov='printed_in_text',effect_size='~5x',effect_size_prov='estimated_from_figure')),
 ('33658354',2,dict(effect_size='~6x',effect_size_prov='estimated_from_figure',sample_size='3',sample_size_prov='visual_only')),
 ('33658354',3,dict(p_value='<=0.001',p_value_prov='printed_in_text',sample_size='4',sample_size_prov='printed_in_text',effect_size='~78%',effect_size_prov='estimated_from_figure')),
]
PATCH += [
 ('29861287',1,dict(p_value='<0.01',p_value_prov='visual_only',effect_size='~10%',effect_size_prov='estimated_from_figure')),
 ('34982109',1,dict(p_value='<0.01',p_value_prov='visual_only',sample_size='3',sample_size_prov='printed_in_text',effect_size='~38%',effect_size_prov='estimated_from_figure')),
 ('34982109',2,dict(location='Fig 7D',p_value='<0.05',p_value_prov='visual_only')),
]
