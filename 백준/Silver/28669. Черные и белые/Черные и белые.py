from math import gcd

n = int(input())
g = gcd(n + 2, 2 * n + 2)
print((n + 2) // g, (2 * n + 2) // g)