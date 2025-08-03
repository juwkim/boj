t = [[0]*13] + [[0] + [*map(int, input().split())] for _ in range(12)]

INF = 10**18
dp = [[INF]*13 for _ in range(7)]
dp[1][1] = t[2][1]
dp[1][2] = t[1][2]
for gidx in range(2, 7):
    m1 = 2 * gidx - 1
    m2 = 2 * gidx
    prev1 = 2 * (gidx - 1) - 1
    prev2 = 2 * (gidx - 1)
    for prev_exit in (prev1, prev2):
        base = dp[gidx - 1][prev_exit]
        dp[gidx][m1] = min(dp[gidx][m1], base + t[prev_exit][m2] + t[m2][m1])
        dp[gidx][m2] = min(dp[gidx][m2], base + t[prev_exit][m1] + t[m1][m2])
print(min(dp[6][11], dp[6][12]))