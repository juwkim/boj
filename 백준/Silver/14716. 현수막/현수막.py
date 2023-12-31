import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

M, N = g()
Map = [input().split() for _ in range(M)]
ans = 0
for x in range(M):
    for y in range(N):
        if Map[x][y] == '0':
            continue
        Map[x][y] = '0'
        ans += 1
        stack = [(x, y)]
        while stack:
            i, j = stack.pop()
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and Map[ni][nj] == '1':
                    Map[ni][nj] = '0'
                    stack.append((ni, nj))                    
print(ans)