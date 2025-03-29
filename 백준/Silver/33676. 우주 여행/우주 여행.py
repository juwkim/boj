N,M,K,L=map(int,input().split())
a=L-N-M+3
print((-1,(N-1)*'D'+a//2*'RL'+(M-1)*'R')[(a>0)*a&1])