msg = []
for word in input().split():
    tmp = []
    for c in word:
        if c == 'u':
            tmp.append('1')
        elif c == 'm':
            tmp.append('0')
        elif c.isalnum():
            tmp = []
            break
    msg += tmp

for i in range(0, len(msg), 7):
    print(chr(int(''.join(msg[i:i+7]), 2)), end='')