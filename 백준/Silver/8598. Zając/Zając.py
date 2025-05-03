import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'z':
            sx, sy = i, j
        elif board[i][j] == 'n':
            ex, ey = i, j

board[sx][sy] = 'x'
dq = deque([(sx, sy, 0)])
ans = "NIE"
while dq:
    x, y, d = dq.popleft()
    if x == ex and y == ey:
        ans = d
        break
    for dx, dy in (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'x':
            board[nx][ny] = 'x'
            dq.append((nx, ny, d + 1))
print(ans)