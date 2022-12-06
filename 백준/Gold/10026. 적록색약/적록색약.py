import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 4)
def dfs(i, j):
    visited[i][j] = 1
    for x, y in ((i+1, j), (i, j+1), (i, j-1), (i-1, j)):
        if 0 <= x < N and 0 <= y < N and Map[x][y] == Map[i][j] and visited[x][y] == 0:
            visited[x][y] = 1
            dfs(x, y)

    

N = int(input())
Map = [[*input()] for _ in range(N)]
visited = [[0] * N for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            ans += 1
print(ans, end=' ')


for i in range(N):
    for j in range(N):
        if Map[i][j] == 'R':
            Map[i][j] = 'G'
visited = [[0] * N for _ in range(N)]        
ans = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i, j)
            ans += 1
print(ans)