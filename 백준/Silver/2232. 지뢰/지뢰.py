N, *nums = map(int, open(0))
nums = [0] + nums + [0]

for i in range(1, N + 1):
    if nums[i] >= max(nums[i - 1], nums[i + 1]):
        print(i)