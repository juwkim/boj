import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

R, C = g()
dp = [[0] * (C + 1) for _ in range(R + 1)]
dp[1][1] = 1
for _ in range(int(input())):
    r, c = g()
    dp[r][c] = -1

for i in range(1, R + 1):
    for j in range(1, C + 1):
        if i == 1 and j == 1 or dp[i][j] == -1:
            continue
        dp[i][j] = max(0, dp[i-1][j]) + max(0, dp[i][j-1])
print(dp[R][C])