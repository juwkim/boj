N, *nums = map(int, open(0).read().split())
dp = [[0 for _ in range(3)] for _ in range(N+1)]
dp[1][1] = nums[0]
for i in range(2, 1 + N):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + nums[i-1]
    dp[i][2] = dp[i-1][1] + nums[i-1]
print(max(dp[N]))