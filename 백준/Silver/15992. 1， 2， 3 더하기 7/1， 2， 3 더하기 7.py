import sys
input = sys.stdin.readline

dp = [[0] * 1001 for _ in range(1001)]
dp[0][0] = 1
for i in range(1, 1001):
    for j in range(1, i + 1):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 3][j - 1]) % 1000000009
for _ in range(int(input())):
    n, m = map(int, input().split())
    print(dp[n][m])