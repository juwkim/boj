import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import product
from collections import defaultdict

s = [*input()]
idx = defaultdict(list)
for i, c in enumerate(s):
    if c.islower():
        idx[c].append(i)
        
dic = {}
for _ in range(int(input())):
    a, b = input().split('=')
    l = []
    for v in b.split(','):
        if '..' in v:
            x, y = map(int, v.split('..'))
            l.extend(range(x, y + 1))
        else:
            l.append(int(v))
    dic[a] = l

keys = dic.keys()
for p in product(*dic.values()):
    for k, v in zip(keys, p):
        for i in idx[k]:
            s[i] = v
    print(*s, sep='')