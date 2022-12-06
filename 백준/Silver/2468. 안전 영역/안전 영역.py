g = lambda: [*map(int, input().split())]

import sys
sys.setrecursionlimit(10000)
N = int(input())
Map = [g() for _ in range(N)]
ans, h = 1, 1

def dfs(i, j):
    visited[i][j] = 1
    for a, b in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
        if 0 <= a <= N-1 and 0 <= b <= N-1 and visited[a][b] == 0 and Map[a][b] > h:
            dfs(a, b)

while True:
    num = 0
    visited = [bytearray(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and Map[i][j] > h:
                num += 1
                dfs(i, j)    
    
    ans = max(ans, num)
    h += 1
    if num == 0:
        break
print(ans)