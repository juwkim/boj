import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from collections import deque

R, C = g()
A = [g() for _ in range(R)]
rule = [g() for _ in range(int(input()))]
cnt = [A[0], *[[0] * C for _ in range(R - 1)]]
dq = deque([(0, j) for j in range(C) if A[0][j]])
while dq:
    x, y = dq.popleft()
    for r, c in rule:
        nx, ny = x + r, y + c
        if 0 <= nx < R and 0 <= ny < C and A[nx][ny] and not cnt[nx][ny]:
            cnt[nx][ny] = cnt[x][y] + 1
            dq.append((nx, ny))
ans = 1e9
for c in cnt[-1]:
    if c:
        ans = min(ans, c - 1)
if ans == 1e9:
    ans = -1
print(ans)