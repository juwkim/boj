import collections as c
for _ in[0]*int(input()):
    s=c.Counter(input())
    for _ in[0]*int(input()):t=c.Counter(input());print('YNEOS'[any(s[x]<t[x]for x in t)::2])                           