import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
from math import gcd

for _ in range(int(input())):
    n, m = g()
    a = [0] * n
    for _ in range(m):
        x, y = g()
        a[x - 1] = y
    if a[0] == 0:
        a[0] = 100
    if a[1] == 0:
        a[1] = a[0]
    for i in range(2, n - 1):
        if a[i] == 0:
            a[i] = max(a[i + 1:])
    s, t = a[0] + a[1], sum(a)
    GCD = gcd(s, t)
    print(f"{s // GCD}/{t // GCD}")