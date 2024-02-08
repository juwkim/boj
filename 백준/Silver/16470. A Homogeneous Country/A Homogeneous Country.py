from collections import Counter
cnt = Counter(open(0))
total = sum(cnt.values())
P = sum((v / total) ** 2 for v in cnt.values())
print(1 - P)