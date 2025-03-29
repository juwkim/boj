N = int(input())
dp = [(0, 0)] + [(1e9, 1e9)] * N
for i in range(N):
    dp[i + 1] = min(dp[i + 1], (dp[i][0] + 1, dp[i][1] + 1))
    if i * 3 <= N:
        dp[i * 3] = min(dp[i * 3], (dp[i][0] + 1, dp[i][1] + 3))
    if i * i <= N:
        dp[i * i] = min(dp[i * i], (dp[i][0] + 1, dp[i][1] + 5))
print(*dp[N])