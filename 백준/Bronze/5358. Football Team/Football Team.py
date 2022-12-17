dic = {a: b for a, b in zip('iIeE', 'eEiI')}
for name in open(0):
    for c in name:
        if c in dic:
            print(dic[c], end='')
        else:
            print(c, end='')