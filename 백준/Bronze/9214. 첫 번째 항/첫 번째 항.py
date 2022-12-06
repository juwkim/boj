cnt = 1
while (s:= input()) != '0':   
    while len(s) % 2 == 0:
        p = ''
        for i in range(0, len(s), 2):
            p += s[i+1] * int(s[i])
        if p == s:
            break
        s = p
    print(f'Test {cnt}: {s}')
    cnt += 1