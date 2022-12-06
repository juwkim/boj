N=int(input())
K='@'*N
P=(K+' '*N*3+K+'\n')*N
S=P+(K*5+'\n')*N
print(S*2+P)