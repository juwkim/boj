from math import isqrt

a, b, c = map(int, input().split())
if c:
    print(c * c - a - b)
else:
    print(isqrt(a + b))