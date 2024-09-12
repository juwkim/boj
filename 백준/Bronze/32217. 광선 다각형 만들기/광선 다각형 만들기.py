n, *a = map(int, open(0).read().split())
print((n - 1) * 180 - 2 * sum(a))