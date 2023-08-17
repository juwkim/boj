from math import sqrt

h, r = int(input()), int(input())
d = int(h * sqrt(3) / 2)
print((r - 1) // d)