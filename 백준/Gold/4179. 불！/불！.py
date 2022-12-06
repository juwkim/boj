from collections import deque

R, C = map(int, input().split())
Map = [input() for _ in range(R)]
Dir = ((0, -1), (0, 1), (-1, 0), (1, 0))
dj = [[0] * C for _ in range(R)]
df = [[0] * C for _ in range(R)]
qj = deque()
qf = deque()


for i in range(R):
    for j in range(C):
        if Map[i][j] == 'J':
            qj.append((i, j))
            dj[i][j] = 1
        elif Map[i][j] == 'F':
            qf.append((i, j))
            df[i][j] = 1

while qf:
    x, y = qf.popleft()

    for dx, dy in Dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and Map[nx][ny] != '#' and df[nx][ny] == 0:
            df[nx][ny] = df[x][y] + 1
            qf.append((nx, ny))

while qj:
    x, y = qj.popleft()

    for dx, dy in Dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if Map[nx][ny] != '#' and dj[nx][ny] == 0:
                if df[nx][ny] == 0 or dj[x][y] + 1 < df[nx][ny]:
                    dj[nx][ny] = dj[x][y] + 1
                    qj.append((nx, ny))
        else:
            print(dj[x][y])
            exit()
print('IMPOSSIBLE')