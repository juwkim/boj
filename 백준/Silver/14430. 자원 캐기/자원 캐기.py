import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [input().split() for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + (a[i - 1][j - 1] == '1')
print(dp[N][M])