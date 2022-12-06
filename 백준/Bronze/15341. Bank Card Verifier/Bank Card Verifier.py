while (s:=input()) != '0000 0000 0000 0000':
    t = 0
    for l in s.split():
        for i in l[::2]:
            s = int(i) * 2
            s -= 9 * (s > 9)
            t += s
        for i in l[1::2]:
            t += int(i)
    if t % 10:
        print('No')
    else:
        print('Yes')