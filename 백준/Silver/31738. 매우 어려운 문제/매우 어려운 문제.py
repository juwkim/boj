N,M=map(int,input().split())
a=1
while a*N:a=a*N%M;N-=1
print(a)