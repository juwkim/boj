mod = 1_000_000_000
N = int(input())
dp = [None, [0] + [1 for _ in range(9)]] + [[0 for _ in range(10)] for _ in range(N-1)]
for i in range(2, 1+N):
    dp[i][1] += dp[i-1][0]
    dp[i][8] += dp[i-1][9]
    dp[i][1] %= mod
    dp[i][8] %= mod
    for j in range(1, 9):
        dp[i][j-1] += dp[i-1][j]
        dp[i][j+1] += dp[i-1][j]
        dp[i][j-1] %= mod
        dp[i][j+1] %= mod
print(sum(dp[N]) % mod)