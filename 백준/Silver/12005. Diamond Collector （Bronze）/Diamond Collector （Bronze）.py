g = lambda: [*map(int, input().split())]

from bisect import bisect_right
N, K = g()
nums = sorted(int(input()) for _ in range(N))

# p[i] = the number of p[i] ~ p[i] + K in nums
p = [bisect_right(nums, nums[i] + K, i+1) - i for i in range(N)]
print(max(p))