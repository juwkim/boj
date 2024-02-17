import sys
from math import dist
g = lambda: map(int, sys.stdin.readline().split())

*p, n = g()
d = []
for _ in range(n):
    *q, r = g()
    d.append(max(0, dist(p, q) - r))
print(int(sorted(d)[2]))