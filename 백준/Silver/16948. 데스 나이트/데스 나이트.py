import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque


N = int(input())
r1, c1, r2, c2 = g()
ans = -1
visited = [[False] * N for _ in range(N)]
visited[r1][c1] = True
dq = deque([(r1, c1, 0)])
while dq:
    r, c, cnt = dq.popleft()
    if r == r2 and c == c2:
        ans = cnt
        break
    cnt += 1
    for dr, dc in ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = True
            dq.append((nr, nc, cnt))
print(ans)