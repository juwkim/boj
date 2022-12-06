N,R,*l=map(int,open(0).read().split())
a=sorted({*range(1,N+1)}-{*l})
print(*a if a else '*')