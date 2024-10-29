N, K, *a = map(int, open(0).read().split())

lo, hi = a[0], a[0]
print(1, end=' ')
for i in range(1, N):
    if lo - K <= a[i] <= hi + K:
        print(1, end=' ')
        lo = min(lo, a[i])
        hi = max(hi, a[i])
    else:
        print(0, end=' ')