import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N, M = g()
a = [g() for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i == 1:
            dp[i][j] = dp[i][j - 1] + a[i - 1][j - 1]
        elif j == 1:
            dp[i][j] = dp[i - 1][j] + a[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + a[i - 1][j - 1]
if dp[N][M] <= int(input()):
    print("YES")
    print(dp[N][M])
else:
    print("NO")