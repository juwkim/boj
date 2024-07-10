g = lambda: [*map(int, input().split())]

N, M = g()
A = g()
lo, hi = 0, max(A) * M
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if sum(mid // x for x in A) >= M:
        hi = mid
    else:
        lo = mid
print(hi)