from math import sin, cos, pi

d = 2 * pi / int(input())
angle = 0
for num in map(int, input().split()):
    print(num * cos(angle), num * sin(angle))
    angle += d