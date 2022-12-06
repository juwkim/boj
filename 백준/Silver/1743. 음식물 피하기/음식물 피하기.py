g = lambda: [*map(int, input().split())]

import sys
sys.setrecursionlimit(10**6)
def dfs(x, y):
    global num
    for p, q in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
        if 0 <= p < N and 0 <= q < M and Map[p][q]:
            Map[p][q] = 0
            num += 1
            dfs(p, q)

N, M, K = g()
Map = [bytearray(M) for _ in range(N)]
for _ in range(K):
    r, c = g()
    Map[r-1][c-1] = 1

ans = 0
for i in range(N):
    for j in range(M):
        if Map[i][j]:
            Map[i][j] = 0
            num = 1
            dfs(i, j)
            ans = max(ans, num)
print(ans)