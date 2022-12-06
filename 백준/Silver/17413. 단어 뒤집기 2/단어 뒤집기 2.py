s = input()
cur = 0
while cur < len(s):
    if s[cur] == ' ':
        print(' ', end='')
        cur += 1
    elif s[cur] == '<':
        idx = s.find('>', cur + 1) + 1
        print(s[cur:idx], end='')
        cur = idx
    else:
        a = s.find(' ', cur + 1)
        b = s.find('<', cur + 1)
        if a == b == -1:
            idx = len(s)
        elif a == -1:
            idx = b
        elif b == -1:
            idx = a
        else:
            idx = min(a, b)
        print(s[cur:idx][::-1], end='')
        
        cur = idx