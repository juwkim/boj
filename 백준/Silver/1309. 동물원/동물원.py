mod = 9901
N = int(input())
dp = [[1] * 3 for _ in range(N)]
for i in range(N-1):
    dp[i+1][0] = sum(dp[i]) % mod
    dp[i+1][1] = (dp[i][0] + dp[i][2]) % mod
    dp[i+1][2] = (dp[i][0] + dp[i][1]) % mod
print(sum(dp[N-1]) % mod) 