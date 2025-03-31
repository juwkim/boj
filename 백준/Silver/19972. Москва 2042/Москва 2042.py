import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from math import radians as rad

n, m = g()
a = [g() for _ in range(n)]
b = [int(input()) for _ in range(m)]
i1, j1 = g()
i2, j2 = g()
num = (b[j2 - 1] - b[j1 - 1]) / 10**6 % 360
l = [rad(num), rad((360 - num) % 360)]
l.insert(0, min(l))
ans = 1e9
for r, t in a: ans = min(ans, r * l[t] + abs(r - a[i1 - 1][0]) + abs(r - a[i2 - 1][0]))
print(ans)