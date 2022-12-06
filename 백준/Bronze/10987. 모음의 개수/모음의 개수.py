from collections import Counter
a = Counter(input())
print(sum(a[s] for s in 'aeiou'))