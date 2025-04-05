N,*a=map(int,open(0).read().split())
a.sort()
print(a[N>>1]+sum(a[-1-i]-a[i]for i in range(N-1>>1)))