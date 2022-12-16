g = lambda: [*map(int, input().split())]

house = 1
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
while sum(S:=g()):
    W, L = S
    Map = [input() for _ in range(L)]
    
    x, y = -1, -1
    idx = Map[0].find('*')
    if idx != -1:
        x, y, d = 0, idx, 3
    if x == -1:
        idx = Map[-1].find('*')
        if idx != -1:
            x, y, d = L - 1, idx, 1
    if x == -1:
        for i in range(L):
            if Map[i][0] == '*':
                x, y, d = i, 0, 0
                break
    if x == -1:
        for i in range(L):
            if Map[i][-1] == '*':
                x, y, d = i, W - 1, 2
                break
    
    Map = [list(line) for line in Map]
    while Map[x][y] != 'x':
        if Map[x][y] == '\\':
            d = 3 - d
        elif Map[x][y] == '/':
            d = (5 - d - 4 * (d < 2))
        x += dx[d]
        y += dy[d]
    Map[x][y] = '&'
    print('HOUSE', house)
    for line in Map:
        print(*line, sep='')
    house += 1