cmd, *l = input().split()
n, *nums = map(int, l)
board = [[0] * 8 for _ in range(8)]
WHITE, BLACK = 1, 2
match cmd:
    case 'a':
        board[3][3], board[4][4] = WHITE, WHITE
        board[3][4], board[4][3] = BLACK, BLACK
    case 'b':
        for i in range(8):
            board[i][i], board[i][7 - i] = BLACK, WHITE
    case 'c':
        for i in range(8):
            board[i][2], board[i][3] = BLACK, BLACK
            board[i][4], board[i][5] = WHITE, WHITE

cur, opp = BLACK, WHITE
for i in range(n):
    r, c = nums[2 * i] - 1, nums[2 * i + 1] - 1
    board[r][c] = cur
    for dr, dc in (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1):
        x, y = r + dr, c + dc
        while 0 <= x < 8 and 0 <= y < 8 and board[x][y] == opp:
            x, y = x + dr, y + dc
            if 0 <= x < 8 and 0 <= y < 8 and board[x][y] == cur:
                while (x, y) != (r, c):
                    x, y = x - dr, y - dc
                    board[x][y] = cur
    cur, opp = opp, cur

b, w = sum(x.count(BLACK) for x in board), sum(x.count(WHITE) for x in board)
print(b, w)