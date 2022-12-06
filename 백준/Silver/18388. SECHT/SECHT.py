dic = {}
a = 'QWERTYUIOP'
b = 'ASDFGHJKL'
c = 'ZXCVBNM'
for s, t in zip(a, a[1:]):
    dic[s] = t
for s, t in zip(b, b[1:]):
    dic[s] = t
for s, t in zip(c, c[1:]):
    dic[s] = t

for c in input():
    if c in dic:
        print(dic[c], end='')
    else:
        print(c, end='')