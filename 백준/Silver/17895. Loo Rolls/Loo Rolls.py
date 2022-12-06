l,n=map(int,input().split())
i=1
while l%n:n-=l%n;i+=1
print(i)