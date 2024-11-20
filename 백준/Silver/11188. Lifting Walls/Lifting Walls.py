import sys
g = lambda: map(int, sys.stdin.readline().split())
from itertools import combinations

l, w, n, r = g()
d = 4 * r * r
s = set()
for _ in range(n):
    x, y = g()
    s.add(tuple((2 * x - a) ** 2 + (2 * y - b) ** 2 <= d for a, b in ((-l, 0), (l, 0), (0, -w), (0, w))))

ans = "Impossible"
for i in range(1, len(s) + 1):
    for c in combinations(s, i):
        if all(any(p[k] for p in c) for k in range(4)):
            ans = i
            break
    else:
        continue
    break
print(ans)