while (s:=input()) != '-1 -1 -1 -1':
    k = [*map(int, s.split())]
    a = k.index(-1)
    flag = -1
    for i in range(1, 10001):
        t = k
        t[a] = i
        if t[1] - t[0] == t[2] - t[1] == t[3] - t[2]:
            flag = i
            break
        elif t[1] / t[0] == t[2] / t[1] == t[3] / t[2]:
            flag = i
            break
    print(flag)