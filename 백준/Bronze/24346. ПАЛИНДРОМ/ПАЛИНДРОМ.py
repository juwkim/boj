from collections import Counter
a = Counter(input())
print(max(1, sum(v&1 for v in a.values())))