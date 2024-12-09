import sys
input = sys.stdin.readline

N = int(input())
A = [[*map(int, input().split())] for _ in range(N)]
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(N):
        dp[i + 1][j + 1] = 2 * max(dp[i + 1][j], dp[i][j + 1]) + A[i][j]
print(dp[N][N])