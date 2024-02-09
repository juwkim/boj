n,*d=map(int,open(0).read().split())
d.sort()
print(sum(max(d[i],d[i-1])for i in range(n)))