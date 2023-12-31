import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

M, N = g()
L = g()
if sum(L) < M:
    ans = 0
else:
    lo, hi = 1, max(L) + 1
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if sum(l // mid for l in L) >= M:
            lo = mid
        else:
            hi = mid
    ans = lo
print(ans)