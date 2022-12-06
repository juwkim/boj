t,n,*l=map(int,open(0).read().split())
print([max(0,sum(l)-2*n),min(l)][t-1])