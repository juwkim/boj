from math import *
while (s:= input()) != '0 0 0 0 0':
    a, b, s, m, n = map(int, s.split())
    x, y = a * m, b * n
    angle = atan(y / x) * 180 / pi
    velocity = sqrt(x*x + y*y) / s
    print(f'{angle:.2f} {velocity:.2f}')