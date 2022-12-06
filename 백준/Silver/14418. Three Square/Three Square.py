n = sorted(sorted(map(int, input().split()), reverse=True) for _ in [0]*3)
if len({i[0] for i in n}) == 1 and sum(i[1] for i in n) == n[0][0]:
    print('YES')
else:
    i, j, x, y = -1, -1, -1, -1
    if n[0][0] == n[1][0]:
        i, j = 0, 0
        if n[0][1] == n[1][1]:
            x, y = 1, 1
    elif n[0][1] == n[1][0]:
        i, j = 1, 0
        if n[0][0] == n[1][1]:
            x, y = 0, 1
    elif n[0][0] == n[1][1]:
        i, j = 0, 1
    elif n[0][1] == n[1][1]:
        i, j = 1, 1
    if i+1 and n[2][0] == (n[2][1] + n[0][i]) == (n[0][1-i] + n[1][1-j]):
        print('YES')
    elif x+1 and n[2][0] == (n[2][1] + n[0][x]) == (n[0][1-x] + n[1][1-y]):
        print('YES')
    else:
        print('NO')