from bisect import*
import sys
g=lambda:map(int,sys.stdin.readline().split())
n,m=g()
A=sorted(g())
for _ in range(m):
 c,*l=g()
 if c==1:print(n-bisect_left(A,l[0]))
 elif c==2:print(n-bisect(A,l[0]))
 else:print(bisect(A,l[1])-bisect_left(A,l[0]))