for s in map(lambda l: [*l.rstrip()[::-1]], open(0)):
    n, i = len(s), 0
    while True:
        if i == n:
            s.append('0')
            n += 1
        if s[i] == '0':
            s[i] = '1'
            break
        s[i] = '0'
        if i + 1 == n:
            s.append('0')
            n += 1
        if s[i + 1] == '1':
            s[i + 1] = '0'
            break
        s[i + 1] = '1'
        i += 2
    while n > 1 and s[-1] == '0':
        s.pop()
        n -= 1
    print(*s[::-1], sep='')