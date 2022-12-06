g = lambda: [*map(int, input().split())]

R, C = g()
Map = [[*input()] for _ in range(R)]

x, y = 0, 0
ans = 0
while Map[x][y] != 'T':
    ans += 1
    
    if Map[x][y] == 0:
        ans = 'Lost'
        break
    cmd = Map[x][y]
    Map[x][y] = 0
    if cmd == 'N':
        if x == 0:
            ans = 'Out'
            break
        else:
            x -= 1
    elif cmd == 'S':
        if x == R - 1:
            ans = 'Out'
            break
        else:
            x += 1
    elif cmd == 'W':
        if y == 0:
            ans = 'Out'
            break
        else:
            y -= 1
    else:
        if y == C - 1:
            ans = 'Out'
            break
        else:
            y += 1
print(ans)