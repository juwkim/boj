import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from math import pi

for _ in range(int(input())):
    N, F = g()
    r = g()
    lo, hi = 0, pi * max(r)**2
    while hi - lo > 1e-5:
        mid = (lo + hi) / 2
        if sum(int(pi * ri**2 / mid) for ri in r) >= F + 1:
            lo = mid
        else:
            hi = mid
    print(lo)