for _ in range(int(input())):
    a, b = input().split('-')
    s = sum(map(lambda x: (ord(x[1])-65) * 26**(2-x[0]), enumerate(a)))
    print('nice' if abs(s - int(b)) <= 100 else 'not nice')