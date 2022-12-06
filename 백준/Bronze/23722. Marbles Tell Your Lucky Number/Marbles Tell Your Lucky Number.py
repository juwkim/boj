while (s:= input()) != '0 0 0 0':    
    l = [*map(int, s.split())]
    while l.count(0) != 3:
        idx, cnt = 0, 101
        for i in range(4):
            if 0 < l[i] < cnt:
                idx = i
                cnt = l[i]
        for i in range(4):
            if i != idx and l[i]:
                l[i] -= l[idx]
    print(max(l))