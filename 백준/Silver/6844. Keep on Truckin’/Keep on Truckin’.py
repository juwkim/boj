A, B, N, *l = map(int, open(0))
nums = sorted(l + [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000])
dp = [0] * len(nums)
dp[0] = 1
for i in range(1, len(nums)):
    for j in range(i):
        if A <= nums[i] - nums[j] <= B:
            dp[i] += dp[j]
print(dp[-1])