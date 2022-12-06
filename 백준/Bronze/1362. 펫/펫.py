i = 1
while (s:=input()) != '0 0':
    o, w = map(int, s.split())
    die = [False]
    while (d:=input()) != '# 0':
        C, n = d.split()
        w += int(n) * (-1) ** (C == 'E')
        die += [w <= 0]
    print(i, 'RIP' if any(die) else ':-)' if o/2 < w < 2*o else ':-(')
    i += 1