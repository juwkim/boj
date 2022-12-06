g = lambda: [*map(int, input().split())]

from statistics import Counter
for _ in range(int(input())):
    a = sorted(Counter(g()).values(), reverse=True)
    if a[0] == 4:
        if a[1] == 2:
            print('tiki pair')
        else:
            print('tiki')
    elif a[0] == 3:
        if a[1] == 3:
            print('two triples')
        elif a[1] == 2:
            print('full house')
        else:
            print('one triple')
    elif a[0] == 2:
        if a[1] == 2:
            if a[2] == 2:
                print('three pairs')
            else:
                print('two pairs')
        else:
            print('one pair')
    else:
        print('single')