s = [*zip(*[input() for _ in range(2)])]
for i in range(len(s)):
    if s[i][1] == 'o':
        s[i] = 'owln.'
    elif s[i][1] == 'w':
        s[i] = '.omln'
    else:
        s[i] = '..oLn'
for line in zip(*s):
    print(*line, sep='')