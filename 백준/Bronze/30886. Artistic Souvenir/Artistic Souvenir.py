import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import pi, sqrt

a = int(input())
r = sqrt(a / pi)
ans = (2 * r + 2) ** 2
print(ans)