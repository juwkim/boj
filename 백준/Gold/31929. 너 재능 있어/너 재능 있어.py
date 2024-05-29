g = lambda: [*map(int, input().split())]

N = int(input())
W = g()
M = int(input())
L = g()
K = int(input())
dp = [[0] * (N + 1) for _ in range(M + 1)]
for i in range(M): dp[i + 1][0] = max((dp[i][0] - 1) // K * K, dp[i][0] - L[i])
for j in range(N): dp[0][j + 1] = dp[0][j] + W[j]
for i in range(M):
    for j in range(N):
        dp[i + 1][j + 1] = max(dp[i + 1][j] + W[j], max((dp[i][j + 1] - 1) // K * K, dp[i][j + 1] - L[i]))
print(dp[M][N])