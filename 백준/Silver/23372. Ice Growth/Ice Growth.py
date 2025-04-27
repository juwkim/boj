import sys
g = lambda: map(int, sys.stdin.readline().split())
from bisect import bisect_left

n, k = g()
prv, nums = 0, []
for a in g():
    nums.append(prv:=max(0, prv - a))
nums.sort()
for b in g():
    print(n - bisect_left(nums, 5 * b), end=' ')