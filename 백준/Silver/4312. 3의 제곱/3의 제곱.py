while n := int(input()):
    num = 1
    buf = []
    for flag in bin(n - 1)[:1:-1]:
        if flag == '1':
            buf.append(str(num))
        num *= 3
    if n == 1:
        print('{ }')
    else:
        print('{', ', '.join(buf), '}')