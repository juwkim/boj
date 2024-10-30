import sys
input = sys.stdin.readline

N = int(input())
A = [[*map(int, input().split())] for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if A[i][j] == 0: continue
        if i + A[i][j] < N: dp[i + A[i][j]][j] += dp[i][j]
        if j + A[i][j] < N: dp[i][j + A[i][j]] += dp[i][j]
print(dp[-1][-1])