while (s:= input()) != '#':
    flag = True
    S, *l = s.split()
    S = int(S)
    home = [0] * 21
    home[S] = 1    
    for visit in l:
        d = visit[0]
        num = int(visit[1:])
        if d == 'U':
            S += num
        else:
            S -= num
        if 1 <= S <= 20 and home[S] == 0:
            home[S] = 1
        else:
            flag = False
            break
        
    if flag:
        buf = [i for i in range(1, 21) if home[i] == 0]
        if buf:
            print(*buf)
        else:
            print('none')
    else:
        print('illegal')