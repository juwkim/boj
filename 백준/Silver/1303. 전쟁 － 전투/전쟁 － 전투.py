import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

M, N = g()
Map = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
def dfs(x, y, target):
    cnt = 1
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny] or Map[nx][ny] != target:
            continue
        visited[nx][ny] = True
        cnt += dfs(nx, ny, target)
    return cnt

W, B = 0, 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        visited[i][j] = True
        if Map[i][j] == 'W':
            W += dfs(i, j, 'W') ** 2
        else:
            B += dfs(i, j, 'B') ** 2
print(W, B)