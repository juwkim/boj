from itertools import*
N,K,*A=map(int,open(0).read().split())
print(sum(sorted(b-a for a,b in pairwise([0]+sorted(A)))[:N-K]))