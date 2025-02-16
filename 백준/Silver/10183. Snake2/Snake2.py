from collections import deque

_dq = deque()
_a = [[''] * 15 for _ in range(15)]
for i in range(15):
    s = input()
    for j, c in enumerate(s + ' ' * (15 - len(s))):
        _a[i][j] = c
        if c == 'X':
            _dq.appendleft((i, j))

for _ in range(int(input())):
    a = [l[:] for l in _a]
    dq = deque(_dq)
    cnt, d = 0, 'R'
    for c in input():
        x, y = dq[0]
        if c == 'O':
            c = d
        else:
            d = c
        match c:
            case 'U': x -= 1
            case 'D': x += 1
            case 'L': y -= 1
            case 'R': y += 1
        if not (0 <= x < 15 and 0 <= y < 15) or a[x][y] == 'X':
            p, q = dq.pop()
            a[p][q] = ' '
            cnt = -1
            break
        if a[x][y] == 'F':
            cnt += 1
        else:
            p, q = dq.pop()
            a[p][q] = ' '
        dq.appendleft((x, y))
        a[x][y] = 'X'
            
    if cnt == -1:
        print("GAME OVER")
    else:
        print(f"{cnt} pellets")
    for i, j in dq:
        a[i][j] = 'X'
    for l in a:
        print(*l, sep='')
    print()