g = lambda: [*map(int, input().split())]

cnt = 1
while (buf:= g())[0]:
    s, c, p, l = buf
    num = s + l - p - c
    ans = None
    for i in range(c):
        if (num + s * i) % c == 0:
            ans = i
            break
    if ans != None:
        if p:
            print(f'Case {cnt}: {ans} {s-p}/{s}')
        else:
            print(f'Case {cnt}: {ans+1} 0/{s}')
    else:
        print(f'Case {cnt}: Never')
    cnt += 1