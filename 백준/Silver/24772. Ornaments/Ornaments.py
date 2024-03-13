import sys
from math import acos, pi

while True:
    r, h, s = map(int, sys.stdin.readline().split())
    if r == 0:
        break
    ans = 2 * ((h**2 - r**2)**.5 + r * (pi - acos(r / h))) * (1 + s / 100)
    print(f"{ans:.2f}")