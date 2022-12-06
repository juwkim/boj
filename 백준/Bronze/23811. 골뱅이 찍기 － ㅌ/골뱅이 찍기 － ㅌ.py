N=int(input())
K='@'*N
P=(K*5+'\n')*N
S=P+(K+'\n')*N
print(S*2+P)