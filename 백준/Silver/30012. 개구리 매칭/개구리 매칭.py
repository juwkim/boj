import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import inf

S, N = g()
E = g()
K, L = g()
ans, num = inf, 0
for i, x in enumerate(E, 1):
    diff = abs(x - S)
    if diff < 2 * K:
        cost = 2 * K - diff
    else:
        cost = L * (diff - 2 * K)
    if cost < ans:
        ans, num = cost, i
print(ans, num)