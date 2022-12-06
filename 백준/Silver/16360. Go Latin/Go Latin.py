table = {'a': 'as', 'i': 'ios', 'y': 'ios', 'l': 'les', 'n': 'anes',
         'o': 'os', 'r': 'res', 't': 'tas', 'u': 'us', 'v': 'ves', 'w': 'was'}

for _ in range(int(input())):
    s = input()
    if s[-2:] == 'ne':
        print(s[:-2] + 'anes')
    elif s[-1] in table:
        print(s[:-1] + table[s[-1]])
    else:
        print(s + 'us')