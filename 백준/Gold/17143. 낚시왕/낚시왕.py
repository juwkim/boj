import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

R, C, M = g()
board = [[[] for _ in range(C)] for _ in range(R)]
shark = []
for _ in range(M):
    r, c, s, d, z = g()
    board[r - 1][c - 1] = [s, d - 1, z]
    shark.append((r - 1, c - 1))

ans = 0
for j in range(C):
    if not shark:
        break
    for i in range(R):
        if board[i][j]:
            ans += board[i][j][2]
            shark.remove((i, j))
            break
    new_shark = []
    new_board = [[[] for _ in range(C)] for _ in range(R)]
    for x, y in shark:
        s, d, z = board[x][y]
        if d < 2:
            dx = [-1, 1, 0, 0][d]
            x += dx * s
            while x < 0 or x >= R:
                if x < 0:
                    x = -x
                else:
                    x = 2 * (R - 1) - x
                d ^= 1
        else:
            dy = [0, 0, 1, -1][d]
            y += dy * s
            while y < 0 or y >= C:
                if y < 0:
                    y = -y
                else:
                    y = 2 * (C - 1) - y
                d ^= 1
        
        if not new_board[x][y] or new_board[x][y][2] < z:
            if not new_board[x][y]:
                new_shark.append((x, y))
            new_board[x][y] = [s, d, z]
    shark = new_shark
    board = new_board
print(ans)