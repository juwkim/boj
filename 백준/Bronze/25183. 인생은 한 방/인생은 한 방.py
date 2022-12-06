N = int(input())
lotto = input()
a = ' ' + ' '.join(str(abs(ord(a) - ord(b))) for a, b in zip(lotto, lotto[1:])) + ' '
print('YES' if ' 1 1 1 1 ' in a else 'NO')