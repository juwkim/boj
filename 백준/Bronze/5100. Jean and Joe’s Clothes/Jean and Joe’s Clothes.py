while t:=int(input()):
    n = [0] * 5
    for _ in [0] * t:
        s = input()
        if s in 'ML':
            n[0] += 1
        elif s == 'S':
            n[3] += 1
        elif s == 'X':
            n[4] += 1
        elif int(s) < 12:
            n[2] += 1
        else:
            n[1] += 1
    print(*n)