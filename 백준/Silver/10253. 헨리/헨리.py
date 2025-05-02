import sys
input = sys.stdin.readline
from math import gcd

for _ in range(int(input())):
    a, b = map(int, input().split())
    while a != 1:
        x = (b + a - 1) // a
        a, b = a * x - b, b * x
        g = gcd(a, b)
        a //= g
        b //= g
    print(b)