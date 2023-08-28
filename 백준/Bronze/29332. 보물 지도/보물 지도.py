import sys
from math import inf

input = sys.stdin.readline
l, r = -inf, inf
d, u = -inf, inf
for _ in range(int(input())):
    x, y, di = input().split()
    x, y = int(x), int(y)
    match di:
        case 'R':
            l = max(l, x + 1)
        case 'L':
            r = min(r, x - 1)
        case 'U':
            d = max(d, y + 1)
        case 'D':
            u = min(u, y - 1)
ans = (r - l + 1) * (u - d + 1)
print("Infinity" if ans == inf else ans)