l, k = map(int, input().split())
dp = [[0] * (l + 1), [0] * (l + 1)]
dp[0][0] = 1
for i in range(1, l + 1):
    dp[0][i] = dp[1][i - 1]
    dp[1][i] = dp[0][i - 1] + (dp[0][i - k] if i >= k else 0)
print(sum(dp[1]))