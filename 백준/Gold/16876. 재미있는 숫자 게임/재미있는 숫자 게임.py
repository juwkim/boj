N, M = input().split()
d = [int(i) for i in N]
N, M = int(N), int(M)
dp = [[-1] * M for _ in range(10000)]

def solve(m):
    n = d[0] * 1000 + d[1] * 100 + d[2] * 10 + d[3]
    if m == M:         return n <= N
    if dp[n][m] != -1: return dp[n][m]
    turn = m & 1
    dp[n][m] = turn ^ 1
    for i in range(4):
        d[i] = (d[i] + 1) % 10
        p = solve(m + 1)
        d[i] = (d[i] - 1) % 10
        if p == turn:
            dp[n][m] = turn
            break
    return dp[n][m]
if solve(0):
    print("cubelover")
else:
    print("koosaga")