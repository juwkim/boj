import bisect as b
g=lambda:[*map(int,input().split())]
def f(x):
 t=x
 while t-p[t]:t=p[t]
 p[x]=t;return t
p=[*range(g()[0])]
a=sorted(g())
for n in g():i=f(b.bisect_left(a,n+1));p[i]=f(i+1);print(a[i])