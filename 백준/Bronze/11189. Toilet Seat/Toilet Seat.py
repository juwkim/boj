s = input()
if s[0] == 'U':
    print(s[1:].count('D') * 2)
else:
    print(s[2:].count('D') * 2 + 1)

if s[0] == 'U':
    print(s[2:].count('U') * 2 + 1)
else:
    print(s[1:].count('U') * 2)
print(sum(i != j for i, j in zip(s, s[1:])))