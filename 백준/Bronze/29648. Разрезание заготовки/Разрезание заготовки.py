from math import isqrt

a, b, s = map(int, input().split())
t = (a - b) ** 2 + 4 * s
if (i := isqrt(t))**2 == t and (a + b + i) % 2 == 0:
    print((a + b + i) // 2)
else:
    print(-1)