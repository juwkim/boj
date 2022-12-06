import sys
input = sys.stdin.readline
from bisect import bisect_left
N, M = map(int, input().split())
nums = sorted(int(input()) for _ in range(N))
for _ in range(M):
    D = int(input())
    idx = bisect_left(nums, D)
    if idx < N and nums[idx] == D:
        print(idx)
    else:
        print(-1)