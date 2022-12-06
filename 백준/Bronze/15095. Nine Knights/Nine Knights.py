cnt = 0
board = [[0, 0] + [*input()] + [0, 0] for _ in range(5)]
board = [[0]*9]*2 + board + [[0]*9]*2
flag = 'valid'
for i in range(2, 7):
    for j in range(2, 7):
        if board[i][j] == 'k':
            cnt += 1
            if any(board[x][y] == 'k' for x, y in ((i+1, j-2), (i+1, j+2), (i+2, j-1), (i+2, j+1))):
                flag = 'invalid'
                break
print(flag if cnt == 9 else 'invalid')