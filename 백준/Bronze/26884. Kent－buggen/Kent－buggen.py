from collections import Counter

cnt = Counter([input() for _ in range(int(input()))])
print(sum(val > 1 for val in cnt.values()))