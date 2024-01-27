import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import product
from math import inf

N = int(input())
P = [g() for _ in range(N)]

X = sorted(set(p[0] for p in P))
Xl = [x - 1 for x in X[:3]]
Xr = [x + 1 for x in X[-3:]]

Y = sorted(set(p[1] for p in P))
Yl = [y - 1 for y in Y[:3]]
Yr = [y + 1 for y in Y[-3:]]

ans = inf
for xl, xr, yl, yr in product(Xl, Xr, Yl, Yr):
    cnt = sum(xl < x < xr and yl < y < yr for x, y in P)
    if cnt >= N - 2:
        ans = min(ans, max(xr - xl, yr - yl) ** 2)
print(ans)