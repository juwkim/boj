import sys
input = sys.stdin.readline

xs, ys = zip(*[[*map(int, input().split())] for _ in range(int(input()))])
xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)
a, b = xmax - xmin, ymax - ymin
if a == 0 or b == 0 or xmax - xmin == ymax - ymin and all(x in (xmin, xmax) or y in (ymin, ymax) for x, y in zip(xs, ys)) or all(x == xmin or y in (ymin, ymax) for x, y in zip(xs, ys)) or all(x == xmax or y in (ymin, ymax) for x, y in zip(xs, ys)) or all(y == ymin or x in (xmin, xmax) for x, y in zip(xs, ys)) or all(y == ymax or x in (xmin, xmax) for x, y in zip(xs, ys)):
    print(max(a, b))
else:
    print(-1)