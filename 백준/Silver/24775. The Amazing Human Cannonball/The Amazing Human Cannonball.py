g = lambda: [*map(float, input().split())]

from math import cos, tan, pi
for _ in range(int(input())):
    v, theta, x, h1, h2 = g()
    theta *= pi / 180
    h = x * tan(theta) - 9.81 * x * x / (2 * v * v * cos(theta)**2)
    if h1 + 1 <= h <= h2 - 1:
        print('Safe')
    else:
        print('Not Safe')