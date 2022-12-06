g = lambda: [*map(int, input().split())]

n, m = g()
nums = g()
print(sum(i > j for i, j in zip(nums, nums[1:])))