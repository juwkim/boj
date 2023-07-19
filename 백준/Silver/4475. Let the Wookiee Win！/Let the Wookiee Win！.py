def check(a, b, c):
    res = False
    board[a][b] = c
    
    for i in range(5):
        if board[i][:4] == [c] * 4 or board[i][1:] == [c] * 4:
            res = True
            break
    for j in range(5):
        if all(board[i][j] == c for i in range(4)) or all(board[i][j] == c for i in range(1, 5)):
            res = True
            break
    if all(board[i][j] == c for i, j in ((0, 1), (1, 2), (2, 3), (3, 4))):
        res = True
    if all(board[i][j] == c for i, j in ((0, 0), (1, 1), (2, 2), (3, 3))):
        res = True
    if all(board[i][j] == c for i, j in ((1, 1), (2, 2), (3, 3), (4, 4))):
        res = True
    if all(board[i][j] == c for i, j in ((1, 0), (2, 1), (3, 2), (4, 3))):
        res = True
    if all(board[i][j] == c for i, j in ((0, 3), (1, 2), (2, 1), (3, 0))):
        res = True
    if all(board[i][j] == c for i, j in ((4, 0), (3, 1), (2, 2), (1, 3))):
        res = True
    if all(board[i][j] == c for i, j in ((3, 1), (2, 2), (1, 3), (0, 4))):
        res = True
    if all(board[i][j] == c for i, j in ((4, 1), (3, 2), (2, 3), (1, 4))):
        res = True
    board[a][b] = '*'
    return res 
    

while True:
    try:
        board = [input().split() for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if board[i][j] != '*':
                    continue
                if check(i, j, 'O') or check(i, j, 'X'):
                    continue
                print(i * 5 + j + 1)
                break
            else:
                continue
            break
        if input() == "Finished":
            break
    except:
        break