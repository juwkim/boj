N, *a = map(int, open(0).read().split())
a.sort()
print(max(sum(a), -a[0]))