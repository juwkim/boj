import sys
input = sys.stdin.readline
from math import isqrt

w, h = map(int, input().split())
a = ['.' + input() + '.' for _ in range(h)]
a = ['.' * (w + 2)] + a + ['.' * (w + 2)]
ans, d2 = None, -1
for i in range(1, h + 1):
    for j in range(1, w + 1):
        cur = min((x - i)**2 + (y - j)**2 for x in range(h + 2) for y in range(w + 2) if a[x][y] == '.')
        cur = min(cur, min(i - 1, j - 1, h - i, w - j)**2 + 1)
        if cur > d2:
            ans, d2 = (j, i), cur
print(isqrt(d2 - 1))
print(*ans)