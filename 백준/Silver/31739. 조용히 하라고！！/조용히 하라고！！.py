import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from itertools import permutations
from collections import Counter

N, M, K, T, P = g()
mosquitos = [g() for _ in range(K)]
cnt = Counter()
for r, c, s in mosquitos:
    cnt[(r, c)] += 1
a = 0
for p in permutations(cnt.keys()):
    (x, y), cur, dist = p[0], cnt[p[0]], 0
    for i in range(1, len(p)):
        nx, ny = p[i]
        dist += abs(x - nx) + abs(y - ny)
        if dist > T:
            break
        cur += cnt[p[i]]
        x, y = nx, ny
    a = max(a, cur)
b = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        cur = 0
        for r, c, s in mosquitos:
            dist = abs(i - r) + abs(j - c)
            if P >= dist * s:
                cur += 1
        b = max(b, cur)
print(a, b)