R, C, N = map(int, input().split())
cmd = input()
Map = [[*input()] for _ in range(R)]

x, y = None, None
for i in range(R):
    for j in range(C):
        if Map[i][j] == 'O':
            x, y = i, j
            break

dx = {'>': 0, '<': 0, 'v': 1, '^': -1}
dy = {'>': 1, '<': -1, 'v': 0, '^': 0}

ans = 1
for c in cmd:
    while True:
        p, q = x + dx[c], y + dy[c]
        if Map[p][q] == '#':
            break
        if Map[p][q] == '.':
            ans += 1
            Map[p][q] = '!'
        x, y = p, q
print(ans)