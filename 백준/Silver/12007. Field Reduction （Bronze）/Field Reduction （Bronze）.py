import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
cows = []
xs = defaultdict(lambda: [(1e9, -1), (-1e9, -1)])
ys = defaultdict(lambda: [(1e9, -1), (-1e9, -1)])
for i in range(N):
    x, y = map(int, input().split())
    cows.append((x, y))
    xs[x][0] = min(xs[x][0], (y, i))
    xs[x][1] = max(xs[x][1], (y, i))
    ys[y][0] = min(ys[y][0], (x, i))
    ys[y][1] = max(ys[y][1], (x, i))

def get_area(ban):
    minx, maxx = 1e9, -1e9
    miny, maxy = 1e9, -1e9
    for i, (x, y) in enumerate(cows):
        if i == ban:
            continue
        minx, maxx = min(minx, x), max(maxx, x)
        miny, maxy = min(miny, y), max(maxy, y)
    return (maxx - minx) * (maxy - miny)

minx, maxx = min(xs), max(xs)
miny, maxy = min(ys), max(ys)
ans = float('inf')
for ban in xs[minx][0][1], xs[minx][1][1], xs[maxx][0][1], xs[maxx][1][1], ys[miny][0][1], ys[miny][1][1], ys[maxy][0][1], ys[maxy][1][1]:
    ans = min(ans, get_area(ban))
print(ans)