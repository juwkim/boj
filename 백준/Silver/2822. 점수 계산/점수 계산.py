nums = sorted((int(input()), i+1) for i in range(8))[3:]
print(sum(nums[i][0] for i in range(5)))
print(*sorted(nums[i][1] for i in range(5)))