S = '*'
for i in range(int(input()) - 1):
    l = 5 + 4 * i
    
    a = '*' * l
    b = '*' + ' ' * (l - 2) + '*'
    S = [a, b] + ['* ' + c + ' *' for c in S] + [b, a]
print(*S, sep='\n')