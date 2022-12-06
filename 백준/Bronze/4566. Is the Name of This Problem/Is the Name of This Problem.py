while (s:= input()) != 'END':
    try:
        a, b = s.split('" ')
        if f'"{b}" {b}' == s and '"' not in b:
            print(f'Quine({b})')
        else:
            print('not a quine')
    except:
        print('not a quine')