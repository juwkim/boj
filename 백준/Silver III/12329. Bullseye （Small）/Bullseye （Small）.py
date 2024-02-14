import sys
input = sys.stdin.readline
from math import isqrt

for tc in range(1, 1 + int(input())):
    r, t = map(int, input().split())
    p = 1 - 2 * r
    ans = (p + isqrt(p * p + 8 * t)) // 4
    print(f"Case #{tc}: {ans}")