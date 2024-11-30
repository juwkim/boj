from math import lcm

n, a, b = map(int, input().split())
r = n // lcm(a, b)
print(n // a - r, n // b - r, r)