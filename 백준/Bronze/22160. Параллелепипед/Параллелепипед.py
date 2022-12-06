while (s:= input())[0] != '0':
    a = sorted(map(int, s.split()))
    p = len(set(a[:4])) + len(set(a[4:8])) + len(set(a[8:]))
    print('yes' if p == 3 else 'no')