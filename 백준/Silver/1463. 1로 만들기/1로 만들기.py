N = int(input())
dp = [100] * (3*N+1)
dp[1] = 0
for i in range(1, N+1):
    minn = dp[i] + 1
    dp[i+1] = min(minn, dp[i+1])
    dp[i*2] = min(minn, dp[i*2])
    dp[i*3] = min(minn, dp[i*3])
print(dp[N])