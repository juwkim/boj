import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import cycle
for _ in range(1, 1 + int(input())):
    
    ID = [*input()]
    num = 0
    
    what = None
    for a, b in zip(ID[::-1], cycle([9, 3, 7])):
        if a == '?':
            what = b
        else:
            num += int(a) * b
    
    for i in range(10):
        if (num + i * what) % 10 == 0:
            ID[ID.index('?')] = i
            break
    print(f'Scenario #{_}:')
    print(*ID, sep='')
    print()