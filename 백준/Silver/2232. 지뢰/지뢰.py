N, *nums = map(int, open(0))
nums.append(0)
print(*[i + 1 for i in range(N) if nums[i] >= max(nums[i - 1], nums[i + 1])])