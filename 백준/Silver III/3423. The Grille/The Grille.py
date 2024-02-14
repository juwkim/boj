while N:=int(input()):
    grill = [input() for _ in range(N)]
    pos = []
    for i in range(N):
        for j in range(N):
            if grill[i][j] == 'O':
                pos.append((i, j))
    s = [input() for _ in range(N)]
    ans = []
    for _ in range(4):
        for i, j in pos:
            ans.append(s[i][j])
        pos = sorted((j, N - 1 - i) for i, j in pos)
    print(*ans, sep='')