import re
g=re.search
q,l,r,t=input(),0,0,0
for s in q:
    if g('[a-gq-tv-z]',s.lower()):l+=1
    if g('[h-pu]',s.lower()):r+=1
    if g('[\sA-Z]',s):t+=1
for _ in [0]*t:
    if l>r:r+=1
    else:l+=1
print(l,r)