import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from math import radians

n, m = g()
a = [g() for _ in range(n)]
b = [int(input()) for _ in range(m)]
i1, j1 = g()
i2, j2 = g()
angle = (b[j2 - 1] - b[j1 - 1]) / 10**6 % 360
l = radians((360 - angle) % 360), radians(angle)
ans = 1e9
for r, t in a:
    if t == 1:
        theta = l[1]
    elif t == -1:
        theta = l[0]
    else:
        theta = min(l)
    ans = min(ans, r * theta + abs(r - a[i1 - 1][0]) + abs(r - a[i2 - 1][0]))
print(ans)