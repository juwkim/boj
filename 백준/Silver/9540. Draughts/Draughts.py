import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(i, j, board):
    ret = 0
    for dx, dy in (-1, -1), (-1, 1), (1, -1), (1, 1):
        x1, y1 = i + dx, j + dy
        x2, y2 = i + 2 * dx, j + 2 * dy
        if 0 <= x2 < 10 and 0 <= y2 < 10 and board[x1][y1] == 'B' and board[x2][y2] == '#':
            board[i][j] = '#'
            board[x1][y1] = '#'
            board[x2][y2] = 'W'
            cnt = 1 + dfs(x2, y2, board)
            board[i][j] = 'W'
            board[x1][y1] = 'B'
            board[x2][y2] = '#'
            ret = max(ret, cnt)
    return ret

for _ in range(int(input())):
    input()
    board = [list(input()) for _ in range(10)]
    ans = 0
    for i in range(10):
        for j in range(i & 1 == 0, 10, 2):
            if board[i][j] == 'W':
                ans = max(ans, dfs(i, j, board))
    print(ans)