while (s:= input()) != '0':
    ans = 0
    l = len(s)
    while s != s[::-1]:
        ans += 1
        s = str(int(s) + 1).rjust(l, '0')
    print(ans)