dx = 0, 1, 0, -1
dy = 1, 0, -1, 0
for _ in range(int(input())):
    p = input()
    i = p.index(' ')
    j = p.index(' ', i + 1)
    R, C = int(p[:i]), int(p[i + 1:j])
    S = p[j + 1:]
    a = [[-1] * C for _ in range(R)]
    x, y, d = 0, 0, 0
    for c in S:
        if c == ' ':
            num = 0
        else:
            num = ord(c) + 1 - ord('A')
        for i in range(4, -1, -1):
            a[x][y] = (num >> i) & 1
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < R and 0 <= ny < C and a[nx][ny] == -1:
                x, y = nx, ny
            else:
                d = (d + 1) % 4
                x, y = x + dx[d], y + dy[d]
    for l in a:
        for c in l:
            if c == -1:
                print(0, end='')
            else:
                print(c, end='')
    print()