from collections import Counter
cnt = Counter([*open(0)][1:])
name = max(cnt, key=cnt.get)
print(['NONE', name][2 * cnt[name] > sum(cnt.values())])