N,*S,T=map(int,open(0).read().split())
print(len({p//T for p in S}))