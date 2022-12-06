f = lambda: int(input())

n = f()
board = [input() for _ in range(n)]
play = [input() for _ in range(n)]
res = [[0] * (n+2) for _ in range(n+2)]
mine = False
for i in range(n):
    for j in range(n):
        if board[i][j] == '*':
            if play[i][j] == 'x':
                mine = True
            res[i+1][j+1] = '*'
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if x != i + 1 or y != j + 1:
                        if 1 <= x <= n and 1 <= y <= n and board[x-1][y-1] != '*':
                            res[x][y] += 1
for i in range(n):
    for j in range(n):
        if play[i][j] == 'x':
            print(res[i+1][j+1], end='')
        elif mine and res[i+1][j+1] == '*':
            print(res[i+1][j+1], end='')
        else:
            print('.', end='')
    print()