import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]) + (board[i][j] == 'C')
    print(dp[n][m])