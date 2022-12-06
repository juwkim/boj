while (s:= input()) != '0':
    n, *p = map(int, s.split())
    for pitch in (50, 60, 70):
        if sum(p) * 2 > pitch:
            ans = 0
        else:
            ans = pitch // max(p) + 1
        print(ans, end=' ')
    print()