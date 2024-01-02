import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

R, C = g()
board = [list(input()) for _ in range(R)]
def find(target):
    for i in range(R):
        for j in range(C):
            if board[i][j] == target:
                board[i][j] = '.'
                return i, j
    return -1, -1

x, y = find('S')
dq = deque([(x, y)])
visited = [[False] * C for _ in range(R)]
visited[x][y] = True
water = deque()
for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            water.append((i, j))

time = 0
while True:
    time += 1
    n_water = deque()
    while water:
        x, y = water.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == '.':
                board[nx][ny] = '*'
                n_water.append((nx, ny))
    water = n_water
    
    n_dq = deque()
    while dq:
        x, y = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == '.':
                    n_dq.append((nx, ny))
                elif board[nx][ny] == 'D':
                    print(time)
                    exit()
    if not n_dq:
        break
    dq = n_dq
print("KAKTUS")