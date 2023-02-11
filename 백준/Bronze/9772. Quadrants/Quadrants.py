while (s:= input()) != '0 0':
    r, c = map(float, s.split())
    if r == 0 or c == 0:
        print('AXIS')
    elif r > 0:
        if c > 0:
            print('Q1')
        else:
            print('Q4')
    else:
        if c > 0:
            print('Q2')
        else:
            print('Q3')
print('AXIS')