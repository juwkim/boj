g = lambda: [*map(int, input().split())]

a = [g() for _ in range(4)]
a += [*zip(*a)]
if len({*map(sum, a)}) == 1:
    print('magic')
else:
    print('not magic')