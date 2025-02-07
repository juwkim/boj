N, K, *T = map(int, open(0).read().split())
lo, hi = 0, (N + K - 1) // K * max(T)
while lo + 1 < hi:
    mi = (lo + hi) // 2
    if sum(mi // t for t in T) < N:
        lo = mi
    else:
        hi = mi
print(hi)