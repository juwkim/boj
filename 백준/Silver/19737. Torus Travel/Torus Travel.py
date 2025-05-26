from math import pi

r, R, n = map(int, input().split())
distance = n * (pi * r / 2)
a = 2 * pi / n * ((n - 1) // 2 * (R - r) + n // 2 * R)
b = (n - 1) * (pi * r / 2 + (R - r) * 2 * pi / n)
distance += min(a, b)
print(distance)