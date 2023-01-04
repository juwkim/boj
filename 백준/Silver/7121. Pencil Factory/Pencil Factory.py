from math import lcm

n, m, k = map(int, input().split())
n, m = n + 1, m + 1
l = lcm(n, m)

b = k // l
c = k // m - k // l
d = k // n - k // l
a = k - (b + c + d)

print(a, b, c, d)