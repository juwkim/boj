N,*B=map(int,open(0))
B.sort()
m=max(B[i]-i for i in range(N))
print(sum(a>=m for a in B))