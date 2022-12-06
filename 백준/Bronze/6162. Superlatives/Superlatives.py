from math import log, ceil
for i in range(1, 1+int(input())):
    E, A = map(int, input().split())
    if E <= A:
        state = 'no drought'
    else:
        num = ceil(round(log(E/A, 5),5)) - 1
        state = ' '.join(['mega'] * num + ['drought'])
    print(f'Data Set {i}:\n{state}\n')