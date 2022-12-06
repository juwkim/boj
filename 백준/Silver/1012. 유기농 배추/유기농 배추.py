import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**9)
g = lambda: [*map(int, input().split())]

def bfs(i, j):
    
    if i < 0 or i >= N or j < 0 or j >= M or Map[i][j] == 0:
        return
    Map[i][j] = 0
    bfs(i-1, j)
    bfs(i+1, j)
    bfs(i, j-1)
    bfs(i, j+1)
        
for _ in range(int(input())):
    M, N, K = g()
    Map = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = g()
        Map[y][x] = 1
    
    ans = 0
    for i in range(N):
        for j in range(M):
            if Map[i][j]:
                bfs(i, j)
                ans += 1
    
    print(ans)