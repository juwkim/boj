N,K,*A=map(int,open(0).read().split())
A=[0]+sorted(A)
print(sum(sorted(A[i+1]-A[i]for i in range(N))[:N-K]))