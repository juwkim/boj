import sys
input = lambda: sys.stdin.readline().rstrip()
from math import isqrt

tc = 1
while (l:=[*map(int, input().split())])[0]:
    a, b = l
    ans = 0
    t, n = isqrt(a) + 1, 1
    while t * t < b:
        while t * t - 1 > n * (n + 1) // 2:
            n += 1
        if t * t - 1 == n * (n + 1) // 2:
            ans += 1
        t += 1
    print(f"Case {tc}: {ans}")
    tc += 1