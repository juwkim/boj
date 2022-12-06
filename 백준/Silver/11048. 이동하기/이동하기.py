g = lambda: [*map(int, input().split())]

N, M = g()
Map = [g() for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, 1 + N):
    for j in range(1, 1 + M):
        dp[i][j] = Map[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])
print(dp[N][M])