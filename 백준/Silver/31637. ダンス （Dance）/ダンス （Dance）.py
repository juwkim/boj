N,D,*A=map(int,open(0).read().split())
A.sort()
print("YNeos"[any(D<A[i+1]-A[i]for i in range(0,2*N,2))::2])