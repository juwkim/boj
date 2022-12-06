g = lambda: [*map(int, input().split())]
from math import pi
for _ in range(int(input())):
    x, y, z, r, a, b, c, d = g()
    print(pi * r * r)