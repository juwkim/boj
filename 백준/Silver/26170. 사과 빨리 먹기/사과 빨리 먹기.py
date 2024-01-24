import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import inf

board = [g() for _ in range(5)]
r, c = g()
def dfs(x, y, apple, step):
    global ans
    if apple == 3:
        ans = min(ans, step)
        return
    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] != -1:
            apple += board[nx][ny] == 1
            tmp = board[nx][ny]
            board[nx][ny] = -1
            dfs(nx, ny, apple, step + 1)
            apple -= tmp == 1
            board[nx][ny] = tmp

ans = inf
apple = board[r][c] == 1
board[r][c] = -1
dfs(r, c, apple, 0)
if ans == inf:
    ans = -1
print(ans)