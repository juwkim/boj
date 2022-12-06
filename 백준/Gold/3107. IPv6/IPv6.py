l = input().split(':')
n = l.count('')
if n == 3:
    l = [''] * 8
elif n == 2:
    if l[0] == '':
        l = [''] * (10 - len(l)) + l[2:]
    else:
        l = l[:len(l)-2] + [''] * (10 - len(l))
elif n == 1:
    idx = l.index('')
    l = l[:idx] + [''] * (9 - len(l))+ l[idx+1:]

l = [i.zfill(4) for i in l]
print(*l, sep=':')