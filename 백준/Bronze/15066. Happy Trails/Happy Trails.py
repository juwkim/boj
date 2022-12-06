g = lambda: [*map(int, input().split())]

from math import radians, sin
ans = 0
for _ in range(int(input())):
    angle, dist = g()
    ans += dist * sin(radians(angle))
print('%.2f' % ans)