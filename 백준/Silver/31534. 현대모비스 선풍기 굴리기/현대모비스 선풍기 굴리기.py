from math import pi
a, b, h = map(int, input().split())
a, b = sorted([a, b])
if a == b:
    print(-1)
else:
    print(pi * (h**2 + (b - a)**2) * (b + a) / (b - a))