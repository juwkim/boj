from collections import Counter
cnt = Counter(open(0))
N = sum(cnt.values())
print(1 - sum((V / N) ** 2 for V in cnt.values()))