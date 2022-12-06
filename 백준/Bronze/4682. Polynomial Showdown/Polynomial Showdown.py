import sys
for line in sys.stdin:
    l = [*map(int, line.split())]
    first = True
    for i in range(8):
        if l[i]:
            k = abs(l[i])
            if first:
                first = False
                if l[i] == 1:
                    print('x', end='')
                elif l[i] == -1:
                    print('-x', end='')
                else:
                    print(f'{l[i]}x', end='')
                if i != 7:
                    print(f'^{8-i}', end='')
                print(' ', end='')
            else:
                op = '-+'[l[i] > 0]
                if l[i] == 1:
                    print('+ x', end='')
                elif l[i] == -1:
                    print('- x', end='')
                else:
                    print(f'{op} {abs(l[i])}x', end='')
                if i != 7:
                    print(f'^{8-i}', end='')
                print(' ', end='')
    
    if first:
        print(l[8], end='')
    elif l[8] > 0:
        print(f'+ {l[8]}', end='')
    elif l[8] < 0:
        print(f'- {-l[8]}', end='')
    print()