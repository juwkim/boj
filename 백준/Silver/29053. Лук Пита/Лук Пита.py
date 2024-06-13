import sys
input = sys.stdin.readline
from math import inf

a, b = -inf, inf
for _ in range(int(input())):
    x, d = map(int, input().split())
    a, b = max(a, x - d), min(b, x + d)
    if a > b:
        b = -1
        break
print(b)