n=int(input())
t=[[*map(int,input().split())]for _ in[0]*n]
while n+1:
    if n==sum(i[0]<=n<=i[1]for i in t):break
    n-=1
print(n)