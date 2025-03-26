n, k, *a = map(int, open(0).read().split())
ans = 1e18
for _ in range(2):
    b = a[:]
    for i in range(1, n, 2):
        b[i] += k
    m = sorted(b)[n >> 1]
    ans = min(ans, sum(abs(num - m) for num in b))
    k = -k
print(ans)