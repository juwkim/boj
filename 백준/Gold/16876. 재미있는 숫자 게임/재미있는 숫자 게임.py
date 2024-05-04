N, M = input().split()
d = [*map(int, N)]
N, M = map(int, (N, M))
dp = [[-1] * (M + 2) for _ in range(10000)]

def num():
    return d[0] * 1000 + d[1] * 100 + d[2] * 10 + d[3]

def solve(m):
    n = num()
    if dp[n][m] != -1:
        return dp[n][m]
    if m > M:
        dp[n][m] = n > N
        return dp[n][m]
    turn = m & 1
    for i in range(4):
        d[i] = (d[i] + 1) % 10
        p = solve(m + 1)
        d[i] = (d[i] - 1) % 10
        if p == turn:
            dp[n][m] = turn
            return dp[n][m]
    dp[n][m] = turn ^ 1
    return dp[n][m]
print(("cubelover", "koosaga")[solve(1)])