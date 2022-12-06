from itertools import permutations
for _ in range(1, 1 + int(input())):
    print(f'Case # {_}:')
    s = input()
    for __ in permutations(s, len(s)):
        print(''.join(__))