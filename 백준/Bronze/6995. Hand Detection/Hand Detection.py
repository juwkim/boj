from itertools import combinations
for _ in[0]*int(input()):
    n = [*map(int, input().split())]
    diff = [abs(x-y) for x,y in combinations(n[1::2], 2)]
    rainbow = {*range(5)} - {*n[::2]}
    if len(diff) == len(set(diff)):
        print('Have a spread.'.ljust(24), end = '')
    else:
        print('Do not have a spread.'.ljust(24), end = '')
    
    if rainbow:
        print('Do not have a rainbow.')
    else:
        print('Have a rainbow.')