A, K, B, M, X = map(int, input().split())
lo, hi = 0, X
while hi > lo + 1:
    m = lo + hi >> 1
    cnt = A * (m - m // K) + B * (m - m // M)
    if cnt < X:
        lo = m
    else:
        hi = m
print(hi)