i = 1
while (s:=input()) != '0':
    r, w, l = map(int, s.split())
    if w**2 + l**2 > 4 * r**2:
        state = 'does not fit on the table.'
    else:
        state = 'fits on the table.'
    print(f'Pizza {i} {state}')
    i += 1