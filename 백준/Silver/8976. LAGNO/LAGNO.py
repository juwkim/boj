dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
board = [input() for _ in range(8)]
ans = 0
for i in range(8):
    for j in range(8):
        if board[i][j] != '.':
            continue
        num = 0
        for a, b in zip(dx, dy):
            x, y = i + a, j + b
            while 0 <= x < 8 and 0 <= y < 8 and board[x][y] != '.':
                if board[x][y] == 'B':
                    num += max(abs(x - i), abs(y - j)) - 1
                    break
                x, y = x + a, y + b
        ans = max(ans, num)
print(ans)