import sys
g = lambda: map(int, sys.stdin.readline().split())
from bisect import bisect

n, k = g()
nums = [0] * (n + 1)
for i, a in enumerate(g()): nums[i+1] = min(0, nums[i] + a)
nums.sort()
print(*[bisect(nums, -5 * b) for b in g()])