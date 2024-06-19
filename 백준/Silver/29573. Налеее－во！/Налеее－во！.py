N, M, K = map(int, input().split())
a = [input() for _ in range(N)]
x, y, d = 0, 0, 3
for i in range(N):
    for j in range(M):
        if a[i][j] == '-':
            x, y = i, j
            if a[i][j - 1] == '/': d = 0
            else:                  d = 2
            break
        elif a[i][j] == '|':
            x, y = i, j
            if a[i - 1][j] == '\\': d = 1
            break
    else:
        continue
    break
for _ in range(K):
    match input()[0]:
        case 'R': d = (d + 1) % 4
        case 'A': d = (d + 2) % 4
        case 'L': d = (d + 3) % 4
        case 'F':
            x += (1, 0, -1, 0)[d]
            y += (0, -1, 0, 1)[d]
ans = [['.'] * M for _ in range(N)]
ans[x][y] = '-|-|'[d]
match d:
    case 0: ans[x][y - 1] = '/'; ans[x][y + 1] = '\\'
    case 1: ans[x - 1][y] = '\\'; ans[x + 1][y] = '/'
    case 2: ans[x][y - 1] = '\\'; ans[x][y + 1] = '/'
    case 3: ans[x - 1][y] = '/'; ans[x + 1][y] = '\\'
for l in ans:
    print(*l, sep='')