g = lambda: [*map(int, input().split())]

from math import sqrt
for _ in range(int(input())):
    R, B = g()
    B = min(B, R * sqrt(2))
    print('%.3f' % (B * sqrt(4 * R * R - B * B)))