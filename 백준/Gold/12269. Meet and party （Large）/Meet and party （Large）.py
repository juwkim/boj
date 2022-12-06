from bisect import bisect
import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for step in range(1, 1 + int(input())):
    xs, ys, xys = [], [], []
    for _ in range(int(input())):
        x1, y1, x2, y2 = g()
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                xs.append(x)
                ys.append(y)
                xys.append((x, y))
    xs.sort()
    ys.sort()
    xys.sort()
    xsum, ysum = [0], [0]
    for x, y in zip(xs, ys):
        xsum.append(xsum[-1] + x)
        ysum.append(ysum[-1] + y)
    n = len(xs)
    cx, cy, d = None, None, 1e30
    for x, y in xys:
        xidx = bisect(xs, x)
        yidx = bisect(ys, y)
        dist = (xidx * x - xsum[xidx]) + (xsum[-1] - xsum[xidx] - (n - xidx) * x) + (yidx * y - ysum[yidx]) + (ysum[-1] - ysum[yidx] - (n - yidx) * y)
        if dist < d:
            cx, cy, d = x, y, dist
    print(f"Case #{step}: {cx} {cy} {d}")