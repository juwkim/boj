n,*p=map(int,open(0).read().split())
a,b=p[-1],1
for i in range(n-2,-1,-1):a,b=b+a*p[i],a
print(f'{a}/{b}')