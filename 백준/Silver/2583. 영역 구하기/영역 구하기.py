import sys
sys.setrecursionlimit(10**5)
g = lambda: [*map(int, input().split())]

M, N, K = g()
Map = [bytearray(M) for _ in range(N)]
for _ in range(K):
    x0, y0, x1, y1 = g()
    for i in range(x0, x1):
        for j in range(y0, y1):
            Map[i][j] = 1
    
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
visited = [bytearray(M) for _ in range(N)]

def dfs(i, j):
    global num
    visited[i][j] = 1
    for p, q in zip(dx, dy):
        u, v = i + p, j + q
        if 0 <= u < N and 0 <= v < M and Map[u][v] == 0 and visited[u][v] == 0:
            num += 1
            dfs(u, v)

cnt = 0
ans = []
for i in range(N):
    for j in range(M):
        if Map[i][j] == 0 and visited[i][j] == 0:
            cnt += 1
    
            num = 1
            dfs(i, j)
            ans.append(num)

ans.sort()
print(cnt)
print(*ans)