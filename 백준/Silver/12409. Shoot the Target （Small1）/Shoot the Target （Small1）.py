import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import sqrt, acos, degrees

def c(x):
    return ((x - x1) * (x - x2) + y1 * y2) / ((x - x1) ** 2 + y1 ** 2) ** 0.5 / ((x - x2) ** 2 + y2 ** 2) ** 0.5

for tc in range(1, 1 + int(input())):
    x1, y1, x2, y2 = g()
    if y1 == y2:
        x = (x1 + x2) / 2
        theta = degrees(acos(c(x)))
    else:
        p = (-x2 * y1 + x1 * y2 + sqrt(((x1 - x2)**2 + (y1 - y2)**2) * y1 * y2)) / (y2 - y1)
        q = (-x2 * y1 + x1 * y2 - sqrt(((x1 - x2)**2 + (y1 - y2)**2) * y1 * y2)) / (y2 - y1)
        theta = max(degrees(acos(c(p))), degrees(acos(c(q))))
    print(f'Case #{tc}:', theta)