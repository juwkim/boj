N = int(input())
if N == 1:
    print('*')
else:
    s = ['*', '*', '*']
    for i in range(N-1):
        s[0] = ['* ', s[0], '**']
        for j in range(1, 3 + 4 * i):
            s[j] = ['* ', *s[j], ' *']
        l = 5 + 4 * i
        s = ['*' * l, '*' + ' ' * (l - 1)] + s + ['*' + ' ' * (l - 2) + '*', '*' * l]
    
    for line in s:
        print(''.join(line).rstrip())