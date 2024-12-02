s = input()
i = s.find('(')
if i == -1:
    print(s)
    print('-')
else:
    print(s[:i-1])
    print(s[i+1:-1])