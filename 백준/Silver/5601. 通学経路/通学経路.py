import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

a, b = g()
blocked = [bytearray(b + 1) for _ in range(a + 1)]
for _ in range(int(input())):
    x, y = g()
    blocked[x][y] = 1

dp = [[0] * (b + 1) for _ in range(a + 1)]
dp[0][1] = 1
for i in range(1, a + 1):
    for j in range(1, b + 1):
        if not blocked[i][j]:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[a][b])