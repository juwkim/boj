N,M=map(int,input().split())
a,i=1,2
while i<=N and (a:=a*i%M):i+=1
print(a)