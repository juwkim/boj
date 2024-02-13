import sys
input = lambda: sys.stdin.readline().rstrip()
from math import sin, cos, pi

while (s:=input()) != "-1 -1 -1":
    L, N, C = s.split()
    L, N, C = int(L), int(N), float(C)
    p = 1 + N * C
    if p == 1:
        print("0.000")
        continue
    l, r = 0, pi
    for _ in range(1000):
        m = (l + r) / 2
        if p * sin(m) < m:
            r = m
        else:
            l = m
    ans = 0.5 * L * p * (1 - cos(m)) / m
    print(f"{ans:.3f}")