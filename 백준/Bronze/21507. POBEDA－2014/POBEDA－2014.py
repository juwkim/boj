import math
g = lambda: [*map(int, input().split())]

a, b, c, d = g()
s = min(a, b) + min(c, d)
t = math.isqrt(s)
print(t)