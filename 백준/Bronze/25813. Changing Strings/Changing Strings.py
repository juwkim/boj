s = input()
a = s.index('U')
b = s.rindex('F')

print('-' * a + 'U' + 'C' * (b - a - 1) + 'F' + '-' * (len(s) - 1 - b))