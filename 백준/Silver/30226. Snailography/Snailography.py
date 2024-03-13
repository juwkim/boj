N = int(input())
table = [['#' for _ in range(N)] for _ in range(N)]
i, j = N >> 1, N >> 1
di, dj, d = (-1, 0, 1, 0), (0, 1, 0, -1), 0
cur, cnt = 0, 2
for c in input():
    table[i][j] = c
    i, j = i + di[d], j + dj[d]
    cur += 1
    if cur == cnt // 2:
        d = (d + 1) % 4
        cur = 0
        cnt += 1
for i in range(N):
    for j in range(N):
        if table[i][j] == '#':
            continue
        print(table[i][j], end='')