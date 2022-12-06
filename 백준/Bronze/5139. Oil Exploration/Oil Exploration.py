g = lambda: [*map(int, input().split())]

for i in range(1, 1 + int(input())):
    h, w = g()
    lines = [*zip(*[input() for _ in range(h)])]
    print(f'Data Set {i}:')
    
    for line in lines:
        idx = ''.join(line).find('X')
        if idx == -1:
            print('N', end=' ')
        else:
            print(sum(1 + 2 * (toil == 'H') for toil in line[:idx]), end=' ')
    print('\n')