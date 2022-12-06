g=lambda:[*map(int, input().split())]
g()
a,b=g(),g()
print(sum(sum(i<=j for j in b)for i in a))