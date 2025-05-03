import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, int(input()) + 1):
    B, N = g()
    M = g()
    lo, hi = -1, (N - 1) // B * max(M)
    while hi > lo + 1:
        mid = lo + hi >> 1
        if B + sum(mid // m for m in M) >= N:
            hi = mid
        else:
            lo = mid
    cnt = N - B - sum((hi - 1) // m for m in M)
    i = 0
    while cnt:
        cnt -= hi % M[i] == 0
        i += 1
    print(f"Case #{tc}: {i}")