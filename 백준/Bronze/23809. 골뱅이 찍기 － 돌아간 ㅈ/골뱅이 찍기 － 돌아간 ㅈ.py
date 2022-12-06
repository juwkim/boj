N=int(input())
K='@'*N
g=lambda X:(K+' '*N*X+K+'\n')*N
print(g(3)+g(2)+(K*3+'\n')*N+g(2)+g(3))