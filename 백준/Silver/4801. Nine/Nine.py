while (s:= input()) != '00:00':
    h, m = map(int, s.split(':'))
    
    T = h * 60 + m
    T9 = T

    ans = None
    nines = -1
    time = None
    while T9 > 0 and 10 * abs(T - T9) < T:
        T9 -= 1
    if 10 * abs(T - T9) >= T:
        T9 += 1
    while 10 * abs(T - T9) < T and T9 < 99 * 60 + 100:
        r, q = divmod(T9, 60)

        a = "%02d:%02d" % (r, q)
        tmp = a.count('9')
        if tmp > nines:
            nines = tmp
            ans = a
            time = T9
        elif tmp == nines:
            if abs(T - T9) < abs(T - time):
                ans = a
                time = T9
            elif abs(T - T9) == abs(T - time) and a < ans:
                ans = a
                time = T9
        
        if r > 0 and q < 40:
            a = "%02d:%02d" % (r-1, q + 60)
            tmp = a.count('9')
            if tmp > nines:
                nines = tmp
                ans = a
                time = T9
            elif tmp == nines:
                if abs(T - T9) < abs(T - time):
                    ans = a
                    time = T9
                elif abs(T - T9) == abs(T - time) and a < ans:
                    ans = a
                    time = T9
        T9 += 1
    print(ans)