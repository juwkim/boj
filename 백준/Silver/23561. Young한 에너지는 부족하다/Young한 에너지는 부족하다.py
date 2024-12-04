N, *a = map(int, open(0).read().split())
a.sort()
print(a[2 * N - 1] - a[N])