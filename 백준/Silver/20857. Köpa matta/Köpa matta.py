import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import isqrt

M, N = g()
ans, diff = [], float('inf')
for a in range(1, 1 + isqrt(N)):
    l = (M + a - 1) // a
    r = N // a
    if l > r:
        continue
    for b in range(l, r + 1):
        if a * b <= N and abs(a - b) < diff:
            ans = [a, b]
            diff = abs(a - b)
            if a == b:
                break
print(*sorted(ans))