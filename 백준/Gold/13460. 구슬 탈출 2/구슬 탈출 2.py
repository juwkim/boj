import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

def find(x, board):
    for i in range(N):
        for j in range(M):
            if board[i][j] == x:
                return i, j
    return -1, -1

N, M = g()
board = [list(input()) for _ in range(N)]
rx, ry = find("R", board); board[rx][ry] = "."
bx, by = find("B", board); board[bx][by] = "."
ox, oy = find("O", board)
dq = deque([(rx, ry, bx, by, 0)])
visited = set([(rx, ry, bx, by)])
ans = -1
while dq:
    rx, ry, bx, by, cnt = dq.popleft()
    if cnt == 10:
        break
    cnt += 1
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nrx, nry, nbx, nby = rx, ry, bx, by
        while board[nrx + dx][nry + dy] == ".":
            nrx += dx; nry += dy
        while board[nbx + dx][nby + dy] == ".":
            nbx += dx; nby += dy
        if board[nbx + dx][nby + dy] == "O":
            continue
        if board[nrx + dx][nry + dy] == "O":
            ans = cnt
            break
        if nrx == nbx and nry == nby:
            if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                nrx -= dx; nry -= dy
            else:
                nbx -= dx; nby -= dy
        if (nrx, nry, nbx, nby) not in visited:
            dq.append((nrx, nry, nbx, nby, cnt))
    else:
        continue
    break
print(ans)