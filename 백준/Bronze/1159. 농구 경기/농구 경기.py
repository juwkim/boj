import collections as c
t=''.join(sorted(s for s,i in c.Counter([input()[0]for _ in[0]*int(input())]).items()if i>4))
print(t or'PREDAJA')