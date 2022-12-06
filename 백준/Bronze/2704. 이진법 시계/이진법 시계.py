g = lambda x: x%2**i
for _ in range(int(input())):
    h, m, s = map(int, input().split(':'))
    
    hv, mv, sv = h, m, s
    for i in range(5, -1, -1):
        print(*map(lambda x: x//2**i, [hv, mv, sv]), sep='', end='')
        hv, mv, sv = map(g, [hv, mv, sv])
    print(' ', end='')
    
    hh, mh, sh = [], [], []
    for i in range(5, -1, -1):
        hh, mh, sh = hh + [str(h//2**i)], mh + [str(m//2**i)], sh + [str(s//2**i)]
        h, m, s = map(g, [h, m, s])
    print(''.join([*hh, *mh, *sh]))