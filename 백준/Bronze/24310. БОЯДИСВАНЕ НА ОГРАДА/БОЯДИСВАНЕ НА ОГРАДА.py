a,b,c,d=map(int,input().split())
a,b=sorted([a,b])
c,d=sorted([c,d])

print(max(b, d) - min(a, c) + 2 - max(1, c - b, a - d))