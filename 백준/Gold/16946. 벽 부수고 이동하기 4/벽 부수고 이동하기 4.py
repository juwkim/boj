import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
from collections import deque

N, M = g()
board = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
area = [[(0, 0)] * M for _ in range(N)]
step = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] or board[i][j] == '1':
            continue
        step += 1
        visited[i][j] = True
        now = [(i, j)]
        dq = deque([(i, j)])
        while dq:
            x, y = dq.popleft()
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if visited[nx][ny] or board[nx][ny] == '1':
                    continue
                visited[nx][ny] = True
                now.append((nx, ny))
                dq.append((nx, ny))
        for x, y in now:
            area[x][y] = (len(now), step)
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            print(0, end='')
        else:
            cnt = 0
            check = set()
            for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue
                if board[nx][ny] == '0' and area[nx][ny][1] not in check:
                    cnt += area[nx][ny][0]
                    check.add(area[nx][ny][1])
            print((cnt + 1) % 10, end='')
    print()