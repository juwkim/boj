import sys
input = sys.stdin.readline
from bisect import bisect

N, Q = map(int, input().split())
px = [0]
for _ in range(N):
    px.append(px[-1] + int(input()))
for _ in range(Q):
    print(bisect(px, int(input())))