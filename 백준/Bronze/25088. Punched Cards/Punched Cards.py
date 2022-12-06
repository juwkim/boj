for i in range(int(input())):
    R, C = map(int, input().split())
    print(f'Case #{i+1}:')
    print('..' + '+-' * (C-1) + '+')
    print('.' + '.|' * C)
    a = '+' + '-+' * C
    b = '|' + '.|' * C
    print(a)
    for _ in range(R-1):
        print(b)
        print(a)