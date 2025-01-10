import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
px = [0] * (N + 1)
for i, num in enumerate(sorted(map(int, input().split()), reverse=True)):
    px[i + 1] = px[i] + num
for _ in range(int(input())):
    print(bisect_left(px, int(input())))