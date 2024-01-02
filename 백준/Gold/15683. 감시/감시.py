import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
board = [g() for _ in range(N)]
def fill(x, y, d):
    dx = [-1, 0, 1, 0][d]
    dy = [0, 1, 0, -1][d]
    x += dx
    y += dy
    filled = []
    while 0 <= x < N and 0 <= y < M and board[x][y] != 6:
        if board[x][y] != '#':
            board[x][y] = '#'
            filled.append((x, y))
        x += dx
        y += dy
    return filled

def unfilled(filled):
    for x, y in filled:
        board[x][y] = 0

cctv = []
five = []
for i in range(N):
    for j in range(M):
        if board[i][j] == '#' or board[i][j] == 0 or board[i][j] == 6:
            continue
        if 1 <= board[i][j] <= 4:
            cctv.append((i, j, board[i][j]))
        else: # board[i][j] == 5
            five.append((i, j))
        board[i][j] = '#'

for x, y in five:
    for d in range(4):
        fill(x, y, d)

def dfs(idx):
    if idx == len(cctv):
        return sum(l.count(0) for l in board)
    x, y, c = cctv[idx]
    idx += 1
    ans = float('inf')
    if c == 1:
        for d in range(4):
            filled = fill(x, y, d)
            ans = min(ans, dfs(idx))
            unfilled(filled)
    elif c == 2:
        for d in range(2):
            filled = fill(x, y, d) + fill(x, y, d + 2)
            ans = min(ans, dfs(idx))
            unfilled(filled)
    elif c == 3:
        for d in range(4):
            filled = fill(x, y, d) + fill(x, y, (d + 1) % 4)
            ans = min(ans, dfs(idx))
            unfilled(filled)
    elif c == 4:
        for d in range(4):
            filled = fill(x, y, d) + fill(x, y, (d + 1) % 4) + fill(x, y, (d + 2) % 4)
            ans = min(ans, dfs(idx))
            unfilled(filled)
    return ans

print(dfs(0))