g=lambda:[*map(int, input().split())]
N,M=g()
print(max(0,max(t-s for(s,t)in zip(g()+[0]*(M-N),g()))))