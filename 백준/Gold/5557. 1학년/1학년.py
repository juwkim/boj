N, num, *nums, res = map(int, open(0).read().split())
dp = [0] * 21
dp[num] = 1
for num in nums:
    tmp = [0] * 21
    for i in range(21):
        if i + num <= 20:
            tmp[i + num] += dp[i]
        if i - num >= 0:
            tmp[i - num] += dp[i]
    dp = tmp
print(dp[res])