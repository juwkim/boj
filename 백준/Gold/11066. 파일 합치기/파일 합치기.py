import sys
import math
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    K = int(input())
    files = g()
    px = [0] * (K + 1)
    for i in range(1, K + 1):
        px[i] = px[i-1] + files[i-1]
    dp = [[math.inf] * K for _ in range(K)] # dp[i][j]: (i, j)까지의 최소 비용
    for i in range(K):
        dp[i][i] = 0
    for d in range(1, K):
        for i, j in zip(range(K - d), range(d, K)):
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + px[j + 1] - px[i])
    print(dp[0][K-1])