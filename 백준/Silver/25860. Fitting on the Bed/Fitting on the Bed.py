from math import cos, sin, radians

L, W, H, x, y, a = map(int, open(0).read().split())
off = 1e-9
if -off <= x + H * cos(radians(a)) <= W + off and -off <= y + H * sin(radians(a)) <= L + off:
    print('YES')
else:
    print('NO')