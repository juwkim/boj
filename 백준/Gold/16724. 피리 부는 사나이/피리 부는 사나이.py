import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
board = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ans = 0
step = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        step += 1
        visited[i][j] = step
        x, y = i, j
        while True:
            if board[x][y] == 'U':
                x -= 1
            elif board[x][y] == 'D':
                x += 1
            elif board[x][y] == 'L':
                y -= 1
            elif board[x][y] == 'R':
                y += 1
            if visited[x][y]:
                if visited[x][y] == step:
                    ans += 1
                break
            visited[x][y] = step
print(ans)