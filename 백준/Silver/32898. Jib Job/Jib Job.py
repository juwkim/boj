import sys
input = sys.stdin.readline
from math import dist

n = int(input())
nums = [[*map(int, input().split())] for _ in range(n)]
ans = [0] * n
arr = []
for idx in sorted(range(n), key=lambda x: nums[x][2], reverse=True):
    d = int(min(dist(p, nums[idx][:2]) for p in arr)) if arr else 1e9
    ans[idx] = min(d, nums[idx][2])
    arr.append(nums[idx][:2])
print(*ans, sep='\n')