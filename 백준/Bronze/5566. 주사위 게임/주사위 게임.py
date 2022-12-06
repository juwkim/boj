N,M=map(int,input().split())
X=[int(input())for _ in[0]*N]
p,i=1,0
while p<N:i+=1;p+=int(input());p+=X[min(N,p)-1]
print(i)