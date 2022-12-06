g = lambda: [*map(int, input().split())]

mod = 1_000_000_007
dp_size = 101
dp = [[0] * dp_size for _ in range(dp_size)]

for i in range(1, dp_size):
    dp[1][i] = 1

for i in range(2, dp_size):
    for j in range(i, dp_size):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j-1]) * i % mod
for cnt in range(1, 1 + int(input())):
    M, N = g()
    print(f'Case #{cnt}:', dp[M][N])