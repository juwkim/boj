g=lambda:map(int,input().split())
g()
print(sum(3*(a>b)+(a==b)for a,b in zip(g(),g())))