g = lambda: [*map(int, input().split())]

from bisect import bisect_left
L = int(input())
nums = [0] + sorted(g())
n = int(input())

idx = bisect_left(nums, n)
if nums[idx] == n:
    print(0)
else:
    print((nums[idx] - n) * (n - nums[idx-1]) - 1)   