N,A,T=int(input()),1,0
C=[*range(1,1+N)]
while(A+T)%N and C[(A+T)%N] == (A+T)%N + 1:
    C[(A+T)%N], T, A = A, (A+T)%N, C[(A+T)%N]
print(A)