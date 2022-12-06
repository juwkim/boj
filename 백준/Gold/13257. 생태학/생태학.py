from math import comb as b
N,C,D,M=map(int,input().split())
if C>M:print(0)
else:
    p=[[0]*(M+1)for _ in range(D+1)]
    p[0][C],p[1][C]=1,b(N,C)
    for d in range(2,D+1):
        for n in range(C,min(M,d*C)+1):
            p[d][n]=sum(p[d-1][i]*b(N-i,n-i)*b(i,C-n+i)for i in range(max(C,n-C),n+1))
    print(p[D][M]/pow(b(N,C),D))