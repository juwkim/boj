while n:= int(input()):
    l, r = 0, 0
    last = 0
    ans = 0
    for cmd in input().split():
        if cmd == 'lu':
            l = 1
        elif cmd == 'ru':
            r = 1
        elif cmd == 'ld':
            l = 0
        else:
            r = 0
        if last == 0 and l + r == 2:
            last = 1
            ans += 1
        elif last == 1 and l + r == 0:
            last = 0
            ans += 1
    print(ans)