from collections import Counter
_, *l = open(0)
cnt = Counter(l)
name = max(cnt, key=cnt.get)
if 2 * cnt[name] > sum(cnt.values()):
    print(name)
else:
    print('NONE')