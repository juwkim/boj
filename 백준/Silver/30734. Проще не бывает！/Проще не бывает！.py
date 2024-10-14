from math import isqrt

n = int(input())
t = n - (k := isqrt(n - 1))**2
print(min(t, 2*k + 2 - t))