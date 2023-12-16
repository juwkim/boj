import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import gcd

M, N, T = g()
gd = gcd(N, T)
if M % gd:
    print("NESUSTOS")
else:
    t = 0
    while (M + t * N) % T:
        t += 1
    print(t)