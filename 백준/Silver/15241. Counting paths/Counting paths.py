import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [input() for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][1] = 1
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if a[i - 1][j - 1] == '.':
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
print(dp[N][M] % 1000000007)