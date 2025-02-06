import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n, C = g()
T, X = g(), g()
lo, hi = 0, 10**6
while hi - lo > 1e-9:
    mid = (lo + hi) / 2
    cur = 0
    for t, x in zip(T, X):
        if x >= mid:
            cur += t * (x - mid)
            if cur > C:
                break
        else:
            cur -= min(t, cur / (mid - x)) * (mid - x)
    else:
        hi = mid
        continue
    lo = mid
print(hi)