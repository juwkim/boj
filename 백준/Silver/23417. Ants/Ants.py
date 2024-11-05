import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from collections import Counter
n, m, k, r, c = g()
r, c = r - 1, c - 1
ans = Counter()
for i in range(n):
    for j, t in enumerate(g()):
        if t:
            ans[abs(i - r) + abs(j - c) + t] += 1
print(len(ans))
for k, v in sorted(ans.items()):
    print(k, v)