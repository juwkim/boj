from collections import deque

N, M, i, j = map(int, input().split())
visited = [bytearray(M + 1) for _ in range(N + 1)]
visited[1][1] = 1
dq = deque([(1, 1, 0)])
ans = "NEVAR"
while dq:
    x, y, d = dq.popleft()
    if x == i and y == j:
        ans = d
        break
    for dx, dy in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
        nx, ny = x + dx, y + dy
        if 1 <= nx <= N and 1 <= ny <= M and not visited[nx][ny]:
            visited[nx][ny] = 1
            dq.append((nx, ny, d + 1))
print(ans)