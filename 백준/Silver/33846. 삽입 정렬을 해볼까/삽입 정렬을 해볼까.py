n, t, *a = map(int, open(0).read().split())
print(*sorted(a[:t]), *a[t:])