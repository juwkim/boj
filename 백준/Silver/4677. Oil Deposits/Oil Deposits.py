import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

while True:
    m, n = map(int, input().split())
    if m == 0:
        break
    A = [input() for _ in range(m)]
    visited = [bytearray(n) for _ in range(m)]
    ans = 0
    for i in range(m):
        for j in range(n):
            if A[i][j] == '*' or visited[i][j]:
                continue
            ans += 1
            visited[i][j] = True
            dq = deque([(i, j)])
            while dq:
                x, y = dq.popleft()
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == dy == 0:
                            continue
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue
                        if A[nx][ny] == '*' or visited[nx][ny]:
                            continue
                        visited[nx][ny] = True
                        dq.append((nx, ny))
    print(ans)