import sys
g = lambda: map(int, sys.stdin.readline().split())
from bisect import bisect

N, M = g()
b = [-1e9] + sorted(g()) + [1e9]
ans = 0
for _ in range(M):
    a, w = g()
    i = bisect(b, a)
    ans = max(ans, w * min(b[i] - a, a - b[i-1]))
print(ans)