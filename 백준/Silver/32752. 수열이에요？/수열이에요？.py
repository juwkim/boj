N,L,R,*A=map(int,open(0).read().split())
s=sorted
A[L-1:R]=s(A[L-1:R])
print(+(A==s(A)))