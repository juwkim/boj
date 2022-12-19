for _ in range(int(input())):
    n = int(input())
    Map = [input() for _ in range(n)]

    a = all(line == line[::-1] for line in Map)
    b = Map == Map[::-1]
    if a and b:
        print('Magnificent')
    elif a:
        print('Graceful')
    elif b:
        print('Beautiful')
    else:
        print('Useless')