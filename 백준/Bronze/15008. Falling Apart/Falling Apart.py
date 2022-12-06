g = lambda: [*map(int, input().split())]
g()
nums = sorted(g(), reverse=True)
print(sum(nums[::2]), sum(nums[1::2]))