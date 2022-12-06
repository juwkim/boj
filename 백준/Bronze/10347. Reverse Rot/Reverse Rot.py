def f(s, n):
    if s == '_':
        k = 91 + n
    elif s == '.':
        k = 92 + n
    else:
        k = ord(s) + n
    if k < 91:
        return chr(k)
    elif k == 91 or k == 119:
        return chr(95)
    elif k == 92 or k == 120:
        return chr(46)
    else:
        return chr(k - 28)

while (s:=input()) != '0':
    n, p = s.split()
    n = int(n)
    print(''.join(map(lambda x: f(x, n), p[::-1])))