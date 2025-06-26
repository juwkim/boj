import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from collections import deque

N, M = g()
image = []
for _ in range(N):
    row = g()
    image.append([(row[3*j], row[3*j+1], row[3*j+2]) for j in range(M)])

cnt = 0
dx = -1, -1, -1, 0, 0, 1, 1, 1
dy = -1, 0, 1, -1, 1, -1, 0, 1
visited = [bytearray(M) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        cnt += 1
        color = image[i][j]
        dq = deque([(i, j)])
        visited[i][j] = True
        while dq:
            x, y = dq.popleft()
            for d in range(8):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and image[nx][ny] == color:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
print(cnt)