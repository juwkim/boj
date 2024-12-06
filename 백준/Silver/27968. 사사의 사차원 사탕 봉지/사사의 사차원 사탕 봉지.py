import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from bisect import bisect_left

N, M = g()
A = g()
px = [0] * (M + 1)
for i in range(M):
    px[i + 1] = px[i] + A[i]
for _ in range(N):
    B = int(input())
    idx = bisect_left(px, B)
    if idx == M + 1:
        print("Go away!")
    else:
        print(idx)