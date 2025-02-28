import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from bisect import bisect

N, M = g()
A = sorted(g())
for num in g():
    idx = bisect(A, num)
    print(int(((idx - .25) / 3) ** .5 + .5) if idx else 0, end=' ')