g = lambda: [*map(int, input().split())]
from math import dist
x1, y1, x2, y2, x3, y3 = g()
a = x1, y1
b = x2, y2
c = x3, y3

if x1 == x2 == x3:
    print(-1)
elif (x3 - x1) * (y2 - y1) == (x2 - x1) * (y3 - y1):
    print(-1)
else:
    d1, d2, d3 = sorted(map(lambda x: dist(*x), [[a, b], [b, c], [c, a]]))
    print(2 * (d3 - d1))