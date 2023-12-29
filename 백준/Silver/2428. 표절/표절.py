import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from bisect import bisect

N = int(input())
nums = sorted([9 * num for num in g()])
ans = 0
for i in range(N - 1):
    idx = bisect(nums, nums[i] * 10 // 9)
    ans += idx - i - 1
print(ans)