N, M = map(int, input().split())
dp = [1] + [0] * N
for i in range(N):
    dp[i + 1] = (dp[i + 1] + dp[i]) % 1000000007
    if i + M <= N:
        dp[i + M] = (dp[i + M] + dp[i]) % 1000000007
print(dp[N] % 1000000007)