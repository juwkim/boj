while (s:= input()) != '0 0':
    n, m = map(int, s.split())
    t = []
    for _ in range(n):
        a, b = map(int, input().split())
        if a <= m:
            t.append((a, b))
    if t:
        a, b = min(t, key=lambda x: (x[1] / x[0], -x[0]))
        print(f'Buy {a} tickets for ${b}')
    else:
        print('No suitable tickets offered')