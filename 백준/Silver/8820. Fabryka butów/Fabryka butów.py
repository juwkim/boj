g=lambda:map(int,input().split())
for _ in[0]*int(input()):
    N,K=g()
    p=[*g()]
    s,t=sum(p[K:]),0
    for i in range(K,N):t=max(t,s*(i+1-K));s-=p[i]
    print(t)