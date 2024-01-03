import sys
import math

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
matrix = [g() for _ in range(N)]
dp = [[math.inf] * N for _ in range(N)] # dp[i][j]: (i, j)까지의 최소 비용
for i in range(N):
    dp[i][i] = 0
for d in range(1, N):
    for i, j in zip(range(N-d), range(d, N)):
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
print(dp[0][N-1])