n = int(input()) - 2
print('|' + '-' * n + '|')
for i in range(n):
    s = min(i, n - 1 - i)
    if i == n // 2:
        print('|' + ' ' * s + '*' + ' ' * s + '|')
    else:
        print('|' + ' ' * s + '*' + ' ' * (n - 2 - 2 * s) + '*' + ' ' * s + '|')
print('|' + '-' * n + '|')