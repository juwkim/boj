import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n, C = g()
T, X = g(), g()
lo, hi = 0, 10**6
while hi - lo > 1e-9:
    R = (lo + hi) / 2
    cur = 0
    for t, x in zip(T, X):
        cur = max(0, cur + t * (x - R))
        if cur > C:
            lo = R
            break
    else:
        hi = R
print(hi)