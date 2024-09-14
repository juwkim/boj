N, M = map(int, input().split())
dp = [1] * M + [0] * (N + 1 - M)
for i in range(M, N + 1):
    dp[i] = (dp[i - M] + dp[i - 1]) % 1000000007
print(dp[N])