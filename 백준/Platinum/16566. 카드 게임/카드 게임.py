from bisect import*
g=lambda:[*map(int,input().split())]
def f(x):
 if x==p[x]:return x
 p[x]=f(p[x]);return p[x]
p=[*range(g()[0])]
a=sorted(g())
for n in g():i=f(bisect_left(a,n+1));p[i]=f(i+1);print(a[i])