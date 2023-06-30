g = lambda: [*map(int, input().split())]
N, X = g()
nums = g()
ans = X * min(a + b for a, b in zip(nums, nums[1:]))
print(ans)