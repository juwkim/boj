import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n = int(input())
m = [g() for _ in range(n)]
is_middle = [bytearray(n + 1) for _ in range(n + 1)]
for _ in range(int(input())):
    r, c = g()
    is_middle[r][c] = 1
dp = [[(0, 0)] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        a, b = max(dp[i - 1][j], dp[i][j - 1])
        dp[i][j] = a + m[i - 1][j - 1], b + is_middle[i][j]
print(*dp[n][n])