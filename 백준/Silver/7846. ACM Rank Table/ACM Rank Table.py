import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from collections import defaultdict

C, N = g()
s = [defaultdict(lambda: [0, 0]) for _ in range(C + 1)]
l = sorted([g() for _ in range(N)], key=lambda x: x[2])
for c, p, t, r in l:
    if s[c][p][1]:
        continue
    if r: s[c][p][1] = t + s[c][p][0]
    else: s[c][p][0] += 1200
ans = sorted(range(1, C + 1), key=lambda x: (-sum(t != 0 for _, t in s[x].values()), sum(t for _, t in s[x].values())))
print(*ans)