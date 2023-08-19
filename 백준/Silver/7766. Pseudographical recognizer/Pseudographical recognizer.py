for _ in range(int(input())):
    n, m = map(int, input().split())
    buf = [list(input()) for _ in range(n)]
    s, t, c = -1, -1, ''
    for i in range(n):
        for j in range(m):
            if buf[i][j] != '.':
                s, t, c = i, j, buf[i][j]
                break
        else:
            continue
        break
    if c == '':
        print("INCORRECT")
        continue
    if c == '|':
        for i in range(s, n):
            if buf[i][t] != c:
                break
            buf[i][j] = '.'
    elif c == '-':
        for j in range(t, m):
            if buf[s][j] != c:
                break
            buf[i][j] = '.'
    elif c == '/':
        while s <= n - 1 and t >= 0 and buf[s][t] == '/':
            buf[s][t] = '.'
            s, t = s + 1, t - 1
    elif c == '\\':
        while s <= n - 1 and t <= m - 1 and buf[s][t] == '\\':
            buf[s][t] = '.'
            s, t = s + 1, t + 1
    if all(all(c == '.' for c in line) for line in buf):
        print("CORRECT")
    else:
        print("INCORRECT")