import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
from collections import deque
import math

N = int(input())
board = [g() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
group = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 0 or visited[i][j]:
            continue
        visited[i][j] = True
        border = [(i, j)]
        dq = deque([(i, j)])
        while dq:
            x, y = dq.popleft()
            is_border = False
            for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == 1:
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            dq.append((nx, ny))
                    else:
                        is_border = True
            if is_border:
                border.append((x, y))
        group.append(border)
ans = math.inf
for i in range(len(group) - 1):
    for j in range(i + 1, len(group)):
        for x, y in group[i]:
            for nx, ny in group[j]:
                ans = min(ans, abs(x - nx) + abs(y - ny) - 1)
print(ans)