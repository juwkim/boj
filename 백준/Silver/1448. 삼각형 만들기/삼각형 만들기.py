N,*l=map(int,open(0).read().split())
l.sort()
s=-1
for i in range(N-1,1,-1):
 if l[i]<l[i-1]+l[i-2]:s=l[i]+l[i-1]+l[i-2];break
print(s)