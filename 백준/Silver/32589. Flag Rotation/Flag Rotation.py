from collections import Counter

n, *a = map(int, open(0).read().split())
cnt = Counter(a)
print(n * n - sum(cnt[num] for num in a))