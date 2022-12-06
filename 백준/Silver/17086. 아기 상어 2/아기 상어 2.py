import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

from collections import deque
N, M = g()
buf = [g() for _ in range(N)]

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]
def bfs(i, j):

    visited = [bytearray(M) for _ in range(N)]
    visited[i][j] = 1
    dq = deque([(i, j, 1)])
    while dq:
        x, y, d = dq.popleft()
        for s, t in zip(dx, dy):
            a, b = x + s, y + t
            if 0 <= a < N and 0 <= b < M and visited[a][b] == 0:
                if buf[a][b]:
                    return d
                else:
                    visited[a][b] = 1
                    dq.append((a, b, d + 1))


ans = 0
for i in range(N):
    for j in range(M):
        if buf[i][j] == 0:
            ans = max(ans, bfs(i, j))
print(ans)