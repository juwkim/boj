import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

R, C, K = g()
Map = [input() for _ in range(R)]
visited = [[False] * C for _ in range(R)]
def dfs(i, j, cnt=1):
    if cnt == K:
        if (i, j) == (0, C - 1):
            return 1
        else:
            return 0
    ret = 0
    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj] and Map[ni][nj] == '.':
            visited[ni][nj] = True
            ret += dfs(ni, nj, cnt + 1)
            visited[ni][nj] = False
    return ret

visited[R - 1][0] = True
ans = dfs(R - 1, 0)
print(ans)