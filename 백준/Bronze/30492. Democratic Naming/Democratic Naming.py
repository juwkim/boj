import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

n, m = g()
ans = []
for l in map(Counter, zip(*[input() for _ in range(n)])):
    c = min(l, key=lambda x: (-l[x], x))
    ans.append(c)
print(*ans, sep='')