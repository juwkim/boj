import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
mask = lambda k, n: k | (1 << n)
N = int(input())
def solve(N):
    mod = 1_000_000_000
    dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(2)]
    cur, prv = 0, 1
    for j in range(1, 10):
        dp[cur][j][1 << j] = 1
    for _ in range(N - 1):
        cur, prv = cur ^ 1, prv ^ 1
        dp[cur] = [[0] * (1 << 10) for _ in range(10)]
        for k in range(1 << 10):
            dp[cur][0][mask(k, 0)] += dp[prv][1][k]
            dp[cur][9][mask(k, 9)] += dp[prv][8][k]
            dp[cur][0][mask(k, 0)] %= mod
            dp[cur][9][mask(k, 9)] %= mod
        for j in range(1, 9):
            for k in range(1 << 10):
                dp[cur][j][mask(k, j)] += dp[prv][j - 1][k] + dp[prv][j + 1][k]
                dp[cur][j][mask(k, j)] %= mod
    ans = sum(dp[cur][j][(1 << 10) - 1] for j in range(10)) % mod
    return ans

print(solve(N))