N, M = map(int, input().split())
grid = [input() for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
ans = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'x':
            dp[i + 1][j + 1] = -1e9
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) + (grid[i][j] == 'o')
        ans = max(ans, dp[i + 1][j + 1])
print(ans)