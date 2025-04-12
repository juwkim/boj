import math

X, Y, c = map(int, input().split())
d = X**2 + Y**2
if 0 < d < c**2:
    print(2)
else:
    i = math.isqrt(d)
    print((i - (i**2 == d)) // c + 1)