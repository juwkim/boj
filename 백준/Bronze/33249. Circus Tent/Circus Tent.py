from math import pi

d, h = map(float, input().split())
print(pi * (d + 10) * (d + 10 + 4 * h) / 4)