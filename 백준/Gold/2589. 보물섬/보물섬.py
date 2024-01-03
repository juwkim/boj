import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

r, c = g()
Map = [list(input()) for _ in range(r)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
ans = 0
for i in range(r):
    for j in range(c):
        if Map[i][j] == 'W':
            continue
        dq = deque([(i, j, 0)])
        visit = [[0] * c for _ in range(r)]
        visit[i][j] = True
        while dq:
            x, y, cnt = dq.popleft()
            ans = max(ans, cnt)
            cnt += 1
            for p, q in zip(dx, dy):
                nx, ny = x + p, y + q
                if 0 <= nx < r and 0 <= ny < c and Map[nx][ny] == 'L' and not visit[nx][ny]:
                    visit[nx][ny] = True
                    dq.append((nx, ny, cnt))
print(ans)