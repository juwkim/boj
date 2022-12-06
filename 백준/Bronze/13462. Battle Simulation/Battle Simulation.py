s, i, a = input(), 0, ''
t = len(s)

if t > 2:
    while i < len(s)-2:
        if len(set(s[i:i+3])) == 3:
            a += 'C'
            f = i - t
            i += 3
        else:
            a += s[i]
            f = i - t
            i += 1
    
    if a[-1] != 'C':
        a += s[-2:]
    elif f+3:
        a += s[f+3:]
else:
    a = s
for i, c in enumerate('RBL'):
    a = a.replace(c, 'SKH'[i])
print(a)