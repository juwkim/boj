from math import cos, sin, radians

L, W, H, x, y, a = map(int, open(0).read().split())
if -1e-9 <= x + H * cos(radians(a)) <= W + 1e-9 and -1e-9 <= y + H * sin(radians(a)) <= L + 1e-9:
    print('YES')
else:
    print('NO')