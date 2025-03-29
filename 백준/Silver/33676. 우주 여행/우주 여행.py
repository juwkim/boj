N,M,K,L=map(int,input().split())
a=L-N-M+2
print(((N-1)*'D'+a//2*'RL'+(M-1)*'R',-1)[a<0 or a&1])