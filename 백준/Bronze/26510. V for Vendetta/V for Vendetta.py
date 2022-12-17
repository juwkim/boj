for n in map(int, input().split()):
    for i in range(n - 1):
        print(' ' * i + '*' + ' ' * (2 * n - 2 * i - 3) + '*')
    print(' ' * (n - 1) + '*')