from collections import deque
g = lambda: [*map(int, input().split())]

M, N, M1, M2 = g()
a = [g() for _ in range(M)]
x, y = -1, -1
for i in range(M):
    for j in range(N):
        if a[i][j] == 3:
            x, y = i, j
            break
    else:
        continue
    break
dq = deque([(x, y, 0)])
visited = [bytearray(N) for _ in range(M)]
visited[x][y] = 1
while dq:
    x, y, d = dq.popleft()
    for dx, dy in (M1, M2), (M1, -M2), (-M1, M2), (-M1, -M2), (M2, M1), (M2, -M1), (-M2, M1), (-M2, -M1):
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny]:
            if a[nx][ny] == 1:
                visited[nx][ny] = 1
                dq.append((nx, ny, d + 1))
            elif a[nx][ny] == 4:
                print(d + 1)
                break
    else:
        continue
    break