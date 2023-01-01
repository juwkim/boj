input = __import__('sys').stdin.readline


def g(): return [*map(int, input().split())]


N = int(input())
home = [g() for _ in range(N)]
# horizontal, vertical, diagonal
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for i in range(N):
    for j in range(2, N):
        if home[i][j] == 1:
            continue
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
        if i >= 2:
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        if i >= 1 and home[i][j-1] == 0 and home[i-1][j] == 0:
            dp[i][j][2] = sum(dp[i-1][j-1])
print(sum(dp[-1][-1]))