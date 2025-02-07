N, K, *T = map(int, open(0).read().split())
lo, hi = 0, (N + K - 1) // K * max(T)
while lo + 1 < hi:
    m = lo + hi >> 1
    if sum(m // t for t in T) < N:
        lo = m
    else:
        hi = m
print(hi)