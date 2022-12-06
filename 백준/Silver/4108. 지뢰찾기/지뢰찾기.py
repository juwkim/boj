while (s:= input()) != '0 0':
    r, c = map(int, s.split())
    board = [input() for _ in range(r)]
    res = [[0] * (c+2) for _ in range(r+2)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == '*':
                res[i+1][j+1] = '*'
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if res[x][y] != '*':
                            res[x][y] += 1
    for line in res[1:-1]:
        print(*line[1:-1], sep='')