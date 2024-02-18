N,l=open(0)
d={}
for c in l.split():d[c]=d.get(c,0)+1
print("YNEOS"[max(d.values())>int(N)+1>>1::2])