dic = {a: b for a, b in zip('iIeE', 'eEiI')}
for n in open(0):
    for c in n:print(dic[c] if c in dic else c, end='')