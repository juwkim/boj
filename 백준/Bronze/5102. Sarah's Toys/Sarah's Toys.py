while (s:=input()) != '0 0':
    s = eval(s.replace(' ', '-'))
    k = s % 2 and s > 1
    print((s - 3 * k) // 2, int(k))