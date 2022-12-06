s = int(input())
rules = [input() for _ in [0]*s]
for _ in [0]*int(input()):
    n = int(input())
    if 0 < n <= s:
        rule = rules[n-1]
    else:
        rule = 'No such rule'
    print(f'Rule {n}: {rule}')