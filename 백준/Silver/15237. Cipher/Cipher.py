from collections import Counter

N, C, *X = map(int, open(0).read().split())
d = {}
for i, x in enumerate(X):
    if x not in d:
        d[x] = i
cnt = Counter(X)
X.sort(key=lambda x: (-cnt[x], d[x]))
print(*X)