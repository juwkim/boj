n,*l=map(int,open(0).read().split())
p=[0,0]
for(a,b)in zip(l,l[1:]):p[a<b]+=abs(b-a)
print(*p)