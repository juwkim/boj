while N:= int(input()):
    Map = [[0] * 50 for _ in range(50)]
    for i in range(10, 30):
        Map[24][i] = i - 9
    
    s = input()
    i = 0
    x, y = 24, 29
    ans = f'The worm successfully made all {len(s)} moves.'
    while i < len(s):
        cmd = s[i]
        if cmd == 'N':
            x -= 1
        elif cmd == 'S':
            x += 1
        elif cmd == 'W':
            y -= 1
        else:
            y += 1
        if 0 <= x <= 49 and 0 <= y <= 49:
            if Map[x][y] > i + 1:
                ans = f'The worm ran into itself on move {i+1}.'
                break
            Map[x][y] = i + 21
        else:
            ans = f'The worm ran off the board on move {i+1}.'
            break
        i += 1
    print(ans)