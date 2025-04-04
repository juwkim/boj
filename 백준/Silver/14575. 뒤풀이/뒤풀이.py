import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, T = g()
L, R = zip(*[g() for _ in range(N)])
if sum(L) > T or sum(R) < T:
    print(-1)
else:
    lo, hi = max(L) - 1, max(R)
    while hi > lo + 1:
        S = lo + hi >> 1
        if sum(min(S, R[i]) for i in range(N)) >= T:
            hi = S
        else:
            lo = S
    print(hi)