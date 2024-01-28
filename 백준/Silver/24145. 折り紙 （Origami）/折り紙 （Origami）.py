import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

n = int(input())
a, b = g()
cnt = Counter()
for _ in range(n):
    p, q, r, s = g()
    for x in range(p, r + 1):
        for y in range(q, s + 1):
            cnt[(x, y)] += 1
m = max(cnt.values())
area = list(cnt.values()).count(m)
print(m, area)