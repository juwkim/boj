while (p := input()) != '0 0 0 0':
    s0, s1, r0, r1 = p.split()
    a = max(s0, s1) + min(s0, s1)
    b = max(r0, r1) + min(r0, r1)
    if a == '21':
        v = +(b != '21')
    elif b == '21':
        v = 2
    elif s0 == s1:
        if r0 == r1:
            v = (a > b) + (a < b) * 2
        else:
            v = 1
    elif r0 == r1:
        v = 2
    else:
        v = (a > b) + (a < b) * 2
    if v:
        print(f'Player {v} wins.')
    else:
        print('Tie.')