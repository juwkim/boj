cnt = 1
while (s:= input()) !='.':

    s, c = s.rstrip('. ').split('=')
    if '+' in s:
        a, b = s.split('+')
        a, b, c = map(lambda x: sum(int(i) for i in x), [a, b, c])
        if (a + b - c) % 9:
            print(f'{cnt}. NOT!')
        else:
            print(f'{cnt}. PASS')
    else:
        a, b = s.split('*')
        a, b, c = map(lambda x: sum(int(i) for i in x), [a, b, c])
        if (a * b - c) % 9:
            print(f'{cnt}. NOT!')
        else:
            print(f'{cnt}. PASS')
    cnt += 1