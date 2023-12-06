import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import dist
N, R = g()
rices = [g() for _ in range(N)]
xi, xj = min(rices, key=lambda x: x[0])[0], max(rices, key=lambda x: x[0])[0]
yi, yj = min(rices, key=lambda x: x[1])[1], max(rices, key=lambda x: x[1])[1]

x, y = max([(x, y) for x in range(xi, xj + 1) for y in range(yi, yj + 1)], key=lambda xy: sum(dist(xy, rice) <= R for rice in rices))
print(x, y)