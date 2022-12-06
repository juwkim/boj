import sys
input = lambda: sys.stdin.readline()

g = lambda: [*map(int, input().split())]

from math import gcd
for _ in range(int(input())):
    n, d = g()
    GCD = gcd(n, d)
    print(n // GCD)