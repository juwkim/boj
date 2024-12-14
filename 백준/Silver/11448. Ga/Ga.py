import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    N = int(input())
    a = [input() for _ in range(N)]
    visited = [bytearray(N) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if a[i][j] != 'w' or visited[i][j]: continue
            dq = deque([(i, j)])
            while dq:
                x, y = dq.popleft()
                for nx, ny in (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1):
                    if 0 <= nx < N and 0 <= ny < N and a[nx][ny] == '-' and not visited[nx][ny]:
                        ans += 1
                        visited[nx][ny] = 1
                        dq.append((nx, ny))
    print(ans)