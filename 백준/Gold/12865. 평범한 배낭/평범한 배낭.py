N, K = map(int, input().split())
sack = [[0, 0]] + [[*map(int, input().split())] for _ in range(N)]
dp = [[0 for i in range(K+1)] for j in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= sack[i][0]:
            dp[i][j] = max(dp[i-1][j], sack[i][1] + dp[i-1][j-sack[i][0]])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])