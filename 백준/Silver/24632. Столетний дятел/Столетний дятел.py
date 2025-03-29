import sys
input = sys.stdin.readline
from collections import defaultdict
from bisect import bisect

xdic = defaultdict(list)
ydic = defaultdict(list)
for _ in range(int(input())):
    x, y = map(int, input().split())
    xdic[x].append(y)
    ydic[y].append(x)
for k in xdic: xdic[k].sort()
for k in ydic: ydic[k].sort()
x, y, d = 0, 0, 0
ans, visited = 0, set()
while True:
    match d:
        case 0:
            i = bisect(ydic[y], x)
            if i == len(ydic[y]): break
            x = ydic[y][i] - 1
        case 1:
            i = bisect(xdic[x], y)
            if i == 0: break
            y = xdic[x][i - 1] + 1
        case 2:
            i = bisect(ydic[y], x)
            if i == 0: break
            x = ydic[y][i - 1] + 1
        case 3:
            i = bisect(xdic[x], y)
            if i == len(xdic[x]): break
            y = xdic[x][i] - 1
    d = (1, 2, 3, 0)[d]
    if (x, y, d) in visited:
        ans = "oo"
        break
    visited.add((x, y, d))
    ans += 1
print(ans)