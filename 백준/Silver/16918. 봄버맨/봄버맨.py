import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

R, C, N = g()
if N % 2 == 0:
    l = 'O' * C
    for _ in range(R):
        print(l)
else:
    board = [input() for _ in range(R)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for _ in range((N - 1) >> 1):
        tmp = [['O'] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    tmp[i][j] = '.'
                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]
                        if 0 <= x < R and 0 <= y < C:
                            tmp[x][y] = '.'
        board = tmp
    for i in range(R):
        print(*board[i], sep='')