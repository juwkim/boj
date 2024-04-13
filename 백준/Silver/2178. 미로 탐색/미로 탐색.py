from collections import deque

N, M = map(int, input().split())
board = [input() for _ in range(N)]
dq = deque([(0, 0, 1)])
visited = [bytearray(M) for _ in range(N)]
visited[0][0] = 1
while dq:
    x, y, val = dq.popleft()
    if (x, y) == (N - 1, M - 1):
        break
    for nx, ny in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
        if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] == '0' or visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        dq.append((nx, ny, val + 1))
print(val)