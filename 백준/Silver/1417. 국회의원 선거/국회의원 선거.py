from heapq import*
N,A,*v=map(int,open(0).read().split())
heapify(v:=[-a for a in v])
d,a=A,-1
while-(a:=heappushpop(v,a+1))>=A:A+=1
print(A-d)