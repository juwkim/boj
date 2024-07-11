import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
a = [input() for _ in range(N)]
x, y = -1, -1
for i in range(N):
    for j in range(M):
        if a[i][j] == '2':
            x, y = i, j
            break
    else:
        continue
    break

ans = -1
dq = deque([(x, y, 0)])
visited = [bytearray(M) for _ in range(N)]
visited[x][y] = 1
while dq:
    x, y, d = dq.popleft()
    if a[x][y] in '345':
        ans = d
        break
    for nx, ny in (x, y + 1), (x, y -1), (x + 1, y), (x - 1, y):
        if 0 <= nx < N and 0 <= ny < M and a[nx][ny] != '1' and not visited[nx][ny]:
            visited[nx][ny] = 1
            dq.append((nx, ny, d + 1))
if ans == -1:
    print('NIE')
else:
    print('TAK')
    print(ans)