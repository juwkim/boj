_,*l=map(int,open(0).read().split())
a,c,m=0,1,10**9+7
for H in sorted(l):a=(a+H*c)%m;c=(c<<1)%m
print(a)