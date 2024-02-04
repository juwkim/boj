import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
while True:
    N, M, S = g()
    if N == 0:
        break
    board = [list(input()) for _ in range(N)]
    x, y, d = -1, -1, -1
    for i in range(N):
        for j in range(M):
            if board[i][j] in 'NLSO':
                x, y = i, j
                d = 'NLSO'.index(board[i][j])
                break
        else:
            continue
        break
    ans = 0
    for cmd in input():
        match cmd:
            case 'D':
                d = (d + 1) % 4
            case 'E':
                d = (d - 1) % 4
            case 'F':
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != '#':
                    x, y = nx, ny
                    if board[x][y] == '*':
                        ans += 1
                        board[x][y] = '.'
    print(ans)