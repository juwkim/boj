import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

sys.setrecursionlimit(25 * 10 ** 4)
n = int(input())
board = [g() for _ in range(n)]
visited = [[False] * n for _ in range(n)]
mem = [[1] * n for _ in range(n)]

def dfs(i, j):
    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and board[i][j] < board[ni][nj]:
            if visited[ni][nj]:
                mem[i][j] = max(mem[i][j], mem[ni][nj] + 1)
            else:
                visited[ni][nj] = True
                mem[i][j] = max(mem[i][j], dfs(ni, nj) + 1)
    return mem[i][j]

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        visited[i][j] = True
        dfs(i, j)
print(max(max(row) for row in mem))