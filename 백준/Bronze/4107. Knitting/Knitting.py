while(s:=input())!='0 0 0':
    N,M,K=map(int,s.split())
    s=[*map(int,input().split())]
    a=[sum(s[:i+1])for i in range(K)]
    x,y=divmod(M-1,K)
    print(N*M+a[-1]*x*(x-1)//2*K+x*(sum(a)+a[-1]*y)+sum(a[:y]))