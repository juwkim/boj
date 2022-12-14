from collections import Counter
_, *l = open(0)
cnt = Counter(l)
name = max(cnt, key=cnt.get)
print(['NONE', name][2 * cnt[name] > sum(cnt.values())])