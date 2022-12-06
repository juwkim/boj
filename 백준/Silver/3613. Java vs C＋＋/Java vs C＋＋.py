s = input()
if '_' in s and any(c.isupper() for c in s):
    print('Error!')
elif s[0] == '_' or s[-1] == '_':
    print('Error!')
elif '__' in s:
    print('Error!')
elif s[0].isupper():
    print('Error!')
elif s.islower():
    a, *l = s.split('_')
    print(a, end='')
    for word in l:
        print(word.capitalize(), end='')
else:
    for c in s:
        if c.isupper():
            print('_' + c.lower(), end='')
        else:
            print(c, end='')