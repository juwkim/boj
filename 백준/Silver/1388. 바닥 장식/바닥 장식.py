g = lambda: map(int, input().split())
N, M = g()
Map = [list(input()) for _ in range(N)]
ans = 0
def dfs(i, j):
    if Map[i][j] == '-':
        Map[i][j] = 0
        if j < M - 1 and Map[i][j+1] == '-':
            dfs(i, j + 1)
    elif Map[i][j] == '|':
        Map[i][j] = 0
        if i < N - 1 and Map[i+1][j] == '|':
            dfs(i + 1, j)
    
    
for i in range(N):
    for j in range(M):
        if Map[i][j]:
            ans += 1
            dfs(i, j)
print(ans)