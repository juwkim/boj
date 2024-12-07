n, k, *h = map(int, open(0).read().split())
h = [h[0]] + h + [h[-1]]
lo, hi = -1, 10**9
while lo + 1 < hi:
    mid = (lo + hi) // 2
    cnt = sum(abs(h[i] - h[i - 1]) > mid or abs(h[i] - h[i + 1]) > mid for i in range(1, n + 1))
    if cnt > k:
        lo = mid
    else:
        hi = mid
print(hi)