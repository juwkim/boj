N, M = map(int, input().split())
C = input()
if C in "UD":
    N, M = M, N
a = [[0] * M for _ in range(N)]
dx = 0, -1, 0, 1
dy = 1, 0, -1, 0
x, y, d = N >> 1, 0, 0
for num in range(1, (x + 1) * M + 1):
    a[x][y], a[-1 - x][y] = num, num
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < N and 0 <= ny < M and a[nx][ny] == 0:
        x, y = nx, ny
    else:
        d = (d + 1) % 4
        x, y = x + dx[d], y + dy[d]
if C == 'R':
    a = [l[::-1] for l in a]
elif C == 'U':
    a = [*zip(*a)]
elif C == 'D':
    a = [*zip(*a)][::-1]
for l in a:
    print(*l)