import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import dist

N = int(input())
eyes = [g() for _ in range(N)]
d = [dist(eyes[i - 1], eyes[i]) for i in range(N)]
ans = sum(d) - max(d)
print(ans)