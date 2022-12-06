import sys
sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]

M, N = g()
Map = [input() for _ in range(M)]
visited = [bytearray(N) for _ in range(M)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 'NO'
def dfs(x, y):
    global ans
    if x == M - 1:
        ans = 'YES'
        return 1
    
    visited[x][y] = 1
    for a, b in zip(dx, dy):
        i, j = x + a, y + b
        if 0 <= i < M and 0 <= j < N and visited[i][j] == 0 and Map[i][j] == '0':
            ret = dfs(i, j)
            if ret == 1:
                return 1
    return 0


for y in range(N):
    if visited[0][y] == 0 and Map[0][y] == '0':
        ret = dfs(0, y)
        if ret == 1:
            break
print(ans)