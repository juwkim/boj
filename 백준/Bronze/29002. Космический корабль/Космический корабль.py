g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()
idx = nums.index(sum(nums) // 2)
nums.append(nums[idx])
del nums[idx]
print(*nums)