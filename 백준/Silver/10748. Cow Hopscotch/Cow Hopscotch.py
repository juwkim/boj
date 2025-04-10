g = lambda: [*map(int, input().split())]

MOD = 10**9 + 7
R, C, K = g()
grid = [g() for _ in range(R)]
dp = [[0] * C for _ in range(R)]
dp[0][0] = 1
for i in range(R):
    for j in range(C):
        for x in range(i + 1, R):
            for y in range(j + 1, C):
                if grid[x][y] != grid[i][j]:
                    dp[x][y] = (dp[x][y] + dp[i][j]) % MOD
print(dp[-1][-1])