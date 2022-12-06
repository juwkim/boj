from collections import*
d=Counter(open(0).read())
del(d[' '],d['\n'])
h=max(d.values())
for l in zip(*[('#'*v).rjust(h)+k for k,v in sorted(d.items())]):print(*l,sep='')