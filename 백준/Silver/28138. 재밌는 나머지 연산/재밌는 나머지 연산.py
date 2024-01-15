import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import isqrt

N, R = g()
P = N - R
ans = 0
for i in range(1, isqrt(P) + 1):
    j, r = divmod(P, i)
    if r:
        continue
    if i > R:
        ans += i
    if i != j and j > R:
        ans += j
print(ans)