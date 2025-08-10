import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    W, H = map(int, input().split())
    if W == 0:
        break
    grid = [input() for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            if grid[i][j].isdigit():
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) * 10 + int(grid[i][j])
    print(max(max(row) for row in dp))