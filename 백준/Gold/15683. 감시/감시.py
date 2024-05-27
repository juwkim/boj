N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def watch(x, y, d):
    dx = [-1, 0, 1, 0][d]
    dy = [0, 1, 0, -1][d]
    x, y = x + dx, y + dy
    watched = []
    while 0 <= x < N and 0 <= y < M and board[x][y] != 6:
        if board[x][y] != '#':
            board[x][y] = '#'
            watched.append((x, y))
        x, y = x + dx, y + dy
    return watched

def unwatched(watched):
    for x, y in watched: board[x][y] = 0

cctv = []
five = []
for i in range(N):
    for j in range(M):
        if board[i][j] == '#' or board[i][j] == 0 or board[i][j] == 6:
            continue
        if 1 <= board[i][j] <= 4:
            cctv.append((i, j, board[i][j]))
        else:
            five.append((i, j))
        board[i][j] = '#'

for x, y in five:
    for d in range(4):
        watch(x, y, d)

def solve(i):
    if i == len(cctv): return sum(l.count(0) for l in board)
    x, y, c = cctv[i]
    i += 1
    cnt = 1e9
    match c:
        case 1:
            for d in range(4):
                watched = watch(x, y, d)
                cnt = min(cnt, solve(i))
                unwatched(watched)
        case 2:
            for d in range(2):
                watched = watch(x, y, d) + watch(x, y, d + 2)
                cnt = min(cnt, solve(i))
                unwatched(watched)
        case 3:
            for d in range(4):
                watched = watch(x, y, d) + watch(x, y, (d + 1) % 4)
                cnt = min(cnt, solve(i))
                unwatched(watched)
        case 4:
            for d in range(4):
                watched = watch(x, y, d) + watch(x, y, (d + 1) % 4) + watch(x, y, (d + 2) % 4)
                cnt = min(cnt, solve(i))
                unwatched(watched)
    return cnt
print(solve(0))