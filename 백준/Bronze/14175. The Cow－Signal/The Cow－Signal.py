M,N,K=map(int,input().split())
for _ in[0]*M:
    a=''.join(K*s for s in input())
    print(*[a for _ in[0]*K],sep='\n')