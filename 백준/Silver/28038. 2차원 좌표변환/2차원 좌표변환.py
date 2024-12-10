import sys
input = sys.stdin.readline
from math import atan2, cos, sin, pi

for _ in range(int(input())):
    cmd = int(input())
    a, b = map(float, input().split())
    if cmd == 1:
        theta = atan2(b, a)
        if theta < 0:
            theta += 2 * pi
        print((a**2 + b**2)**0.5, theta)
    else:
        print(a * cos(b), a * sin(b))