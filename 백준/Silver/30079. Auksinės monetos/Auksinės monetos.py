N, M = map(int, input().split())
grid = [input() for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) + (grid[i][j] == 'o') - (grid[i][j] == 'x') * 10**9
print(max(max(row) for row in dp))