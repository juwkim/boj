import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
from bisect import bisect

N, M = g()
px = [0] * (N + 1)
for i, num in enumerate(g()):
    px[i + 1] = px[i] + num
for _ in range(M):
    print(bisect(px, int(input())) - 1)